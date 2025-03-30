# Subscribing to Database Changes

Listen to database changes in real-time from your website or application.

You can use Supabase to subscribe to real-time database changes. There are two options available:

1. [Broadcast](https://supabase.com/docs/guides/realtime/broadcast). This is the recommended method for scalability and security.
2. [Postgres Changes](https://supabase.com/docs/guides/realtime/postgres-changes). This is a simpler method. It requires less setup, but does not scale as well as Broadcast.

## Using Broadcast

To automatically send messages when a record is created, updated, or deleted, we can attach a [Postgres trigger](https://supabase.com/docs/guides/database/postgres/triggers) to any table. Supabase Realtime provides a `realtime.broadcast_changes()` function which we can use in conjunction with a trigger.

### Broadcast Authorization

[Realtime Authorization](https://supabase.com/docs/guides/realtime/authorization) is required for receiving Broadcast messages. This is an example of a policy that allows authenticated users to listen to messages from topics:

```sql
create policy "Authenticated users can receive broadcasts"
on "realtime"."messages"
for select
to authenticated
using ( true );
```

### Create a Trigger Function

Let's create a function that we can call any time a record is created, updated, or deleted. This function will make use of some of Postgres's native [trigger variables](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-DML-TRIGGER). For this example, we want to have a topic with the name `topic:<record id>` to which we're going to broadcast events.

```sql
create or replace function public.your_table_changes()
returns trigger
language plpgsql
as $$
begin
  perform realtime.broadcast_changes(
    'topic:' || coalesce(NEW.topic, OLD.topic) ::text, -- topic - the topic to which we're broadcasting
    TG_OP,                                             -- event - the event that triggered the function
    TG_OP,                                             -- operation - the operation that triggered the function
    TG_TABLE_NAME,                                     -- table - the table that caused the trigger
    TG_TABLE_SCHEMA,                                   -- schema - the schema of the table that caused the trigger
    NEW,                                               -- new record - the record after the change
    OLD                                                -- old record - the record before the change
  );
  return null;
end;
$$;
```

### Create a Trigger

Let's set up a trigger so the function is executed after any changes to the table.

```sql
create trigger handle_your_table_changes
after insert or update or delete
on public.your_table
for each row
execute function your_table_changes ();
```

#### Listening on Client Side

Finally, on the client side, listen to the topic `topic:<record_id>` to receive the events. Remember to set the channel as a private channel, since `realtime.broadcast_changes` uses Realtime Authorization.

```javascript
const gameId = 'id'
await supabase.realtime.setAuth() // Needed for Realtime Authorization
const changes = supabase
  .channel(`topic:${gameId}`, {
    config: { private: true },
  })
  .on('broadcast', { event: 'INSERT' }, (payload) => console.log(payload))
  .on('broadcast', { event: 'UPDATE' }, (payload) => console.log(payload))
  .on('broadcast', { event: 'DELETE' }, (payload) => console.log(payload))
  .subscribe()
```

## Using Postgres Changes

Postgres Changes are simple to use, but have some [limitations](https://supabase.com/docs/guides/realtime/postgres-changes#limitations) as your application scales. We recommend using Broadcast for most use cases.

### Enable Postgres Changes

You'll first need to create a `supabase_realtime` publication and add your tables (that you want to subscribe to) to the publication:

```sql
begin;
-- remove the supabase_realtime publication
drop  publication if exists supabase_realtime;

-- re-create the supabase_realtime publication with no tables
create publication supabase_realtime;
commit;

-- add a table called 'messages' to the publication
-- (update this to match your tables)
alter  publication supabase_realtime add table messages;
```

### Streaming Inserts

You can use the `INSERT` event to stream all new rows.

```javascript
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY)

const channel = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

### Streaming Updates

You can use the `UPDATE` event to stream all updated rows.

```javascript
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY)

const channel = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      event: 'UPDATE',
      schema: 'public',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```

## Video Tutorial

For a visual guide on how to subscribe to real-time database changes, watch the [How to subscribe to real-time changes on your database](https://www.youtube.com/watch?v=2rUjcmgZDwQ) tutorial on YouTube.
