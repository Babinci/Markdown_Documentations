# High Swap Usage Troubleshooting

This guide explains what high swap usage means, what can cause it, and how to effectively resolve it in your Supabase project.

## Understanding Swap Space

Every Supabase project runs on a dedicated virtual machine with hardware specifications determined by your [compute add-on](https://supabase.com/docs/guides/platform/compute-add-ons). Swap is a portion of your instance's disk reserved for the operating system to use when available RAM has been exhausted.

Because swap uses disk rather than memory, it's substantially slower to access and is generally used as a last resort when RAM is insufficient. However, swap utilization alone isn't necessarily problematic - it's the context that matters.

### Normal vs. Problematic Swap Usage

**Normal Swap Usage:**
- Your instance may use swap even with plenty of available RAM
- This "preemptive swapping" moves background processes to disk to optimize RAM for active operations
- Occasional, limited swap usage with stable performance is not concerning

**Problematic Swap Usage:**
- Consistently high RAM utilization (>75%) combined with high swap usage
- Frequent swapping between RAM and disk (constant page swapping)
- Performance degradation and increased latency
- Elevated disk I/O due to constant swapping

## Monitoring Swap Usage

You have several options to track swap usage:

1. **Supabase Dashboard**: Navigate to the [Database Health page](https://supabase.com/dashboard/project/_/reports/database) in the Reports section.

2. **Custom Monitoring**: Set up Prometheus/Grafana monitoring using the [metrics guide](https://supabase.com/docs/guides/platform/metrics) and [example repository](https://github.com/supabase/supabase-grafana).

3. **Key Metrics to Monitor**:
   - `node_memory_SwapFree_bytes` - Available swap space
   - `node_vmstat_pswpin` and `node_vmstat_pswpout` - Pages swapped in/out (spikes indicate active swapping)
   - `node_memory_MemTotal_bytes` and `node_memory_MemFree_bytes` - Total and available RAM
   - `node_disk_io_time_seconds_total` and `node_disk_io_now` - Disk I/O time (indirect indicator of swapping)

## Common Causes of High Swap Usage

1. **Inefficient Queries**: High read traffic or queries processing large amounts of data
   
2. **Missing Indexes**: Forcing database scans through large datasets instead of using efficient indexes
   
3. **Insufficient Compute Resources**: Your project's compute size may be inadequate for your workload
   
4. **Read-Heavy Workloads**: Patterns involving frequent reads or large result sets
   
5. **Resource-Intensive Extensions**: Some PostgreSQL extensions significantly increase memory requirements

## Solutions

If you're experiencing performance issues due to high RAM and swap usage, consider these approaches:

### 1. Optimize Performance

Improve your instance's efficiency:
- Follow the [performance tuning guide](https://supabase.com/docs/guides/platform/performance#examining-query-performance)
- Implement recommendations from the [production readiness guide](https://supabase.com/docs/guides/platform/going-into-prod#performance)
- Create [proper indexes](https://supabase.com/docs/guides/database/postgres/indexes) for frequently queried columns
- Implement pagination for large result sets
- Optimize database queries to reduce resource consumption

### 2. Upgrade Compute Resources

If optimization isn't sufficient:
- Consider a [Compute Add-on](https://supabase.com/dashboard/project/_/settings/compute-and-disk) for your project
- Select a tier with sufficient RAM for your workload patterns

### 3. Implement Read Replicas

For read-heavy workloads:
- Distribute read traffic across [read replicas](https://supabase.com/docs/guides/platform/read-replicas)
- Keep write operations on the primary database
- Scale horizontally to handle increased read loads

## Preventive Measures

To avoid swap-related performance issues:
- Regularly monitor resource usage
- Implement alerts for high memory/swap usage
- Test application changes with production-like data volumes
- Plan for scaling before reaching resource limits
