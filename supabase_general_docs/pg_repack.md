# pg_repack: Physical Storage Optimization and Maintenance

## Introduction

[pg_repack](https://github.com/reorg/pg_repack) is a PostgreSQL extension to remove bloat from tables and indexes, and optionally restore the physical order of clustered indexes. Unlike CLUSTER and VACUUM FULL, pg_repack runs "online" and does not hold exclusive locks on the processed tables, allowing ongoing database operations to continue. pg_repack's efficiency is comparable to using CLUSTER directly.

The extension provides the following methods to optimize physical storage:

- **Online CLUSTER**: Ordering table data by cluster index in a non-blocking way
- **Custom ordering**: Ordering table data by specified columns
- **Online VACUUM FULL**: Packing rows only in a non-blocking way
- **Index optimization**: Rebuild or relocate only the indexes of a table

pg_repack has two components: the database extension and a client-side CLI to control it.

## Requirements

- A target table must have a PRIMARY KEY, or a UNIQUE total index on a NOT NULL column
- Performing a full-table repack requires free disk space about twice as large as the target table and its indexes

pg_repack requires the PostgreSQL superuser role by default. That role is not available to users on the Supabase platform. To avoid that requirement, use the `-k` or `--no-superuser-check` flags on every `pg_repack` CLI command.

The first version of pg_repack with full support for non-superuser repacking is 1.5.2. You can check the version installed on your Supabase instance using:

```sql
SELECT default_version
FROM pg_available_extensions
WHERE name = 'pg_repack';
```

If pg_repack is not present, or the version is < 1.5.2, [upgrade to the latest version](https://supabase.com/docs/guides/platform/upgrading) of Supabase to gain access.

## Usage

### Enable the Extension

#### Using the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for "pg_repack" and enable the extension

#### Using SQL

```sql
CREATE EXTENSION pg_repack;
```

### Install the CLI

Select an option from the pg_repack docs to [install the client CLI](https://reorg.github.io/pg_repack/#download).

### Command Syntax

All pg_repack commands should include the `-k` flag to skip the client-side superuser check:

```
pg_repack -k [OPTION]... [DBNAME]
```

Common options include:
- `-h, --host=HOSTNAME`: Database server host
- `-p, --port=PORT`: Database server port
- `-U, --username=USERNAME`: Database user name
- `-d, --dbname=DBNAME`: Database to connect to
- `-t, --table=TABLE`: Repack only specified table(s)
- `--no-order`: Do not order table (equivalent to VACUUM FULL)
- `--dry-run`: Show what would be done, but don't actually repack
- `-T, --tablespace=TBLSPC`: Move the repacked tables to the specified tablespace

## Example

Perform an online `VACUUM FULL` on the tables `public.foo` and `public.bar` in the database `postgres`:

```bash
pg_repack -k -h db.<PROJECT_REF>.supabase.co -p 5432 -U postgres -d postgres --no-order --table public.foo --table public.bar
```

## When to Use pg_repack

pg_repack is particularly useful in the following scenarios:

1. **Tables with high bloat**: After many updates/deletes, tables can contain significant unused space
2. **Performance degradation**: When queries slow down due to table fragmentation
3. **Disk space concerns**: When reclaiming space without downtime is needed
4. **Index clustering**: To improve read performance by physically ordering data

## Limitations

- pg_repack cannot reorganize temporary tables
- pg_repack cannot cluster tables by GiST indexes
- You cannot perform DDL commands on the target tables except VACUUM or ANALYZE while pg_repack is working (pg_repack holds an ACCESS SHARE lock on the target table to enforce this restriction)

## Resources

- [Official pg_repack documentation](https://reorg.github.io/pg_repack/)
- [GitHub repository](https://github.com/reorg/pg_repack)
