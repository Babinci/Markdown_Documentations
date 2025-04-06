# Storage Cache Metrics

This guide explains how to monitor and analyze the cache performance of your Supabase Storage service using the Logs Explorer. Proper monitoring helps you optimize delivery and reduce costs by maximizing cache efficiency.

## Understanding Cache Status Values

Cache status indicators in the logs show how your content is being served:

- **HIT**: Content was served from cache
- **STALE**: Content was served from cache but is outdated
- **REVALIDATED**: Content was updated in cache and served
- **UPDATING**: Content was served from cache while being updated
- **MISS**: Content wasn't in cache and was fetched from origin
- **NONE/UNKNOWN**: Cache status couldn't be determined
- **EXPIRED**: Content was in cache but expired
- **BYPASS**: Caching was explicitly bypassed
- **DYNAMIC**: Content was marked as uncacheable

Any of the first four statuses (**HIT**, **STALE**, **REVALIDATED**, **UPDATING**) are considered cache hits.

## Analyzing Cache Misses

To identify storage objects that aren't being cached effectively, you can run the following query in the [Logs Explorer](https://supabase.com/docs/guides/platform/logs#logs-explorer):

```sql
select
  r.path as path,
  r.search as search,
  count(id) as count
from
  edge_logs as f
  cross join unnest(f.metadata) as m
  cross join unnest(m.request) as r
  cross join unnest(m.response) as res
  cross join unnest(res.headers) as h
where
  starts_with(r.path, '/storage/v1/object')
  and r.method = 'GET'
  and h.cf_cache_status in ('MISS', 'NONE/UNKNOWN', 'EXPIRED', 'BYPASS', 'DYNAMIC')
group by path, search
order by count desc
limit 50;
```

[Try this query in the Logs Explorer](https://supabase.com/dashboard/project/_/logs/explorer?q=%0Aselect%0A++r.path+as+path%2C%0A++r.search+as+search%2C%0A++count%28id%29+as+count%0Afrom%0A++edge_logs+as+f%0A++cross+join+unnest%28f.metadata%29+as+m%0A++cross+join+unnest%28m.request%29+as+r%0A++cross+join+unnest%28m.response%29+as+res%0A++cross+join+unnest%28res.headers%29+as+h%0Awhere%0A++starts_with%28r.path%2C+%27%2Fstorage%2Fv1%2Fobject%27%29%0A++and+r.method+%3D+%27GET%27%0A++and+h.cf_cache_status+in+%28%27MISS%27%2C+%27NONE%2FUNKNOWN%27%2C+%27EXPIRED%27%2C+%27BYPASS%27%2C+%27DYNAMIC%27%29%0Agroup+by+path%2C+search%0Aorder+by+count+desc%0Alimit+50%3B)

This query will show you:
- Which storage objects are frequently accessed but not cached
- The query parameters used when accessing these objects
- How many times each uncached path was requested

## Measuring Cache Hit Ratio Over Time

To track your cache efficiency over time, use this query to calculate your hourly cache hit ratio:

```sql
select
  timestamp_trunc(timestamp, hour) as timestamp,
  countif(h.cf_cache_status in ('HIT', 'STALE', 'REVALIDATED', 'UPDATING')) / count(f.id) as ratio
from
  edge_logs as f
  cross join unnest(f.metadata) as m
  cross join unnest(m.request) as r
  cross join unnest(m.response) as res
  cross join unnest(res.headers) as h
where starts_with(r.path, '/storage/v1/object') and r.method = 'GET'
group by timestamp
order by timestamp desc;
```

[Try this query in the Logs Explorer](https://supabase.com/dashboard/project/_/logs/explorer?q=%0Aselect%0A++timestamp_trunc%28timestamp%2C+hour%29+as+timestamp%2C%0A++countif%28h.cf_cache_status+in+%28%27HIT%27%2C+%27STALE%27%2C+%27REVALIDATED%27%2C+%27UPDATING%27%29%29+%2F+count%28f.id%29+as+ratio%0Afrom%0A++edge_logs+as+f%0A++cross+join+unnest%28f.metadata%29+as+m%0A++cross+join+unnest%28m.request%29+as+r%0A++cross+join+unnest%28m.response%29+as+res%0A++cross+join+unnest%28res.headers%29+as+h%0Awhere+starts_with%28r.path%2C+%27%2Fstorage%2Fv1%2Fobject%27%29+and+r.method+%3D+%27GET%27%0Agroup+by+timestamp%0Aorder+by+timestamp+desc%3B)

This query:
- Groups storage object requests by hour
- Calculates what percentage were served from cache
- Orders results with the most recent hours first

## Improving Cache Performance

If your cache hit ratio is low, consider these optimizations:

1. **Set appropriate cache-control headers** when uploading files
2. **Use consistent URL structures** for accessing objects
3. **Minimize query parameters** that aren't necessary
4. **Use image transformations with caching** for different sizes
5. **Implement versioning in filenames** rather than using cache-busting query parameters

A higher cache hit ratio means less origin fetches, which typically results in:
- Faster content delivery
- Lower bandwidth costs 
- Reduced load on your database
