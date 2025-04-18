# Presence

## Share state between users with Realtime Presence

Presence allows you to track and synchronize state between multiple users in real-time. This guide explains how to implement Realtime Presence to track state between multiple users.

## Usage

You can use the Supabase client libraries to track Presence state between users.

### Initialize the client

Go to your Supabase project's [API Settings](https://supabase.com/dashboard/project/_/settings/api) and grab the `URL` and `anon` public API key.

```javascript
import { createClient } from '@supabase/supabase-js'

const SUPABASE_URL = 'https://<project>.supabase.co'
const SUPABASE_KEY = '<your-anon-key>'
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)
```

### Sync and track state

Listen to the `sync`, `join`, and `leave` events triggered whenever any client joins or leaves the channel or changes their slice of state:

```javascript
const roomOne = supabase.channel('room_01')

roomOne
  .on('presence', { event: 'sync' }, () => {
    const newState = roomOne.presenceState()
    console.log('sync', newState)
  })
  .on('presence', { event: 'join' }, ({ key, newPresences }) => {
    console.log('join', key, newPresences)
  })
  .on('presence', { event: 'leave' }, ({ key, leftPresences }) => {
    console.log('leave', key, leftPresences)
  })
  .subscribe()
```

### Sending state

You can send state to all subscribers using `track()`:

```javascript
const roomOne = supabase.channel('room_01')

const userStatus = {
  user: 'user-1',
  online_at: new Date().toISOString(),
}

roomOne.subscribe(async (status) => {
  if (status !== 'SUBSCRIBED') { return }
  const presenceTrackStatus = await roomOne.track(userStatus)
  console.log(presenceTrackStatus)
})
```

A client will receive state from any other client that is subscribed to the same topic (in this case `room_01`). It will also automatically trigger its own `sync` and `join` event handlers.

### Stop tracking

You can stop tracking presence using the `untrack()` method. This will trigger the `sync` and `leave` event handlers.

```javascript
const untrackPresence = async () => {
  const presenceUntrackStatus = await roomOne.untrack()
  console.log(presenceUntrackStatus)
}

untrackPresence()
```

## Presence options

You can pass configuration options while initializing the Supabase Client.

### Presence key

By default, Presence will generate a unique `UUIDv1` key on the server to track a client channel's state. If you prefer, you can provide a custom key when creating the channel. This key should be unique among clients.

```javascript
import { createClient } from '@supabase/supabase-js'

const channelC = supabase.channel('test', {
  config: {
    presence: {
      key: 'userId-123',
    },
  },
})
```

## Resources

- [Supabase Realtime Documentation](https://supabase.com/docs/guides/realtime)
- [Supabase JavaScript Client](https://supabase.com/docs/reference/javascript/introduction)
