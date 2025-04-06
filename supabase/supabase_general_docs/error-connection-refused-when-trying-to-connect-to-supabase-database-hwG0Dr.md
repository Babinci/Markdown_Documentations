# Error: "Connection refused" when trying to connect to Supabase database

## Problem

When attempting to connect to your Supabase database, you might encounter one of the following error messages:

- `connect ECONNREFUSED 1.2.3.4:5432`
- `psql: error: connection to server at "db.xxxxxxxxxxxxxxxxxxxx.supabase.co" (1.2.3.4), port 5432 failed: Connection refused Is the server running on that host and accepting TCP/IP connections?`

## Cause

This issue is typically caused by banned IPs on your project through Fail2ban, which activates when someone attempts to log in with incorrect passwords twice in a row.

## Solution

These bans will automatically clear after 30 minutes, but you can manually unban IPs using the Supabase CLI:

1. Install the [Supabase CLI](https://supabase.com/docs/guides/cli) if you haven't already
2. List the banned IPs with the following command:

```bash
supabase network-bans get --project-ref <project_reference_id> --experimental
```

3. Unban specific IP addresses with:

```bash
supabase network-bans remove --db-unban-ip <ip_address> --project-ref <project_reference_id> --experimental
```

Replace `<project_reference_id>` with your actual project reference ID and `<ip_address>` with the IP address that needs to be unbanned.

## Prevention

To prevent this issue from occurring:
- Store and use correct database credentials
- Use password managers to avoid typing mistakes
- Consider using connection pooling for applications that frequently connect to the database
