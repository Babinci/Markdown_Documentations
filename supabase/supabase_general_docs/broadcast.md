# Broadcast

Broadcast lets you send low-latency messages using the client libraries, REST, or your Database.

## Table of Contents

- [Subscribe to messages](#subscribe-to-messages)
  - [Initialize the client](#initialize-the-client)
  - [Receiving Broadcast messages](#receiving-broadcast-messages)
- [Send messages](#send-messages)
  - [Broadcast using the client libraries](#broadcast-using-the-client-libraries)
  - [Broadcast from the Database](#broadcast-from-the-database)
  - [Broadcast using the REST API](#broadcast-using-the-rest-api)
- [Broadcast options](#broadcast-options)
  - [Self-send messages](#self-send-messages)
  - [Acknowledge messages](#acknowledge-messages)

## Subscribe to messages

You can use the Supabase client libraries to receive Broadcast messages.

### Initialize the client

Go to your Supabase project's [API Settings](https://supabase.com/dashboard/project/_/settings/api) and grab the `URL` and `anon` public API key.

```javascript
import { createClient } from '@supabase/supabase-js'

const SUPABASE_URL = 'https://<project>.supabase.co'
const SUPABASE_KEY = '<your-anon-key>'

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)
```

### Receiving Broadcast messages

You can provide a callback for the `broadcast` channel to receive message. This example will receive any `broadcast` messages that are sent to `test-channel`:

```javascript
// Join a room/topic. Can be anything except for 'realtime'.
const myChannel = supabase.channel('test-channel')

// Simple function to log any messages we receive
function messageReceived(payload) {
  console.log(payload)
}

// Subscribe to the Channel
myChannel
  .on(
    'broadcast',
    { event: 'shout' }, // Listen for "shout". Can be "*" to listen to all events
    (payload) => messageReceived(payload)
  )
  .subscribe()
```

## Send messages

### Broadcast using the client libraries

You can use the Supabase client libraries to send Broadcast messages.

```javascript
const myChannel = supabase.channel('test-channel')

/**
 * Sending a message before subscribing will use HTTP
 */
myChannel
  .send({
    type: 'broadcast',
    event: 'shout',
    payload: { message: 'Hi' },
  })
  .then((resp) => console.log(resp))

/**
 * Sending a message after subscribing will use Websockets
 */
myChannel.subscribe((status) => {
  if (status !== 'SUBSCRIBED') {
    return null
  }
  
  myChannel.send({
    type: 'broadcast',
    event: 'shout',
    payload: { message: 'Hi' },
  })
})
```

### Broadcast from the Database

This feature is in Public Alpha. [Submit a support ticket](https://supabase.help/) if you have any issues.

You can send messages directly from your database using the `realtime.send()` function:

```sql
select
  realtime.send(
    jsonb_build_object('hello', 'world'), -- JSONB Payload
    'event', -- Event name
    'topic', -- Topic
    false -- Public / Private flag
  );
```

It's a common use case to broadcast messages when a record is created, updated, or deleted. We provide a helper function specific to this use case, `realtime.broadcast_changes()`. For more details, check out the [Subscribing to Database Changes](https://supabase.com/docs/guides/realtime/subscribing-to-database-changes) guide.

### Broadcast using the REST API

You can send a Broadcast message by making an HTTP request to Realtime servers.

```bash
curl -v \
-H 'apikey: <SUPABASE_TOKEN>' \
-H 'Content-Type: application/json' \
--data-raw '{
  "messages": [
    {
      "topic": "test",
      "event": "event",
      "payload": { "test": "test" }
    }
  ]
}' \
'https://<PROJECT_REF>.supabase.co/realtime/v1/api/broadcast'
```

## Broadcast options

You can pass configuration options while initializing the Supabase Client.

### Self-send messages

By default, broadcast messages are only sent to other clients. You can broadcast messages back to the sender by setting Broadcast's `self` parameter to `true`.

```javascript
const myChannel = supabase.channel('room-2', {
  config: {
    broadcast: { self: true },
  },
})

myChannel.on(
  'broadcast',
  { event: 'test-my-messages' },
  (payload) => console.log(payload)
)

myChannel.subscribe((status) => {
  if (status !== 'SUBSCRIBED') { return }
  
  channelC.send({
    type: 'broadcast',
    event: 'test-my-messages',
    payload: { message: 'talking to myself' },
  })
})
```

### Acknowledge messages

You can confirm that the Realtime servers have received your message by setting Broadcast's `ack` config to `true`.

```javascript
const myChannel = supabase.channel('room-3', {
  config: {
    broadcast: { ack: true },
  },
})

myChannel.subscribe(async (status) => {
  if (status !== 'SUBSCRIBED') { return }
  
  const serverResponse = await myChannel.send({
    type: 'broadcast',
    event: 'acknowledge',
    payload: {},
  })
  
  console.log('serverResponse', serverResponse)
})
```

Use this to guarantee that the server has received the message before resolving `channelD.send`'s promise. If the `ack` config is not set to `true` when creating the channel, the promise returned by `channelD.send` will resolve immediately.
