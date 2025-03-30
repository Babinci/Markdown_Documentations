# Realtime Protocol

The Realtime Protocol is a set of message formats used for communication over a WebSocket connection between a Realtime client and server. These messages are used to initiate a connection, update access tokens, receive system status updates, and receive real-time updates from the Postgres database.

## Connection

In the initial message, the client sends a message specifying the features they want to use (Broadcast, Presence, Postgres Changes).

```json
{
   "event": "phx_join",
   "topic": string,
   "payload": {
      "config": {
         "broadcast": {
            "self": boolean
         },
         "presence": {
            "key": string
         },
         "postgres_changes": [
            {
               "event": "*" | "INSERT" | "UPDATE" | "DELETE",
               "schema": string,
               "table": string,
               "filter": string + '=' + "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "in" +  '.' + string
            }
         ]
      }
   },
   "ref": string
}
```

The `in` filter has the format `COLUMN_NAME=in.(value1,value2,value3)`. However, other filters use the format `COLUMN_NAME=FILTER_NAME.value`.

In response, the server sends the Postgres configuration with a unique ID. With this ID, the client should route incoming changes to the appropriate callback.

```json
{
   "event": "phx_reply",
   "topic": string,
   "payload": {
      "response": {
         "postgres_changes": [
            {
               "id": number,
               "event": "*" | "INSERT" | "UPDATE" | "DELETE",
               "schema": string,
               "table": string,
               "filter": string + '=' + "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "in" +  '.' + string
            }
         ]
      },
      "status": "ok" | "error"
   },
   "ref": string
}
```

## System Messages

System messages are used to inform a client about the status of the Postgres subscription. The `payload.status` indicates if the subscription was successful or not.
The body of the `payload.message` can be "Subscribed to Postgres" or "Subscribing to Postgres failed" with subscription params.

```json
{
   "event": "system",
   "topic": string,
   "payload":{
      "channel": string,
      "extension": "postgres_changes",
      "message": "Subscribed to PostgreSQL" | "Subscribing to PostgreSQL failed",
      "status": "ok" | "error"
   },
   "ref": null
}
```

## Heartbeat

The heartbeat message should be sent every 30 seconds to avoid a connection timeout.

```json
{
   "event": "heartbeat",
   "topic": "phoenix",
   "payload": {},
   "ref": string
}
```

## Access Token

To update the access token, you need to send to the server a message specifying a new token in the `payload.access_token` value.

```json
{
   "event": "access_token",
   "topic": string,
   "payload":{
      "access_token": string
   },
   "ref": string
}
```

## Postgres CDC Message

Realtime sends a message with the following structure. By default, the payload only includes new record changes, and the `old` entry includes the changed row's primary id. If you want to receive old records, you can set the replicate identity of your table to full. Check out [this section of the guide](https://supabase.com/docs/guides/realtime/postgres-changes#receiving-old-records).

```json
{
   "event": "postgres_changes",
   "topic": string,
   "payload": {
      "data": {
         "schema": string,
         "table": string,
         "commit_timestamp": string,
         "eventType": "*" | "INSERT" | "UPDATE" | "DELETE",
         "new": {"key": "value"},
         "old": {"key": "value"},
         "errors": string | null
      },
      "ids": [number]
   },
   "ref": null
}
```

## Broadcast Message

Structure of the broadcast event:

```json
{
   "event": "broadcast",
   "topic": string,
   "payload": {
      "event": string,
      "payload": {"key": "value"},
      "type": "broadcast"
   },
   "ref": null
}
```

## Presence Message

The Presence events allow clients to monitor the online status of other clients in real-time.

### State Update

After joining, the server sends a `presence_state` message to a client with presence information. The payload field contains keys in UUID format, where each key represents a client and its value is a JSON object containing information about that client.

```json
{
   "event": "presence_state",
   "topic": string,
   "payload": {
      "key": {"metas": [{"phx_ref": string, "name": string, "t": float}]}
   },
   "ref": null
}
```

### Diff Update

After a change to the presence state, such as a client joining or leaving, the server sends a presence_diff message to update the client's view of the presence state. The payload field contains two keys, `joins` and `leaves`, which represent clients that have joined and left, respectively. The values associated with each key are UUIDs of the clients.

```json
{
   "event": "presence_diff",
   "topic": string,
   "payload": {
      "joins": {"metas": [{"phx_ref": string, "name": string, "t": float}]},
      "leaves": {"metas": [{"phx_ref": string, "name": string, "t": float}]}
   },
   "ref": null
}
```

## Resources

- [Realtime Documentation](https://supabase.com/docs/guides/realtime)
- [Postgres Changes](https://supabase.com/docs/guides/realtime/postgres-changes)
- [Broadcast](https://supabase.com/docs/guides/realtime/broadcast)
- [Presence](https://supabase.com/docs/guides/realtime/presence)
