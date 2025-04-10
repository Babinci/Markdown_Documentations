# Storage Logs

Accessing the [Storage Logs](https://supabase.com/dashboard/project/__/logs/explorer?q=select+id%2C+storage_logs.timestamp%2C+event_message+from+storage_logs%0A++%0A++order+by+timestamp+desc%0A++limit+100%0A++) allows you to examine all incoming request logs to your Storage service. You can also filter logs and delve into specific aspects of your requests.

## Common log queries

### Filter by status 5XX error

```sql
select
  id,
  storage_logs.timestamp,
  event_message,
  r.statusCode,
  e.message as errorMessage,
  e.raw as rawError
from
  storage_logs
  cross join unnest(metadata) as m
  cross join unnest(m.res) as r
  cross join unnest(m.error) as e
where r.statusCode >= 500
order by timestamp desc
limit 100;
```

### Filter by status 4XX error

```sql
select
  id,
  storage_logs.timestamp,
  event_message,
  r.statusCode,
  e.message as errorMessage,
  e.raw as rawError
from
  storage_logs
  cross join unnest(metadata) as m
  cross join unnest(m.res) as r
  cross join unnest(m.error) as e
where r.statusCode >= 400 and r.statusCode < 500
order by timestamp desc
limit 100;
```

### Filter by method

```sql
select id, storage_logs.timestamp, event_message, r.method
from
  storage_logs
  cross join unnest(metadata) as m
  cross join unnest(m.req) as r
where r.method in ("POST")
order by timestamp desc
limit 100;
```

### Filter by IP address

```sql
select id, storage_logs.timestamp, event_message, r.remoteAddress
from
  storage_logs
  cross join unnest(metadata) as m
  cross join unnest(m.req) as r
where r.remoteAddress in ("IP_ADDRESS")
order by timestamp desc
limit 100;
```
