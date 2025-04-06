# pg_net: Asynchronous Networking

## Introduction

[pg_net](https://github.com/supabase/pg_net/) enables PostgreSQL to make asynchronous HTTP/HTTPS requests in SQL. It differs from the [`http`](https://supabase.com/docs/guides/database/extensions/http) extension in that it is asynchronous by default, making it useful in blocking functions (like triggers).

The extension eliminates the need for servers to continuously poll for database changes and instead allows the database to proactively notify external resources about significant events.

> **Note**: The pg_net API is in beta. Function signatures may change.

## Enable the Extension

### Using the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for "pg_net" and enable the extension

### Using SQL

```sql
CREATE EXTENSION pg_net;
```

## API Functions

### http_get

Creates an HTTP GET request returning the request's ID. HTTP requests are not started until the transaction is committed.

#### Signature

This is a PostgreSQL [SECURITY DEFINER](https://supabase.com/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function.

```sql
net.http_get(
    -- url for the request
    url text,
    -- key/value pairs to be url encoded and appended to the `url`
    params jsonb default '{}'::jsonb,
    -- key/values to be included in request headers
    headers jsonb default '{}'::jsonb,
    -- the maximum number of milliseconds the request may take before being canceled
    timeout_milliseconds int default 2000
)
    -- request_id reference
    returns bigint
    strict
    volatile
    parallel safe
    language plpgsql
```

#### Usage

```sql
SELECT
  net.http_get('https://news.ycombinator.com')
  AS request_id;
```

Result:
```
request_id
----------
         1
(1 row)
```

### http_post

Creates an HTTP POST request with a JSON body, returning the request's ID. HTTP requests are not started until the transaction is committed.

The body's character set encoding matches the database's `server_encoding` setting.

#### Signature

This is a PostgreSQL [SECURITY DEFINER](https://supabase.com/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function.

```sql
net.http_post(
    -- url for the request
    url text,
    -- body of the POST request
    body jsonb default '{}'::jsonb,
    -- key/value pairs to be url encoded and appended to the `url`
    params jsonb default '{}'::jsonb,
    -- key/values to be included in request headers
    headers jsonb default '{"Content-Type": "application/json"}'::jsonb,
    -- the maximum number of milliseconds the request may take before being canceled
    timeout_milliseconds int default 2000
)
    -- request_id reference
    returns bigint
    volatile
    parallel safe
    language plpgsql
```

#### Usage

```sql
SELECT
  net.http_post(
    url:='https://httpbin.org/post',
    body:='{"hello": "world"}'::jsonb
  ) AS request_id;
```

Result:
```
request_id
----------
         1
(1 row)
```

### http_delete

Creates an HTTP DELETE request, returning the request's ID. HTTP requests are not started until the transaction is committed.

#### Signature

This is a PostgreSQL [SECURITY DEFINER](https://supabase.com/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function.

```sql
net.http_delete(
    -- url for the request
    url text,
    -- key/value pairs to be url encoded and appended to the `url`
    params jsonb default '{}'::jsonb,
    -- key/values to be included in request headers
    headers jsonb default '{}'::jsonb,
    -- the maximum number of milliseconds the request may take before being canceled
    timeout_milliseconds int default 2000
)
    -- request_id reference
    returns bigint
    strict
    volatile
    parallel safe
    language plpgsql
    security definer
```

#### Usage

```sql
SELECT
  net.http_delete(
    'https://dummy.restapiexample.com/api/v1/delete/2'
  ) AS request_id;
```

Result:
```
request_id
----------
         1
(1 row)
```

## Analyzing Responses

Waiting requests are stored in the `net.http_request_queue` table. Upon execution, they are deleted.

```sql
CREATE UNLOGGED TABLE
  net.http_request_queue (
    id bigint NOT NULL DEFAULT nextval('net.http_request_queue_id_seq'::regclass),
    method text NOT NULL,
    url text NOT NULL,
    headers jsonb NOT NULL,
    body bytea NULL,
    timeout_milliseconds integer NOT NULL
  )
```

Once a response is returned, by default, it is stored for 6 hours in the `net._http_response` table.

```sql
CREATE UNLOGGED TABLE
  net._http_response (
    id bigint NULL,
    status_code integer NULL,
    content_type text NULL,
    headers jsonb NULL,
    content text NULL,
    timed_out boolean NULL,
    error_msg text NULL,
    created timestamp with time zone NOT NULL DEFAULT now()
  )
```

The responses can be observed with the following query:

```sql
SELECT * FROM net._http_response;
```

The data can also be observed in the `net` schema with the [Supabase Dashboard's SQL Editor](https://supabase.com/dashboard/project/_/editor).

## Debugging Requests

### Inspecting Request Data

The [Postman Echo API](https://documenter.getpostman.com/view/5025623/SWTG5aqV) returns a response with the same body and content as the request. It can be used to inspect the data being sent.

Sending a post request to the echo API:

```sql
SELECT
  net.http_post(
    url := 'https://postman-echo.com/post',
    body := '{"key1": "value", "key2": 5}'::jsonb
  ) AS request_id;
```

Inspecting the echo API response content to ensure it contains the right body:

```sql
SELECT
  "content"
FROM net._http_response
WHERE id = <request_id>
-- returns information about the request
-- including the body sent: {"key1": "value", "key2": 5}
```

Alternatively, by wrapping a request in a [database function](https://supabase.com/docs/guides/database/functions), sent row data can be logged or returned for inspection and debugging:

```sql
CREATE OR REPLACE FUNCTION debugging_example (row_id int)
RETURNS jsonb AS $$
DECLARE
  -- Store payload data
  row_data_var jsonb;
BEGIN
  -- Retrieve row data and convert to JSON
  SELECT to_jsonb("<example_table>".*) INTO row_data_var
  FROM "<example_table>"
  WHERE "<example_table>".id = row_id;

  -- Initiate HTTP POST request to URL
  PERFORM
    net.http_post(
      url := 'https://postman-echo.com/post',
      -- Use row data as payload
      body := row_data_var
    ) AS request_id;

  -- Optionally Log row data or other data for inspection in Supabase Dashboard's Postgres Logs
  RAISE LOG 'Logging an entire row as JSON (%)', row_data_var;

  -- return row data to inspect
  RETURN row_data_var;

-- Handle exceptions here if needed
EXCEPTION
  WHEN others THEN
    RAISE EXCEPTION 'An error occurred: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- calling function
SELECT debugging_example(<row_id>);
```

### Inspecting Failed Requests

Finds all failed requests:

```sql
SELECT
  *
FROM net._http_response
WHERE "status_code" >= 400 OR "error_msg" IS NOT NULL
ORDER BY "created" DESC;
```

## Configuration

> **Note**: You must be on pg_net v0.12.0 or above to reconfigure settings.

Supabase supports reconfiguring pg_net starting from v0.12.0+. For the latest release, initiate a PostgreSQL upgrade in the [Infrastructure Settings](https://supabase.com/dashboard/project/*/settings/infrastructure).

The extension is configured to reliably execute up to 200 requests per second. The response messages are stored for only 6 hours to prevent needless buildup. The default behavior can be modified by rewriting config variables.

### Getting Current Settings

```sql
SELECT
  "name",
  "setting"
FROM pg_settings
WHERE "name" LIKE 'pg_net%';
```

### Altering Settings

Change variables:

```sql
ALTER ROLE "postgres" SET pg_net.ttl TO '24 hours';
ALTER ROLE "postgres" SET pg_net.batch_size TO 500;
```

Then reload the settings and restart the `pg_net` background worker with:

```sql
SELECT net.worker_restart();
```

## Examples

### Invoke a Supabase Edge Function

Make a POST request to a Supabase Edge Function with auth header and JSON body payload:

```sql
SELECT
  net.http_post(
    url:='https://project-ref.supabase.co/functions/v1/function-name',
    headers:='{"Content-Type": "application/json", "Authorization": "Bearer <YOUR_ANON_KEY>"}'::jsonb,
    body:='{"name": "pg_net"}'::jsonb
  ) AS request_id;
```

### Call an Endpoint Every Minute with pg_cron

The [pg_cron](https://supabase.com/docs/guides/database/extensions/pgcron) extension enables PostgreSQL to become its own cron server. With it, you can schedule regular calls with up to a minute precision to endpoints:

```sql
SELECT cron.schedule(
    'cron-job-name',
    '* * * * *', -- Executes every minute (cron syntax)
    $$
        -- SQL query
        SELECT "net"."http_post"(
          -- URL of Edge function
          url:='https://project-ref.supabase.co/functions/v1/function-name',
          headers:='{"Authorization": "Bearer <YOUR_ANON_KEY>"}'::jsonb,
          body:='{"name": "pg_net"}'::jsonb
        ) AS "request_id";
    $$
);
```

### Execute pg_net in a Trigger

Make a call to an external endpoint when a trigger event occurs:

```sql
-- function called by trigger
CREATE OR REPLACE FUNCTION <function_name>()
  RETURNS trigger
  LANGUAGE plpgSQL
AS $$
BEGIN
  -- calls pg_net function net.http_post
  -- sends request to postman API
  PERFORM "net"."http_post"(
    'https://postman-echo.com/post'::text,
    jsonb_build_object(
      'old_row', to_jsonb(old.*),
      'new_row', to_jsonb(new.*)
    ),
    headers:='{"Content-Type": "application/json"}'::jsonb
  ) AS request_id;
  RETURN new;
END $$;

-- trigger for table update
CREATE TRIGGER <trigger_name>
  AFTER UPDATE ON <table_name>
  FOR EACH ROW
  EXECUTE FUNCTION <function_name>();
```

### Send Multiple Table Rows in One Request

```sql
WITH "selected_table_rows" AS (
  SELECT
    -- Converts all the rows into a JSONB array
    jsonb_agg(to_jsonb(<table_name>.*)) AS JSON_payload
  FROM <table_name>
  -- good practice to LIMIT the max amount of rows
)
SELECT
  net.http_post(
    url := 'https://postman-echo.com/post'::text,
    body := JSON_payload
  ) AS request_id
FROM "selected_table_rows";
```

More examples can be seen on the [Extension's GitHub page](https://github.com/supabase/pg_net/).

## Limitations

- To improve speed and performance, the requests and responses are stored in [unlogged tables](https://pgpedia.info/u/unlogged-table.html), which are not preserved during a crash or unclean shutdown.
- By default, response data is saved for only 6 hours
- Can only make POST requests with JSON data. No other data formats are supported
- Intended to handle at most 200 requests per second. Increasing the rate can introduce instability
- Does not have support for PATCH/PUT requests
- Can only work with one database at a time. It defaults to the `postgres` database.

## Resources

- Source code: [github.com/supabase/pg_net](https://github.com/supabase/pg_net/)
- Official Docs: [github.com/supabase/pg_net](https://github.com/supabase/pg_net/)
