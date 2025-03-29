# How to Check if My Queries Are Being Blocked by Other Queries

Last edited: 1/17/2025

When database queries are running slowly, it could be because they're being blocked by other operations. PostgreSQL uses a locking mechanism to ensure data consistency, but this can sometimes lead to query blocking.

## Creating a Lock Monitor View

You can create a dedicated view to monitor query locks in your database. Once you run a query that takes a long time to complete, you can check this view to identify which operations might be blocking it.

Run the following SQL to create a lock monitoring view:

```sql
CREATE VIEW public.lock_monitor AS
SELECT
  COALESCE(
    blockingl.relation::regclass::text,
    blockingl.locktype
  ) AS locked_item,
  now() - blockeda.query_start AS waiting_duration,
  blockeda.pid AS blocked_pid,
  blockeda.query AS blocked_query,
  blockedl.mode AS blocked_mode,
  blockinga.pid AS blocking_pid,
  blockinga.query AS blocking_query,
  blockingl.mode AS blocking_mode
FROM
  pg_locks blockedl
  JOIN pg_stat_activity blockeda ON blockedl.pid = blockeda.pid
  JOIN pg_locks blockingl ON (
    blockingl.transactionid = blockedl.transactionid
    OR blockingl.relation = blockedl.relation
    AND blockingl.locktype = blockedl.locktype
  )
  AND blockedl.pid <> blockingl.pid
  JOIN pg_stat_activity blockinga ON blockingl.pid = blockinga.pid
  AND blockinga.datid = blockeda.datid
WHERE
  NOT blockedl.granted
  AND blockinga.datname = current_database();
```

## Using the Lock Monitor

After creating the view, you can query it at any time to see if there are blocked queries:

```sql
SELECT * FROM public.lock_monitor;
```

The view provides the following information:

- **locked_item**: The database object (usually a table) being locked
- **waiting_duration**: How long the blocked query has been waiting
- **blocked_pid**: Process ID of the blocked query
- **blocked_query**: SQL text of the blocked query
- **blocked_mode**: Lock mode requested by the blocked query
- **blocking_pid**: Process ID of the blocking query
- **blocking_query**: SQL text of the query that's holding the lock
- **blocking_mode**: Lock mode held by the blocking query

## Common Solutions for Blocked Queries

If you discover blocked queries, here are some common solutions:

1. **Terminate the blocking query** (if it's stuck or less important):
   ```sql
   SELECT pg_terminate_backend(blocking_pid);
   ```

2. **Analyze and optimize the blocking query** to release locks faster

3. **Review transaction management** to ensure transactions are being properly committed or rolled back

4. **Implement explicit locking strategies** for critical operations

5. **Restructure queries** to minimize lock contention
