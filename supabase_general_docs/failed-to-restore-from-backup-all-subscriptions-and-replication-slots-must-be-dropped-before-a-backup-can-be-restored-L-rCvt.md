# Failed to Restore from Backup: Replication Slots Error

## Problem

When attempting to restore a database from a backup in Supabase, you may encounter the following error:

```
Failed to restore from backup: All subscriptions and replication slots must be dropped before a backup can be restored.
```

This error occurs because active logical replication slots and subscriptions prevent the restoration process, as they maintain connections to the WAL (Write-Ahead Log) that cannot be disrupted during restoration.

## Solution

To resolve this issue, you need to manually drop any existing subscriptions and replication slots before attempting the backup restoration again.

### Step 1: Identify Existing Replication Slots and Subscriptions

Run the following SQL queries to identify what needs to be dropped:

```sql
-- Check for existing replication slots
SELECT * FROM pg_replication_slots;

-- Check for existing subscriptions
SELECT * FROM pg_subscription;
```

### Step 2: Drop Subscriptions and Replication Slots

After identifying the subscriptions and replication slots, drop them with the following commands:

```sql
-- Drop a subscription
DROP SUBSCRIPTION subscription_name;

-- Drop a replication slot
SELECT pg_drop_replication_slot('slot_name');
```

Replace `subscription_name` with the actual subscription name and `slot_name` with the actual slot name from your query results in step 1.

## Important Notes

1. **Data Safety**: Dropping replication slots and subscriptions is a destructive action that will break replication. This is acceptable in this scenario since you're about to overwrite your database with a backup.

2. **Re-establishing Replication**: If you were using replication for a specific purpose (like read replicas), you'll need to set up the replication again after the backup restore completes.

3. **Permission Requirements**: You'll need superuser privileges to perform these operations.

4. **Production Impact**: If the database is in production, dropping replication slots might affect connected services. Plan accordingly.

## Prevention

To avoid this issue in future backup restorations:

1. Document any replication setup so it can be easily recreated after restoration
2. Consider implementing a pre-restore script that automatically drops existing replication slots and subscriptions
3. In development environments, avoid unnecessary replication setups if you frequently restore backups
