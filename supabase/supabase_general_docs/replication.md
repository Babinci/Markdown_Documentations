# Replication

Replication is a technique for copying data from one database to another. Supabase uses replication functionality to provide a real-time API, allowing your application to receive database changes as they happen.

## Benefits of Replication

Replication offers several advantages:

- **Load Distribution**: Spread database load across multiple instances, improving performance during high-traffic periods
- **Geographic Optimization**: Reduce latency by placing database replicas closer to users in different regions
- **Real-time Updates**: Enable instant data synchronization across clients and services
- **Fault Tolerance**: Improve system reliability with redundant data copies
- **Analytics**: Create read-only replicas for running complex analytics without affecting your primary database

## Publication Basics

In PostgreSQL, replication is managed through _publications_, which allow you to specify which changes to send to other systems (typically another PostgreSQL database). Publications can be managed through the Supabase Dashboard or using SQL directly.

## Managing Publications in the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Publications** in the sidebar
3. Control which database events are sent by toggling **Insert**, **Update**, and **Delete**
4. Control which tables broadcast changes by selecting **Source** and toggling each table

## SQL Commands for Managing Publications

### Create a Publication for All Tables

This publication contains changes to all tables in the database:

```sql
create publication publication_name
for all tables;
```

### Create a Publication for Specific Tables

```sql
create publication publication_name
for table table_one, table_two;
```

### Add Tables to an Existing Publication

```sql
alter publication publication_name
add table table_name;
```

### Listen to Specific Operations

#### Insert Events Only

```sql
create publication publication_name
for all tables
with (publish = 'insert');
```

#### Update Events Only

```sql
create publication publication_name
for all tables
with (publish = 'update');
```

#### Delete Events Only

```sql
create publication publication_name
for all tables
with (publish = 'delete');
```

### Multiple Operations

You can combine operation types:

```sql
create publication publication_name
for all tables
with (publish = 'insert, update');
```

### Remove a Publication

```sql
drop publication if exists publication_name;
```

### Recreate a Publication

If you're recreating a publication, it's best to do it in a transaction to ensure the operation succeeds:

```sql
begin;
  -- remove the publication
  drop publication if exists publication_name;
  
  -- re-create the publication but don't enable it for any tables
  create publication publication_name;
commit;
```

## Replication with Supabase Realtime

Supabase Realtime uses PostgreSQL's replication functionality to deliver database changes to clients. By default, Supabase creates a publication called `supabase_realtime` that powers the Realtime feature.

### Setting Up Realtime for a Table

To enable Realtime for a specific table:

1. Go to the Database > Replication section in the Supabase Dashboard
2. Find your table under the "Source" dropdown
3. Enable the publication for your table
4. Choose which operations (Insert, Update, Delete) to broadcast

## Advanced Replication Scenarios

### Filtering Replicated Data

You can use Row Level Security (RLS) policies to filter what data gets replicated through Supabase Realtime:

```sql
-- Only replicate rows where status is 'public'
create policy "Only replicate public items"
on items
for select
to authenticated
using (status = 'public');
```

### External Replication Targets

While Supabase primarily uses replication for its Realtime feature, you can set up external replication targets for scenarios like:

- Data warehousing
- Cross-region replication
- Disaster recovery

For these scenarios, you may need to configure a logical replication slot and use tools like `pg_recvlogical` or third-party replication solutions.

## Troubleshooting

### Common Issues

1. **Publication not working**: Verify the publication exists with:
   ```sql
   select * from pg_publication;
   ```

2. **Tables missing from publication**: Check which tables are included:
   ```sql
   select * from pg_publication_tables;
   ```

3. **Replication lag**: If changes are delayed, check for replication lag:
   ```sql
   select * from pg_stat_replication;
   ```

4. **Permissions issues**: Ensure the replication user has appropriate permissions

## Resources

- [PostgreSQL Logical Replication Documentation](https://www.postgresql.org/docs/current/logical-replication.html)
- [Supabase Realtime Documentation](https://supabase.com/docs/guides/realtime)
