# Canceling Statement Due to "Statement Timeout"

This article provides guidance on handling statement timeout errors in Supabase.

## Introduction

When you encounter a "canceling statement due to statement timeout" error, it means your SQL query exceeded the maximum execution time allowed by PostgreSQL. This is a safety mechanism to prevent long-running queries from consuming excessive resources.

## Checking Current Settings

You can run this query to check the current timeout settings for your roles:

```sql
SELECT rolname, rolconfig FROM pg_roles;
```

## Increasing the Statement Timeout

To increase the `statement_timeout` for a specific role, follow the instructions in the [Supabase Timeouts documentation](https://supabase.com/docs/guides/database/timeouts#changing-the-default-timeout). 

Note that after changing these settings, a quick database reboot may be required for the changes to take effect.

## Troubleshooting Query Performance

If you're experiencing timeout issues, you can:

1. Check the Query Performance report in your Supabase dashboard:
   - Navigate to: [https://app.supabase.com/project/_/reports/query-performance](https://app.supabase.com/project/_/reports/query-performance)

2. Use the query plan analyzer on expensive queries:
   ```sql
   EXPLAIN ANALYZE <query-statement-here>;
   ```

3. For supabase-js or PostgREST queries, use the `.explain()` method to analyze performance.

## Examining Postgres Logs

Postgres logs provide useful information about when queries were executed and why they might have timed out:
- Access logs at: [https://app.supabase.com/project/_/logs/postgres-logs](https://app.supabase.com/project/_/logs/postgres-logs)

## Fixing Dashboard Timeouts

If you're experiencing 504 or timeout errors in the Dashboard specifically, check out the [detailed guide on GitHub](https://github.com/orgs/supabase/discussions/21133#discussioncomment-9573776) for troubleshooting steps.
