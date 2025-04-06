# How to Change Max Database Connections

Last edited: 2/21/2025

> **WARNING**: Manually configuring the connection count hard-codes it. If you upgrade or downgrade your database, the connection count will not auto-resize. You must manually update it after changing compute tiers.

## Default Connection Limits

Each compute instance has default settings for direct connections and pooler connections. Here are the current limits:

| Compute Size | Direct Connections | Pooler Connections |
| --- | --- | --- |
| Nano (free) | 60 | 200 |
| Micro | 60 | 200 |
| Small | 90 | 400 |
| Medium | 120 | 600 |
| Large | 160 | 800 |
| XL | 240 | 1,000 |
| 2XL | 380 | 1,500 |
| 4XL | 480 | 3,000 |
| 8XL | 490 | 6,000 |
| 12XL | 500 | 9,000 |
| 16XL | 500 | 12,000 |

## Configuring Direct Connection Limits

> Note: The Supavisor (pooler) connection limits are hard-coded and cannot be changed without upgrading the compute size.

You can configure the maximum number of connections that PostgreSQL will accept using the [Supabase CLI](https://supabase.com/docs/guides/platform/custom-postgres-config):

```bash
npx supabase login
npx supabase --experimental --project-ref <PROJECT_REF> postgres-config update --config max_connections=<INTEGER_VALUE>
```

To verify the changes, run the following SQL query in the SQL Editor:

```sql
SHOW max_connections;
```

## Dangers of Increasing Direct Connection Limits

Consider these three critical factors before adjusting the direct connection limit:

### 1. Process Schedulers and PostgreSQL Internals

Allowing too many direct connections can overburden PostgreSQL schedulers and other internal modules, resulting in decreased query throughput despite having more connections. EnterpriseDB provides an excellent [article](https://www.enterprisedb.com/postgres-tutorials/why-you-should-use-connection-pooling-when-setting-maxconnections-postgres) detailing these considerations.

The default values are set based on PostgreSQL architecture understanding, and deviating significantly from them will likely hinder performance. Unless there's a compelling reason to adjust the setting, it's generally advisable to stick with the defaults or change the values judiciously.

### 2. Memory Considerations

> If you don't know how to monitor memory and CPU with Supabase Grafana, [check this guide](https://github.com/orgs/supabase/discussions/27141).

#### Each direct connection is a running process that consumes active memory

This is what unhealthy memory usage looks like in Grafana:

![Unhealthy memory usage chart](https://supabase.com/docs/img/troubleshooting/47685206-7914-440e-a010-da62f5c38186.png)

The chart colors represent:
- **Yellow**: Active memory
- **Red**: SWAP (disk storage used as memory)
- **Green**: Unclaimed memory (system always keeps some memory unclaimed)
- **Blue**: Cached data and buffer

PostgreSQL's cache is crucial because it stores frequently accessed data for rapid retrieval. If too much active memory is needed, it risks displacing cache, forcing queries to check disk, which is significantly slower.

While most database data is idle, when there's little available memory or uncached data is rapidly accessed, [thrashing](https://en.wikipedia.org/wiki/Thrashing_(computer_science)) can occur.

To avoid displacing cache or straining system resources, only increase direct connections if you have clear excess of unclaimed memory (green).

PostgreSQL will allow memory overcommitment. You can run this query to find the hypothetical maximum value you could set without risking memory failure:

```sql
SELECT '(SERVER MEMORY - ' || current_setting('shared_buffers') || ' - (' || 
        current_setting('autovacuum_max_workers') || ' * ' || 
        current_setting('maintenance_work_mem') || ')) / ' || 
        current_setting('work_mem');
```

> NOTE: You can find your server memory in the [compute add-ons documentation](https://supabase.com/docs/guides/platform/compute-add-ons)

### 3. CPU Impact

The chart below shows what can happen to CPU usage if hundreds of connections are inappropriately opened/closed every second or many CPU-intensive queries run in parallel:

![High CPU usage chart](https://supabase.com/docs/img/troubleshooting/0e7f6842-78fd-44f9-b463-425507815fb6.png)

If you plan to increase your direct connection numbers, your database should have relatively predictable or low CPU usage, similar to this example:

![Healthy CPU usage chart](https://github.com/supabase/supabase/assets/91111415/ee3e4f4c-87a1-4ef8-9ca5-af9094fc1b93)
