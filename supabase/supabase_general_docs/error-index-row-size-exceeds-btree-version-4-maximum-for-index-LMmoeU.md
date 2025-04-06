# Error: Index Row Size Exceeds BTree Version 4 Maximum for Index

## Error Message

```
index row size exceeds btree version 4 maximum 2704 for index "idx_name"
```

## Summary

PostgreSQL has a limit on a B-tree tuple (row) size. It needs to fit at least 3 B-tree tuples on an 8KB page, which cannot be changed. This error occurs when attempting to create an index with rows that are too large.

B-tree rows can consist of a single attribute or multiple attributes. Each case requires a different solution approach.

## Solutions

### When B-tree is Built with Multiple Attributes

B-tree indexes with multiple attributes perform well only when:
- Queries typically use several attributes that include the first attributes of the index
- The workload has a high number of INSERT/UPDATE operations compared to SELECT operations

In most cases where this error occurs with a multi-attribute index, the best solution is to:

1. Build separate single-attribute indexes for each attribute
2. Drop the multiple-attribute B-tree index

This approach is often the only viable solution when encountering this error.

### When B-tree is Built on a Single Long Attribute

This situation commonly occurs when indexing text, JSON columns, or other large data types. While B-tree indexes can be created on these data types, they're often ineffective for very large values.

The solution is to use hashing to transform the values into a narrower space. For example:

1. Create a functional index using a hash function:

```sql
CREATE INDEX ON table_name(MD5(column_name));
```

2. Modify your queries to use the same function:

```sql
SELECT * FROM table_name WHERE MD5(column_name) = MD5('search_value');
```

Instead of:

```sql
SELECT * FROM table_name WHERE column_name = 'search_value';
```

For some data types that allow queries by partial inclusion (like JSON or when implementing tsvector phrase search), consider using GIST/GIN indexes which are better suited for these scenarios.

## Further Reading

- [PostgreSQL Documentation on Creating Indexes by Expression](https://www.postgresql.org/docs/current/sql-createindex.html)
- [PostgreSQL Documentation on GIN/GiST Indexes](https://www.postgresql.org/docs/current/textsearch-indexes.html)
