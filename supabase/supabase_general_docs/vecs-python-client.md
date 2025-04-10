# Python client

## Manage unstructured vector stores in PostgreSQL

Supabase provides a Python client called [`vecs`](https://github.com/supabase/vecs) for managing unstructured vector stores. This client provides a set of useful tools for creating and querying collections in Postgres using the [pgvector](https://supabase.com/docs/guides/database/extensions/pgvector) extension.

## Quick start

Let's see how Vecs works using a local database. Make sure you have the Supabase CLI [installed](https://supabase.com/docs/guides/cli#installation) on your machine.

### Initialize your project

Start a local Postgres instance in any folder using the `init` and `start` commands. Make sure you have Docker running!

```bash
# Initialize your project
supabase init

# Start Postgres
supabase start
```

### Create a collection

Inside a Python shell, run the following commands to create a new collection called "docs", with 3 dimensions.

```python
import vecs

# create vector store client
vx = vecs.create_client("postgresql://postgres:postgres@localhost:54322/postgres")

# create a collection of vectors with 3 dimensions
docs = vx.get_or_create_collection(name="docs", dimension=3)
```

### Add embeddings

Now we can insert some embeddings into our "docs" collection using the `upsert()` command:

```python
import vecs

# create vector store client
docs = vecs.get_or_create_collection(name="docs", dimension=3)

# a collection of vectors with 3 dimensions
vectors=[
  ("vec0", [0.1, 0.2, 0.3], {"year": 1973}),
  ("vec1", [0.7, 0.8, 0.9], {"year": 2012})
]

# insert our vectors
docs.upsert(vectors=vectors)
```

### Query the collection

You can now query the collection to retrieve a relevant match:

```python
import vecs

docs = vecs.get_or_create_collection(name="docs", dimension=3)

# query the collection filtering metadata for "year" = 2012
docs.query(
    data=[0.4,0.5,0.6],      # required
    limit=1,                         # number of records to return
    filters={"year": {"$eq": 2012}}, # metadata filters
)
```

## Deep dive

For a more in-depth guide on `vecs` collections, see [API](https://supabase.com/docs/guides/ai/python/api).

## Resources

- Official Vecs Documentation: [https://supabase.github.io/vecs/api](https://supabase.github.io/vecs/api)
- Source Code: [https://github.com/supabase/vecs](https://github.com/supabase/vecs)
