# pg_cron: Schedule Recurring Jobs with Cron Syntax in PostgreSQL

## Introduction

[`pg_cron`](https://github.com/citusdata/pg_cron) is a PostgreSQL extension that enables scheduling recurring jobs using cron syntax directly within your database. It serves as the foundation for Supabase Cron, allowing you to automate database tasks and operations.

## How pg_cron Works

Under the hood, Supabase Cron uses the `pg_cron` PostgreSQL extension as the scheduling and execution engine for your jobs. The extension:

- Creates a `cron` schema in your database
- Stores all jobs in the `cron.job` table
- Records each job's execution and status in the `cron.job_run_details` table

With pg_cron, you can schedule jobs to run anywhere from every second to once a year, depending on your use case.

## Capabilities

Jobs created with pg_cron can:
- Run SQL snippets or database functions with zero network latency
- Make HTTP requests, such as invoking a Supabase Edge Function
- Perform database maintenance tasks
- Update materialized views
- Clean up old data

## Performance Recommendations

For best performance, consider the following guidelines:
- No more than 8 jobs should run concurrently
- Each job should run no more than 10 minutes

## Limitations

Note that `pg_cron` is not fully supported on Fly Postgres. See the [Fly Postgres limitations](https://supabase.com/docs/guides/platform/fly-postgres#limitations) documentation for more details.

## Resources

- [pg_cron GitHub Repository](https://github.com/citusdata/pg_cron)
- [Supabase Cron Documentation](https://supabase.com/docs/guides/cron)
