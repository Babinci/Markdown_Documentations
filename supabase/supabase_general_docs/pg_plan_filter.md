# pg_plan_filter: Restrict Total Query Cost

## Introduction

[`pg_plan_filter`](https://github.com/pgexperts/pg_plan_filter) is a PostgreSQL extension that blocks execution of statements where the query planner's estimate of the total cost exceeds a specified threshold. This extension gives database administrators a way to restrict the impact that individual queries can have on overall database load.

By setting cost limits, you can prevent resource-intensive queries from overloading your database, helping maintain consistent performance for all users.

## Enable the Extension

`pg_plan_filter` can be enabled on a per-connection basis:

```sql
LOAD 'plan_filter';
```

Or for all connections (requires database restart):

```sql
ALTER DATABASE some_db SET session_preload_libraries = 'plan_filter';
```

## Configuration Parameters

The extension provides two primary configuration parameters:

- **`plan_filter.statement_cost_limit`**: Restricts the maximum total cost for executed statements
- **`plan_filter.limit_select_only`**: When set to true, restricts filtering to `SELECT` statements only

Note that `limit_select_only = true` is not the same as read-only mode because `SELECT` statements may still modify data, for example, through function calls.

## Usage Example

To demonstrate total cost filtering, we'll compare how `plan_filter.statement_cost_limit` treats queries that are under and over its cost limit. First, we set up a table with some data:

```sql
CREATE TABLE book(
  id int primary key
);
-- CREATE TABLE

INSERT INTO book(id) SELECT * FROM generate_series(1, 10000);
-- INSERT 0 10000
```

Next, we can review the explain plans for a single record select and a whole table select:

```sql
EXPLAIN SELECT * FROM book WHERE id = 1;
                             QUERY PLAN
---------------------------------------------------------------------------
 Index Only Scan using book_pkey on book  (cost=0.28..2.49 rows=1 width=4)
   Index Cond: (id = 1)
(2 rows)

EXPLAIN SELECT * FROM book;
                      QUERY PLAN
---------------------------------------------------------
 Seq Scan on book  (cost=0.00..135.00 rows=10000 width=4)
(1 row)
```

Now we can choose a `statement_cost_limit` value between the total cost for the single select (2.49) and the whole table select (135.0) so one statement will succeed and one will fail:

```sql
LOAD 'plan_filter';
SET plan_filter.statement_cost_limit = 50; -- between 2.49 and 135.0

SELECT * FROM book WHERE id = 1;
 id
----
  1
(1 row)
-- SUCCESS
```

When we try to run the more expensive query:

```sql
SELECT * FROM book;
ERROR:  plan cost limit exceeded
HINT:  The plan for your query shows that it would probably have an excessive run time. 
This may be due to a logic error in the SQL, or it maybe just a very costly query. 
Rewrite your query or increase the configuration parameter "plan_filter.statement_cost_limit".
-- FAILURE
```

## Benefits

1. **Protection Against Resource-Intensive Queries**: Prevent long-running queries from monopolizing database resources
2. **Query Optimization Enforcement**: Encourages developers to write optimized queries with proper indexing
3. **Multi-tenant Environment Protection**: Prevents one tenant's bad query from affecting others
4. **Application Layer Error Prevention**: Catches problematic queries before they impact the database
5. **DoS Attack Mitigation**: Adds a layer of protection against simple denial of service attacks

## Resources

- [Official pg_plan_filter documentation](https://github.com/pgexperts/pg_plan_filter)
