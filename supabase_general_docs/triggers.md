# Postgres Triggers

## Automatically execute SQL on table events

In Postgres, a trigger executes a set of actions automatically on table events such as INSERTs, UPDATEs, DELETEs, or TRUNCATE operations.

## Creating a trigger

Creating triggers involve 2 parts:

1. A [Function](https://supabase.com/docs/guides/database/functions) which will be executed (called the Trigger Function)
2. The actual Trigger object, with parameters around when the trigger should be run.

An example of a trigger is:

```sql
create trigger "trigger_name"
after insert on "table_name"
for each row
execute function trigger_function();
```

## Trigger functions

A trigger function is a user-defined [Function](https://supabase.com/docs/guides/database/functions) that Postgres executes when the trigger is fired.

### Example trigger function

Here is an example that updates `salary_log` whenever an employee's salary is updated:

```sql
-- Example: Update salary_log when salary is updated
create function update_salary_log()
returns trigger
language plpgsql
as $$
begin
  insert into salary_log(employee_id, old_salary, new_salary)
  values (new.id, old.salary, new.salary);
  return new;
end;
$$;

create trigger salary_update_trigger
after update on employees
for each row
execute function update_salary_log();
```

### Trigger variables

Trigger functions have access to several special variables that provide information about the context of the trigger event and the data being modified. In the example above you can see the values inserted into the salary log are `old.salary` and `new.salary` - in this case `old` specifies the previous values and `new` specifies the updated values.

Here are some of the key variables and options available within trigger functions:

- `TG_NAME`: The name of the trigger being fired.
- `TG_WHEN`: The timing of the trigger event (`BEFORE` or `AFTER`).
- `TG_OP`: The operation that triggered the event (`INSERT`, `UPDATE`, `DELETE`, or `TRUNCATE`).
- `OLD`: A record variable holding the old row's data in `UPDATE` and `DELETE` triggers.
- `NEW`: A record variable holding the new row's data in `UPDATE` and `INSERT` triggers.
- `TG_LEVEL`: The trigger level (`ROW` or `STATEMENT`), indicating whether the trigger is row-level or statement-level.
- `TG_RELID`: The object ID of the table on which the trigger is being fired.
- `TG_TABLE_NAME`: The name of the table on which the trigger is being fired.
- `TG_TABLE_SCHEMA`: The schema of the table on which the trigger is being fired.
- `TG_ARGV`: An array of string arguments provided when creating the trigger.
- `TG_NARGS`: The number of arguments in the `TG_ARGV` array.

## Types of triggers

There are two types of trigger, `BEFORE` and `AFTER`:

### Trigger before changes are made

Executes before the triggering event.

```sql
create trigger before_insert_trigger
before insert on orders
for each row
execute function before_insert_function();
```

### Trigger after changes are made

Executes after the triggering event.

```sql
create trigger after_delete_trigger
after delete on customers
for each row
execute function after_delete_function();
```

## Execution frequency

There are two options available for executing triggers:

- `for each row`: specifies that the trigger function should be executed once for each affected row.
- `for each statement`: the trigger is executed once for the entire operation (for example, once on insert). This can be more efficient than `for each row` when dealing with multiple rows affected by a single SQL statement, as they allow you to perform calculations or updates on groups of rows at once.

## Dropping a trigger

You can delete a trigger using the `drop trigger` command:

```sql
drop trigger "trigger_name" on "table_name";
```

## Resources

- Official Postgres Docs: [Triggers](https://www.postgresql.org/docs/current/triggers.html)
- Official Postgres Docs: [Overview of Trigger Behavior](https://www.postgresql.org/docs/current/trigger-definition.html)
- Official Postgres Docs: [CREATE TRIGGER](https://www.postgresql.org/docs/current/sql-createtrigger.html)
