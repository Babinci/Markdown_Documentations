# pg_stat_statements: Query Performance Monitoring

## Introduction

`pg_stat_statements` is a PostgreSQL extension that exposes a view of the same name to track statistics about SQL statements executed on the database. This extension is essential for performance monitoring, query optimization, and understanding database workloads.

The extension collects execution statistics for all SQL statements executed by the server, providing detailed metrics on query performance, frequency, and resource usage.

## Key Statistics

The `pg_stat_statements` view provides numerous statistics and metadata, including:

| Column Name | Column Type | Description |
| --- | --- | --- |
| `userid` | `oid` (references `pg_authid.oid`) | OID of user who executed the statement |
| `dbid` | `oid` (references `pg_database.oid`) | OID of database in which the statement was executed |
| `toplevel` | `bool` | True if the query was executed as a top-level statement |
| `queryid` | `bigint` | Hash code to identify identical normalized queries |
| `query` | `text` | Text of a representative statement |
| `plans` | `bigint` | Number of times the statement was planned |
| `total_plan_time` | `double precision` | Total time spent planning the statement, in milliseconds |
| `min_plan_time` | `double precision` | Minimum time spent planning the statement, in milliseconds |
| `max_plan_time` | `double precision` | Maximum time spent planning the statement, in milliseconds |
| `mean_plan_time` | `double precision` | Mean time spent planning the statement, in milliseconds |
| `calls` | `bigint` | Number of times the statement was executed |
| `total_exec_time` | `double precision` | Total time spent executing the statement, in milliseconds |
| `min_exec_time` | `double precision` | Minimum time spent executing the statement, in milliseconds |
| `max_exec_time` | `double precision` | Maximum time spent executing the statement, in milliseconds |
| `mean_exec_time` | `double precision` | Mean time spent executing the statement, in milliseconds |
| `stddev_exec_time` | `double precision` | Population standard deviation of time spent executing the statement, in milliseconds |
| `rows` | `bigint` | Total number of rows retrieved or affected by the statement |

A full list of statistics is available in the [pg_stat_statements documentation](https://www.postgresql.org/docs/current/pgstatstatements.html).

For more information on query optimization, check out the [query performance guide](https://supabase.com/docs/guides/platform/performance#examining-query-performance).

## Enable the Extension

### Using the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for "pg_stat_statements" and enable the extension

### Using SQL

```sql
CREATE EXTENSION pg_stat_statements;
```

## Inspecting Query Activity

A common use for `pg_stat_statements` is to track down expensive or slow queries. The view contains a row for each executed query with statistics inlined. For example, you can leverage the statistics to identify frequently executed and slow queries against a given table:

```sql
SELECT
  calls,
  mean_exec_time,
  max_exec_time,
  total_exec_time,
  stddev_exec_time,
  query
FROM
  pg_stat_statements
WHERE
  calls > 50                   -- at least 50 calls
  AND mean_exec_time > 2.0     -- averaging at least 2ms/call
  AND total_exec_time > 60000  -- at least one minute total server time spent
  AND query ILIKE '%user_in_organization%' -- filter to queries that touch the user_in_organization table
ORDER BY
  calls DESC;
```

From these results, you can make informed decisions about which queries to optimize or which indexes to create.

## Practical Use Cases

1. **Identifying Slow Queries**: Find queries that consistently take the longest time to execute
2. **Detecting Frequent Queries**: Identify the most commonly executed queries for optimization
3. **Resource Usage Analysis**: Determine which queries consume the most database resources
4. **Application Profiling**: Understand how your application interacts with the database
5. **Index Optimization**: Identify candidate queries that could benefit from better indexing

## Resetting Statistics

You can reset the collected statistics using:

```sql
SELECT pg_stat_statements_reset();
```

This is useful when you want to start collecting fresh statistics after making optimizations.

## Resources

- [Official pg_stat_statements documentation](https://www.postgresql.org/docs/current/pgstatstatements.html)
- [PostgreSQL Query Optimization Guide](https://supabase.com/docs/guides/platform/performance#examining-query-performance)
