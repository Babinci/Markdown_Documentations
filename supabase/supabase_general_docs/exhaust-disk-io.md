# High Disk I/O Usage Troubleshooting

This guide helps you understand, monitor, and resolve high disk I/O issues that can affect the performance and stability of your Supabase project.

## Understanding Disk I/O and Disk I/O Budget

Disk I/O refers to two key metrics:
- **Throughput** (measured in Megabits per Second)
- **IOPS** (Input/Output Operations per Second)

Different compute add-ons for your Supabase instance provide [different baseline performances](https://supabase.com/docs/guides/platform/compute-add-ons#compute-size).

Smaller compute instances can temporarily exceed their baseline performance through "bursting," which consumes from a daily quota called your Disk I/O Budget. Once this budget is depleted, your instance reverts to its baseline performance. For consistent performance, see [choosing the right compute instance](https://supabase.com/docs/guides/platform/compute-add-ons#choosing-the-right-compute-instance-for-consistent-disk-performance).

## Effects of Depleted Disk I/O Budget

When you run out of Disk I/O Budget, your instance effectively becomes throttled, which can lead to:

- Noticeably increased response times
- Elevated CPU usage due to I/O wait
- Disruption of [daily backup](https://supabase.com/docs/guides/platform/backups#daily-backups) routines
- Disruption of internal PostgreSQL processes such as [autovacuuming](https://supabase.com/docs/guides/platform/database-size#vacuum-operations)
- Unresponsive instance behavior

## Monitoring Your Disk I/O Budget

You can monitor your Disk I/O Budget in two ways:

1. **Supabase Dashboard**: Navigate to [Database Health in the Reports section](https://supabase.com/dashboard/project/_/reports/database)

2. **Prometheus/Grafana**: Set up more detailed monitoring and alerts using the integrated metrics system. This provides fine-grained insights into:
   - RAM usage for caching
   - Swap usage
   - I/O patterns

For detailed setup instructions, see the [Metrics Guide](https://supabase.com/docs/guides/platform/metrics).

## Common Causes of High Disk I/O Usage

Most operations in your Supabase project require disk I/O. Common reasons for excessive usage include:

1. **High Memory Usage**: When RAM is insufficient, the system frequently uses the 1GB of swap space allocated on disk

2. **Low Cache Hit Rate**: When database requests frequently bypass the cache and access the disk directly. See the [Cache Hit Rate Guide](https://supabase.com/docs/guides/platform/performance#hit-rate) for optimization

3. **Inefficient Queries**: Slow queries (>1 second) often indicate inefficient disk usage. Learn about [examining query performance](https://supabase.com/docs/guides/platform/performance#examining-query-performance)

4. **High Traffic Volume**: Success can bring its own challenges if your project receives more requests than it can handle

## Solutions

### 1. Upgrade Your Compute Add-on

Larger compute options (especially 4XL and above) provide more consistent disk performance:

- View your [upgrade options](https://supabase.com/dashboard/project/_/settings/compute-and-disk) in the dashboard
- Compare [baseline performances](https://supabase.com/docs/guides/platform/compute-add-ons#compute-size) of different compute tiers

### 2. Optimize Performance

Get more from your existing resources:

- Follow the [performance tuning guide](https://supabase.com/docs/guides/platform/performance#examining-query-performance)
- Implement recommendations from the [production readiness guide](https://supabase.com/docs/guides/platform/going-into-prod#performance)
- Consider implementing caching strategies at the application level
- Optimize your database schema and indexing strategy
