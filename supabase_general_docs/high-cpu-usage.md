# High CPU Usage

Learn what high CPU usage could mean for your Supabase instance and what could have caused it.

## The Danger of High CPU Usage

Every Supabase project runs in its dedicated virtual machine. Your instance will have a different set of hardware provisioned depending on your [compute add-on](compute-and-disk.md). Your hardware may not be suitable for the intended workload and may experience high CPU usage.

High CPU usage could come with a range of issues:

- Slower queries
- Disruption of daily backup routines
- In rare cases, your instance may become unresponsive

Moreover, your instance might not be able to handle future traffic spikes if it already has a high CPU usage.

## Monitor Your CPU

You can check your CPU usage directly on the Supabase Platform. For this go to database health in the reports section or [click here](https://supabase.com/dashboard/project/_/reports/database) and select your project.

![CPU usage reported on Supabase dashboard](https://supabase.com/docs/img/guides/platform/exhaust-cpu-report.png)

It is also possible to monitor your resources and set up alerts using Prometheus/Grafana. You can find a guide for this in the [metrics documentation](metrics.md).

## Common Reasons for High CPU Usage

Everything you do with your Supabase project requires compute. Hence, there can be many reasons for high CPU usage. Here are some common ones:

- **Query performance:** Queries that take a long time to complete (>1 second) as well as excessive amounts of querying can put a strain on the CPU. Check our guide on [examining query performance](performance.md#examining-query-performance).
- **Missing indexes:** Your database might have to scan through a large amount of data to find the information it needs. Creating indexes helps your database find data faster. Learn more about [database indexes](indexes.md).
- **Unsuitable compute:** The compute size of your Supabase project might not be suitable for your application as you might have more traffic or run resource-intensive operations.

## Solving High CPU Usage

There are two ways to solve high CPU usage:

1. **Optimize performance:** Get more out of your instance's resources by optimizing your usage. Have a look at our [performance tuning guide](performance.md#examining-query-performance) and our [production readiness guide](going-into-prod.md#performance).
2. **Upgrade your compute:** You can get a Compute Add-on for your project. Visit your project settings under Compute and Disk to see your upgrade options.
