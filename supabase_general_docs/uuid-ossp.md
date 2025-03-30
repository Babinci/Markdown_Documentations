# uuid-ossp: Unique Identifiers

The `uuid-ossp` extension can be used to generate a `UUID`.

## Overview

A `UUID` is a "Universally Unique Identifier" and it is, for practical purposes, unique.
This makes them particularly well suited as Primary Keys. It is occasionally referred to as a `GUID`, which stands for "Globally Unique Identifier".

## Enable the extension

**Note**:
Currently `uuid-ossp` extension is enabled by default and cannot be disabled.

### Dashboard
1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard.
2. Click on **Extensions** in the sidebar.
3. Search for `uuid-ossp` and enable the extension.

### SQL
```sql
-- This is already enabled by default
create extension if not exists "uuid-ossp";
```

## The `uuid` type

Once the extension is enabled, you now have access to a `uuid` type.

## `uuid_generate_v1()`

Creates a UUID value based on the combination of computer's MAC address, current timestamp, and a random value.

UUIDv1 leaks identifiable details, which might make it unsuitable for certain security-sensitive applications.

## `uuid_generate_v4()`

Creates UUID values based solely on random numbers. You can also use Postgres's built-in [`gen_random_uuid()`](https://www.postgresql.org/docs/current/functions-uuid.html) function to generate a UUIDv4.

## Examples

### Within a query

```sql
select uuid_generate_v4();
```

### As a primary key

Automatically create a unique, random ID in a table:

```sql
create table contacts (
  id uuid default uuid_generate_v4(),
  first_name text,
  last_name text,
  primary key (id)
);
```

## Resources

- [Choosing a Postgres Primary Key](https://supabase.com/blog/choosing-a-postgres-primary-key)
- [The Basics Of Postgres `UUID` Data Type](https://www.postgresqltutorial.com/postgresql-uuid/)
