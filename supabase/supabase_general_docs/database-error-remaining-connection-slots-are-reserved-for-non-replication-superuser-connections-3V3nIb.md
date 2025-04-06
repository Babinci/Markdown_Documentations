# Database Error: Remaining Connection Slots Are Reserved For Non-Replication Superuser Connections

## Problem

This error usually occurs when the database reaches the maximum number of connections allowed based on the compute add-on. The full error message typically looks like:

```
FATAL: remaining connection slots are reserved for non-replication superuser connections
```

## Solutions

### 1. Optimize Your Connections

Review your application code to make sure you're properly managing database connections. Implement connection pooling at the application level and make sure connections are being closed when they're no longer needed.

See the [Performance documentation](https://supabase.com/docs/guides/platform/performance#optimizing-the-number-of-connections) for more details on optimizing the number of connections.

### 2. Use Connection Pooling

Supabase provides connection pooling which can help solve this issue by efficiently managing connections:

```
postgresql://postgres:[YOUR-PASSWORD]@[db.ref.supabase.co]:6543/postgres
```

Learn more about the [Connection Pooler](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler).

### 3. Upgrade Your Compute Add-on

If you're already using connection pooling and still hitting the maximum connections, consider upgrading your compute add-on to one that allows more connections:

[See available Compute Add-ons](https://supabase.com/docs/guides/platform/compute-add-ons)

Each compute tier supports a different maximum number of connections, and upgrading to a higher tier will provide more connection slots.
