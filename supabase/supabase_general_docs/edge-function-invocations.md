# Managing Edge Function Invocations Usage

This guide explains how Supabase charges for Edge Function invocations, how to view your usage, and includes billing examples.

## What You Are Charged For

You are charged for the number of times your functions get invoked, regardless of the response status code.

## How Charges Are Calculated

Edge Function Invocations are billed using package pricing, with each package representing 1 million invocations. If your usage falls between two packages, you are billed for the next whole package.

### Example

For simplicity, let's assume a package size of 1 million and a charge of $2 per package without a free quota:

| Invocations | Packages Billed | Costs |
| --- | --- | --- |
| 999,999 | 1 | $2 |
| 1,000,000 | 1 | $2 |
| 1,000,001 | 2 | $4 |
| 1,500,000 | 2 | $4 |

### Usage on Your Invoice

Usage is shown as "Function Invocations" on your invoice.

## Pricing

The current pricing is $2 per 1 million invocations. You are only charged for usage exceeding your subscription plan's quota.

| Plan | Quota | Over-Usage |
| --- | --- | --- |
| Free | 500,000 | - |
| Pro | 2 million | $2 per 1 million invocations |
| Team | 2 million | $2 per 1 million invocations |
| Enterprise | Custom | Custom |

## Billing Examples

### Within Quota

When your organization's function invocations are within the quota, no additional charges apply:

| Line Item | Units | Costs |
| --- | --- | --- |
| Pro Plan | 1 | $25 |
| Compute Hours Micro | 744 hours | $10 |
| Function Invocations | 1,800,000 invocations | $0 |
| **Subtotal** |  | **$35** |
| Compute Credits |  | -$10 |
| **Total** |  | **$25** |

### Exceeding Quota

When your organization's function invocations exceed the quota, you incur charges for the additional usage:

| Line Item | Units | Costs |
| --- | --- | --- |
| Pro Plan | 1 | $25 |
| Compute Hours Micro | 744 hours | $10 |
| Function Invocations | 3,400,000 invocations | $4 |
| **Subtotal** |  | **$39** |
| Compute Credits |  | -$10 |
| **Total** |  | **$29** |

In this example, the usage exceeds the quota by 1.4 million invocations, resulting in charges for 2 additional million invocations.

## Viewing Your Usage

You can view Edge Function Invocations usage on your [organization's usage page](https://supabase.com/dashboard/org/_/usage). The page shows the usage of all projects by default:

1. To view usage for a specific project, select it from the dropdown menu
2. You can also select a different time period for the usage report

![Usage page navigation bar](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fusage-navbar--light.png&w=3840&q=75)

In the Edge Function Invocations section, you can see how many invocations your projects have had during the selected time period:

![Usage page Edge Function Invocations section](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fplatform%2Fusage-function-invocations--light.png&w=3840&q=75)