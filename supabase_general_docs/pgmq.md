# PGMQ Extension

PGMQ (PostgreSQL Message Queue) is a lightweight message queue built on Postgres.

## Features

- Lightweight - No background worker or external dependencies, just Postgres functions packaged in an extension
- "Exactly once" delivery of messages to a consumer within a visibility timeout
- API parity with AWS SQS and RSMQ
- Messages stay in the queue until explicitly removed
- Messages can be archived, instead of deleted, for long-term retention and replayability

## Enable the extension

```sql
create extension pgmq;
```

## Usage

### Queue management

#### `create`

Create a new queue.

```sql
pgmq.create(queue_name text) returns void
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| queue_name | text | The name of the queue |

Example:

```sql
select from pgmq.create('my_queue');
```

#### `create_unlogged`

Creates an unlogged table. This is useful when write throughput is more important than durability.
See Postgres documentation for [unlogged tables](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-UNLOGGED) for more information.

```sql
pgmq.create_unlogged(queue_name text) returns void
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| queue_name | text | The name of the queue |

Example:

```sql
select pgmq.create_unlogged('my_unlogged');
```

#### `detach_archive`

Drop the queue's archive table as a member of the PGMQ extension. Useful for preventing the queue's archive table from being drop when `drop extension pgmq` is executed.
This does not prevent the further archives() from appending to the archive table.

```sql
pgmq.detach_archive(queue_name text)
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| queue_name | text | The name of the queue |

Example:

```sql
select * from pgmq.detach_archive('my_queue');
```

#### `drop_queue`

Deletes a queue and its archive table.

```sql
pgmq.drop_queue(queue_name text) returns boolean
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| queue_name | text | The name of the queue |

Example:

```sql
select * from pgmq.drop_queue('my_unlogged');
```

### Sending messages

#### `send`

Send a single message to a queue.

```sql
pgmq.send(
    queue_name text,
    msg jsonb,
    delay integer default 0
) returns setof bigint
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `msg` | `jsonb` | The message to send to the queue |
| `delay` | `integer` | Time in seconds before the message becomes visible. Defaults to 0. |

Example:

```sql
select * from pgmq.send('my_queue', '{"hello": "world"}');
```

#### `send_batch`

Send 1 or more messages to a queue.

```sql
pgmq.send_batch(
    queue_name text,
    msgs jsonb[],
    delay integer default 0
) returns setof bigint
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `msgs` | `jsonb[]` | Array of messages to send to the queue |
| `delay` | `integer` | Time in seconds before the messages becomes visible. Defaults to 0. |

Example:

```sql
select * from pgmq.send_batch(
    'my_queue',
    array[
      '{"hello": "world_0"}'::jsonb,
      '{"hello": "world_1"}'::jsonb
    ]
);
```

### Reading messages

#### `read`

Read 1 or more messages from a queue. The VT specifies the delay in seconds between reading and the message becoming invisible to other consumers.

```sql
pgmq.read(
    queue_name text,
    vt integer,
    qty integer
) returns setof pgmq.message_record
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `vt` | `integer` | Time in seconds that the message become invisible after reading |
| `qty` | `integer` | The number of messages to read from the queue. Defaults to 1 |

Example:

```sql
select * from pgmq.read('my_queue', 10, 2);
```

#### `read_with_poll`

Same as read(). Also provides convenient long-poll functionality.
When there are no messages in the queue, the function call will wait for `max_poll_seconds` in duration before returning.
If messages reach the queue during that duration, they will be read and returned immediately.

```sql
pgmq.read_with_poll(
    queue_name text,
    vt integer,
    qty integer,
    max_poll_seconds integer default 5,
    poll_interval_ms integer default 100
) returns setof pgmq.message_record
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `vt` | `integer` | Time in seconds that the message become invisible after reading. |
| `qty` | `integer` | The number of messages to read from the queue. Defaults to 1. |
| `max_poll_seconds` | `integer` | Time in seconds to wait for new messages to reach the queue. Defaults to 5. |
| `poll_interval_ms` | `integer` | Milliseconds between the internal poll operations. Defaults to 100. |

Example:

```sql
select * from pgmq.read_with_poll('my_queue', 1, 1, 5, 100);
```

#### `pop`

Reads a single message from a queue and deletes it upon read.

Note: utilization of pop() results in at-most-once delivery semantics if the consuming application does not guarantee processing of the message.

```sql
pgmq.pop(queue_name text) returns setof pgmq.message_record
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| queue_name | text | The name of the queue |

Example:

```sql
select * from pgmq.pop('my_queue');
```

### Deleting/Archiving messages

#### `delete` (single)

Deletes a single message from a queue.

```sql
pgmq.delete(queue_name text, msg_id bigint) returns boolean
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `msg_id` | `bigint` | Message ID of the message to delete |

Example:

```sql
select pgmq.delete('my_queue', 5);
```

#### `delete` (batch)

Delete one or many messages from a queue.

