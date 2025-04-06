# Postgres Changes

Listen to Postgres changes using Supabase Realtime.

## Quick start

In this example we'll set up a database table, secure it with Row Level Security, and subscribe to all changes using the Supabase client libraries.

### 1. Set up a Supabase project with a 'todos' table

[Create a new project](https://app.supabase.com/) in the Supabase Dashboard.

After your project is ready, create a table in your Supabase database. You can do this with either the Table interface or the [SQL Editor](https://app.supabase.com/project/_/sql).

```sql
-- Create a table called "todos"
-- with a column to store tasks.
create table todos (
  id serial primary key,
  task text
);
```

### 2. Allow anonymous access

In this example we'll turn on [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) for this table and allow anonymous access. In production, be sure to secure your application with the appropriate permissions.

```sql
-- Turn on security
alter table "todos"
enable row level security;

-- Allow anonymous access
create policy "Allow anonymous access"
on todos
for select
to anon
using (true);
```

### 3. Enable Postgres replication

Go to your project's [Publications settings](https://supabase.com/dashboard/project/_/database/publications), and under `supabase_realtime`, toggle on the tables you want to listen to.

### 4. Install the client

Install the Supabase JavaScript client.

```bash
npm install @supabase/supabase-js
```

### 5. Create the client

This client will be used to listen to Postgres changes.

```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  'https://<project>.supabase.co',
  '<your-anon-key>'
)
```

### 6. Listen to changes by schema

Listen to changes on all tables in the `public` schema by setting the `schema` property to 'public' and event name to `*`. The event name can be one of:

- `INSERT`
- `UPDATE`
- `DELETE`
- `*`

The channel name can be any string except 'realtime'.

```javascript
const channelA = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      event: '*',
      schema: 'public',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

### 7. Insert dummy data

Now we can add some data to our table which will trigger the `channelA` event handler.

```sql
insert into todos (task)
values ('Change!');
```

## Usage

You can use the Supabase client libraries to subscribe to database changes.

### Listening to specific schemas

Subscribe to specific schema events using the `schema` parameter:

```javascript
const changes = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      schema: 'public', // Subscribes to the "public" schema in Postgres
      event: '*',       // Listen to all changes
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to `INSERT` events

Use the `event` parameter to listen only to database `INSERT`s:

```javascript
const changes = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT', // Listen only to INSERTs
      schema: 'public',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to `UPDATE` events

Use the `event` parameter to listen only to database `UPDATE`s:

```javascript
const changes = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      event: 'UPDATE', // Listen only to UPDATEs
      schema: 'public',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to `DELETE` events

Use the `event` parameter to listen only to database `DELETE`s:

```javascript
const changes = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      event: 'DELETE', // Listen only to DELETEs
      schema: 'public',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to specific tables

Subscribe to specific table events using the `table` parameter:

```javascript
const changes = supabase
  .channel('table-db-changes')
  .on(
    'postgres_changes',
    {
      event: '*',
      schema: 'public',
      table: 'todos',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

The channel name can be any string except 'realtime'.

### Listening to multiple changes

To listen to different events and schema/tables/filters combinations with the same channel:

```javascript
const channel = supabase
  .channel('db-changes')
  .on(
    'postgres_changes',
    {
      event: '*',
      schema: 'public',
      table: 'messages',
    },
    (payload) => console.log(payload)
  )
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'users',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

### Filtering for specific changes

Use the `filter` parameter for granular changes:

```javascript
const changes = supabase
  .channel('table-filter-changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'todos',
      filter: 'id=eq.1',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

## Available filters

Realtime offers filters so you can specify the data your client receives at a more granular level.

### Equal to (`eq`)

To listen to changes when a column's value in a table equals a client-specified value:

```javascript
const channel = supabase
  .channel('changes')
  .on(
    'postgres_changes',
    {
      event: 'UPDATE',
      schema: 'public',
      table: 'messages',
      filter: 'body=eq.hey',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

This filter uses Postgres's `=` filter.

### Not equal to (`neq`)

To listen to changes when a column's value in a table does not equal a client-specified value:

```javascript
const channel = supabase
  .channel('changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'messages',
      filter: 'body=neq.bye',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

This filter uses Postgres's `!=` filter.

### Less than (`lt`)

To listen to changes when a column's value in a table is less than a client-specified value:

```javascript
const channel = supabase
  .channel('changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'profiles',
      filter: 'age=lt.65',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

This filter uses Postgres's `<` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.

### Less than or equal to (`lte`)

To listen to changes when a column's value in a table is less than or equal to a client-specified value:

```javascript
const channel = supabase
  .channel('changes')
  .on(
    'postgres_changes',
    {
      event: 'UPDATE',
      schema: 'public',
      table: 'profiles',
      filter: 'age=lte.65',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

This filter uses Postgres's `<=` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.

### Greater than (`gt`)

To listen to changes when a column's value in a table is greater than a client-specified value:

```javascript
const channel = supabase
  .channel('changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'products',
      filter: 'quantity=gt.10',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

This filter uses Postgres's `>` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.

### Greater than or equal to (`gte`)

To listen to changes when a column's value in a table is greater than or equal to a client-specified value:

```javascript
const channel = supabase
  .channel('changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'products',
      filter: 'quantity=gte.10',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

This filter uses Postgres's `>=` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.

### Contained in list (`in`)

To listen to changes when a column's value in a table equals any client-specified values:

```javascript
const channel = supabase
  .channel('changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'colors',
      filter: 'name=in.(red, blue, yellow)',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

This filter uses Postgres's `= ANY`. Realtime allows a maximum of 100 values for this filter.

## Receiving `old` records

By default, only `new` record changes are sent but if you want to receive the `old` record (previous values) whenever you `UPDATE` or `DELETE` a record, you can set the `replica identity` of your table to `full`:

```sql
alter table messages replica identity full;
```

RLS policies are not applied to `DELETE` statements, because there is no way for Postgres to verify that a user has access to a deleted record. When RLS is enabled and `replica identity` is set to `full` on a table, the `old` record contains only the primary key(s).

## Private schemas

Postgres Changes works out of the box for tables in the `public` schema. You can listen to tables in your private schemas by granting table `SELECT` permissions to the database role found in your access token. You can run a query similar to the following:

```sql
grant select on "non_private_schema"."some_table" to authenticated;
```

We strongly encourage you to enable RLS and create policies for tables in private schemas. Otherwise, any role you grant access to will have unfettered read access to the table.

## Custom tokens

You may choose to sign your own tokens to customize claims that can be checked in your RLS policies.

Your project JWT secret is found with your [Project API keys](https://app.supabase.com/project/_/settings/api) in your dashboard.

Do not expose the `service_role` token on the client because the role is authorized to bypass row-level security.

To use your own JWT with Realtime make sure to set the token after instantiating the Supabase client and before connecting to a Channel.

```javascript
const { createClient } = require('@supabase/supabase-js')
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY, {})

// Set your custom JWT here
supabase.realtime.setAuth('your-custom-jwt')

const channel = supabase
  .channel('db-changes')
  .on(
    'postgres_changes',
    {
      event: '*',
      schema: 'public',
      table: 'messages',
      filter: 'body=eq.bye',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

### Refreshed tokens

You will need to refresh tokens on your own, but once generated, you can pass them to Realtime.

For example, if you're using the `supabase-js` `v2` client then you can pass your token like this:

```javascript
// Client setup
supabase.realtime.setAuth('fresh-token')
```

## Limitations

### Delete events are not filterable

You can't filter Delete events when tracking Postgres Changes. This limitation is due to the way changes are pulled from Postgres.

### Spaces in table names

Realtime currently does not work when table names contain spaces.

### Database instance and realtime performance

Realtime systems usually require forethought because of their scaling dynamics. For the `Postgres Changes` feature, every change event must be checked to see if the subscribed user has access. For instance, if you have 100 users subscribed to a table where you make a single insert, it will then trigger 100 "reads": one for each user.

There can be a database bottleneck which limits message throughput. If your database cannot authorize the changes rapidly enough, the changes will be delayed until you receive a timeout.

Database changes are processed on a single thread to maintain the change order. That means compute upgrades don't have a large effect on the performance of Postgres change subscriptions. You can estimate the expected maximum throughput for your database below.

If you are using Postgres Changes at scale, you should consider using separate "public" table without RLS and filters. Alternatively, you can use Realtime server-side only and then re-stream the changes to your clients using a Realtime Broadcast.

#### Current maximum possible throughput (based on compute size)

| Compute | Filters | RLS | Clients | Total DB changes/sec | Max messages per client/sec | Max total messages/sec | Latency p95 |
|---------|---------|-----|---------|---------------------|----------------------------|----------------------|------------|
| Micro   | No      | No  | 500     | 64                  | 64                         | 32,000              | 238ms      |
| Small-Medium | No | No  | 5,000   | 128                 | 128                        | 640,000             | 200ms      |
| Large-16XL | No  | No  | 10,000   | 256                 | 256                        | 2,560,000           | 150ms      |
| Micro   | Yes     | No  | 500     | 32                  | 32                         | 16,000              | 350ms      |
| Small-Medium | Yes | No | 5,000   | 64                  | 64                         | 320,000             | 300ms      |
| Large-16XL | Yes | No  | 10,000   | 128                 | 128                        | 1,280,000           | 250ms      |
| Micro   | No      | Yes | 500     | 32                  | 32                         | 16,000              | 350ms      |
| Small-Medium | No | Yes | 5,000   | 64                  | 64                         | 320,000             | 300ms      |
| Large-16XL | No  | Yes | 10,000   | 128                 | 128                        | 1,280,000           | 250ms      |
| Micro   | Yes     | Yes | 500     | 16                  | 16                         | 8,000               | 500ms      |
| Small-Medium | Yes | Yes | 5,000  | 32                  | 32                         | 160,000             | 450ms      |
| Large-16XL | Yes | Yes | 10,000   | 64                  | 64                         | 640,000             | 400ms      |

Don't forget to run your own benchmarks to make sure that the performance is acceptable for your use case.

We are making many improvements to Realtime's Postgres Changes. If you are uncertain about the performance of your use case, reach out using [Support Form](https://supabase.com/dashboard/support/new) and we will be happy to help you. We have a team of engineers that can advise you on the best solution for your use-case.
