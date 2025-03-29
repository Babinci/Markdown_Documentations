# Interpreting Supabase Grafana CPU Charts

> See [this guide](metrics.md) for setting up Supabase Grafana

## Understanding CPU Utilization

Here are examples of unhealthy CPU utilization:

![Unhealthy CPU utilization example 1](https://supabase.com/docs/img/troubleshooting/e7d78109-b09d-48ca-8cc6-e4913693e163.png)
![Unhealthy CPU utilization example 2](https://supabase.com/docs/img/troubleshooting/49e175d9-6338-4b17-97be-4bf7853e319f.png)

The CPU chart shows 4 distinct metrics of interest:

- **Yellow**: It represents CPU utilized in [kernel space](https://en.wikipedia.org/wiki/User_space_and_kernel_space) (privileged OS operations). If this is high, it may be a sign that your app is connecting/disconnecting too aggressively. It could also be symptomatic of extension-related errors.

- **Blue**: It represents requests in user space and mainly reflects the CPU usage from regular queries. For optimization tips, check out the links at the end of the page.

- **Red**: It represents cycles the CPU spent idle because it was waiting on IO tasks. Any amount of red often implies [disk](https://github.com/orgs/supabase/discussions/27003) or, indirectly, [memory](https://github.com/orgs/supabase/discussions/27021) problems. The links outline how to address this type of issue.

- **Green**: These are CPU cycles spent idle.

As the CPU peaks towards 100%, queries and database tasks will begin to throttle, as they won't have enough time or access to the CPU.

## Other Useful Supabase Grafana Guides

- [Connections](https://github.com/orgs/supabase/discussions/27141)
- [Disk](https://github.com/orgs/supabase/discussions/27003)
- [Memory](https://github.com/orgs/supabase/discussions/27021)

## Optimization Strategies

1. [Optimize your queries](query-optimization.md)
2. [Add indexes](indexes.md) if possible
3. [Increasing the compute size](compute-add-ons.md)
4. [Distribute load by using read-replicas](https://supabase.com/dashboard/project/_/settings/infrastructure)
