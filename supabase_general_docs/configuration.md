# Database Configuration

This guide covers updating the default configuration for your PostgreSQL database on Supabase.

## Table of Contents

- [Default Configuration](#default-configuration)
- [Timeouts](#timeouts)
- [Statement Optimization](#statement-optimization)
- [Managing Timezones](#managing-timezones)
  - [Change Timezone](#change-timezone)
  - [Full List of Timezones](#full-list-of-timezones)
  - [Search for a Specific Timezone](#search-for-a-specific-timezone)

## Default Configuration

PostgreSQL provides a set of sensible defaults for your database size. In some cases, these defaults can be updated. We do not recommend changing these defaults unless you know what you're doing.

## Timeouts

See the [Timeouts](https://supabase.com/docs/guides/database/postgres/timeouts) section for more information about configuring query timeouts.

## Statement Optimization

All Supabase projects come with the [`pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html) extension installed, which tracks planning and execution statistics for all statements executed against it. These statistics can be used to diagnose the performance of your project.

This data can further be used in conjunction with the [`explain`](https://www.postgresql.org/docs/current/using-explain.html) functionality of PostgreSQL to optimize your usage.

## Managing Timezones

Every Supabase database is set to UTC timezone by default. We strongly recommend keeping it this way, even if your users are in a different location. This is because it makes it much easier to calculate differences between timezones if you adopt the mental model that everything in your database is in UTC time.

### Change Timezone

```sql
alter database postgres
set timezone to 'America/New_York';
```

### Full List of Timezones

Get a full list of timezones supported by your database. This will return the following columns:

- `name`: Time zone name
- `abbrev`: Time zone abbreviation
- `utc_offset`: Offset from UTC (positive means east of Greenwich)
- `is_dst`: True if currently observing daylight savings

```sql
select name, abbrev, utc_offset, is_dst
from pg_timezone_names()
order by name;
```

### Search for a Specific Timezone

Use `ilike` (case insensitive search) to find specific timezones.

```sql
select *
from pg_timezone_names()
where name ilike '%york%';
```
