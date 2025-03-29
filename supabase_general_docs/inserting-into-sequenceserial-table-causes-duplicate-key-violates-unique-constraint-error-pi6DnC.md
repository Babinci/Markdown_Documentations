# Resolving "Duplicate Key Violates Unique Constraint" Errors with Serial Columns

If you are receiving the below error for an auto-incremented table:

> ERROR: duplicate key violates unique constraint

it likely means that the table's sequence has somehow become out of sync, likely because of a mass import process (or something along those lines).

Call it a "bug by design", but it seems that you have to manually reset the primary key index after restoring from a dump file.

## Checking if your sequence is out of sync

You can run the following commands on your database to see if your sequence is out-of-sync:

```sql
SELECT MAX(<sequenced_column>) FROM <table_name>;
SELECT nextval(pg_get_serial_sequence('<public.table_name>', '<sequenced_column_name>'));
```

If the values are off by more than 1, you need to resynchronize your sequence.

## Creating a backup

Before making changes, back up your PostgreSQL database by restarting in the [General Settings](https://supabase.com/dashboard/project/_/settings/general) (just in case). When you restore your database, you will have a backup saved. Alternatively, you can also just download your properties table instead as a backup.

## Resetting the sequence

Then you can run this SQL command to fix the issue:

```sql
SELECT SETVAL('public.<table_name>_<column_name>_seq', (SELECT MAX(<column_name>) FROM <table_name>)+1);
```

This will set the sequence to the next available value that's higher than any existing primary key in the sequence, allowing new inserts to work properly without conflicts.
