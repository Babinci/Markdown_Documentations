# HypoPG: Hypothetical Indexes for PostgreSQL

`HypoPG` is a PostgreSQL extension for creating hypothetical/virtual indexes. It enables users to rapidly create virtual indexes that have no resource cost (CPU, disk, memory) but are visible to the PostgreSQL query planner.

The primary benefit of HypoPG is allowing users to quickly test if an index would improve a slow query without consuming server resources or waiting for physical indexes to build.

## Enabling the Extension

You can enable the HypoPG extension through the Supabase Dashboard:

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for `hypopg` and enable the extension

Alternatively, you can enable it with SQL:

```sql
CREATE EXTENSION hypopg;
```

## Optimizing Query Performance

### Example Scenario

Let's create a sample table and query to demonstrate HypoPG's capabilities:

```sql
CREATE TABLE account (
  id int,
  address text
);

INSERT INTO account(id, address)
SELECT 
  id,
  id || ' main street'
FROM 
  generate_series(1, 10000) id;
```

Now, let's examine how PostgreSQL plans to execute a simple query:

```sql
EXPLAIN SELECT * FROM account WHERE id=1;
```

The result shows a sequential scan, which is inefficient for this type of query:

```
                      QUERY PLAN
-------------------------------------------------------
 Seq Scan on account  (cost=0.00..180.00 rows=1 width=13)
   Filter: (id = 1)
(2 rows)
```

### Testing with a Hypothetical Index

Using HypoPG, we can create a virtual index and see if it improves the query plan:

```sql
SELECT * FROM hypopg_create_index('CREATE INDEX ON account(id)');
EXPLAIN SELECT * FROM account WHERE id=1;
```

The new query plan shows an index scan using our virtual index:

```
                                    QUERY PLAN
------------------------------------------------------------------------------------
 Index Scan using <13504>btree_account_id on hypo  (cost=0.29..8.30 rows=1 width=13)
   Index Cond: (id = 1)
(2 rows)
```

### Important Note on Connections

Virtual indexes created by HypoPG are only visible in the PostgreSQL connection that created them. Since Supabase connects to PostgreSQL through a connection pooler, you should execute the `hypopg_create_index` statement and the `EXPLAIN` statement in a single query for consistent results.

### Creating a Real Index

Once you've confirmed that an index will improve performance, you can create a real index:

```sql
CREATE INDEX ON account(id);
```

## Available Functions

HypoPG provides several useful functions for working with hypothetical indexes:

| Function | Description |
|----------|-------------|
| `hypopg_create_index(text)` | Creates a hypothetical index from a CREATE INDEX statement |
| `hypopg_list_indexes` | A view that lists all hypothetical indexes that have been created |
| `hypopg()` | Lists all hypothetical indexes with the same format as `pg_index` |
| `hypopg_get_index_def(oid)` | Displays the CREATE INDEX statement that would create the index |
| `hypopg_get_relation_size(oid)` | Estimates how large a hypothetical index would be |
| `hypopg_drop_index(oid)` | Removes a specific hypothetical index by OID |
| `hypopg_reset()` | Removes all hypothetical indexes |

## Use Cases

- Troubleshooting slow queries without impacting production systems
- Testing various index configurations quickly
- Validating index strategies before implementing them
- Index performance tuning during development
- Educational purposes for understanding query planning

## Resources

- [Official HypoPG Documentation](https://hypopg.readthedocs.io/en/rel1_stable/)
- [GitHub Repository](https://github.com/HypoPG/hypopg)
