# Performance Tuning

## Introduction

The Supabase platform automatically optimizes your PostgreSQL database to take advantage of the compute resources of the plan your project is on. However, these optimizations are based on assumptions about the type of workflow the project is being utilized for, and it is likely that better results can be obtained by tuning the database for your particular workflow.

## Examining Query Performance

Unoptimized queries are a major cause of poor database performance. To analyze the performance of your queries, see the [Debugging and Monitoring guide](https://supabase.com/docs/guides/database/inspect).

## Optimizing the Number of Connections

The default connection limits for PostgreSQL and Supavisor is based on your compute size. See the default connection numbers in the [Compute Add-ons](https://supabase.com/docs/guides/platform/compute-add-ons) section.

If the number of connections is insufficient, you will receive the following error upon connecting to the DB:

```
$ psql -U postgres -h ...
FATAL: remaining connection slots are reserved for non-replication superuser connections
```

In such a scenario, you can consider:

- [Upgrading to a larger compute add-on](https://supabase.com/dashboard/project/_/settings/compute-and-disk)
- Configuring your clients to use fewer connections
- Manually configuring the database for a higher number of connections

### Configuring Clients to Use Fewer Connections

You can use the [pg_stat_activity](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW) view to debug which clients are holding open connections on your DB. `pg_stat_activity` only exposes information on direct connections to the database. Information on the number of connections to Supavisor is available [via the metrics endpoint](https://supabase.com/docs/guides/platform/metrics).

Depending on the clients involved, you might be able to configure them to work with fewer connections (e.g., by imposing a limit on the maximum number of connections they're allowed to use), or shift specific workloads to connect via [Supavisor](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler) instead. Transient workflows, which can quickly scale up and down in response to traffic (e.g., serverless functions), can especially benefit from using a connection pooler rather than connecting to the DB directly.

### Allowing Higher Number of Connections

You can configure PostgreSQL connection limit among other parameters by using [Custom PostgreSQL Config](https://supabase.com/docs/guides/platform/custom-postgres-config#custom-postgres-config).

## Enterprise Support

[Contact Supabase](https://forms.supabase.com/enterprise) if you need help tuning your database for your specific workflow.
