# plv8: JavaScript Language

The `plv8` extension allows you to use JavaScript within Postgres.

## Overview

While Postgres natively runs SQL, it can also run other procedural languages.
`plv8` allows you to run JavaScript code - specifically any code that runs on the [V8 JavaScript engine](https://v8.dev/).

It can be used for database functions, triggers, queries and more.

## Enable the extension

### Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard.
2. Click on **Extensions** in the sidebar.
3. Search for "plv8" and enable the extension.

### SQL

```sql
create extension plv8;
```

## Create `plv8` functions

Functions written in `plv8` are written just like any other Postgres functions, only
with the `language` identifier set to `plv8`.

```sql
create or replace function function_name()
returns void as $$
    // V8 JavaScript
    // code
    // here
$$ language plv8;
```

You can call `plv8` functions like any other Postgres function:

```sql
select function_name();
```

## Examples

### Scalar functions

A [scalar function](https://plv8.github.io/#scalar-function-calls) is anything that takes in some user input and returns a single result.

```sql
create or replace function hello_world(name text)
returns text as $$
    let output = `Hello, ${name}!`;
    return output;
$$ language plv8;
```

### Executing SQL

You can execute SQL within `plv8` code using the [`plv8.execute` function](https://plv8.github.io/#plv8-execute).

```sql
create or replace function update_user(id bigint, first_name text)
returns smallint as $$
    var num_affected = plv8.execute(
        'update profiles set first_name = $1 where id = $2',
        [first_name, id]
    );
    return num_affected;
$$ language plv8;
```

### Set-returning functions

A [set-returning function](https://plv8.github.io/#set-returning-function-calls) is anything that returns a full set of results - for example, rows in a table.

```sql
create or replace function get_messages()
returns setof messages as $$
    var json_result = plv8.execute(
        'select * from messages'
    );
    return json_result;
$$ language plv8;

select * from get_messages();
```

## Resources

- Official [`plv8` documentation](https://plv8.github.io/)
- [plv8 GitHub Repository](https://github.com/plv8/plv8)
