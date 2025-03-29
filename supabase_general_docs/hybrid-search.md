# Hybrid Search: Combining Keyword and Semantic Search

Hybrid search combines [full text search](https://supabase.com/docs/guides/ai/keyword-search) (searching by keyword) with [semantic search](https://supabase.com/docs/guides/ai/semantic-search) (searching by meaning) to identify results that are both directly and contextually relevant to the user's query. This powerful approach leverages the strengths of both methods to provide more comprehensive search results.

## Use Cases for Hybrid Search

Sometimes a single search method doesn't capture what a user is really looking for. For example, if a user searches for "Italian recipes with tomato sauce" on a cooking app:

- **Keyword search** would pull up recipes that specifically mention "Italian," "recipes," and "tomato sauce" in the text, but might miss dishes that use variations like "pasta sauce" or "marinara."
- **Semantic search** might understand the culinary context and find recipes like "Spaghetti Marinara," even without exact keyword matches, but could also suggest contextually related but irrelevant items like "Mexican salsa."

Hybrid search combines these approaches to prioritize recipes explicitly mentioning the keywords while including semantically related dishes that might not have the exact search terms.

## When to Consider Hybrid Search

The decision to use hybrid search depends on your users' needs:

- **Keyword search** is ideal for code repositories where developers need exact matches for lines of code or error messages.
- **Semantic search** works better for applications like mental health forums where users search for content related to their feelings, not just specific words.
- **Hybrid search** is perfect for shopping applications where customers might search for specific product names but are also open to related suggestions.

## How Search Methods Are Combined

Hybrid search merges keyword and semantic search through a process called "fusion":

1. Each search method executes separately, generating its own results
2. The separate results are combined using a ranking or scoring system
3. A unified list is created that leverages the strengths of both methods

## Reciprocal Ranked Fusion (RRF)

One of the most common fusion methods is Reciprocal Ranked Fusion (RRF). This approach gives more weight to top-ranked items in each individual result list when building the final combined list.

In RRF, each record receives a score calculated as 1 divided by that record's rank in each list, summed together. For example:

- If a record with ID `123` ranked third in keyword search and ninth in semantic search, its score would be 1/3 + 1/9 = 0.444
- If a record appears in only one list, it receives a score of 0 for the missing list
- Records are then sorted by this score to create the final ranked list

This method ensures items that rank high in multiple lists receive high rankings in the final list.

### Smoothing Constant `k`

To prevent extremely high scores for top-ranked items, a constant `k` is added to the denominator:

1/(k+rank)

This smoothing constant prevents first-ranked items from dominating the results. A constant of 1 would give a first-place record a score of 1/(1+1) = 0.5 instead of 1/1 = 1.

## Implementing Hybrid Search in PostgreSQL

Let's implement hybrid search using `tsvector` (keyword search) and `pgvector` (semantic search).

### 1. Create a Documents Table

```sql
CREATE TABLE documents (
  id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  content text,
  fts tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED,
  embedding vector(512)
);
```

The table contains:
- `id`: Auto-generated unique identifier
- `content`: The text to search over
- `fts`: Auto-generated `tsvector` column for full-text search
- `embedding`: Vector column for semantic search (512 dimensions in this example)

### 2. Create Indexes for Performance

```sql
-- Create an index for the full-text search
CREATE INDEX ON documents USING gin(fts);

-- Create an index for the semantic vector search
CREATE INDEX ON documents USING hnsw (embedding vector_ip_ops);
```

### 3. Create the Hybrid Search Function

```sql
CREATE OR REPLACE FUNCTION hybrid_search(
  query_text text,
  query_embedding vector(512),
  match_count int,
  full_text_weight float = 1,
  semantic_weight float = 1,
  rrf_k int = 50
)
RETURNS SETOF documents
LANGUAGE sql
AS $$
WITH full_text AS (
  SELECT
    id,
    -- Note: ts_rank_cd is not indexable but will only rank matches of the where clause
    -- which shouldn't be too big
    row_number() OVER(ORDER BY ts_rank_cd(fts, websearch_to_tsquery(query_text)) DESC) AS rank_ix
  FROM
    documents
  WHERE
    fts @@ websearch_to_tsquery(query_text)
  ORDER BY rank_ix
  LIMIT least(match_count, 30) * 2
),
semantic AS (
  SELECT
    id,
    row_number() OVER (ORDER BY embedding <#> query_embedding) AS rank_ix
  FROM
    documents
  ORDER BY rank_ix
  LIMIT least(match_count, 30) * 2
)
SELECT
  documents.*
FROM
  full_text
  FULL OUTER JOIN semantic
    ON full_text.id = semantic.id
  JOIN documents
    ON coalesce(full_text.id, semantic.id) = documents.id
ORDER BY
  coalesce(1.0 / (rrf_k + full_text.rank_ix), 0.0) * full_text_weight +
  coalesce(1.0 / (rrf_k + semantic.rank_ix), 0.0) * semantic_weight
  DESC
LIMIT
  least(match_count, 30)
$$;
```

#### Function Parameters:

- **Required parameters**:
  - `query_text`: The user's search query text
  - `query_embedding`: Vector representation of the user's query
  - `match_count`: Number of records to return

- **Optional parameters**:
  - `full_text_weight`: Weight given to full-text search results (default: 1)
  - `semantic_weight`: Weight given to semantic search results (default: 1)
  - `rrf_k`: Smoothing constant for RRF (default: 50)

## Using Hybrid Search

### SQL Query Example

```sql
SELECT *
FROM hybrid_search(
  'Italian recipes with tomato sauce', -- user query
  '[...]'::vector(512), -- embedding generated from user query
  10
);
```

### JavaScript Example with Edge Function

```javascript
import { createClient } from 'jsr:@supabase/supabase-js@2'
import OpenAI from 'npm:openai'

const supabaseUrl = Deno.env.get('SUPABASE_URL')!
const supabaseServiceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
const openaiApiKey = Deno.env.get('OPENAI_API_KEY')!

Deno.serve(async (req) => {
  // Grab the user's query from the JSON payload
  const { query } = await req.json()
  
  // Instantiate OpenAI client
  const openai = new OpenAI({ apiKey: openaiApiKey })
  
  // Generate a one-time embedding for the user's query
  const embeddingResponse = await openai.embeddings.create({
    model: 'text-embedding-3-large',
    input: query,
    dimensions: 512,
  })
  const [{ embedding }] = embeddingResponse.data
  
  // Instantiate the Supabase client
  // (replace service role key with user's JWT if using Supabase auth and RLS)
  const supabase = createClient(supabaseUrl, supabaseServiceRoleKey)
  
  // Call hybrid_search Postgres function via RPC
  const { data: documents } = await supabase.rpc('hybrid_search', {
    query_text: query,
    query_embedding: embedding,
    match_count: 10,
  })
  
  return new Response(JSON.stringify(documents), {
    headers: { 'Content-Type': 'application/json' },
  })
})
```

## Related Resources

- [Embedding concepts](https://supabase.com/docs/guides/ai/concepts)
- [Vector columns](https://supabase.com/docs/guides/ai/vector-columns)
- [Vector indexes](https://supabase.com/docs/guides/ai/vector-indexes)
- [Semantic search](https://supabase.com/docs/guides/ai/semantic-search)
- [Full text (keyword) search](https://supabase.com/docs/guides/database/full-text-search)
