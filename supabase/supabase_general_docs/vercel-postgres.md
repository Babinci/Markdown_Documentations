# Migrate from Vercel Postgres to Supabase

This guide demonstrates how to migrate your Vercel Postgres database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

## Retrieve Your Vercel Postgres Database Credentials

1. Log in to your [Vercel Dashboard](https://vercel.com/login)
2. Click on the **Storage** tab
3. Click on your Postgres Database
4. Under the **Quickstart** section, select **psql** then click **Show Secret** to reveal your database password
5. Copy the string after `psql ` to the clipboard

Example:
```
psql "postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
```

Copy this part to your clipboard:
```
"postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
```

## Set Your `OLD_DB_URL` Environment Variable

Set the **OLD_DB_URL** environment variable at the command line using your Vercel Postgres Database credentials:

```bash
export OLD_DB_URL="postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
```

## Retrieve Your Supabase Connection String

1. If you're new to Supabase, [create a project](https://supabase.com/dashboard).
   Make a note of your password, you will need this later. If you forget it, you can [reset it here](https://supabase.com/dashboard/project/_/settings/database).

2. Go to the [Database settings](https://supabase.com/dashboard/project/_/settings/database) for your project in the Supabase Dashboard.

3. Under **Connection string**, select **URI**, make sure **Display connection pooler** is checked, and **Mode: Session** is set.

4. Click the **Copy** button to the right of your connection string to copy it to the clipboard.

## Set Your `NEW_DB_URL` Environment Variable

Set the **NEW_DB_URL** environment variable at the command line using your Supabase connection string. You will need to replace `[YOUR-PASSWORD]` with your actual database password:

```bash
export NEW_DB_URL="postgresql://postgres.xxxxxxxxxxxxxxxxxxxx:[YOUR-PASSWORD]@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
```

## Migrate the Database

You will need the [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full [Postgres installation](https://www.postgresql.org/download).

1. Export your database to a file in console:

   Use `pg_dump` with your Postgres credentials to export your database to a file (e.g., `dump.sql`):

   ```bash
   pg_dump "$OLD_DB_URL" \
     --clean \
     --if-exists \
     --quote-all-identifiers \
     --no-owner \
     --no-privileges \
     > dump.sql
   ```

2. Import the database to your Supabase project:

   Use `psql` to import the Postgres database file to your Supabase project:

   ```bash
   psql -d "$NEW_DB_URL" -f dump.sql
   ```

### Additional Options

- To only migrate a single database schema, add the `--schema=PATTERN` parameter to your `pg_dump` command
- To exclude a schema: `--exclude-schema=PATTERN`
- To only migrate a single table: `--table=PATTERN`
- To exclude a table: `--exclude-table=PATTERN`

Run `pg_dump --help` for a full list of options.

### Recommendations for Large Databases

- If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](https://supabase.com/docs/guides/platform/compute-add-ons) to ensure you have the necessary resources
- For databases smaller than 150 GB, you can increase the size of the disk on paid projects from the [Database Settings](https://supabase.com/dashboard/project/_/settings/database)
- For databases larger than 150 GB, [contact the support team](https://supabase.com/dashboard/support/new) for assistance in provisioning the required resources

## Enterprise Support

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.
