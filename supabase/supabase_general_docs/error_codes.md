# Realtime Operational Error Codes

This reference guide provides a comprehensive list of operational error codes for Supabase Realtime, helping you understand deployment and usage issues.

## Error Code Reference Table

| Code | Description | Action |
| --- | --- | --- |
| `RealtimeDisabledForConfiguration` | The configuration provided to Realtime on connect will not be able to provide you any Postgres Changes | Verify your configuration on channel startup as you might not have your tables properly registered |
| `TenantNotFound` | The tenant you are trying to connect to does not exist | Verify the tenant name you are trying to connect to exists in the realtime.tenants table |
| `ErrorConnectingToWebSocket` | Error when trying to connect to the WebSocket server | Verify user information on connect |
| `ErrorAuthorizingWebSocket` | Error when trying to authorize the WebSocket connection | Verify user information on connect |
| `TableHasSpacesInName` | The table you are trying to listen to has spaces in its name which we are unable to support | Change the table name to not have spaces in it |
| `UnableToDeleteTenant` | Error when trying to delete a tenant | Contact Support |
| `UnableToSetPolicies` | Error when setting up Authorization Policies | Contact Support |
| `UnableCheckoutConnection` | Error when trying to checkout a connection from the tenant pool | Contact Support |
| `UnableToSubscribeToPostgres` | Error when trying to subscribe to Postgres changes | Contact Support |
| `ChannelRateLimitReached` | The number of channels you can create has reached its limit | Contact support to increase your rate limits |
| `ConnectionRateLimitReached` | The number of connected clients as reached its limit | Contact support to increase your rate limits |
| `ClientJoinRateLimitReached` | The rate of joins per second from your clients as reached the channel limits | Contact support to increase your rate limits |
| `UnableToConnectToTenantDatabase` | Realtime was not able to connect to the tenant's database | Contact support for further instructions |
| `RealtimeNodeDisconnected` | Realtime is a distributed application and this means that one the system is unable to communicate with one of the distributed nodes | Contact support for further instructions |
| `MigrationsFailedToRun` | Error when running the migrations against the Tenant database that are required by Realtime | Contact support for further instructions |
| `ErrorStartingPostgresCDCStream` | Error when starting the Postgres CDC stream which is used for Postgres Changes | Contact support for further instructions |
| `UnknownDataProcessed` | An unknown data type was processed by the Realtime system | Contact support for further instructions |
| `ErrorStartingPostgresCDC` | Error when starting the Postgres CDC extension which is used for Postgres Changes | Contact support for further instructions |
| `ReplicationSlotBeingUsed` | The replication slot is being used by another transaction | Contact support for further instructions |
| `PoolingReplicationPreparationError` | Error when preparing the replication slot | Contact support for further instructions |
| `PoolingReplicationError` | Error when pooling the replication slot | Contact support for further instructions |
| `SubscriptionDeletionFailed` | Error when trying to delete a subscription for Postgres changes | Contact support for further instructions |
| `UnableToDeletePhantomSubscriptions` | Error when trying to delete subscriptions that are no longer being used | Contact support for further instructions |
| `UnableToCheckProcessesOnRemoteNode` | Error when trying to check the processes on a remote node | Contact support for further instructions |
| `UnableToCreateCounter` | Error when trying to create a counter to track rate limits for a tenant | Contact support for further instructions |
| `UnableToIncrementCounter` | Error when trying to increment a counter to track rate limits for a tenant | Contact support for further instructions |
| `UnableToDecrementCounter` | Error when trying to decrement a counter to track rate limits for a tenant | Contact support for further instructions |
| `UnableToUpdateCounter` | Error when trying to update a counter to track rate limits for a tenant | Contact support for further instructions |
| `UnableToFindCounter` | Error when trying to find a counter to track rate limits for a tenant | Contact support for further instructions |
| `UnhandledProcessMessage` | Unhandled message received by a Realtime process | Contact support for further instructions |
| `UnknownError` | An unknown error occurred | Contact support for further instructions |

## Common Error Troubleshooting

### Rate Limit Errors

If you encounter any of these errors:
- `ChannelRateLimitReached`
- `ConnectionRateLimitReached`
- `ClientJoinRateLimitReached`

Consider these solutions:
1. Optimize your client connection strategy to reduce simultaneous connections
2. Implement connection pooling if applicable
3. Contact Supabase support to discuss increasing your rate limits

### Configuration Errors

For errors like:
- `RealtimeDisabledForConfiguration`
- `TableHasSpacesInName`

Check your channel configuration and table naming conventions:
1. Ensure tables are properly registered for Postgres Changes
2. Rename tables to avoid spaces and special characters
3. Verify your Realtime subscription settings

### System-Level Errors

Most other errors in the table above require Supabase support assistance. When contacting support about these errors:
1. Include the specific error code
2. Describe your Realtime implementation and usage
3. Share any relevant logs or timestamps when the error occurred
