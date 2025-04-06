# HTTP: RESTful Client Extension for PostgreSQL

The `http` extension allows you to call RESTful endpoints directly from within PostgreSQL functions and queries. This powerful capability enables your database to interact with external services without needing an intermediate application layer.

## Overview

The extension lets you make HTTP requests to external services using standard REST protocols:

- **GET** - Read-only access to a resource
- **POST** - Create a new resource
- **DELETE** - Remove a resource
- **PUT** - Update an existing resource or create a new resource
- **HEAD** - Similar to GET but only retrieves headers

With this functionality, you can build database functions that fetch real-time data or trigger external services directly from your Supabase database.

## Enabling the Extension

You can enable the `http` extension through the Supabase Dashboard:

1. Navigate to the [Database](https://supabase.com/dashboard/project/_/database/tables) page
2. Click on **Extensions** in the sidebar
3. Search for `http` and enable the extension

Alternatively, you can enable it with SQL:

```sql
CREATE EXTENSION http WITH SCHEMA extensions;
```

## Available Functions

While the main function is `http('http_request')`, the extension provides 5 wrapper functions for specific HTTP methods:

| Function | Description |
|----------|-------------|
| `http_get()` | Makes a GET request |
| `http_post()` | Makes a POST request |
| `http_put()` | Makes a PUT request |
| `http_delete()` | Makes a DELETE request |
| `http_head()` | Makes a HEAD request |

## Response Structure

A successful call to a web URL returns a record with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `status` | integer | HTTP status code of the response |
| `content_type` | character varying | Content type header value |
| `headers` | http_header[] | Array of response headers |
| `content` | character varying | Response body (typically cast to `jsonb` using `content::jsonb`) |

## Examples

### Simple GET Request

Retrieve a single todo item from a public API:

```sql
SELECT 
  status, 
  content::jsonb
FROM 
  http_get('https://jsonplaceholder.typicode.com/todos/1');
```

### POST Request with JSON Body

Create a new resource on a public API:

```sql
SELECT 
  status, 
  content::jsonb
FROM 
  http_post(
    'https://jsonplaceholder.typicode.com/posts',
    '{ "title": "foo", "body": "bar", "userId": 1 }',
    'application/json'
  );
```

### Using with Headers

Make a request with custom headers:

```sql
SELECT
  status,
  content::jsonb
FROM
  http((
    'GET',
    'https://api.example.com/data',
    ARRAY[
      ('Authorization'::text, 'Bearer your-token-here'::text),
      ('Content-Type'::text, 'application/json'::text)
    ],
    NULL,
    NULL
  )::http_request);
```

## Practical Applications

- Fetch exchange rates or financial data in real-time
- Send notifications through 3rd party services
- Synchronize data with external systems
- Trigger webhooks from database functions
- Enrich database records with external API data

## Security Considerations

- The database user running the function needs network access to the external services
- Consider timeouts for external API calls
- Handle errors gracefully to prevent database query failures
- Credentials in functions should be properly secured

## Resources

- [Official `http` GitHub Repository](https://github.com/pramsey/pgsql-http)
- [Video Tutorial: Using PostgreSQL functions to call an API with Supabase](https://www.youtube.com/watch?v=rARgrELRCwY)
