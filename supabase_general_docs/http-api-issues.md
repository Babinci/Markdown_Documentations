# Diagnosing HTTP API Issues

Last edited: 2/3/2025

When using Supabase's HTTP APIs, you might encounter various issues that affect your application's performance and reliability. This guide will help you identify common problems and implement effective solutions.

## Common Symptoms

The main symptoms of HTTP API issues include:

- HTTP timeouts
- 5xx response codes (500, 502, 503, 504)
- High response times

## Under-Provisioned Resources

The most common cause of HTTP timeouts and 5xx response codes is under-provisioning of resources for your project. When your project lacks sufficient resources to handle incoming traffic, API failures occur.

Each Supabase project has [segregated compute resources](https://supabase.com/docs/guides/platform/compute-add-ons), allowing it to serve unlimited requests within its provisioned capacity. However, complex queries or those processing large amounts of data require more resources than simple operations.

### Monitoring Resource Usage

You can monitor your project's resource utilization through the [Dashboard Reports page](https://supabase.com/dashboard/project/_/reports/database).

### Solutions for Resource Constraints

1. **Upgrade Compute Resources**:
   - [Upgrade to a larger compute add-on](https://supabase.com/dashboard/project/_/settings/compute-and-disk) to accommodate higher traffic volumes
   - Reference the [compute add-ons documentation](https://supabase.com/docs/guides/platform/compute-add-ons) for sizing options

2. **Optimize Queries**:
   - [Review and optimize](https://supabase.com/docs/guides/platform/performance#examining-query-performance) the queries being executed
   - Add appropriate indexes to improve query performance

3. **Reduce Connection Count**:
   - [Configure clients to use fewer connections](https://supabase.com/docs/guides/platform/performance#configuring-clients-to-use-fewer-connections)
   - Use connection pooling when possible

4. **Restart the Project** (temporary solution):
   - [Restart your project](https://supabase.com/dashboard/project/_/settings/general) to terminate ongoing workloads
   - This affects all databases including read replicas
   - For selective restarts, use the [Infrastructure Settings page](https://supabase.com/dashboard/project/_/settings/infrastructure)

### Disk I/O Budget Exhaustion

If your [Disk I/O budget](https://supabase.com/docs/guides/platform/compute-add-ons#disk-io) has been depleted, you have two options:
- Wait for automatic replenishment the next day
- Upgrade to a larger compute add-on to increase the available budget

## Connection Issues

### Too Many Open Connections

If you're unable to establish new database connections but can still access the Supabase Dashboard, you might be hitting connection limits.

Error messages and solutions:

- **"No more connections allowed (max_client_conn)"**:
  - Configure applications to [use fewer connections](https://supabase.com/docs/guides/platform/performance#configuring-clients-to-use-fewer-connections)
  - [Upgrade to a larger compute add-on](https://supabase.com/docs/guides/platform/compute-add-ons) with higher connection limits

- **"Sorry, too many clients already" or "remaining connection slots are reserved for non-replication superuser connections"**:
  - Implement the solutions above
  - Switch to using the [connection pooler](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pool)

### Connection Refused

If you receive a "connection refused" error after several failed connection attempts:

1. Your client may be temporarily blocked to protect against brute-force attacks
2. Wait 30 minutes before retrying with the correct credentials
3. Alternatively, [contact support](https://supabase.com/dashboard/support/new) with your client's IP address for manual unblocking

If you also cannot access the project via the Dashboard, review the [under-provisioned resources](#under-provisioned-resources) section.
