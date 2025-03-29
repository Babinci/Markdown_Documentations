# Engineering for Scale: Vector Architecture

This guide explains how to build an enterprise-grade vector database architecture that can scale as your application grows.

## Introduction

Content sources for vectors can be extremely large. As your application scales, you may need to distribute your vector workloads across several secondary databases (sometimes called "pods"), allowing each collection to scale independently.

## Simple Workloads

For small to medium workloads, a single database approach is typically sufficient.

If you've used [Vecs](https://supabase.com/docs/guides/ai/vecs-python-client) to create collections (for example, collections named `docs`, `posts`, and `images`), you can expose these collections to your web or mobile application using [views](https://supabase.com/docs/guides/database/tables#views).

For example, to expose the "docs" collection in the public schema:

```sql
create view public.docs as
select
  id,
  embedding,
  metadata, -- Expose the metadata as JSON
  (metadata->>'url')::text as url -- Extract the URL as a string
from vector
```

You can then access your collections within your applications using any of the client libraries:

```javascript
const { data, error } = await supabase
  .from('docs')
  .select('id, embedding, metadata')
  .eq('url', '/hello-world')
```

## Enterprise Workloads

As you move into production with larger workloads, it's recommended to split your collections into separate projects. This approach offers several advantages:

- Allows vector stores to scale independently of production data
- Accommodates different resource requirements for vector vs. operational data
- Removes single points of failure
- Isolates performance impact of vector operations

You can use as many secondary databases as needed to manage your collections efficiently.

### Accessing Collections: Two Approaches

With a multi-database architecture, you have two options for accessing collections:

1. **Direct Query Using Vecs** - Query the collections directly using the Vecs API
2. **Wrapper Access** - Access collections from your primary database through Foreign Data Wrappers

Both approaches can be used together depending on your use case, but direct querying with Vecs is generally recommended for maximum scalability.

### Option 1: Query Collections Using Vecs

Vecs provides methods for querying collections using either cosine similarity or metadata filtering:

```python
# Cosine similarity search
docs.query(query_vector=[0.4, 0.5, 0.6], limit=5)

# Metadata filtering
docs.query(
    query_vector=[0.4, 0.5, 0.6],
    limit=5,
    filters={"year": {"$eq": 2012}}  # metadata filters
)
```

### Option 2: Accessing External Collections Using Wrappers

Supabase supports [Foreign Data Wrappers](https://supabase.com/blog/postgres-foreign-data-wrappers-rust), which allow you to connect databases together and query them over the network.

#### Step 1: Connect to the Remote Database

In your primary database, provide credentials to access the secondary database:

```sql
create extension postgres_fdw;

create server docs_server
foreign data wrapper postgres_fdw
options (host 'db.xxx.supabase.co', port '5432', dbname 'postgres');

create user mapping for docs_user
server docs_server
options (user 'postgres', password 'password');
```

#### Step 2: Create a Foreign Table

Create a foreign table to access the data in your secondary project:

```sql
create foreign table docs (
  id text not null,
  embedding vector(384),
  metadata jsonb,
  url text
)
server docs_server
options (schema_name 'public', table_name 'docs');
```

You can then continue to use the client libraries to access your collections through the foreign table:

```javascript
const { data, error } = await supabase
  .from('docs')
  .select('id, embedding, metadata')
  .eq('url', '/hello-world')
```

## Enterprise Architecture Diagram

The recommended enterprise architecture allows you to access collections either with client libraries or using Vecs directly:

```
┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │
│  Web/Mobile App │     │     Vecs API    │
│                 │     │                 │
└────────┬────────┘     └────────┬────────┘
         │                       │
         ▼                       │
┌─────────────────┐              │
│                 │              │
│ Primary Database│              │
│  (Foreign Data  │              │
│    Wrapper)     │              │
│                 │              │
└────────┬────────┘              │
         │                       │
         ├───────────────────────┘
         │
         ▼
┌─────────────────┐
│                 │
│   Secondary     │
│   Database      │
│  (Vector Data)  │
│                 │
└─────────────────┘
```

You can add as many secondary databases as needed to accommodate different collections or workloads.

## Scaling Considerations

When implementing an enterprise vector architecture, consider:

- **Collection Size**: Larger collections may require dedicated resources
- **Query Patterns**: High-frequency search operations may benefit from specialized tuning
- **Isolation Requirements**: Some collections may need to be isolated for security or compliance
- **Index Types**: Different vector collections may benefit from different index types (HNSW, IVF, etc.)
- **Resource Allocation**: Allocate computing resources based on the importance and usage patterns of each collection