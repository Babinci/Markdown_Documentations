# Hardening the Data API

Your database's automatically generated Data API exposes the `public` schema by default. If your `public` schema is used by other tools as a default space, you might want to lock down this schema. This helps prevent accidental exposure of data that's automatically added to `public`.

There are two levels of security hardening for the Data API:

- Disabling the Data API entirely. This is recommended if you _never_ need to access your database via Supabase client libraries or the REST and GraphQL endpoints.
- Removing the `public` schema from the Data API and replacing it with a custom schema (such as `api`).

## Disabling the Data API

You can disable the Data API entirely if you never intend to use the Supabase client libraries or the REST and GraphQL data endpoints. For example, if you only access your database via a direct connection on the server, disabling the Data API gives you the greatest layer of protection.

1. Go to [API Settings](https://supabase.com/dashboard/project/_/settings/api) in the Supabase Dashboard.
2. Under **Data API Settings**, toggle **Enable Data API** off.

## Exposing a custom schema instead of `public`

If you want to use the Data API but with increased security, you can expose a custom schema instead of `public`. By not using `public`, which is often used as a default space and has laxer default permissions, you get more conscious control over your exposed data.

Any data, views, or functions that should be exposed need to be deliberately put within your custom schema (which we will call `api`), rather than ending up there by default.

### Step 1: Remove `public` from exposed schemas

1. Go to [**API Settings**](https://supabase.com/dashboard/project/_/settings/api) in the Supabase Dashboard.
2. Under **Data API Settings**, remove `public` from **Exposed schemas**. Also remove `public` from **Extra search path**.
3. Click **Save**.
4. Go to [**Database Extensions**](https://supabase.com/dashboard/project/_/database/extensions) and disable the `pg_graphql` extension.

### Step 2: Create an `api` schema and expose it

1. Connect to your database. You can use `psql`, the [Supabase SQL Editor](https://supabase.com/dashboard/project/_/sql), or the Postgres client of your choice.

2. Create a new schema named `api`:

```sql
create schema if not exists api;
```

3. Grant the `anon` and `authenticated` roles usage on this schema.

```sql
grant usage on schema api to anon, authenticated;
```

4. Go to [API Settings](https://supabase.com/dashboard/project/_/settings/api) in the Supabase Dashboard.

5. Under **Data API Settings**, add `api` to **Exposed schemas**. Make sure it is the first schema in the list, so that it will be searched first by default.

6. Under these new settings, `anon` and `authenticated` can execute functions defined in the `api` schema, but they have no automatic permissions on any tables. On a table-by-table basis, you can grant them permissions. For example:

```sql
grant select on table api.<your_table> to anon;
grant select, insert, update, delete on table api.<your_table> to authenticated;
```
