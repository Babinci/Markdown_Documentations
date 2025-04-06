# Realtime

Supabase provides a globally distributed [Realtime](https://github.com/supabase/realtime) service that enables you to send and receive messages to connected clients with low latency.

## Features

Supabase Realtime includes three core features:

### Broadcast

[Broadcast](https://supabase.com/docs/guides/realtime/broadcast) allows you to send low-latency messages using the client libraries, REST API, or directly from your database. This is ideal for:

- Chat applications
- Notifications
- Status updates
- Real-time dashboards

### Presence

[Presence](https://supabase.com/docs/guides/realtime/presence) enables you to track and synchronize shared state between users. Use cases include:

- Online user indicators
- Typing indicators
- Collaborative editing status
- User location tracking
- Activity status management

### Postgres Changes

[Postgres Changes](https://supabase.com/docs/guides/realtime/postgres-changes) lets you listen to database changes and send them to authorized users in real-time. This is perfect for:

- Live data updates
- Real-time dashboards
- Collaborative applications
- Data synchronization
- Event-driven architectures

## Implementation

To use Supabase Realtime in your application:

1. **Set up a Supabase project** - Create a project in the Supabase dashboard
2. **Configure Realtime** - Enable Realtime for your tables or set up broadcast channels
3. **Connect clients** - Integrate the Supabase client library in your application
4. **Subscribe to channels** - Listen for events on specific channels

## Examples

### Broadcast Example

```javascript
// Subscribe to a broadcast channel
const channel = supabase.channel('room-1')
  .on('broadcast', { event: 'message' }, (payload) => {
    console.log('New message received:', payload)
  })
  .subscribe()

// Send a message to the channel
await channel.send({
  type: 'broadcast',
  event: 'message',
  payload: { text: 'Hello, world!' }
})
```

### Presence Example

```javascript
// Join a presence channel with user information
const channel = supabase.channel('room-1')
  .on('presence', { event: 'sync' }, () => {
    const state = channel.presenceState()
    console.log('Current users:', state)
  })
  .on('presence', { event: 'join' }, ({ key, newPresences }) => {
    console.log('User joined:', newPresences)
  })
  .on('presence', { event: 'leave' }, ({ key, leftPresences }) => {
    console.log('User left:', leftPresences)
  })
  .subscribe(async (status) => {
    if (status === 'SUBSCRIBED') {
      await channel.track({ user_id: 1, username: 'supabot' })
    }
  })
```

### Postgres Changes Example

```javascript
// Listen to all changes in the messages table
const channel = supabase.channel('schema-db-changes')
  .on('postgres_changes', { 
    event: '*', 
    schema: 'public', 
    table: 'messages' 
  }, (payload) => {
    console.log('Change received:', payload)
  })
  .subscribe()
```

## Demo Applications

Check out [multiplayer.dev](https://multiplayer.dev/), a demo application that showcases Supabase Realtime features including mouse movements and chat messages.

## Resources

- [Supabase Realtime Source Code](https://github.com/supabase/realtime) - View the source code on GitHub
- [Realtime: Multiplayer Edition Blog Post](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability) - Read about the latest features in Supabase Realtime
- [Supabase Realtime Documentation](https://supabase.com/docs/guides/realtime) - Official documentation

## Performance Considerations

For optimal performance with Supabase Realtime:

1. **Limit payload size** - Keep messages as small as possible
2. **Target specific tables and events** - Only subscribe to the changes you need
3. **Implement filtering** - Use filters to reduce unnecessary message processing
4. **Handle reconnections** - Implement reconnection logic for dropped connections
5. **Monitor usage** - Keep track of your Realtime usage to stay within plan limits
