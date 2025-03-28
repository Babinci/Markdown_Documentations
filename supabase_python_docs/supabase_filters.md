# Supabase Query Filters and Modifiers

## Table of Contents
- [Introduction](#introduction)
- [Using Filters](#using-filters)
  - [Column is equal to a value](#column-is-equal-to-a-value)
  - [Column is not equal to a value](#column-is-not-equal-to-a-value)
  - [Column is greater than a value](#column-is-greater-than-a-value)
  - [Column is greater than or equal to a value](#column-is-greater-than-or-equal-to-a-value)
  - [Column is less than a value](#column-is-less-than-a-value)
  - [Column is less than or equal to a value](#column-is-less-than-or-equal-to-a-value)
  - [Column matches a pattern](#column-matches-a-pattern)
  - [Column matches a case-insensitive pattern](#column-matches-a-case-insensitive-pattern)
  - [Column is a value](#column-is-a-value)
  - [Column is in an array](#column-is-in-an-array)
  - [Column contains every element in a value](#column-contains-every-element-in-a-value)
  - [Contained by value](#contained-by-value)
  - [Greater than a range](#greater-than-a-range)
  - [Greater than or equal to a range](#greater-than-or-equal-to-a-range)
  - [Less than a range](#less-than-a-range)
  - [Less than or equal to a range](#less-than-or-equal-to-a-range)
  - [Mutually exclusive to a range](#mutually-exclusive-to-a-range)
  - [With a common element](#with-a-common-element)
  - [Match a string](#match-a-string)
  - [Match an associated value](#match-an-associated-value)
  - [Don't match the filter](#dont-match-the-filter)
  - [Match at least one filter](#match-at-least-one-filter)
  - [Match the filter](#match-the-filter)
- [Using Modifiers](#using-modifiers)
  - [Order the results](#order-the-results)
  - [Limit the number of rows returned](#limit-the-number-of-rows-returned)
  - [Limit the query to a range](#limit-the-query-to-a-range)
  - [Retrieve one row of data](#retrieve-one-row-of-data)
  - [Retrieve zero or one row of data](#retrieve-zero-or-one-row-of-data)
  - [Retrieve as a CSV](#retrieve-as-a-csv)
  - [Using explain](#using-explain)
- [Other Documentation Files](#other-documentation-files)

## Introduction

Supabase provides a variety of filters to refine your database queries. These filters can be used with `select()`, `update()`, `upsert()`, and `delete()` operations.

## Using Filters

Filters allow you to only return rows that match certain conditions.

Filters can be used on `select()`, `update()`, `upsert()`, and `delete()` queries.

If a Postgres function returns a table response, you can also apply filters.

### Example

```python
# Correct
response = (
    supabase.table("instruments")
    .select("name, section_id")
    .eq("name", "flute")
    .execute()
)

# Incorrect
response = (
    supabase.table("instruments")
    .eq("name", "flute")
    .select("name, section_id")
    .execute()
)
```

## Column is equal to a value

Match only rows where `column` is equal to `value`.

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **value** *Required* `any`  
  The value to filter by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .eq("name", "Earth")
    .execute()
)
```

## Column is not equal to a value

Match only rows where `column` is not equal to `value`.

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **value** *Required* `any`  
  The value to filter by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .neq("name", "Earth")
    .execute()
)
```

## Column is greater than a value

Match only rows where `column` is greather than `value`.

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **value** *Required* `any`  
  The value to filter by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .gt("id", 2)
    .execute()
)
```

## Column is greater than or equal to a value

Match only rows where `column` is greater than or equal to `value`.

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **value** *Required* `any`  
  The value to filter by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .gte("id", 2)
    .execute()
)
```

## Column is less than a value

Match only rows where `column` is less than `value`.

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **value** *Required* `any`  
  The value to filter by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .lt("id", 2)
    .execute()
)
```

## Column is less than or equal to a value

Match only rows where `column` is less than or equal to `value`.

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **value** *Required* `any`  
  The value to filter by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .lte("id", 2)
    .execute()
)
```

## Column matches a pattern

Match only rows where `column` matches `pattern` case-sensitively.

### Parameters

- **column** *Required* `string`  
  The name of the column to apply a filter on

- **pattern** *Required* `string`  
  The pattern to match by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .like("name", "%Ea%")
    .execute()
)
```

## Column matches a case-insensitive pattern

Match only rows where `column` matches `pattern` case-insensitively.

### Parameters

- **column** *Required* `string`  
  The name of the column to apply a filter on

- **pattern** *Required* `string`  
  The pattern to match by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .ilike("name", "%ea%")
    .execute()
)
```

## Column is a value

Match only rows where `column` IS `value`.

### Parameters

- **column** *Required* `string`  
  The name of the column to apply a filter on

- **value** *Required* `null | boolean`  
  The value to match by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .is_("name", "null")
    .execute()
)
```

## Column is in an array

Match only rows where `column` is included in the `values` array.

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **values** *Required* `array`  
  The values to filter by

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .in_("name", ["Earth", "Mars"])
    .execute()
)
```

## Column contains every element in a value

Only relevant for jsonb, array, and range columns. Match only rows where `column` contains every element appearing in `value`.

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **values** *Required* `object`  
  The jsonb, array, or range value to filter with

### Example

```python
response = (
    supabase.table("issues")
    .select("*")
    .contains("tags", ["is:open", "priority:low"])
    .execute()
)
```

## Contained by value

Only relevant for jsonb, array, and range columns. Match only rows where every element appearing in `column` is contained by `value`.

### Parameters

- **column** *Required* `string`  
  The jsonb, array, or range column to filter on

- **value** *Required* `object`  
  The jsonb, array, or range value to filter with

### Example

```python
response = (
    supabase.table("classes")
    .select("name")
    .contained_by("days", ["monday", "tuesday", "wednesday", "friday"])
    .execute()
)
```

## Greater than a range

Only relevant for range columns. Match only rows where every element in `column` is greater than any element in `range`.

### Parameters

- **column** *Required* `string`  
  The range column to filter on

- **range** *Required* `array`  
  The range to filter with

### Example

```python
response = (
    supabase.table("reservations")
    .select("*")
    .range_gt("during", ["2000-01-02 08:00", "2000-01-02 09:00"])
    .execute()
)
```

## Greater than or equal to a range

Only relevant for range columns. Match only rows where every element in `column` is either contained in `range` or greater than any element in `range`.

### Parameters

- **column** *Required* `string`  
  The range column to filter on

- **range** *Required* `string`  
  The range to filter with

### Example

```python
response = (
    supabase.table("reservations")
    .select("*")
    .range_gte("during", ["2000-01-02 08:30", "2000-01-02 09:30"])
    .execute()
)
```

## Less than a range

Only relevant for range columns. Match only rows where every element in `column` is less than any element in `range`.

### Parameters

- **column** *Required* `string`  
  The range column to filter on

- **range** *Required* `array`  
  The range to filter with

### Example

```python
response = (
    supabase.table("reservations")
    .select("*")
    .range_lt("during", ["2000-01-01 15:00", "2000-01-01 16:00"])
    .execute()
)
```

## Less than or equal to a range

Only relevant for range columns. Match only rows where every element in `column` is less than any element in `range`.

### Parameters

- **column** *Required* `string`  
  The range column to filter on

- **range** *Required* `array`  
  The range to filter with

### Example

```python
response = (
    supabase.table("reservations")
    .select("*")
    .range_lte("during", ["2000-01-01 14:00", "2000-01-01 16:00"])
    .execute()
)
```

## Mutually exclusive to a range

Only relevant for range columns. Match only rows where `column` is mutually exclusive to `range` and there can be no element between the two ranges.

### Parameters

- **column** *Required* `string`  
  The range column to filter on

- **range** *Required* `array`  
  The range to filter with

### Example

```python
response = (
    supabase.table("reservations")
    .select("*")
    .range_adjacent("during", ["2000-01-01 12:00", "2000-01-01 13:00"])
    .execute()
)
```

## With a common element

Only relevant for array and range columns. Match only rows where `column` and `value` have an element in common.

### Parameters

- **column** *Required* `string`  
  The array or range column to filter on

- **value** *Required* `Iterable[Any]`  
  The array or range value to filter with

### Example

```python
response = (
    supabase.table("issues")
    .select("title")
    .overlaps("tags", ["is:closed", "severity:high"])
    .execute()
)
```

## Match a string

Only relevant for text and tsvector columns. Match only rows where `column` matches the query string in `query`.

- For more information, see [Postgres full text search](https://supabase.com/docs/guides/database/full-text-search).

### Parameters

- **column** *Required* `string`  
  The text or tsvector column to filter on

- **query** *Required* `string`  
  The query text to match with

- **options** *Optional* `object`  
  Named parameters

### Example

```python
response = (
    supabase.table("texts")
    .select("content")
    .text_search(
        "content", 
        "'eggs' & 'ham'",
        options={"config": "english"},
    )
    .execute()
)
```

## Match an associated value

Match only rows where each column in `query` keys is equal to its associated value. Shorthand for multiple `.eq()` s.

### Parameters

- **query** *Required* `dict`  
  The object to filter with, with column names as keys mapped to their filter values

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .match({"id": 2, "name": "Earth"})
    .execute()
)
```

## Don't match the filter

Match only rows which doesn't satisfy the filter. `not_` expects you to use the raw PostgREST syntax for the filter values.

```python
.not_.in_('id', '(5,6,7)')  # Use `()` for `in` filter
.not_.contains('arraycol', '{"a","b"}')  # Use `{}` for array values
```

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .not_.is_("name", "null")
    .execute()
)
```

## Match at least one filter

or_() expects you to use the raw PostgREST syntax for the filter names and values.

```python
.or_('id.in.(5,6,7), arraycol.cs.{"a","b"}')  # Use `()` for `in` filter, `{}` for array values and `cs` for `contains()`.
.or_('id.in.(5,6,7), arraycol.cd.{"a","b"}')  # Use `cd` for `containedBy()`
```

### Parameters

- **filters** *Required* `string`  
  The filters to use, following PostgREST syntax

- **reference_table** *Optional* `string`  
  Set this to filter on referenced tables instead of the parent table

### Example

```python
response = (
    supabase.table("planets")
    .select("name")
    .or_("id.eq.2,name.eq.Mars")
    .execute()
)
```

## Match the filter

filter() expects you to use the raw PostgREST syntax for the filter values.

```python
.filter('id', 'in', '(5,6,7)')  # Use `()` for `in` filter
.filter('arraycol', 'cs', '{"a","b"}')  # Use `cs` for `contains()`, `{}` for array values
```

### Parameters

- **column** *Required* `string`  
  The column to filter on

- **operator** *Optional* `string`  
  The operator to filter with, following PostgREST syntax

- **value** *Optional* `any`  
  The value to filter with, following PostgREST syntax

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .filter("name", "in", '("Mars","Tatooine")')
    .execute()
)
```

## Using Modifiers

Filters work on the row level—they allow you to return rows that only match certain conditions without changing the shape of the rows. Modifiers are everything that don't fit that definition—allowing you to change the format of the response (e.g., returning a CSV string).

Modifiers must be specified after filters. Some modifiers only apply for queries that return rows (e.g., `select()` or `rpc()` on a function that returns a table response).

## Order the results

Order the query result by `column`.

### Parameters

- **column** *Required* `string`  
  The column to order by

- **desc** *Optional* `bool`  
  Whether the rows should be ordered in descending order or not.

- **foreign_table** *Optional* `string`  
  Foreign table name whose results are to be ordered.

- **nullsfirst** *Optional* `bool`  
  Order by showing nulls first

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .order("name", desc=True)
    .execute()
)
```

## Limit the number of rows returned

### Parameters

- **size** *Required* `number`  
  The maximum number of rows to return

- **foreign_table** *Optional* `string`  
  Set this to limit rows of foreign tables instead of the parent table.

### Example

```python
response = (
    supabase.table("planets")
    .select("name")
    .limit(1)
    .execute()
)
```

## Limit the query to a range

Limit the query result by starting at an offset (`start`) and ending at the offset (`end`). Only records within this range are returned. This respects the query order and if there is no order clause the range could behave unexpectedly.

The `start` and `end` values are 0-based and inclusive: `range(1, 3)` will include the second, third and fourth rows of the query.

### Parameters

- **start** *Required* `number`  
  The starting index from which to limit the result.

- **end** *Required* `number`  
  The last index to which to limit the result.

- **foreign_table** *Optional* `string`  
  Set this to limit rows of foreign tables instead of the parent table.

### Example

```python
response = (
    supabase.table("planets")
    .select("name")
    .range(0, 1)
    .execute()
)
```

## Retrieve one row of data

Return `data` as a single object instead of an array of objects.

### Example

```python
response = (
    supabase.table("planets")
    .select("name")
    .limit(1)
    .single()
    .execute()
)
```

## Retrieve zero or one row of data

Return `data` as a single object instead of an array of objects.

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .eq("name", "Earth")
    .maybe_single()
    .execute()
)
```

## Retrieve as a CSV

Return `data` as a string in CSV format.

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .csv()
    .execute()
)
```

## Using explain

For debugging slow queries, you can get the [Postgres `EXPLAIN` execution plan](https://www.postgresql.org/docs/current/sql-explain.html) of a query using the `explain()` method. This works on any query, even for `rpc()` or writes.

Explain is not enabled by default as it can reveal sensitive information about your database. It's best to only enable this for testing environments but if you wish to enable it for production you can provide additional protection by using a `pre-request` function.

Follow the [Performance Debugging Guide](https://supabase.com/docs/guides/database/debugging-performance) to enable the functionality on your project.

### Parameters

- **wal** *Optional* `boolean`  
  If `true`, include information on WAL record generation.

- **verbose** *Optional* `boolean`  
  If `true`, the query identifier will be returned and `data` will include the output columns of the query.

- **settings** *Optional* `boolean`  
  If `true`, include information on configuration parameters that affect query planning.

- **format** *Optional* `boolean`  
  The format of the output, can be `"text"` (default) or `"json"`.

- **format** *Optional* `"text" | "json"`  
  The format of the output, can be `"text"` (default) or `"json"`.

- **buffers** *Optional* `boolean`  
  If `true`, include information on buffer usage.

- **analyze** *Optional* `boolean`  
  If `true`, the query will be executed and the actual run time will be returned.

### Example

```python
response = (
    supabase.table("planets")
    .select("*")
    .explain()
    .execute()
)
```

## Other Documentation Files

- [Overview](./supabase_overview.md)
- [Database Operations](./supabase_database.md)
- [Authentication Basics](./supabase_auth_basics.md)
- [OAuth Authentication](./supabase_auth_oauth.md)
- [Multi-factor Authentication](./supabase_auth_mfa.md)
- [Admin Authentication Methods](./supabase_auth_admin.md)
- [Realtime](./supabase_realtime.md)
- [Storage](./supabase_storage.md)
- [Edge Functions](./supabase_edge_functions.md)
