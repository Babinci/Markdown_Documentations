# Supabase Realtime

## Table of Contents
- [Introduction](#introduction)
- [Subscribe to Channel](#subscribe-to-channel)
- [Unsubscribe from a Channel](#unsubscribe-from-a-channel)
- [Unsubscribe from All Channels](#unsubscribe-from-all-channels)
- [Retrieve All Channels](#retrieve-all-channels)
- [Broadcast a Message](#broadcast-a-message)
- [Other Documentation Files](#other-documentation-files)

## Introduction

Supabase Realtime allows you to listen to changes in your database in real-time via WebSockets. You can use the realtime functionality to build collaborative and interactive applications.

## Subscribe to Channel

- By default, Broadcast and Presence are enabled for all projects.
- By default, listening to database changes is disabled for new projects due to database performance and security concerns. You can turn it on by managing Realtime's [replication](https://supabase.com/docs/guides/api#realtime-api-overview).
- You can receive the "previous" data for updates and deletes by setting the table's `REPLICA IDENTITY` to `FULL` (e.g., `ALTER TABLE your_table REPLICA IDENTITY FULL;`).
- Row level security is not applied to delete statements. When RLS is enabled and replica identity is set to full, only the primary key is sent to clients.

### Example

```python
channel = supabase.channel("room1")

def on_subscribe(status, err):
    if status == RealtimeSubscribeStates.SUBSCRIBED:
        channel.send_broadcast(
            "cursor-pos", 
            {"x": random.random(), "y": random.random()}
        )

def handle_broadcast(payload):
    print("Cursor position received!", payload)

channel.on_broadcast(event="cursor-pos", callback=handle_broadcast).subscribe(on_subscribe)
```

## Unsubscribe from a Channel

- Removing a channel is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.

### Example

```python
supabase.remove_channel(myChannel)
```

## Unsubscribe from All Channels

- Removing channels is a great way to maintain the performance of your project's Realtime service as well as your database if you're listening to Postgres changes. Supabase will automatically handle cleanup 30 seconds after a client is disconnected, but unused channels may cause degradation as more clients are simultaneously subscribed.

### Example

```python
supabase.remove_all_channels()
```

## Retrieve All Channels

### Example

```python
channels = supabase.get_channels()
```

## Broadcast a Message

Broadcast a message to all connected clients to a channel.

### Example

```python
channel = supabase.channel("room1")

def on_subscribe(status, err):
    if status == RealtimeSubscribeStates.SUBSCRIBED:
        channel.send_broadcast('cursor-pos', {"x": random.random(), "y": random.random()})

channel.subscribe(on_subscribe)
```

## Other Documentation Files

- [Overview](./supabase_overview.md)
- [Database Operations](./supabase_database.md)
- [Query Filters](./supabase_filters.md)
- [Authentication Basics](./supabase_auth_basics.md)
- [OAuth Authentication](./supabase_auth_oauth.md)
- [Multi-factor Authentication](./supabase_auth_mfa.md)
- [Admin Authentication Methods](./supabase_auth_admin.md)
- [Storage](./supabase_storage.md)
- [Edge Functions](./supabase_edge_functions.md)
