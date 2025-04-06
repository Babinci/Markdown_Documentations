# HTTP Status Codes in Supabase

Last edited: 2/3/2025

The Supabase platform provides multiple HTTP APIs for each project. These APIs use standard and custom HTTP status codes to indicate the state of the project and the processing status of requests. You can access the status codes returned for requests via the [logs explorer](https://supabase.com/docs/guides/platform/logs#logs-explorer).

## 2XX Success Codes

Status codes in the 2XX range indicate that the request was processed successfully:

| Status Code | Description |
|-------------|-------------|
| 200 | OK - The request has succeeded |
| 201 | Created - The request has succeeded and a new resource has been created |
| 204 | No Content - The request has succeeded but returns no message body |

## 3XX Redirect Codes

Status codes in the 3XX range indicate that the client must take additional action to complete the request. The most common use is to redirect the client to a different location:

| Status Code | Description |
|-------------|-------------|
| 301 | Moved Permanently - The resource has been moved permanently |
| 302 | Found - The resource has been moved temporarily |
| 304 | Not Modified - The client can use its cached version |

## 4XX Client Error Codes

Status codes in the 4XX range indicate an issue with the client's request. These could include:

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - The server cannot process the request due to a client error |
| 401 | Unauthorized - Authentication is required and has failed or not been provided |
| 402 | Service Restriction - See details below |
| 403 | Forbidden - The client does not have access rights to the content |
| 404 | Not Found - The server cannot find the requested resource |
| 405 | Method Not Allowed - The request method is known but not supported |
| 408 | Request Timeout - The server timed out waiting for the request |
| 409 | Conflict - The request conflicts with the current state of the server |
| 429 | Too Many Requests - The user has sent too many requests in a given time (rate limiting) |

### 402 Service Restriction

When the Fair Use Policy is applied, your organization's projects may be restricted from processing requests. In this case, projects will return a 402 status code with a description of why the project is restricted:

- `exceeded_*` indicates that the project has continued to exceed its quota limits (e.g., `exceeded_egress_quota`, `exceeded_db_size_quota`)
- `overdue_payment` indicates that the organization has overdue bills

Even when the Fair Use Policy is applied, you will still have access to your data through the Supabase dashboard.

For more information about the restrictions and how to remove them, see the [Fair Use Policy](https://supabase.com/docs/guides/platform/billing-faq#fair-use-policy) documentation.

## 5XX Server or Project Error Codes

Status codes in the 5XX range indicate that the project was unable to process the request successfully, but not because of an issue with the client's request:

| Status Code | Description |
|-------------|-------------|
| 500 | Internal Server Error - An unexpected condition was encountered |
| 502 | Bad Gateway - The server received an invalid response from an upstream server |
| 503 | Service Unavailable - The server is not ready to handle the request |
| 504 | Gateway Timeout - The server did not receive a timely response from an upstream server |

These errors often occur when a project doesn't have enough [compute resources](https://supabase.com/docs/guides/platform/compute-add-ons) to process complex requests or handle high request volumes.

## 54X Custom Project Error Codes

Supabase uses custom 54X status codes to indicate specific project states:

### 540 Project Paused

The project the request was made against has been paused and cannot process requests until it is unpaused by the owner.

Free Plan projects may be paused due to:
- Inactivity
- Owner request
- Policy violations (in rare instances)

### 544 Project API Gateway Timeout

The request was not completed within the configured time limit.

These timeout limits prevent long-running queries that can cause performance issues, increase latency, and potentially crash the project.

### 546 Edge Functions Resource Limit

This code applies only to Edge Functions and indicates that function execution was stopped due to exceeding a resource limit (`WORKER_LIMIT`).

The Edge Function logs should provide details about which specific [resource limit](https://supabase.com/docs/guides/functions/limits) was exceeded, such as:
- Memory limit
- CPU time limit
- Execution duration
- Network operation limits
