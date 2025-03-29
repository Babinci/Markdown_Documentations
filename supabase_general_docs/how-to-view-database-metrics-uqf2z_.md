# How to View Database Metrics

Last edited: 1/17/2025

Monitoring your database performance is crucial for ensuring optimal operation and identifying potential issues before they impact your application. Supabase provides multiple options for accessing and analyzing your database metrics.

## Real-time Metrics with Grafana

For comprehensive real-time monitoring of your database, including:
- CPU utilization
- EBS (disk) performance 
- Active database connections
- Memory usage
- And more detailed metrics

You can deploy a Grafana Dashboard using our open-source configuration. Setup options include:

1. **Local deployment**: Run Grafana on your own infrastructure
2. **Fly.io deployment**: Use the free tier of Fly.io for a hosted solution

Detailed setup instructions are available in our [GitHub repository](https://github.com/supabase/supabase-grafana).

## Dashboard Reports

The [Supabase Dashboard Reports page](https://supabase.com/dashboard/project/_/reports) provides an alternative view of metrics with some important differences:

- Shows hourly averages rather than real-time second-by-second data
- Includes query metrics that aren't available in the Grafana Dashboard
- More convenient for historical trend analysis
- Doesn't require additional setup

## Metrics Documentation

For more information about the metrics endpoint and available data, refer to our [metrics documentation](https://supabase.com/docs/guides/platform/metrics).

## When to Use Each Option

- **Use Grafana** when you need real-time monitoring, detailed system metrics, or custom alerting
- **Use Dashboard Reports** for quick access to query performance trends and when real-time data isn't necessary
