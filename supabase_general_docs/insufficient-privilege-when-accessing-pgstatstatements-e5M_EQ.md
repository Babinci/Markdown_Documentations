# Resolving "Insufficient Privilege" Error When Accessing pg_stat_statements

If you see the error "insufficient privilege" when accessing [pg_stat_statements](pg_stat_statements.md) or when accessing the [Query Performance Report](https://supabase.com/dashboard/project/_/reports/query-performance), it means that the Postgres role you're using doesn't have the required permissions.

## Solution

You can run the following SQL command to allow the Postgres role to read all statistics from the system:

```sql
GRANT pg_read_all_stats TO postgres;
```

This grants the necessary permissions to the `postgres` role, allowing it to read statistics from the pg_stat_statements view and other internal Postgres statistics views.

After running this command, you should be able to access the Query Performance Report in the dashboard and query the pg_stat_statements view directly without permission errors.
