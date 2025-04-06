# Fly Postgres

Fly Postgres is a Supabase-supported PostgreSQL database service deployed on the Fly.io edge network. This integration allows you to run Supabase databases in all regions where Fly.io operates.

> **Important Note**: Fly Postgres is being deprecated on April 11, 2025. For more information, please refer to the [official announcement](https://github.com/orgs/supabase/discussions/33413).

## Quickstart

To begin using Fly Postgres:

1. Install the Fly CLI if you haven't already
2. Authenticate with the CLI:
   ```bash
   flyctl auth login
   ```
3. Access the Supabase dashboard through the CLI:
   ```bash
   flyctl extensions supabase dashboard <app-name>
   ```

For a complete list of available CLI commands, consult the [Fly documentation](https://fly.io/docs/flyctl/extensions-supabase/).

## Connecting to Your Database

Connectivity options depend on your network's IP capabilities:

### IPv6 Networks
If your network supports IPv6, you can connect directly to your Fly Postgres database. The database's domain name resolves to an IPv6 address, which is accessible from within your Fly applications.

### IPv4-Only Networks
For networks with only IPv4 support, use Supavisor instead of connecting directly to the database. Supavisor's domain name resolves to an IPv4 address, enabling connectivity for networks without IPv6 support.

To find your database connection strings, visit the [Database Settings page](https://supabase.com/dashboard/project/_/settings/database) in your Supabase dashboard.

## Supabase Studio Integration

Access the full Supabase Studio interface by running:

```bash
flyctl extensions supabase dashboard <app-name>
```

This command authenticates with Fly via OAuth and logs you into the Supabase dashboard, where you can access:

- **SQL Editor**: Execute SQL queries against your database
- **Table Editor**: Create, modify, and delete tables and columns through a graphical interface
- **Log Explorer**: View real-time logs for database operations and queries
- **Postgres Upgrades**: Manage and initiate PostgreSQL version upgrades

## Permission Management

The relationship between Supabase and Fly organizations is one-to-one. When you launch your first Fly Postgres database, a corresponding Supabase organization is automatically created if it doesn't already exist.

User accounts are created on demand:
- Every Fly user receives a unique Supabase account
- This account is separate from any existing Supabase accounts you may have
- The user who initiates a Fly Postgres database deployment is granted the owner role
- Subsequent users are added with the developer role
- Role assignments can be modified in the Supabase dashboard as needed

## Limitations

When using Fly Postgres, be aware of these current limitations:

1. **IPv6 Dependency**: Direct database connections are only supported via IPv6. For IPv4-only networks, you must use Supavisor as described above.

2. **Network Restrictions**: [Network restrictions](https://supabase.com/docs/guides/platform/network-restrictions) are not supported for Fly Postgres instances.

3. **Limited Service Support**: Currently, only the core database, Supavisor, and PostgREST are supported. Support for additional Supabase services (Realtime, Storage, Auth) is planned for future releases.

4. **pg_cron Limitations**: The [pg_cron](https://supabase.com/docs/guides/database/extensions/pg_cron) extension has limited functionality with Fly projects:
   - Fly projects automatically shut down after 15 minutes of inactivity
   - They restart when an external request is received
   - pg_cron jobs are not considered external requests
   - Therefore, scheduled jobs don't run when the database is in a shut-down state

## Migration Considerations

Given the upcoming deprecation in April 2025, users should begin planning migration strategies to alternative Supabase hosting options. Refer to the [official announcement](https://github.com/orgs/supabase/discussions/33413) for migration recommendations and support.
