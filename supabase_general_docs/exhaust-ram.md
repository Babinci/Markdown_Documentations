# High RAM Usage Troubleshooting

High memory usage doesn't necessarily indicate a problem with your Supabase instance. Memory used for caching and buffers actually improves data access speed. However, if you notice performance degradation alongside high memory usage, you may need to address memory-related issues.

## Base Memory Usage

You may observe elevated memory usage even when your database has little to no load. This is normal, as Supabase requires multiple services besides PostgreSQL to operate, resulting in a higher base memory footprint.

On the smallest compute instance (1 GB RAM), a base memory usage of approximately 50% is common even without active workloads.

## Issues with High Memory Usage

Every Supabase project runs in its own dedicated virtual machine with hardware resources determined by your [compute add-on](https://supabase.com/docs/guides/platform/compute-add-ons). If your workload exceeds your current hardware capacity, you'll experience memory pressure.

A reliable indicator of unhealthy memory usage is swap utilization. When your system runs out of RAM, it offloads memory to the much slower disk swap partition. If your swap usage exceeds 70%, your current compute configuration is likely inadequate for your workload.

High RAM usage can lead to several issues:

- Degraded overall performance when swap memory is heavily utilized
- Operating system killing processes as available memory becomes scarce
- In severe cases, your instance becoming unresponsive

## Monitoring RAM Usage

To check your RAM usage on the Supabase Platform:
1. Navigate to [Database Health in the Reports section](https://supabase.com/dashboard/project/_/reports/database)
2. Review the memory and swap utilization metrics

For more detailed monitoring, you can set up Prometheus/Grafana to:
- Track memory usage by type (cache, application, etc.)
- Monitor swap utilization trends
- Create custom alerts

For details on setting up advanced monitoring, see the [Metrics Guide](https://supabase.com/docs/guides/platform/metrics).

## Common Causes of High RAM Usage

Memory is required for all operations in your Supabase project. Common causes of high RAM usage include:

1. **Inefficient Queries**: Queries taking more than 1 second to complete often use RAM inefficiently. See the guide on [examining query performance](https://supabase.com/docs/guides/platform/performance#examining-query-performance).

2. **Too Many Connections**: Each database connection consumes memory. Check your active connections under [Database Roles](https://supabase.com/dashboard/project/_/database/roles) and review the guide on [managing connections](https://supabase.com/docs/guides/platform/troubleshooting#too-many-open-connections).

3. **Resource-Intensive Extensions**: Extensions like `timescaledb` or `pg_cron` can significantly increase memory usage. The cumulative effect of multiple extensions can also impact memory. Manage extensions in the dashboard under [Extensions](https://supabase.com/dashboard/project/_/database/extensions).

4. **Complex Queries**: Queries involving large sorts, joins on large tables, or heavy aggregations can consume substantial amounts of memory.

5. **Large Result Sets**: Retrieving large datasets without pagination can exhaust available memory.

## Solutions

### 1. Upgrade Your Compute Resources

If your workload consistently requires more memory than your current plan provides:

- Evaluate [compute add-on options](https://supabase.com/dashboard/project/_/settings/compute-and-disk)
- Select a plan with adequate RAM for your workload patterns
- Consider the RAM requirements of any extensions you're using

### 2. Optimize Performance

Get more from your existing resources:

- Implement the recommendations in the [performance tuning guide](https://supabase.com/docs/guides/platform/performance#examining-query-performance)
- Follow best practices from the [production readiness guide](https://supabase.com/docs/guides/platform/going-into-prod#performance)
- Optimize query patterns to reduce memory consumption
- Use pagination for large result sets
- Implement connection pooling to manage database connections efficiently
- Disable unused extensions to free up memory
