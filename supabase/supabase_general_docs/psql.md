# Connecting with PSQL

[`psql`](https://www.postgresql.org/docs/current/app-psql.html) is a command-line tool that comes with Postgres.

## Connecting with SSL

You should connect to your database using SSL wherever possible, to prevent snooping and man-in-the-middle attacks.

You can obtain your connection info and Server root certificate from your application's dashboard:

![Connection Info and Certificate.](https://supabase.com/docs/img/database/database-settings-ssl.png)

Download your SSL certificate to `/path/to/prod-supabase.cer`.

Find your connection settings:
1. Go to your [`Database Settings`](https://supabase.com/dashboard/project/_/settings/database) 
2. Make sure `Use connection pooling` is checked
3. Change the connection mode to `Session`
4. Copy the parameters into the connection string:

```bash
psql "sslmode=verify-full sslrootcert=/path/to/prod-supabase.cer host=[CLOUD_PROVIDER]-0-[REGION].pooler.supabase.com dbname=postgres user=postgres.[PROJECT_REF]"
```

## Common PSQL Commands

Once connected, you can use these common psql commands:

- `\l` - List all databases
- `\c database_name` - Connect to a specific database
- `\dt` - List all tables in the current database
- `\d table_name` - Describe a table structure
- `\du` - List all users and their roles
- `\q` - Quit psql

## Resources

- [PostgreSQL Documentation - psql](https://www.postgresql.org/docs/current/app-psql.html)
- [Supabase Database Settings](https://supabase.com/dashboard/project/_/settings/database)
