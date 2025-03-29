# Error: No pg_hba.conf Entry for Host, SSL Off

## Problem

When attempting to connect to your Supabase database, you may encounter an error message that looks like this:

```
error: no pg_hba.conf entry for host "xx.xxx.xxx.xxx", user "postgres", database "postgres", SSL off
```

This error indicates that an authentication attempt to your database has failed because the connection wasn't using SSL encryption.

## Cause

In Supabase, this error typically occurs when [SSL enforcement](https://supabase.com/docs/guides/platform/ssl-enforcement) is enabled on your project (which is the default security setting). The PostgreSQL server is configured to reject non-SSL connections as a security measure.

## Solution

You have two options to resolve this issue:

1. **Connect with SSL** (Recommended):
   - Modify your database connection code or configuration to use SSL
   - Most PostgreSQL clients and libraries support SSL connections
   - Example for connection strings: add `sslmode=require` parameter
   - Example for connection objects: set the SSL property to true

2. **Disable SSL enforcement** (Not recommended for production):
   - Go to your Supabase Dashboard
   - Navigate to Project Settings > Database
   - Find the SSL Enforcement setting and disable it
   - Note that this reduces the security of your database connections

## Security Considerations

- If this error appears from unknown IP addresses, it may indicate attempted unauthorized access and can generally be ignored
- Always use SSL connections for production databases to protect data in transit
- Consider implementing IP restrictions as an additional layer of security

## Related Documentation

For more information, consult the [Supabase SSL Enforcement documentation](https://supabase.com/docs/guides/platform/ssl-enforcement).
