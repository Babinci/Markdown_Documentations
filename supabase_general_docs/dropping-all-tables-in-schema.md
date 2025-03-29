# Drop All Tables in a PostgreSQL Schema

This guide explains how to drop all tables in a specific schema in your PostgreSQL database.

## Warning

This procedure will delete all tables and their associated data in the specified schema. **Ensure you have a recent [backup](https://supabase.com/docs/guides/platform/backups) before proceeding.**

## SQL Script

Execute the following SQL script to drop all tables in a given schema:

```sql
do $$ 
declare
    r record;
begin
    for r in (select tablename from pg_tables where schemaname = 'my-schema-name') loop
        execute 'drop table if exists ' || quote_ident(r.tablename) || ' cascade';
    end loop;
end $$;
```

Replace `'my-schema-name'` with the name of your schema. In Supabase, the default schema is `public`.

## How It Works

This SQL script:
1. Creates an anonymous code block using PostgreSQL's PL/pgSQL syntax (`do $$ ... $$`)
2. Declares a record variable `r` to hold each table name
3. Loops through all tables in the specified schema by querying the `pg_tables` system catalog
4. Dynamically constructs and executes a `DROP TABLE` statement for each table
5. Uses the `CASCADE` option to automatically drop any dependent objects (like constraints)

## Running the Script

You can run this script using:

1. The [SQL Editor](https://supabase.com/dashboard/project/_/sql) in the Supabase Dashboard
2. `psql` if you're [connecting directly to the database](https://supabase.com/docs/guides/database/connecting-to-postgres#direct-connections)
3. Any other PostgreSQL client that allows executing SQL queries

## Use Cases

This script is useful for:
- Cleaning up development or testing environments
- Starting fresh with a schema while maintaining its structure
- Batch removal of tables during database reorganization

Remember to always make backups before performing destructive operations like this on your database.