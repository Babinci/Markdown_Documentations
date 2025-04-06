# Installing the Cron Postgres Module

Install the Supabase Cron Postgres Module to begin scheduling recurring Jobs.

## Installation Options

### Using the Dashboard

1. Go to the [Cron Postgres Module](https://supabase.com/dashboard/project/_/integrations/cron/overview) under Integrations in the Dashboard.
2. Enable the `pg_cron` extension.

### Using SQL

```sql
CREATE EXTENSION pg_cron;
```

## Uninstall

Uninstall Supabase Cron by disabling the `pg_cron` extension:

```sql
DROP EXTENSION IF EXISTS pg_cron;
```

> **Warning**: Disabling the `pg_cron` extension will permanently delete all Jobs.
