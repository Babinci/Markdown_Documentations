# pg_graphql: GraphQL for PostgreSQL

## Introduction

[pg_graphql](https://supabase.github.io/pg_graphql/) is a PostgreSQL extension for interacting with the database using [GraphQL](https://graphql.org/) instead of SQL.

The extension automatically reflects a GraphQL schema from the existing SQL schema and exposes it through a SQL function, `graphql.resolve(...)`. This enables any programming language that can connect to PostgreSQL to query the database via GraphQL with no additional servers, processes, or libraries.

The `pg_graphql` resolve method is designed to interoperate with [PostgREST](https://postgrest.org/en/stable/index.html), the tool that underpins the Supabase API. The `graphql.resolve` function can be called via RPC to safely and performantly expose the GraphQL API over HTTP/S.

For more information about how the SQL schema is reflected into a GraphQL schema, see the [pg_graphql API docs](https://supabase.github.io/pg_graphql/api/).

## Enable the Extension

### Using the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for "pg_graphql" and enable the extension

### Using SQL

```sql
CREATE EXTENSION pg_graphql;
```

## Usage Example

Given a table:

```sql
CREATE TABLE "Blog" (
  id serial primary key,
  name text not null,
  description text
);

INSERT INTO "Blog" (name) VALUES ('My Blog');
```

The reflected GraphQL schema can be queried immediately as:

```sql
SELECT graphql.resolve($$
  {
    blogCollection(first: 1) {
      edges {
        node {
          id,
          name
        }
      }
    }
  }
$$);
```

This returns the JSON:

```json
{
  "data": {
    "blogCollection": {
      "edges": [
        {
          "node": {
            "id": 1,
            "name": "My Blog"
          }
        }
      ]
    }
  }
}
```

Note that `pg_graphql` fully supports schema introspection, so you can connect any GraphQL IDE or schema inspection tool to see the full set of fields and arguments available in the API.

## API Functions

- **`graphql.resolve(query text)`**: A SQL function for executing GraphQL queries

## Resources

- [Official pg_graphql documentation](https://github.com/supabase/pg_graphql)
- [pg_graphql API documentation](https://supabase.github.io/pg_graphql/api/)
