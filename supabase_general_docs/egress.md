# Managing Egress Usage

This guide explains what egress is, how it's billed, and how to optimize your usage to control costs.

## What You Are Charged For

Egress refers to network data transmitted out of the Supabase platform to connected clients. Egress is incurred by all Supabase services - Database, Auth, Storage, Edge Functions, Realtime, and Log Drains.

### Database Egress

Data sent to the client when retrieving data stored in your database.

**Example:** A user views their order history in an online shop. The client application requests the database to retrieve the user's past orders. The order data sent back to the client contributes to Database Egress.

There are various ways to interact with your database:
- Through the PostgREST API using one of the client SDKs (labeled as **Database Egress** in the Dashboard)
- Via the Supavisor connection pooler (labeled as **Supavisor Egress** in the Dashboard)

### Auth Egress

Data sent from Supabase Auth to the client while managing your application's users. This includes actions like signing in, signing out, or creating new users, e.g., via the JavaScript Client SDK.

**Example:** A user signs in to an application. The session data, including authentication tokens and user profile details, sent back to the client contributes to Auth Egress.

### Storage Egress

Data sent from Supabase Storage to the client when retrieving assets. This includes actions like downloading files, images, or other stored content.

**Example:** A user downloads an invoice from an online shop. The file sent back to the client contributes to Storage Egress.

### Edge Functions Egress

Data sent to the client when executing Edge Functions.

**Example:** A user completes a checkout process, triggering an Edge Function to process payment. The confirmation response sent back to the client contributes to Edge Functions Egress.

### Realtime Egress

Data pushed to clients via Supabase Realtime for subscribed events.

**Example:** When users view a live dashboard with real-time updates. As data changes, Supabase Realtime pushes updates to all subscribed clients, contributing to Realtime Egress.

### Log Drain Egress

Data pushed to connected log drain services.

**Example:** Each log sent to a configured log drain is considered egress. You can toggle the GZIP option to reduce egress if your provider supports compressed logs.

## How Charges Are Calculated

Egress is charged by gigabyte. Charges apply only for usage exceeding your subscription plan's quota. This quota is called the Unified Egress Quota because it can be used across all services.

### Usage on Your Invoice

Usage is shown as "Egress GB" on your invoice.

## Pricing

$0.09 per GB per month. You are only charged for usage exceeding your subscription plan's quota.

| Plan | Unified Egress Quota | Over-Usage per month |
| --- | --- | --- |
| Free | 5 GB | - |
| Pro | 250 GB | $0.09 per GB |
| Team | 250 GB | $0.09 per GB |
| Enterprise | Custom | Custom |

## Billing Examples

### Within Quota

When your organization's Egress usage is within the quota, no charges for Egress apply:

| Line Item | Units | Costs |
| --- | --- | --- |
| Pro Plan | 1 | $25 |
| Compute Hours Micro | 744 hours | $10 |
| Egress | 200 GB | $0 |
| **Subtotal** |  | **$35** |
| Compute Credits |  | -$10 |
| **Total** |  | **$25** |

### Exceeding Quota

When your organization's Egress usage exceeds the quota, you incur charges for the additional usage:

| Line Item | Units | Costs |
| --- | --- | --- |
| Pro Plan | 1 | $25 |
| Compute Hours Micro | 744 hours | $10 |
| Egress | 300 GB | $4.5 |
| **Subtotal** |  | **$39.5** |
| Compute Credits |  | -$10 |
| **Total** |  | **$29.5** |

In this example, the usage exceeds the quota by 50 GB (300 GB total - 250 GB quota), resulting in an additional charge of $4.50.

## Viewing Your Usage

### Usage Page

You can view Egress usage on your [organization's usage page](https://supabase.com/dashboard/org/_/usage):

1. The page shows the usage of all projects by default
2. To view usage for a specific project, select it from the dropdown
3. You can also select a different time period

In the Total Egress section, you can see the usage for the selected time period. Hover over a specific date to view a breakdown by service.

### Custom Report

1. On the [reports page](https://supabase.com/dashboard/project/_/reports), click **New custom report** in the left navigation menu
2. After creating a new report, add charts for one or more Supabase services by clicking **Add block**

## Debugging Usage

To better understand your Egress usage, identify what's driving the most traffic:

### Frequent Database Queries

On the Advisors [Query performance view](https://supabase.com/dashboard/project/_/database/query-performance?preset=most_frequent&sort=calls&order=desc), you can see the most frequent queries and the average number of rows returned.

### Most Requested API Endpoints

In the [Logs Explorer](https://supabase.com/dashboard/project/_/logs/explorer), you can access Edge Logs and review the top paths to identify heavily queried endpoints.

## Optimizing Usage

- **Reduce retrieved data:** Select only needed fields or entries when querying your database
- **Optimize client code:** Reduce the number of queries or calls by optimizing client code or using caches
- **Minimize response data:** For update or insert queries, configure your ORM to not return the entire row if not needed
- **Optimize backups:** When running manual backups through Supavisor, remove unneeded tables and/or reduce the frequency
- **Use compression:** Enable GZIP compression for log drains and API responses where supported

For Storage-specific optimizations, refer to the [Storage Optimizations guide](https://supabase.com/docs/guides/storage/production/scaling#egress).