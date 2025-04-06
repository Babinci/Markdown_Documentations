# How to Interpret and Explore PostgreSQL Logs

Last edited: 2/21/2025

> For API logs interpretation, see the [complementary guide](https://github.com/orgs/supabase/discussions/22849)

Logs provide valuable insights into PostgreSQL operations, helping meet compliance requirements, detect suspicious activity, and troubleshoot problems. This guide shows you how to effectively use and interpret PostgreSQL logs in Supabase.

## Table of Contents

- [Querying Logs](#querying-logs)
  - [postgres_logs Table Structure](#postgres_logs-table-structure)
  - [Parsed Metadata Fields](#parsed-metadata-fields)
- [Filtering Logs](#filtering-logs)
  - [Excluding Routine Events](#excluding-routine-events)
  - [By Timeframe](#by-timeframe)
  - [By Error Severity](#by-error-severity)
  - [By Query](#by-query)
  - [By APIs/Roles](#by-apisroles)
  - [By Dashboard Queries](#by-dashboard-queries)
  - [Full Example for Finding Errors](#full-example-for-finding-errors)
- [Logging for Compliance and Security](#logging-for-compliance-and-security)
- [Reviewing Log Settings](#reviewing-log-settings)
  - [Changing Log Settings](#changing-log-settings)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Other Resources](#other-resources)

## Querying Logs

The most practical way to explore and filter logs is through the [Logs Explorer](https://supabase.com/dashboard/project/_/logs/explorer).

It uses a subset of BigQuery SQL syntax and pre-parses queries for optimization. This imposes three primary limitations:

- No subqueries or `WITH` statements
- No `*` wildcards for column names
- No `ILIKE` statements

Although there are many strategies to filter logs, such as `LIKE` and `IN` statements, a helper function called [`regexp_contains`](https://github.com/orgs/supabase/discussions/22640) provides the most flexibility and control.

### postgres_logs Table Structure

The table contains 3 fundamental columns:

| Column | Description |
| --- | --- |
| event_message | The log's message |
| timestamp | Time event was recorded |
| parsed metadata | Metadata about event |

The parsed metadata column is an array that contains relevant information about events. To access the information, it must be unnested using a `CROSS JOIN`:

```sql
SELECT
  event_message,
  parsed.<column_name>
FROM
  postgres_logs
-- Unpack data stored in the 'metadata' field
CROSS JOIN unnest(metadata) AS metadata
-- After unpacking the 'metadata' field, extract the 'parsed' field from it
CROSS JOIN unnest(parsed) AS parsed;
```

### Parsed Metadata Fields

#### Query Information

| Field | Description | Example |
| --- | --- | --- |
| parsed.query | The SQL query executed | `SELECT * FROM table;` |
| parsed.command_tag | Tag identifying the type of command | `SELECT`, `INSERT`, `UPDATE`... |
| parsed.internal_query | An internal query used to facilitate a primary query | `SELECT to_jsonb()` |

**Suggested use cases:**
- Identifying slow queries
- Identifying failing queries

#### Error/Warning Information

| Field | Description | Example |
| --- | --- | --- |
| parsed.error_severity | Event severity | `LOG`, `WARNING`, `ERROR`... |
| parsed.detail | Explanation of the event | "Key (fk_table)=(553585367) already exists." |
| parsed.sql_state_code | Error code from PostgreSQL's error table | `42501` |
| parsed.hint | Hint on how to solve the error | "No function matches the given name and argument types." |
| parsed.context | Insight into where an error occurred | "PL/pgSQL function public.find_text(public.vector,integer) line 3 at IF" |

**Suggested use cases:**
- Filter by error severity or SQL code
- Get hints, details, and context about error events

#### Connection/Identification Information

| Field | Description | Example |
| --- | --- | --- |
| parsed.session_id | The session ID | 12345 |
| parsed.session_start_time | The start time of the session | 2024-05-08 15:30:00 |
| parsed.connection_from | The connection IP | 192.165.1.100 |
| parsed.user_name | The connecting database user | `postgres` |
| parsed.application_name | The name of the application | Supavisor, PostgREST |
| parsed.database_name | The name of the database | `postgres` |
| parsed.process_id | The process ID | 1234 |
| parsed.backend_type | Origin of the event | `client backend` |

**Suggested use cases:**
- Identify events by server/API
- Filter connections by IP
- Identify connections to specific databases
- Filter connections by sessions for debugging
- Identify extension events

## Filtering Logs

### Excluding Routine Events

Most PostgreSQL logs during normal periods are routine events. When exploring for atypical behavior, filter out expected values:

```sql
-- Excluding routine events
WHERE NOT regexp_contains(event_message, '^cron|PgBouncer|checkpoint|connection received|authenticated|authorized')
```

### By Timeframe

To investigate issues around a specific period:

```sql
-- Filtering by time period
WHERE timestamp BETWEEN '2024-05-06 04:44:00' AND '2024-05-06 04:45:00'
```

### By Error Severity

This filter finds all errors, fatals, and panics:

```sql
-- Find error events
WHERE parsed.error_severity IN ('ERROR', 'FATAL', 'PANIC')
```

Severity levels:
- **ERROR**: Reports an error that caused the current command to abort
- **FATAL**: Reports an error that caused the current session to abort
- **PANIC**: Reports an error that caused all database sessions to abort

Failure events include an `sql_state_code` that can be referenced in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/errcodes-appendix.html).

### By Query

> NOTE: Unless pg_audit is configured, only failed queries are logged

```sql
-- Find specific queries
WHERE regexp_contains(parsed.query, '(?i)SELECT . <some_table>')
```

Common regex patterns:
- `(?i)`: Ignore case sensitivity
- `.`: Wildcard
- `^`: Look for values at start of string
- `|`: OR operator

### By APIs/Roles

All failed queries, including those from PostgREST, Auth, and external libraries are logged with helpful error messages for debugging.

#### Server/Role Mapping

API servers have assigned database roles:

| Role | API/Tool |
| --- | --- |
| `supabase_admin` | Used by Supabase for project configuration and monitoring |
| `authenticator` | PostgREST |
| `supabase_auth_admin` | Auth |
| `supabase_storage_admin` | Storage |
| `supabase_realtime_admin` | Realtime |
| `supabase_replication_admin` | Synchronizes Read Replicas |
| `postgres` | Supabase Dashboard and External Tools |
| Custom roles | External Tools (e.g., Prisma, SQLAlchemy, PSQL...) |

Filter by role:

```sql
-- Find events based on role/server
WHERE parsed.user_name = '<ROLE>'
```

### By Dashboard Queries

Queries from the Supabase Dashboard are executed under the `postgres` role and include the comment `-- source: dashboard`:

```sql
-- Find queries executed by the Dashboard
WHERE regexp_contains(parsed.query, '-- source: dashboard')
```

### Full Example for Finding Errors

```sql
SELECT
  CAST(postgres_logs.timestamp AS datetime) AS timestamp,
  event_message,
  parsed.error_severity,
  parsed.user_name,
  parsed.query,
  parsed.detail,
  parsed.hint,
  parsed.sql_state_code,
  parsed.backend_type
FROM
  postgres_logs
  CROSS JOIN unnest(metadata) AS metadata
  CROSS JOIN unnest(metadata.parsed) AS parsed
WHERE
  regexp_contains(parsed.error_severity, 'ERROR|FATAL|PANIC')
  AND parsed.user_name = 'postgres'
  AND regexp_contains(event_message, 'duration|operator')
  AND NOT regexp_contains(parsed.query, '<key_words>')
  AND postgres_logs.timestamp BETWEEN '2024-04-15 10:50:00' AND '2024-04-15 10:50:27'
ORDER BY timestamp DESC
LIMIT 100;
```

## Logging for Compliance and Security

### Customized Object and Role Activity Logging

> ⚠️ NOTE: This is specifically for those using the `postgres` role or custom roles. Those using the Database REST API should reference the [Database API Logging Guide](https://github.com/orgs/supabase/discussions/22849).

When recording access patterns, logging based on database roles and objects is the most reliable approach. You can use the [pg_audit](https://supabase.com/docs/guides/database/extensions/pgaudit) extension to selectively log relevant queries (not just errors) by certain roles and against specific database objects.

Take care not to log all database events, but only what is necessary. Over-logging can strain the database and create noise that makes filtering difficult.

**Filtering by pg_audit**:

```sql
-- All pg_audit recorded events start with 'AUDIT'
WHERE regexp_contains(event_message, '^AUDIT')
  AND parsed.user_name = 'API_role'
```

### Filtering by IP

> If connecting from a known range of IP addresses, enable [network restrictions](https://supabase.com/docs/guides/platform/network-restrictions).

Monitoring IPs is challenging with dynamic addressing (serverless or edge environments) and when using connection poolers like Prisma Accelerate, Supavisor, or Cloudflare's Hyperdrive, which record their own IP instead of the origin.

IP tracking works best with direct database connections from servers with static IPs:

```sql
-- Filter by IP
SELECT
  event_message,
  connection_from AS ip,
  COUNT(connection_from) AS ip_count
FROM
  postgres_logs
  CROSS JOIN unnest(metadata) AS metadata
  CROSS JOIN unnest(parsed) AS parsed
WHERE
  regexp_contains(user_name, '<ROLE>')
  AND regexp_contains(backend_type, 'client backend') -- Only external connections
  AND regexp_contains(event_message, '^connection authenticated') -- Only successful authentications
GROUP BY connection_from, event_message
ORDER BY ip_count DESC
LIMIT 100;
```

## Reviewing Log Settings

The `pg_settings` table describes system and logging configurations:

```sql
-- View system variables
SELECT * FROM pg_settings;
```

Logging-related settings are categorized under:

| Category | Description |
| --- | --- |
| `Reporting and Logging / What to Log` | Specifies system events worth logging |
| `Reporting and Logging / When to Log` | Specifies conditions or rules for logging |
| `Customized Options` | Configures extensions enhancing logging (e.g., auto_explain, pg_audit) |

View all log settings:

```sql
-- View all log-related settings
SELECT *
FROM pg_settings
WHERE
  (
    category LIKE 'Reporting and Logging / What to Log'
    OR category LIKE 'Reporting and Logging / When to Log'
    OR category = 'Customized Options'
  )
  AND name LIKE '%log%';
```

### Changing Log Settings

> WARNING: Lenient settings can lead to over-logging, impacting performance and creating log noise.

#### Severity Levels

The `log_min_messages` variable determines what is severe enough to log:

| Severity | Usage |
| --- | --- |
| DEBUG1 .. DEBUG5 | Successively-more-detailed information for developers |
| INFO | Information implicitly requested by the user |
| NOTICE | Information that might be helpful to users |
| WARNING | Warnings of likely problems |
| ERROR | Reports an error that caused the current command to abort |
| LOG | Information of interest to administrators |
| FATAL | Reports an error that caused the current session to abort |
| PANIC | Reports an error that caused all database sessions to abort |

To adjust the setting:

```sql
ALTER ROLE postgres SET log_min_messages = '<NEW_VALUE>';
-- View new setting
SHOW log_min_messages; -- default WARNING
```

#### Configuring Queries Logged

By default, only failed queries are logged. The [PGAudit extension](https://supabase.com/docs/guides/database/extensions/pgaudit) can selectively track all queries by:
- Role
- Session
- Database object
- Entire database

#### Logging Within Database Functions

To track or debug functions, configure logging by following the [function debugging guide](https://supabase.com/docs/guides/database/functions#general-logging).

## Frequently Asked Questions

### How to join different log tables?

Log tables are independent and don't share primary/foreign key relations for joining.

### How to download logs?

Currently, logs can be downloaded through the Log Dashboard as a CSV.

### What is logged?

To see the default logged events, check this [guide](https://gist.github.com/TheOtherBrian1/991d32c2b00dbc75d29b80d4cdf41aa7).

## Other Resources

- [Regex for filtering logs](https://github.com/orgs/supabase/discussions/22640)
- [Debugging with the DB API logs](https://github.com/orgs/supabase/discussions/22849)
- [Debugging Database Functions](https://supabase.com/docs/guides/database/functions#debugging-functions)
- [pg_audit documentation](https://supabase.com/docs/guides/database/extensions/pgaudit)
- [Supabase Logging](https://supabase.com/docs/guides/platform/logs)
- [Self-Hosting Logs](https://supabase.com/docs/reference/self-hosting-analytics/introduction)
