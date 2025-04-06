# How Long Does It Take to Restore a Database from a Point-in-Time Backup (PITR)?

Last edited: 1/18/2025

The time required for a Point-in-Time Recovery (PITR) restoration varies based on several factors. Unlike a simple fixed timeframe, the restoration process is influenced by multiple variables that affect the overall duration.

## Key Factors Affecting Restoration Time

### 1. Time Since Last Full Backup

Supabase performs full database backups on a weekly basis. The amount of time that has passed since the last full backup is a significant factor in determining restoration time. The further away your restoration point is from the most recent full backup, the more Write-Ahead Log (WAL) files need to be processed.

### 2. Write-Ahead Logging (WAL) Activity

The volume of database activity since the last full backup directly impacts restoration time:

- **High Transaction Volume**: Databases with frequent writes, updates, and deletes generate more WAL data
- **Complex Queries**: Operations that modify large amounts of data create larger WAL entries
- **Batch Operations**: Bulk operations can significantly increase WAL size

During restoration, all WAL files must be replayed sequentially, which means higher WAL volume leads to longer restoration times.

### 3. Database Size

While database size is a factor, it's not always the primary determinant of restoration time:

- **Small Databases with High Activity**: Can sometimes take longer to restore than larger databases with minimal changes
- **Large Databases with Low Activity**: May restore relatively quickly if WAL volume is low

## What to Expect

- **Typical Range**: From 30 minutes to several hours
- **Large, Active Databases**: May take 4-8+ hours in some cases
- **Small, Less Active Databases**: Generally restore more quickly

For time-sensitive operations, it's advisable to contact Supabase support in advance to discuss your specific situation and get a more accurate time estimate based on your database characteristics.
