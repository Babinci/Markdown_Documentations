# Replicate to Another Postgres Database Using Logical Replication

This guide shows how to set up logical replication from your Supabase database to an external Postgres database.

## Prerequisites

For this example, you will need:

- A Supabase project
- A Postgres database (running v10 or newer)

You will be running commands on both of these databases to publish changes from the Supabase database to the external database.

## Steps

### 1. Create a Publication on the Supabase Database

```sql
CREATE PUBLICATION example_pub;
```

### 2. Create a Replication Slot on the Supabase Database

```sql
SELECT pg_create_logical_replication_slot('example_slot', 'pgoutput');
```

### 3. Subscribe to the Publication from the External Database

This will need a direct connection to your database. You can find the connection info in the [Dashboard](https://supabase.com/dashboard/project/_/settings/database).

You will also need to ensure that IPv6 is supported by your replication destination.

If you would prefer not to use the `postgres` user, you can run `CREATE ROLE <user> WITH REPLICATION;` using the `postgres` user.

```sql
CREATE SUBSCRIPTION example_sub
CONNECTION 'host=db.oaguxblfdassqxvvwtfe.supabase.co user=postgres password=YOUR_PASS dbname=postgres'
PUBLICATION example_pub
WITH (copy_data = true, create_slot=false, slot_name=example_slot);
```

- `create_slot` is set to `false` because `slot_name` is provided and the slot was already created in Step 2.
- To copy data from before the slot was created, set `copy_data` to `true`.

### 4. Add Tables to the Publication

Add all the tables that you want to replicate to the publication:

```sql
ALTER PUBLICATION example_pub ADD TABLE example_table;
```

### 5. Check the Replication Status

You can check the replication status using `pg_stat_replication`:

```sql
SELECT * FROM pg_stat_replication;
```