```sql
pgmq.delete(queue_name text, msg_ids bigint[]) returns setof bigint
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `msg_ids` | `bigint[]` | Array of message IDs to delete |

Examples:

Delete two messages that exist:

```sql
select * from pgmq.delete('my_queue', array[2, 3]);
```

Delete two messages, one that exists and one that does not:

```sql
select * from pgmq.delete('my_queue', array[6, 999]);
```

#### `purge_queue`

Permanently deletes all messages in a queue. Returns the number of messages that were deleted.

```sql
pgmq.purge_queue(queue_name text) returns bigint
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| queue_name | text | The name of the queue |

Example:

```sql
select * from pgmq.purge_queue('my_queue');
```

#### `archive` (single)

Removes a single requested message from the specified queue and inserts it into the queue's archive.

```sql
pgmq.archive(queue_name text, msg_id bigint) returns boolean
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `msg_id` | `bigint` | Message ID of the message to archive |

Returns a boolean value indicating success or failure of the operation.

Example:

```sql
select * from pgmq.archive('my_queue', 1);
```

#### `archive` (batch)

Deletes a batch of requested messages from the specified queue and inserts them into the queue's archive.
Returns an array of message ids that were successfully archived.

```sql
pgmq.archive(queue_name text, msg_ids bigint[]) RETURNS SETOF bigint
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `msg_ids` | `bigint[]` | Array of message IDs to archive |

Examples:

Delete and archive multiple messages:

```sql
select * from pgmq.archive('my_queue', array[1, 2]);
```

Delete messages 4, which exists and 999, which does not exist:

```sql
select * from pgmq.archive('my_queue', array[4, 999]);
```

### Utilities

#### `set_vt`

Sets the visibility timeout of a message to a specified time duration in the future. Returns the record of the message that was updated.

```sql
pgmq.set_vt(
    queue_name text,
    msg_id bigint,
    vt_offset integer
) returns pgmq.message_record
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `msg_id` | `bigint` | ID of the message to set visibility time |
| `vt_offset` | `integer` | Duration from now, in seconds, that the message's VT should be set to |

Example:

```sql
select * from pgmq.set_vt('my_queue', 11, 30);
```

#### `list_queues`

List all the queues that currently exist.

```sql
pgmq.list_queues() RETURNS TABLE(
    queue_name text,
    created_at timestamp with time zone,
    is_partitioned boolean,
    is_unlogged boolean
)
```

Example:

```sql
select * from pgmq.list_queues();
```

#### `metrics`

Get metrics for a specific queue.

```sql
pgmq.metrics(queue_name text) returns table(
    queue_name text,
    queue_length bigint,
    newest_msg_age_sec integer,
    oldest_msg_age_sec integer,
    total_messages bigint,
    scrape_time timestamp with time zone
)
```

**Parameters:**

| Parameter | Type | Description |
| :-- | :-- | :-- |
| queue_name | text | The name of the queue |

**Returns:**

| Attribute | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `queue_length` | `bigint` | Number of messages currently in the queue |
| `newest_msg_age_sec` | `integer` or `null` | Age of the newest message in the queue, in seconds |
| `oldest_msg_age_sec` | `integer` or `null` | Age of the oldest message in the queue, in seconds |
| `total_messages` | `bigint` | Total number of messages that have passed through the queue over all time |
| `scrape_time` | `timestamp with time zone` | The current timestamp |

Example:

```sql
select * from pgmq.metrics('my_queue');
```

#### `metrics_all`

Get metrics for all existing queues.

```sql
pgmq.metrics_all() RETURNS TABLE(
    queue_name text,
    queue_length bigint,
    newest_msg_age_sec integer,
    oldest_msg_age_sec integer,
    total_messages bigint,
    scrape_time timestamp with time zone
)
```

**Returns:**

| Attribute | Type | Description |
| :-- | :-- | :-- |
| `queue_name` | `text` | The name of the queue |
| `queue_length` | `bigint` | Number of messages currently in the queue |
| `newest_msg_age_sec` | `integer` or `null` | Age of the newest message in the queue, in seconds |
| `oldest_msg_age_sec` | `integer` or `null` | Age of the oldest message in the queue, in seconds |
| `total_messages` | `bigint` | Total number of messages that have passed through the queue over all time |
| `scrape_time` | `timestamp with time zone` | The current timestamp |

Example:

```sql
select * from pgmq.metrics_all();
```

### Types

#### `message_record`

The complete representation of a message in a queue.

| Attribute Name | Type | Description |
| :-- | :-- | :-- |
| `msg_id` | `bigint` | Unique ID of the message |
| `read_ct` | `bigint` | Number of times the message has been read. Increments on read(). |
| `enqueued_at` | `timestamp with time zone` | Time that the message was inserted into the queue |
| `vt` | `timestamp with time zone` | Timestamp when the message will become available for consumers to read |
| `message` | `jsonb` | The message payload |

Example:

```
msg_id | read_ct |          enqueued_at          |              vt               |      message
--------+---------+-------------------------------+-------------------------------+--------------------
      1 |       1 | 2023-10-28 19:06:19.941509-05 | 2023-10-28 19:06:27.419392-05 | {"hello": "world"}
```

## Resources

- Official Docs: [pgmq/api](https://tembo.io/pgmq/#creating-a-queue)
