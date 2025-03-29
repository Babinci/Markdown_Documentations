# How PostgreSQL Chooses Which Index to Use

Last edited: 2/21/2025

> For a complete list of built-in PostgreSQL index types, see the [official documentation](https://www.postgresql.org/docs/current/indexes-types.html).

## PostgreSQL Internals

PostgreSQL processes queries through several components:

| Module | Description |
| --- | --- |
| Parser | Converts SQL into a traversable query tree |
| Planner/Optimizer | Uses rules and database statistics to find the optimal strategy for retrieving data |
| Executor | Executes the plan created by the planner |

### How an Index is Chosen

The planner considers using an index when an indexed column appears in specific operations:

- `WHERE` clauses
- `LIKE` and `ILIKE` expressions
- `DISTINCT` operations
- `SIMILAR TO` comparisons
- `JOIN` conditions
- `ORDER BY` clauses

Without these conditions, PostgreSQL typically performs a full table scan (sequential scan).

In most cases, the indexed column must be used with a compatible comparison operator (`=`, `>`, `<`, etc.) that works with the specific index type.

#### Example with GIN Index for JSONB

Consider a table with the following structure:

| Column Name | Data Type |
| --- | --- |
| id | INT |
| data | JSONB |

You can create a GIN index for the JSONB column:

```sql
CREATE INDEX some_arbitrary_index_name ON some_table USING gin (data);
```

GIN indexes support specific operators like `@>` but not others like `>`:

```sql
-- GIN index will NOT be used
SELECT * FROM some_table
WHERE data -> 'val' > 5;

-- GIN index WILL be considered
SELECT id FROM some_table
WHERE data @> '[ { "itemId": "p11" } ]';
```

### B-tree Indexes (Default)

The most common index type is B-tree, which supports the following comparison operators:

| Comparison Operator |
| --- |
| `<` |
| `<=` |
| `=` |
| `>=` |
| `>` |

Functional equivalents like `IN`, `BETWEEN`, and `ANY` are also valid.

### Index Selection Factors

Meeting the basic requirements doesn't guarantee index usage. PostgreSQL considers additional factors:

1. **Table Size**: For small tables, a sequential scan might be faster than index lookup
2. **Result Set Size**: If many rows will be returned, an index may not be beneficial
3. **Statistics**: PostgreSQL maintains statistics about tables to inform these decisions

You can view the query plan with the `EXPLAIN` command:

```sql
EXPLAIN <your query>
```

For interpretation help, see this [detailed explainer](https://github.com/orgs/supabase/discussions/22839).

If statistics become stale, you can reset them:

```sql
-- Use judiciously
SELECT pg_stat_reset();
```

## Advanced Index Types

### Multi-column Indexes

Instead of using multiple individual indexes, you can create a single index across multiple columns:

```sql
-- Multi-column index
CREATE INDEX test2_mm_idx ON test2 (major, minor);

-- Query that can use this index:
SELECT name
FROM test2
WHERE major = constant AND minor = constant;
```

### Ordered Indexes

You can pre-sort indexes for better performance with `ORDER BY` clauses:

```sql
-- Organizes the index in descending order, placing NULL values at the end
CREATE INDEX test3_desc_index ON test3 (id DESC NULLS LAST);
```

### Functional Indexes

Indexes can be created on transformed column values:

```sql
-- Index on modified column through function
CREATE INDEX test1_lower_col1_idx ON test1 (lower(col1));

-- Index will be considered for this query:
SELECT * FROM test1 WHERE lower(col1) = 'value';
```

### Covering Indexes

You can include additional columns in an index for faster retrieval:

```sql
CREATE INDEX a_b_idx ON x (a, b) INCLUDE (c);
```

This technique (also called a "covering index") stores copies of the included columns directly in the index, reducing the need to access the table. However, this increases storage requirements, so use it judiciously.

### Indexes on JSONB

While GIN/GIST indexes can index entire JSONB documents, you can also target specific key-values with standard B-tree indexes:

```sql
-- Example table
CREATE TABLE person (
  id serial primary key,
  data jsonb
);

-- Index on a specific JSON property
CREATE INDEX index_name ON person ((data ->> 'name'));
```

For more details, check the [PostgreSQL documentation on multi-column indexes](https://www.postgresql.org/docs/current/indexes-multicolumn.html).
