# Manage Realtime Peak Connections Usage

This guide explains how Supabase Realtime Peak Connections are billed and how to monitor your usage.

## What You Are Charged For

Realtime Peak Connections are measured by tracking the highest number of concurrent connections for each project during the billing cycle. Regardless of fluctuations, only the peak count per project is used for billing, and the totals from all projects are summed. Only successful connections are counted; connection attempts are not included.

### Example of Peak Connection Calculation

For simplicity, this example assumes a billing cycle of only three days.

| Project | Peak Connections Day 1 | Peak Connections Day 2 | Peak Connections Day 3 |
| --- | --- | --- | --- |
| Project A | 80 | 100 | 90 |
| Project B | 120 | 110 | 150 |

**Total billed connections:** 100 (Project A's peak) + 150 (Project B's peak) = **250 connections**

## How Charges Are Calculated

Realtime Peak Connections are billed using Package pricing, with each package representing 1,000 peak connections. If your usage falls between two packages, you are billed for the next whole package.

### Package Pricing Example

For simplicity, let's assume a package size of 1,000 and a charge of $10 per package with no quota.

| Peak Connections | Packages Billed | Costs |
| --- | --- | --- |
| 999 | 1 | $10 |
| 1,000 | 1 | $10 |
| 1,001 | 2 | $20 |
| 1,500 | 2 | $20 |

### Usage on Your Invoice

Usage is shown as "Realtime Peak Connections" on your invoice.

## Pricing

$10 per 1,000 peak connections. You are only charged for usage exceeding your subscription plan's quota.

| Plan | Quota | Over-Usage |
| --- | --- | --- |
| Free | 200 | - |
| Pro | 500 | $10 per 1,000 peak connections |
| Team | 500 | $10 per 1,000 peak connections |
| Enterprise | Custom | Custom |

## Billing Examples

### Within Quota

The organization's connections are within the quota, so no charges apply.

| Line Item | Units | Costs |
| --- | --- | --- |
| Pro Plan | 1 | $25 |
| Compute Hours Micro | 744 hours | $10 |
| Realtime Peak Connections | 350 connections | $0 |
| **Subtotal** |  | **$35** |
| Compute Credits |  | -$10 |
| **Total** |  | **$25** |

### Exceeding Quota

The organization's connections exceed the quota by 1,200, incurring charges for this additional usage.

| Line Item | Units | Costs |
| --- | --- | --- |
| Pro Plan | 1 | $25 |
| Compute Hours Micro | 744 hours | $10 |
| Realtime Peak Connections | 1,700 connections | $20 |
| **Subtotal** |  | **$55** |
| Compute Credits |  | -$10 |
| **Total** |  | **$45** |

## View Usage

You can view Realtime Peak Connections usage on the [organization's usage page](https://supabase.com/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

![Usage page navigation bar](https://supabase.com/docs/img/guides/platform/usage-navbar--light.png)

In the Realtime Peak Connections section, you can see the usage for the selected time period.

![Usage page Realtime Peak Connections section](https://supabase.com/docs/img/guides/platform/usage-realtime-peak-connections--light.png)

## Managing Peak Connections

To control your Realtime Peak Connections usage, consider these strategies:

1. **Optimize connection lifecycle**: Ensure clients disconnect when they're inactive or no longer need the connection.

2. **Implement connection pooling**: For server-side applications, use connection pooling to minimize the number of concurrent connections.

3. **Use shared connections**: Where possible, share a single connection among multiple features in your application rather than creating separate connections.

4. **Implement progressive loading**: Instead of connecting all users simultaneously during peak times, consider staggering connections.

5. **Monitor connection patterns**: Analyze your usage patterns to identify opportunities for optimization.

6. **Set up alerts**: Configure alerts to notify you when approaching your quota or when there are unusual spikes in connections.
