# Supabase Database Operations

## Table of Contents
- [Introduction](#introduction)
- [Fetch Data](#fetch-data)
- [Insert Data](#insert-data)
- [Update Data](#update-data)
- [Upsert Data](#upsert-data)
- [Delete Data](#delete-data)
- [Call a Postgres Function](#call-a-postgres-function)
- [Other Documentation Files](#other-documentation-files)

## Introduction

The Supabase client provides a simple interface for interacting with your Postgres database. This document covers basic operations like fetching, inserting, updating, upserting, and deleting data, as well as calling stored procedures.

## Fetch Data

- By default, Supabase projects return a maximum of 1,000 rows. This setting can be changed in your project's [API settings](https://supabase.com/dashboard/project/_/settings/api). It's recommended that you keep it low to limit the payload size of accidental or malicious requests. You can use `range()` queries to paginate through your data.
- `select()` can be combined with [Filters](./supabase_filters.md#using-filters)
- `select()` can be combined with [Modifiers](./supabase_filters.md#using-modifiers)
- `apikey` is a reserved keyword if you're using the [Supabase Platform](https://supabase.com/docs/guides/platform) and [should be avoided as a column name](https://github.com/supabase/supabase/issues/5465).

### Parameters

- **columns** *Optional* `string`  
  The columns to retrieve, defaults to `*`.

- **count** *Optional* `CountMethod`  
  The property to use to get the count of rows returned.

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .execute()
)
```

## Insert Data

### Parameters

- **json** *Required* `dict, list`  
  The values to insert. Pass a dict to insert a single row or a list to insert multiple rows.

- **count** *Optional* `CountMethod`  
  The property to use to get the count of rows returned.

- **returning** *Optional* `ReturnMethod`  
  Either 'minimal' or 'representation'. Defaults to 'representation'.

- **default_to_null** *Optional* `bool`  
  Make missing fields default to `null`. Otherwise, use the default value for the column. Only applies for bulk inserts.

### Example

Create a record:

```python
response = (
    supabase.table("planets")
    .insert({"id": 1, "name": "Pluto"})
    .execute()
)
```

## Update Data

- `update()` should always be combined with [Filters](./supabase_filters.md#using-filters) to target the item(s) you wish to update.

### Parameters

- **json** *Required* `dict, list`  
  The values to insert. Pass a dict to insert a single row or a list to insert multiple rows.

- **count** *Optional* `CountMethod`  
  The property to use to get the count of rows returned.

### Example

```python
response = (
    supabase.table("instruments")
    .update({"name": "piano"})
    .eq("id", 1)
    .execute()
)
```

## Upsert Data

- Primary keys must be included in the `values` dict to use upsert.

### Parameters

- **json** *Required* `dict, list`  
  The values to insert. Pass a dict to insert a single row or a list to insert multiple rows.

- **count** *Optional* `CountMethod`  
  The property to use to get the count of rows returned.

- **returning** *Optional* `ReturnMethod`  
  Either 'minimal' or 'representation'. Defaults to 'representation'.

- **ignore_duplicates** *Optional* `bool`  
  Whether duplicate rows should be ignored.

- **on_conflict** *Optional* `string`  
  Specified columns to be made to work with UNIQUE constraint.

- **default_to_null** *Optional* `bool`  
  Make missing fields default to `null`. Otherwise, use the default value for the column. Only applies for bulk inserts.

### Example

```python
response = (
    supabase.table("instruments")
    .upsert({"id": 1, "name": "piano"})
    .execute()
)
```

## Delete Data

- `delete()` should always be combined with [filters](./supabase_filters.md#using-filters) to target the item(s) you wish to delete.
- If you use `delete()` with filters and you have [RLS](https://supabase.com/docs/learn/auth-deep-dive/auth-row-level-security) enabled, only rows visible through `SELECT` policies are deleted. Note that by default no rows are visible, so you need at least one `SELECT`/ `ALL` policy that makes the rows visible.
- When using `delete().in_()`, specify an array of values to target multiple rows with a single query. This is particularly useful for batch deleting entries that share common criteria, such as deleting users by their IDs. Ensure that the array you provide accurately represents all records you intend to delete to avoid unintended data removal.

### Parameters

- **count** *Optional* `CountMethod`  
  The property to use to get the count of rows returned.

- **returning** *Optional* `ReturnMethod`  
  Either 'minimal' or 'representation'. Defaults to 'representation'.

### Example

```python
response = (
    supabase.table("countries")
    .delete()
    .eq("id", 1)
    .execute()
)
```

## Call a Postgres Function

You can call Postgres functions as _Remote Procedure Calls_, logic in your database that you can execute from anywhere. Functions are useful when the logic rarely changes—like for password resets and updates.

```sql
create or replace function hello_world() returns text as $$
  select 'Hello world';
$$ language sql;
```

### Parameters

- **fn** *Required* `callable`  
  The stored procedure call to be executed.

- **params** *Optional* `dict of any`  
  Parameters passed into the stored procedure call.

- **get** *Optional* `dict of any`  
  When set to `true`, `data` will not be returned. Useful if you only need the count.

- **head** *Optional* `dict of any`  
  When set to `true`, the function will be called with read-only access mode.

- **count** *Optional* `CountMethod`  
  Count algorithm to use to count rows returned by the function. Only applicable for [set-returning functions](https://www.postgresql.org/docs/current/functions-srf.html). `"exact"`: Exact but slow count algorithm. Performs a `COUNT(*)` under the hood. `"planned"`: Approximated but fast count algorithm. Uses the Postgres statistics under the hood. `"estimated"`: Uses exact count for low numbers and planned count for high numbers.

### Example

```python
response = (
    supabase.rpc("hello_world")
    .execute()
)
```

## Other Documentation Files

- [Overview](./supabase_overview.md)
- [Query Filters](./supabase_filters.md)
- [Authentication Basics](./supabase_auth_basics.md)
- [OAuth Authentication](./supabase_auth_oauth.md)
- [Multi-factor Authentication](./supabase_auth_mfa.md)
- [Admin Authentication Methods](./supabase_auth_admin.md)
- [Realtime](./supabase_realtime.md)
- [Storage](./supabase_storage.md)
- [Edge Functions](./supabase_edge_functions.md)
