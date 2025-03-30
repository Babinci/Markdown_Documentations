# PGAudit: PostgreSQL Auditing

## Introduction

[PGAudit](https://www.pgaudit.org/) extends PostgreSQL's built-in logging abilities. It can be used to selectively track activities within your database.

This helps you with:

- **Compliance**: Meeting audit requirements for regulations
- **Security**: Detecting suspicious database activity
- **Troubleshooting**: Identifying and fixing database issues

## Enable the Extension

### Using the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for `pgaudit` and enable the extension

### Using SQL

```sql
create extension pgaudit;
```

## Configure the Extension

PGAudit can be configured with different levels of precision:

- **Session**: Logs activity within a connection, such as a [psql](https://supabase.com/docs/guides/database/connecting-to-postgres#connecting-with-psql) connection
- **User**: Logs activity by a particular database user (for example, `anon` or `postgres`)
- **Global**: Logs activity across the entire database
- **Object**: Logs events related to specific database objects (for example, the auth.users table)

Although Session, User, and Global modes differ in their precision, they're all considered variants of **Session Mode** and are configured with the same input categories.

### Session Mode Categories

These modes can monitor predefined categories of database operations:

| Category | What it Logs | Description |
| --- | --- | --- |
| `read` | Data retrieval (SELECT, COPY) | Tracks what data is being accessed |
| `write` | Data modification (INSERT, DELETE, UPDATE, TRUNCATE, COPY) | Tracks changes made to your database |
| `function` | FUNCTION, PROCEDURE, and DO/END block executions | Tracks routine/function executions |
| `role` | User management actions (CREATE, DROP, ALTER on users and privileges) | Tracks changes to user permissions and access |
| `ddl` | Schema changes (CREATE, DROP, ALTER statements) | Monitors modifications to your database structure (tables, indexes, etc.) |
| `misc` | Less common commands (FETCH, CHECKPOINT) | Captures obscure actions for deeper analysis if needed |
| `all` | Everything above | Comprehensive logging for complete audit trails |

Example of how to assign PGAudit to monitor specific categories:

```sql
-- log all CREATE, ALTER, and DROP events
ALTER SYSTEM SET pgaudit.log = 'ddl';

-- log all CREATE, ALTER, DROP, and SELECT events
ALTER SYSTEM SET pgaudit.log = 'read, ddl';

-- log nothing
ALTER SYSTEM SET pgaudit.log = 'none';
```

### Session Logging

When you are connecting in a session environment, such as a [psql](https://supabase.com/docs/guides/database/connecting-to-postgres#connecting-with-psql) connection, you can configure PGAudit to record events initiated within the session.

The [Dashboard](https://supabase.com/dashboard/project/_) is a transactional environment and won't sustain a session.

Inside a session, by default, PGAudit will log nothing:

```sql
-- returns 'none'
SHOW pgaudit.log;
```

In the session, you can `SET` the `pgaudit.log` variable to record events:

```sql
-- log CREATE, ALTER, and DROP events
SET pgaudit.log = 'ddl';

-- log all CREATE, ALTER, DROP, and SELECT events
SET pgaudit.log = 'read, ddl';

-- log nothing
SET pgaudit.log = 'none';
```

### User Logging

There are some cases where you may want to monitor a database user's actions. For instance, let's say you connected your database to [Zapier](https://supabase.com/partners/integrations/zapier) and created a custom role for it to use:

```sql
CREATE USER "zapier" WITH PASSWORD '<new password>';
```

You may want to log all actions initiated by `zapier`, which can be done with the following command:

```sql
ALTER ROLE "zapier" SET pgaudit.log TO 'all';
```

To remove the settings, execute the following code:

```sql
-- disables role's log
ALTER ROLE "zapier" SET pgaudit.log TO 'none';

-- check to make sure the changes are finalized:
SELECT 
  rolname,
  rolconfig
FROM pg_roles
WHERE rolname = 'zapier';
-- should return a rolconfig path with "pgaudit.log=none" present
```

### Global Logging

Use global logging cautiously. It can generate many logs and make it difficult to find important events. Consider limiting the scope of what is logged by using session, user, or object logging where possible.

The below SQL configures PGAudit to record all events associated with the `postgres` role. Since it has extensive privileges, this effectively monitors all database activity.

```sql
ALTER ROLE "postgres" SET pgaudit.log TO 'all';
```

To check if the `postgres` role is auditing, execute the following command:

```sql
SELECT 
  rolname,
  rolconfig
FROM pg_roles
WHERE rolname = 'postgres';
-- should return a rolconfig path with "pgaudit.log=all" present
```

To remove the settings, execute the following code:

```sql
ALTER ROLE "postgres" SET pgaudit.log TO 'none';
```

### Object Logging

To fine-tune what object events PGAudit will record, you must create a custom database role with limited permissions:

```sql
CREATE ROLE "some_audit_role" NOINHERIT;
```

No other PostgreSQL user can assume or login via this role. It solely exists to securely define what PGAudit will record.

Once the role is created, you can direct PGAudit to log by assigning it to the `pgaudit.role` variable:

```sql
ALTER ROLE "postgres" SET pgaudit.role TO 'some_audit_role';
```

You can then assign the role to monitor only approved object events, such as `SELECT` statements that include a specific table:

```sql
GRANT SELECT ON random_table TO "some_audit_role";
```

With this privilege granted, PGAudit will record all select statements that reference the `random_table`, regardless of _who_ or _what_ actually initiated the event. All assignable privileges can be viewed in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/ddl-priv.html).

If you would no longer like to use object logging, you will need to unassign the `pgaudit.role` variable:

```sql
-- change pgaudit.role to no longer reference some_audit_role
ALTER ROLE "postgres" SET pgaudit.role TO '';

-- view if pgaudit.role changed with the following command:
SELECT 
  rolname,
  rolconfig
FROM pg_roles
WHERE rolname = 'postgres';
-- should return a rolconfig path with "pgaudit.role="
```

## Interpreting Audit Logs

PGAudit was designed for storing logs as CSV files with the following headers:

Referenced from the [PGAudit official docs](https://github.com/pgaudit/pgaudit/blob/master/README.md#format)

| Header | Description |
| --- | --- |
| AUDIT_TYPE | SESSION or OBJECT |
| STATEMENT_ID | Unique statement ID for this session. Sequential even if some statements are not logged. |
| SUBSTATEMENT_ID | Sequential ID for each sub-statement within the main statement. Continuous even if some are not logged. |
| CLASS | ..., READ, ROLE (see pgaudit.log). |
| COMMAND | ..., ALTER TABLE, SELECT. |
| OBJECT_TYPE | TABLE, INDEX, VIEW, etc. Available for SELECT, DML, and most DDL statements. |
| OBJECT_NAME | The fully qualified object name (for example, public.account). Available for SELECT, DML, and most DDL. |
| STATEMENT | Statement executed on the backend. |
| PARAMETER | If pgaudit.log_parameter is set, this field contains the statement parameters as quoted CSV, or <none>. Otherwise, it's <not logged>. |

A log made from the following create statement:

```sql
CREATE TABLE account (
  id int primary key,
  name text,
  description text
);
```

Generates the following log in the [Dashboard's PostgreSQL Logs](https://supabase.com/dashboard/project/_/logs/postgres-logs):

```
AUDIT: SESSION,1,1,DDL,CREATE TABLE,TABLE,public.account,create table account(  id int,  name text,  description text); <not logged>
```

## Finding and Filtering Audit Logs

Logs generated by PGAudit can be found in [PostgreSQL Logs](https://supabase.com/dashboard/project/_/logs/postgres-logs?s=AUDIT). To find a specific log, you can use the log explorer. Below is a basic example to extract logs referencing `CREATE TABLE` events:

```sql
SELECT
  CAST(t.timestamp AS datetime) AS timestamp,
  event_message
FROM
  postgres_logs AS t
  CROSS JOIN UNNEST(metadata) AS m
  CROSS JOIN UNNEST(m.parsed) AS p
WHERE event_message LIKE 'AUDIT%CREATE TABLE%'
ORDER BY timestamp DESC
LIMIT 100;
```

## Practical Examples

### Monitoring API Events

API requests are already recorded in the [API Edge Network](https://supabase.com/dashboard/project/_/logs/edge-logs) logs.

To monitor all writes initiated by the PostgREST API roles:

```sql
ALTER ROLE "authenticator" SET pgaudit.log TO 'write';
-- the above is the practical equivalent to:
-- ALTER ROLE "anon" SET pgaudit.log TO 'write';
-- ALTER ROLE "authenticated" SET pgaudit.log TO 'write';
-- ALTER ROLE "service_role" SET pgaudit.log TO 'write';
```

### Monitoring the `auth.users` Table

In the worst case scenario, where a privileged roles' password is exposed, you can use PGAudit to monitor if the `auth.users` table was targeted. It should be stated that API requests are already monitored in the [API Edge Network](https://supabase.com/dashboard/project/_/logs/edge-logs) and this is more about providing greater clarity about what is happening at the database level.

Logging `auth.user` should be done in Object Mode and requires a custom role:

```sql
-- create logging role
CREATE ROLE "auth_auditor" NOINHERIT;

-- give role permission to observe relevant table events
GRANT SELECT ON auth.users TO "auth_auditor";
GRANT DELETE ON auth.users TO "auth_auditor";

-- assign auth_auditor to pgaudit.role
ALTER ROLE "postgres" SET pgaudit.role TO 'auth_auditor';
```

With the above code, any query involving reading or deleting from the auth.users table will be logged.

## Best Practices

### Disabling Excess Logging

PGAudit, if not configured mindfully, can log all database events, including background tasks. This can generate an undesirably large amount of logs in a few hours.

The first step to solve this problem is to identify which database users PGAudit is observing:

```sql
-- find all users monitored by pgaudit
SELECT
  rolname,
  rolconfig
FROM pg_roles
WHERE
  EXISTS (
    SELECT
      1
    FROM UNNEST(rolconfig) AS c
    WHERE c LIKE '%pgaudit.role%' OR c LIKE '%pgaudit.log%'
  );
```

To prevent PGAudit from monitoring the problematic roles, you'll want to change their `pgaudit.log` values to `none` and `pgaudit.role` values to `empty quotes ''`:

```sql
-- Use to disable object level logging  
ALTER ROLE "<role name>" SET pgaudit.role TO '';  
-- Use to disable global and user level logging  
ALTER ROLE "<role name>" SET pgaudit.log TO 'none';
```

## FAQ

### Using PGAudit to Debug Database Functions

Technically yes, but it is not the best approach. It is better to check out the [function debugging guide](https://supabase.com/docs/guides/database/functions#general-logging) instead.

### Downloading Database Logs

In the [Logs Dashboard](https://supabase.com/dashboard/project/_/logs/postgres-logs) you can download logs as CSVs.

### Logging Observed Table Rows

By default, PGAudit records queries, but not the returned rows. You can modify this behavior with the `pgaudit.log_rows` variable:

```sql
-- enable
ALTER ROLE "postgres" SET pgaudit.log_rows TO 'on';
-- disable
ALTER ROLE "postgres" SET pgaudit.log_rows TO 'off';
```

You should not do this unless you are _absolutely_ certain it is necessary for your use case. It can expose sensitive values to your logs that ideally should not be preserved. Furthermore, if done in excess, it can noticeably reduce database performance.

### Logging Function Parameters

Supabase doesn't currently support configuring `pgaudit.log_parameter` because it may log secrets in encrypted columns if you are using [pgsodium](https://supabase.com/docs/guides/database/extensions/pgsodium) or [Vault](https://supabase.com/docs/guides/database/vault).

You can upvote this [feature request](https://github.com/orgs/supabase/discussions/20183) with your use-case if you'd like this restriction lifted.

### System-wide Configurations

PGAudit allows settings to be applied to 3 different database scopes:

| Scope | Description | Configuration File/Command |
| --- | --- | --- |
| System | Entire server | ALTER SYSTEM commands |
| Database | Specific database | ALTER DATABASE commands |
| Role | Specific user/role | ALTER ROLE commands |

Supabase limits full privileges for file system and database variables, meaning PGAudit modifications can only occur at the role level. Assigning PGAudit to the `postgres` role grants it nearly complete visibility into the database, making role-level adjustments a practical alternative to configuring at the database or system level.

PGAudit's [official documentation](https://www.pgaudit.org/) focuses on system and database level configs, but its docs officially supports role level configs, too.

## Resources

- [Official PGAudit documentation](https://www.pgaudit.org/)
- [Database Function Logging](https://supabase.com/docs/guides/database/functions#general-logging)
- [Supabase Logging](https://supabase.com/docs/guides/platform/logs)
- [Self-Hosting Logs](https://supabase.com/docs/reference/self-hosting-analytics/introduction)
