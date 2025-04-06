# Error: Prepared Statement "XXX" Already Exists

## Problem

When connecting to your Supabase database, you might encounter an error message like:

```
Error: prepared statement "XXX" already exists
```

This error typically occurs when you're trying to use prepared statements with PgBouncer, which is the connection pooler that handles the default port (6543) in Supabase projects.

## Cause

PgBouncer does not support prepared statements in transaction pooling mode, which is the default configuration in Supabase. When a client attempts to create a prepared statement, it conflicts with existing prepared statements in the pooled connections.

## Solutions

You have several options to resolve this issue:

### 1. Use Direct Database Connection (Port 5432)

The simplest solution is to connect directly to PostgreSQL using port 5432 instead of the PgBouncer port (6543):

```
postgresql://postgres:[YOUR-PASSWORD]@[HOST].supabase.co:5432/postgres
```

This bypasses PgBouncer completely and allows prepared statements to work normally.

### 2. Disable Prepared Statements in Your Client

Many database clients and ORMs offer options to disable prepared statements:

#### For Prisma:

Add the `pgbouncer=true` parameter to your connection string:

```
postgresql://postgres:[YOUR-PASSWORD]@[HOST].supabase.co:6543/postgres?pgbouncer=true
```

For more details, see the [Prisma PgBouncer configuration guide](https://www.prisma.io/docs/guides/performance-and-optimization/connection-management/configure-pg-bouncer).

#### For other clients:

Consult your client's documentation for options to disable prepared statements or work with connection poolers.

## Considerations

- Direct connections (port 5432) may hit connection limits more easily than pooled connections
- If you need to use prepared statements with many connections, consider upgrading your Supabase plan for higher connection limits
- For high-traffic applications, using the connection pooler with disabled prepared statements is often the best approach

## Related Documentation

For more information on connection management in Supabase, see the [Connection Management guide](https://supabase.com/docs/guides/database/connecting-to-postgres).
