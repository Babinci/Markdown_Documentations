# LangChain

[LangChain](https://langchain.com/) is a popular framework for working with AI, Vectors, and embeddings. LangChain supports using Supabase as a [vector store](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase), using the `pgvector` extension.

## Initializing your database

Prepare your database with the relevant tables:

### Using the Dashboard SQL Editor

1. Go to the [SQL Editor](https://supabase.com/dashboard/project/_/sql) page in the Dashboard.
2. Click **LangChain** in the Quick start section.
3. Click **Run**.

## Usage

You can now search your documents using any Node.js application. This is intended to be run on a secure server route.

```javascript
import { SupabaseVectorStore } from 'langchain/vectorstores/supabase'
import { OpenAIEmbeddings } from 'langchain/embeddings/openai'
import { createClient } from '@supabase/supabase-js'

const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEY
if (!supabaseKey) throw new Error(`Expected SUPABASE_SERVICE_ROLE_KEY`)

const url = process.env.SUPABASE_URL
if (!url) throw new Error(`Expected env var SUPABASE_URL`)

export const run = async () => {
  const client = createClient(url, supabaseKey)

  const vectorStore = await SupabaseVectorStore.fromTexts(
    ['Hello world', 'Bye bye', "What's this?"],
    [{ id: 2 }, { id: 1 }, { id: 3 }],
    new OpenAIEmbeddings(),
    {
      client,
      tableName: 'documents',
      queryName: 'match_documents',
    }
  )

  const resultOne = await vectorStore.similaritySearch('Hello world', 1)
  console.log(resultOne)
}
```

### Simple metadata filtering

Given the above `match_documents` Postgres function, you can also pass a filter parameter to only return documents with a specific metadata field value. This filter parameter is a JSON object, and the `match_documents` function will use the Postgres JSONB Containment operator `@>` to filter documents by the metadata field values you specify. See details on the [Postgres JSONB Containment operator](https://www.postgresql.org/docs/current/datatype-json.html#JSON-CONTAINMENT) for more information.

```javascript
import { SupabaseVectorStore } from 'langchain/vectorstores/supabase'
import { OpenAIEmbeddings } from 'langchain/embeddings/openai'
import { createClient } from '@supabase/supabase-js'

// First, follow set-up instructions above
const privateKey = process.env.SUPABASE_SERVICE_ROLE_KEY
if (!privateKey) throw new Error(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)

const url = process.env.SUPABASE_URL
if (!url) throw new Error(`Expected env var SUPABASE_URL`)

export const run = async () => {
  const client = createClient(url, privateKey)

  const vectorStore = await SupabaseVectorStore.fromTexts(
    ['Hello world', 'Hello world', 'Hello world'],
    [{ user_id: 2 }, { user_id: 1 }, { user_id: 3 }],
    new OpenAIEmbeddings(),
    {
      client,
      tableName: 'documents',
      queryName: 'match_documents',
    }
  )

  const result = await vectorStore.similaritySearch('Hello world', 1, {
    user_id: 3,
  })

  console.log(result)
}
```

### Advanced metadata filtering

You can also use query builder-style filtering ([similar to how the Supabase JavaScript library works](https://supabase.com/docs/reference/javascript/using-filters)) instead of passing an object. Note that since the filter properties will be in the metadata column, you need to use arrow operators (`->` for integer or `->>` for text) as defined in [PostgREST API documentation](https://postgrest.org/en/stable/references/api/tables_views.html?highlight=operators#json-columns) and specify the data type of the property (e.g. the column should look something like `metadata->some_int_value::int`).

```javascript
import { SupabaseFilterRPCCall, SupabaseVectorStore } from 'langchain/vectorstores/supabase'
import { OpenAIEmbeddings } from 'langchain/embeddings/openai'
import { createClient } from '@supabase/supabase-js'

// First, follow set-up instructions above
const privateKey = process.env.SUPABASE_SERVICE_ROLE_KEY
if (!privateKey) throw new Error(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)

const url = process.env.SUPABASE_URL
if (!url) throw new Error(`Expected env var SUPABASE_URL`)

export const run = async () => {
  const client = createClient(url, privateKey)
  const embeddings = new OpenAIEmbeddings()
  const store = new SupabaseVectorStore(embeddings, {
    client,
    tableName: 'documents',
  })

  const docs = [
    {
      pageContent:
        'This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to expand upon the notion of quantum fluff, a theoretical concept where subatomic particles coalesce to form transient multidimensional spaces. Yet, this abstraction holds no real-world application or comprehensible meaning, reflecting a cosmic puzzle.',
      metadata: { b: 1, c: 10, stuff: 'right' },
    },
    {
      pageContent:
        'This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to proceed by discussing the echo of virtual tweets in the binary corridors of the digital universe. Each tweet, like a pixelated canary, hums in an unseen frequency, a fascinatingly perplexing phenomenon that, while conjuring vivid imagery, lacks any concrete implication or real-world relevance, portraying a paradox of multidimensional spaces in the age of cyber folklore.',
      metadata: { b: 2, c: 9, stuff: 'right' },
    },
    { pageContent: 'hello', metadata: { b: 1, c: 9, stuff: 'right' } },
    { pageContent: 'hello', metadata: { b: 1, c: 9, stuff: 'wrong' } },
    { pageContent: 'hi', metadata: { b: 2, c: 8, stuff: 'right' } },
    { pageContent: 'bye', metadata: { b: 3, c: 7, stuff: 'right' } },
    { pageContent: "what's this", metadata: { b: 4, c: 6, stuff: 'right' } },
  ]

  await store.addDocuments(docs)

  const funcFilterA: SupabaseFilterRPCCall = (rpc) =>
    rpc
      .filter('metadata->b::int', 'lt', 3)
      .filter('metadata->c::int', 'gt', 7)
      .textSearch('content', `'multidimensional' & 'spaces'`, {
        config: 'english',
      })

  const resultA = await store.similaritySearch('quantum', 4, funcFilterA)

  const funcFilterB: SupabaseFilterRPCCall = (rpc) =>
    rpc
      .filter('metadata->b::int', 'lt', 3)
      .filter('metadata->c::int', 'gt', 7)
      .filter('metadata->>stuff', 'eq', 'right')

  const resultB = await store.similaritySearch('hello', 2, funcFilterB)

  console.log(resultA, resultB)
}
```

## Hybrid search

LangChain supports the concept of a hybrid search, which combines Similarity Search with Full Text Search. Read the official docs to get started: [Supabase Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid).

You can install the LangChain Hybrid Search function though our [database.dev package manager](https://database.dev/langchain/hybrid_search).

## Resources

- Official [LangChain site](https://langchain.com/)
- Official [LangChain docs](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase)
- Supabase [Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid)
