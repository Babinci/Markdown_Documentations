# OrioleDB Overview

## Introduction

The [OrioleDB](https://www.orioledb.com/) Postgres extension provides a drop-in replacement storage engine for the default heap storage method. It is designed to improve Postgres' scalability and performance.

## Performance Benefits

OrioleDB addresses PostgreSQL's scalability limitations by removing bottlenecks in the shared memory cache under high concurrency. It also optimizes write-ahead-log (WAL) insertion through row-level WAL logging. These changes lead to significant improvements in the industry standard TPC-C benchmark, which approximates a real-world transactional workload. The following benchmark was performed on a c7g.metal instance and shows OrioleDB's performance outperforming the default Postgres heap method with a 3.3x speedup.

![TPC-C (warehouses = 500)](https://supabase.com/docs/img/database/orioledb-tpc-c-500-warehouse.png)

## Current Status and Limitations

OrioleDB is in active development and currently has [certain limitations](https://www.orioledb.com/docs/usage/getting-started#current-limitations). Currently, only B-tree indexes are supported, so features like pg_vector's HNSW indexes are not yet available. An Index Access Method bridge to unlock support for all index types used with heap storage is under active development. In the Supabase OrioleDB image the default storage method has been updated to use OrioleDB, granting better performance out of the box.

## Key Concepts

### Index-organized Tables

OrioleDB uses index-organized tables, where table data is stored in the index structure. This design eliminates the need for separate heap storage, reduces overhead and improves lookup performance for primary key queries.

### No Buffer Mapping

In-memory pages are connected to the storage pages using direct links. This allows OrioleDB to bypass PostgreSQL's shared buffer pool and eliminate the associated complexity and contention in buffer mapping.

### Undo Log

Multi-Version Concurrency Control (MVCC) is implemented using an undo log. The undo log stores previous row versions and transaction information, which enables consistent reads while removing the need for table vacuuming completely.

### Copy-on-write Checkpoints

OrioleDB implements copy-on-write checkpoints to persist data efficiently. This approach writes only modified data during a checkpoint, reducing the I/O overhead compared to traditional Postgres checkpointing and allowing row-level WAL logging.

## Getting Started

### Creating an OrioleDB Project

You can get started with OrioleDB by enabling the extension in your Supabase dashboard.
To get started with OrioleDB you need to [create a new Supabase project](https://supabase.com/dashboard/new/_) and choose `OrioleDB Public Alpha` Postgres version.

![Creating OrioleDB project](https://supabase.com/docs/img/database/orioledb-creating-project--light.png)

### Creating Tables

To create a table using the OrioleDB storage engine, simply execute the standard `CREATE TABLE` statement. By default it will create a table using OrioleDB storage engine. For example:

```sql
-- Create a table
CREATE TABLE blog_post (
  id int8 NOT NULL,
  title text NOT NULL,
  body text NOT NULL,
  author text NOT NULL,
  published_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
  views bigint NOT NULL,
  PRIMARY KEY (id)
);
```

### Creating Indexes

OrioleDB tables always have a primary key. If it wasn't defined explicitly, a hidden primary key is created using the `ctid` column.
Additionally, you can create secondary indexes.

Currently, only B-tree indexes are supported, so features like pg_vector's HNSW indexes are not yet available.

```sql
-- Create an index
CREATE INDEX blog_post_published_at ON blog_post (published_at);
CREATE INDEX blog_post_views ON blog_post (views) WHERE (views > 1000);
```

### Data Manipulation

You can query and modify data in OrioleDB tables using standard SQL statements, including `SELECT`, `INSERT`, `UPDATE`, `DELETE` and `INSERT ... ON CONFLICT`.

```sql
INSERT INTO blog_post (id, title, body, author, views)
VALUES (1, 'Hello, World!', 'This is my first blog post.', 'John Doe', 1000);

SELECT * FROM blog_post ORDER BY published_at DESC LIMIT 10;
```

Result:
```
 id │     title     │            body             │  author  │         published_at          │ views
────┼───────────────┼─────────────────────────────┼──────────┼───────────────────────────────┼───────
  1 │ Hello, World! │ This is my first blog post. │ John Doe │ 2024-11-15 12:04:18.756824+01 │  1000
```

### Viewing Query Plans

You can see the execution plan using standard `EXPLAIN` statement.

```sql
EXPLAIN SELECT * FROM blog_post ORDER BY published_at DESC LIMIT 10;
```

Result:
```
                                                 QUERY PLAN
──────────────────────────────────────────────────────────────────────────────────────────────────────────── 
 Limit  (cost=0.15..1.67 rows=10 width=120)
   ->  Index Scan Backward using blog_post_published_at on blog_post  (cost=0.15..48.95 rows=320 width=120)
```

```sql
EXPLAIN SELECT * FROM blog_post WHERE id = 1;
```

Result:
```
                                    QUERY PLAN
────────────────────────────────────────────────────────────────────────────────── 
 Index Scan using blog_post_pkey on blog_post  (cost=0.15..8.17 rows=1 width=120)
   Index Cond: (id = 1)
```

```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM blog_post ORDER BY published_at DESC LIMIT 10;
```

Result:
```
                                                                      QUERY PLAN
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
 Limit  (cost=0.15..1.67 rows=10 width=120) (actual time=0.052..0.054 rows=1 loops=1)
   ->  Index Scan Backward using blog_post_published_at on blog_post  (cost=0.15..48.95 rows=320 width=120) (actual time=0.050..0.052 rows=1 loops=1)
 Planning Time: 0.186 ms
 Execution Time: 0.088 ms
```

## Resources

- [Official OrioleDB documentation](https://www.orioledb.com/docs)
- [OrioleDB GitHub repository](https://github.com/orioledb/orioledb)
