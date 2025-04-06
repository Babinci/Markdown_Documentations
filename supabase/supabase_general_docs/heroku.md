# Migrate from Heroku to Supabase

Supabase is one of the best [free alternatives to Heroku Postgres](https://supabase.com/alternatives/supabase-vs-heroku-postgres). This guide shows how to migrate your Heroku Postgres database to Supabase. This migration requires the [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) CLI tools, which are installed automatically as part of the complete Postgres installation package.

Alternatively, use the [Heroku to Supabase migration tool](https://migrate.supabase.com/) to migrate in just a few clicks.

## Quick demo

[![Migrate Your Heroku Database to Supabase](https://img.youtube.com/vi/xsRhPMphtZ4/0.jpg)](https://www.youtube.com/watch?v=xsRhPMphtZ4)

## Retrieve your Heroku database credentials

1. Log in to your [Heroku account](https://heroku.com/) and select the project you want to migrate.
2. Click **Resources** in the menu and select your **Heroku Postgres** database.
3. Click **Settings** in the menu.
4. Click **View Credentials** and save the following information:
   - Host (`$HEROKU_HOST`)
   - Database (`$HEROKU_DATABASE`)
   - User (`$HEROKU_USER`)
   - Password (`$HEROKU_PASSWORD`)

## Retrieve your Supabase connection string

1. If you're new to Supabase, [create a project](https://supabase.com/dashboard).
2. Go to the [Database settings](https://supabase.com/dashboard/project/_/settings/database) for your project in the Supabase Dashboard.
3. Under **Connection string**, make sure `Use connection pooling` is enabled. Copy the URI and replace the password placeholder with your database password.

## Export your Heroku database to a file

Use `pg_dump` with your Heroku credentials to export your Heroku database to a file (e.g., `heroku_dump.sql`).

```bash
pg_dump --clean --if-exists --quote-all-identifiers \
  -h $HEROKU_HOST -U $HEROKU_USER -d $HEROKU_DATABASE \
  --no-owner --no-privileges > heroku_dump.sql
```

## Import the database to your Supabase project

Use `psql` to import the Heroku database file to your Supabase project.

```bash
psql -d "$YOUR_CONNECTION_STRING" -f heroku_dump.sql
```

## Additional options

- To only migrate a single database schema, add the `--schema=PATTERN` parameter to your `pg_dump` command.
- To exclude a schema: `--exclude-schema=PATTERN`.
- To only migrate a single table: `--table=PATTERN`.
- To exclude a table: `--exclude-table=PATTERN`.

Run `pg_dump --help` for a full list of options.

- If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](https://supabase.com/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.

- For databases smaller than 150 GB, you can increase the size of the disk on paid projects by navigating to [Database Settings](https://supabase.com/dashboard/project/_/settings/database).

- If you're dealing with a database larger than 150 GB, we strongly advise you to [contact our support team](https://supabase.com/dashboard/support/new) for assistance in provisioning the required resources and ensuring a smooth migration process.

## Enterprise

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.
