# How to Update Connection Pool Settings in Your Dashboard

Last edited: 2/21/2025

This guide covers common questions about updating settings for PgBouncer or Supavisor, the connection poolers available in Supabase.

## How to identify your connection pooler

You can tell which connection pooler you're using by examining your connection string:

- **PgBouncer** connection string looks like:  
  `postgres://postgres:[YOUR-PASSWORD]@db.xxxxxxxxxx.supabase.co:6543/postgres`

- **Supavisor** connection string looks like:  
  `postgres://postgres.xxxxxxxxx:[YOUR-PASSWORD]@aws-0-us-west-1.pooler.supabase.com:6543/postgres`

Note: The subdomain will vary depending on your project's region. For Supavisor, the project reference must be included in the username following a period (e.g., `postgres.[PROJECT_REF]`).

## Adjusting Connection Pool Settings

You can modify the following settings in your database configuration page at:
[https://supabase.com/dashboard/project/_/settings/database](https://supabase.com/dashboard/project/_/settings/database)

### Pool Size Settings

- **Max Client Connections**: Controls the maximum number of connections to the database
- **Default Pool Size**: Adjusts the client connection limit

### Connection Mode Settings

With Supavisor, you can:

1. Automatically use `session` mode by using the connection string with port `5432`
2. Configure port 6543 to use `session` mode in the database settings

The connection mode determines how transactions are handled:
- **Transaction mode**: Each query uses a new connection from the pool (default)
- **Session mode**: Maintains a dedicated connection for the duration of a session
