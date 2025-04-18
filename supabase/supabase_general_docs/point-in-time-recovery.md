# Manage Point-in-Time Recovery Usage

## What you are charged for

You can configure [Point-in-Time Recovery (PITR)](https://supabase.com/docs/guides/platform/backups#point-in-time-recovery) for a project by enabling the [PITR add-on](https://supabase.com/dashboard/project/_/settings/addons?panel=pitr). You are charged for every enabled PITR add-on across your projects.

## How charges are calculated

PITR is charged by the hour, meaning you are charged for the exact number of hours that PITR is active for a project. If PITR is active for part of an hour, you are still charged for the full hour.

### Example

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you activate PITR for your project. At the end of the billing cycle you are billed for 512 hours.

| Time Window | PITR Activated | Hours Billed | Description |
| --- | --- | --- | --- |
| January 1, 00:00 AM - January 10, 4:00 PM | No | 0 | |
| January 10, 04:00 PM - January 10, 4:30 PM | No | 0 | |
| January 10, 04:30 PM - January 10, 5:00 PM | Yes | 1 | full hour is billed |
| January 10, 05:00 PM - January 31, 23:59 PM | Yes | 511 | |

### Usage on your invoice

Usage is shown as "Point-in-time recovery Hours" on your invoice.

## Pricing

Pricing depends on the recovery retention period, which determines how many days back you can restore data to any chosen point of up to seconds in granularity.

| Recovery Retention Period in Days | Hourly Price USD | Monthly Price USD |
| --- | --- | --- |
| 7 | $0.137 | $100 |
| 14 | $0.274 | $200 |
| 28 | $0.55 | $400 |

## Billing examples

### One project

The project has PITR with a recovery retention period of 7 days activated throughout the entire billing cycle.

| Line Item | Hours | Costs |
| --- | --- | --- |
| Pro Plan | - | $25 |
| Compute Hours Small Project 1 | 744 | $15 |
| PITR Hours | 744 | $100 |
| **Subtotal** | | **$140** |
| Compute Credits | | -$10 |
| **Total** | | **$130** |

### Multiple projects

All projects have PITR with a recovery retention period of 14 days activated throughout the entire billing cycle.

| Line Item | Hours | Costs |
| --- | --- | --- |
| Pro Plan | - | $25 |
| | | |
| Compute Hours Small Project 1 | 744 | $15 |
| PITR Hours Project 1 | 744 | $200 |
| | | |
| Compute Hours Small Project 2 | 744 | $15 |
| PITR Hours Project 2 | 744 | $200 |
| | | |
| **Subtotal** | | **$455** |
| Compute Credits | | -$10 |
| **Total** | | **$445** |

## Optimize usage

- Review your [backup frequency](https://supabase.com/docs/guides/platform/backups#frequency-of-backups) needs to determine whether you require PITR or free Daily Backups are sufficient
- Regularly check your projects and disable PITR where no longer needed
- Consider disabling PITR for non-production databases
