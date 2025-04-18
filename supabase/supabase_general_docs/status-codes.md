# Status Codes

Edge Functions can return following status codes.

## 2XX Success

A successful Edge Function Response

## 3XX Redirect

The Edge Function has responded with a `Response.redirect` [API docs](https://developer.mozilla.org/en-US/docs/Web/API/Response/redirect_static)

## 4XX Client Errors

### 401 Unauthorized

If the Edge Function has `Verify JWT` option enabled, but the request was made with an invalid JWT.

### 404 Not Found

Requested Edge Function was not found.

### 405 Method Not Allowed

Edge Functions only support these HTTP methods: 'POST', 'GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'

## 5XX Server Errors

### 500 Internal Server Error

Edge Function threw an uncaught exception (`WORKER_ERROR`). Check Edge Function logs to find the cause.

### 503 Service Unavailable

Edge Function failed to start (`BOOT_ERROR`). Check Edge Function logs to find the cause.

### 504 Gateway Timeout

Edge Function didn't respond before the [request idle timeout](https://supabase.com/docs/guides/functions/limits).

### 546 Resource Limit (Custom Error Code)

Edge Function execution was stopped due to a resource limit (`WORKER_LIMIT`). Edge Function logs should provide which [resource limit](https://supabase.com/docs/guides/functions/limits) was exceeded.
