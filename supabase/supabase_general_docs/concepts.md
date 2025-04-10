# Realtime Concepts

This guide explains the core concepts and extensions available in Supabase Realtime for building real-time applications with collaborative/multiplayer functionality.

## Table of Contents

- [Core Extensions](#core-extensions)
- [Channels](#channels)
- [Broadcast](#broadcast)
- [Presence](#presence)
- [Postgres Changes](#postgres-changes)
- [Choosing Between Broadcast and Presence](#choosing-between-broadcast-and-presence)

## Core Extensions

Supabase Realtime includes three core extensions:

- **Broadcast**: Sends rapid, ephemeral messages to other connected clients. You can use it to track mouse movements, for example.
- **Presence**: Sends user state between connected clients. You can use it to show an "online" status, which disappears when a user is disconnected.
- **Postgres Changes**: Receives database changes in real-time.

## Channels

A Channel is the basic building block of Realtime. You can think of a Channel as a chatroom, similar to a Discord or Slack channel, where participants are able to see who's online and send and receive messages.

When you initialize your Supabase Realtime client, you define a `topic` that uniquely references a channel. Clients can bi-directionally send and receive messages over a Channel.

```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient('https://<project>.supabase.co', '<your-anon-key>')
const roomOne = supabase.channel('room-one') // set your topic here
```

## Broadcast

Realtime Broadcast follows the [publish-subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) where a client publishes messages to a channel based on a unique topic. For example, a user could send a message to a channel with topic `room-one`.

```javascript
roomOne.send({
  type: 'broadcast',
  event: 'test',
  payload: { message: 'hello, world' },
})
```

Other clients can receive the message in real-time by subscribing to the Channel with topic `room-one`. These clients continue to receive messages as long as they are subscribed and connected to the same Channel topic.

An example use-case is sharing a user's cursor position with other clients in an online game.

## Presence

Presence can be used to share an individual's state with others within a Channel.

```javascript
const presenceTrackStatus = await roomOne.track({
  user: 'user-1',
  online_at: new Date().toISOString(),
})
```

Each client maintains their own state, and this is then combined into a "shared state" for that Channel topic. It's commonly used for sharing statuses (e.g. "online" or "inactive"). The neat thing about Presence is that if a client is suddenly disconnected (for example, they go offline), their state is automatically removed from the shared state. If you've ever tried to build an "I'm online" feature which handles unexpected disconnects, you'll appreciate how useful this is.

When a new client subscribes to a channel, it will immediately receive the channel's latest state in a single message because the state is held by the Realtime server.

## Postgres Changes

The Postgres Changes extension listens for database changes and sends them to clients. Clients are required to subscribe with a JWT dictating which changes they are allowed to receive based on the database's [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security).

```javascript
const allChanges = supabase
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

Anyone with access to a valid JWT signed with the project's JWT secret is able to listen to your database's changes, unless tables have [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) enabled and policies in place.

Clients can choose to receive `INSERT`, `UPDATE`, `DELETE`, or `*` (all) changes for all changes in a schema, a table in a schema, or a column's value in a table. Your clients should only listen to tables in the `public` schema and you must first enable the tables you want your clients to listen to.

## Choosing Between Broadcast and Presence

We recommend using Broadcast by default, and then Presence when required. Presence utilizes an in-memory conflict-free replicated data type (CRDT) to track and synchronize shared state in an eventually consistent manner. It computes the difference between existing state and new state changes and sends the necessary updates to clients via Broadcast. This is computationally heavy, so you should use it sparingly.

If you use Presence, it's best to throttle your changes so that you are sending updates less frequently.
