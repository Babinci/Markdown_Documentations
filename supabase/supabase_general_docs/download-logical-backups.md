# Downloading Logical Backups with Physical Backups Enabled

## Overview

If you've enabled physical backups for your Supabase project but still need to obtain logical backups, you can use an alternative approach through the Supabase CLI.

## Solution

When physical backups are enabled, the dashboard download option for logical backups may be unavailable. In this case, you can use the Supabase CLI command `pgdump` as an alternative method to create and download logical backups.

## Steps

1. Install the [Supabase CLI](https://supabase.com/docs/guides/cli) if you haven't already
2. Authenticate the CLI with your Supabase account
3. Use the `supabase db dump` command to create a logical backup

## Documentation Links

For detailed, step-by-step instructions on this process, refer to:
- [Backup & Restore guide](https://supabase.com/docs/guides/platform/migrating-within-supabase/backup-restore)

To learn more about backup types and functionality in Supabase:
- [Database Backups documentation](https://supabase.com/docs/guides/platform/backups)

## Command Example

```bash
# Example of using the Supabase CLI to create a logical backup
supabase db dump -p your-project-ref -f backup.sql
```

This command creates a logical backup of your database in SQL format that you can download and store wherever needed.