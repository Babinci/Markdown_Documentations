# pgvector: Embeddings and Vector Similarity

[pgvector](https://github.com/pgvector/pgvector/) is a PostgreSQL extension for vector similarity search. It can also be used for storing [embeddings](https://supabase.com/blog/openai-embeddings-postgres-vector).

The name of pgvector's PostgreSQL extension is [vector](https://github.com/pgvector/pgvector/blob/258eaf58fdaff1843617ff59ea855e0768243fe9/README.md?plain=1#L64).

Learn more about Supabase's [AI & Vector](https://supabase.com/docs/guides/ai) offering.

## Concepts

### Vector similarity

Vector similarity refers to a measure of the similarity between two related items. For example, if you have a list of products, you can use vector similarity to find similar products. To do this, you need to convert each product into a "vector" of numbers, using a mathematical model. You can use a similar model for text, images, and other types of data. Once all of these vectors are stored in the database, you can use vector similarity to find similar items.

### Embeddings

This is particularly useful if you're building on top of OpenAI's [GPT-3](https://openai.com/blog/gpt-3-apps/). You can create and store [embeddings](https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings) for retrieval augmented generation.

## Usage

### Enable the extension

#### Using the Dashboard

1. Go to the Database page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for "vector" and enable the extension

#### Using SQL

```sql
create extension vector;
```

### Create a table to store vectors

```sql
create table posts (
  id serial primary key,
  title text not null,
  body text not null,
  embedding vector(384)
);
```

### Storing a vector / embedding

In this example we'll generate a vector using Transformer.js, then store it in the database using the Supabase client.

```javascript
import { pipeline } from '@xenova/transformers'

const generateEmbedding = await pipeline('feature-extraction', 'Supabase/gte-small')

const title = 'First post!'
const body = 'Hello world!'

// Generate a vector using Transformers.js
const output = await generateEmbedding(body, {
  pooling: 'mean',
  normalize: true,
})

// Extract the embedding output
const embedding = Array.from(output.data)

// Store the vector in Postgres
const { data, error } = await supabase.from('posts').insert({
  title,
  body,
  embedding,
})
```

## Specific usage cases

### Queries with filtering

If you use an IVFFlat or HNSW index and naively filter the results based on the value of another column, you may get fewer rows returned than requested.

For example, the following query may return fewer than 5 rows, even if 5 corresponding rows exist in the database. This is because the embedding index may not return 5 rows matching the filter.

```sql
SELECT * FROM items WHERE category_id = 123 ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

To get the exact number of requested rows, use [iterative search](https://github.com/pgvector/pgvector/?tab=readme-ov-file#iterative-index-scans) to continue scanning the index until enough results are found.

## More pgvector and Supabase resources

- [Supabase Clippy: ChatGPT for Supabase Docs](https://supabase.com/blog/chatgpt-supabase-docs)
- [Storing OpenAI embeddings in Postgres with pgvector](https://supabase.com/blog/openai-embeddings-postgres-vector)
- [A ChatGPT Plugins Template built with Supabase Edge Runtime](https://supabase.com/blog/building-chatgpt-plugins-template)
- [Template for building your own custom ChatGPT style doc search](https://github.com/supabase-community/nextjs-openai-doc-search)
