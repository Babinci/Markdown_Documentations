# pgTAP: Unit Testing

`pgTAP` is a unit testing extension for PostgreSQL.

## Overview

Let's cover some basic concepts:

- **Unit tests**: Allow you to test small parts of a system (like a database table).
- **TAP**: Stands for [Test Anything Protocol](http://testanything.org/). It is a framework which aims to simplify error reporting during testing.

## Enable the extension

### Using the Dashboard

1. Go to the Database page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for `pgtap` and enable the extension

### Using SQL

```sql
create extension pgtap;
```

## Testing tables

```sql
begin;
select plan(1);
select has_table('profiles');
select * from finish();
rollback;
```

API:

- [`has_table()`](https://pgtap.org/documentation.html#has_table): Tests whether or not a table exists in the database
- [`has_index()`](https://pgtap.org/documentation.html#has_index): Checks for the existence of a named index associated with the named table
- [`has_relation()`](https://pgtap.org/documentation.html#has_relation): Tests whether or not a relation exists in the database

## Testing columns

```sql
begin;
select plan(2);
select has_column('profiles', 'id'); -- test that the "id" column exists in the "profiles" table
select col_is_pk('profiles', 'id'); -- test that the "id" column is a primary key
select * from finish();
rollback;
```

API:

- [`has_column()`](https://pgtap.org/documentation.html#has_column): Tests whether or not a column exists in a given table, view, materialized view or composite type
- [`col_is_pk()`](https://pgtap.org/documentation.html#col_is_pk): Tests whether the specified column or columns in a table is/are the primary key for that table

## Testing RLS policies

```sql
begin;
select plan(1);
select policies_are(
  'public',
  'profiles',
  ARRAY [
    'Profiles are public', -- Test that there is a policy called "Profiles are public" on the "profiles" table
    'Profiles can only be updated by the owner' -- Test that there is a policy called "Profiles can only be updated by the owner" on the "profiles" table
  ]
);
select * from finish();
rollback;
```

API:

- [`policies_are()`](https://pgtap.org/documentation.html#policies_are): Tests that all of the policies on the named table are only the policies that should be on that table
- [`policy_roles_are()`](https://pgtap.org/documentation.html#policy_roles_are): Tests whether the roles to which policy applies are only the roles that should be on that policy
- [`policy_cmd_is()`](https://pgtap.org/documentation.html#policy_cmd_is): Tests whether the command to which policy applies is the same as command that is given in function arguments

You can also use the `results_eq()` method to test that a Policy returns the correct data:

```sql
begin;
select plan(1);
select results_eq(
    'select * from profiles()',
    $$VALUES (1, 'Anna'), (2, 'Bruce'), (3, 'Caryn')$$,
    'profiles() should return all users'
);
select * from finish();
rollback;
```

API:

- [`results_eq()`](https://pgtap.org/documentation.html#results_eq): Tests that the results of a query match the expected results
- [`results_ne()`](https://pgtap.org/documentation.html#results_ne): Tests that the results of a query do not match the expected results

## Testing functions

```sql
prepare hello_expr as select 'hello';

begin;
select plan(3);

-- You'll need to create hello_world and is_even functions first
select function_returns('hello_world', 'text');                      -- test if the function "hello_world" returns text
select function_returns('is_even', ARRAY['integer'], 'boolean');     -- test if the function "is_even" returns a boolean
select results_eq('select * from hello_world()', 'hello_expr');      -- test if the function "hello_world" returns "hello"

select * from finish();
rollback;
```

API:

- [`function_returns()`](https://pgtap.org/documentation.html#function_returns): Tests that a particular function returns a particular data type
- [`is_definer()`](https://pgtap.org/documentation.html#is_definer): Tests that a function is a security definer (that is, a `setuid` function)

## Resources

- Official [`pgTAP` documentation](https://pgtap.org/)
