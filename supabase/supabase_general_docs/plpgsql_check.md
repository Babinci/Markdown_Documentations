# plpgsql_check: PL/pgSQL Linter

[plpgsql_check](https://github.com/okbob/plpgsql_check) is a Postgres extension that lints plpgsql for syntax, semantic and other related issues. The tool helps developers to identify and correct errors before executing the code. plpgsql_check is most useful for developers who are working with large or complex SQL codebases, as it can help identify and resolve issues early in the development cycle.

## Enable the extension

### Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard.
2. Click on **Extensions** in the sidebar.
3. Search for "plpgsql_check" and enable the extension.

### SQL

```sql
create extension plpgsql_check;
```

## API

- [`plpgsql_check_function( ... )`](https://github.com/okbob/plpgsql_check#active-mode): Scans a function for errors.

`plpgsql_check_function` is highly customizable. For a complete list of available arguments see [the docs](https://github.com/okbob/plpgsql_check#arguments).

## Usage

To demonstrate `plpgsql_check` we can create a function with a known error. In this case we create a function `some_func`, that references a non-existent column `place.created_at`.

```sql
create table place(
  x float,
  y float
);

create or replace function public.some_func()
  returns void
  language plpgsql
as $$
declare
  rec record;
begin
  for rec in select * from place
  loop
    -- Bug: There is no column `created_at` on table `place`
    raise notice '%', rec.created_at;
  end loop;
end;
$$;
```

Note that executing the function would not catch the invalid reference error because the `loop` does not execute if no rows are present in the table.

```sql
select public.some_func();

  some_func 
───────────
 
(1 row)
```

Now we can use plpgsql_check's `plpgsql_check_function` function to identify the known error.

```sql
select plpgsql_check_function('public.some_func()');

                   plpgsql_check_function
------------------------------------------------------------
 error:42703:8:RAISE:record "rec" has no field "created_at"
 Context: SQL expression "rec.created_at"
```

## Resources

- Official [`plpgsql_check` documentation](https://github.com/okbob/plpgsql_check)
