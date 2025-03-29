# Dashboard Errors When Managing Users

## Problem

### Receiving error messages in the Dashboard when managing users

You may encounter errors like:
- "Database error"
- "Error sending"

Or, you might receive a comparable 500 error from the Auth REST API with a message like:
- "Database error ..."

These errors typically occur when there are permission issues with triggers or constraints related to the auth.users table.

## Solution 1 (Trigger Related)

Check if the auth schema contains any triggers in the [Dashboard's trigger section](https://supabase.com/dashboard/project/_/database/triggers). Remove all triggers by dropping their functions with a CASCADE modifier:

```sql
DROP FUNCTION <function name>() CASCADE;

-- If you'd prefer, you can drop the trigger alone with the following query:
-- DROP TRIGGER <trigger_name> on auth.<table_name>;
```

Then recreate the functions with a [security definer](https://supabase.com/docs/guides/database/functions#security-definer-vs-invoker) modifier before recreating the triggers.

The [SQL Editor](https://supabase.com/dashboard/project/_/sql/) contains a template for [User Management](https://supabase.com/dashboard/project/_/sql/quickstarts). Within it, there is a working example of how to setup triggers with security definer that may be worth referencing:

```sql
create table profiles (
  id uuid references auth.users on delete cascade not null primary key,
  updated_at timestamp with time zone,
  username text unique,
  full_name text,
  avatar_url text,
  website text,
  constraint username_length check (char_length(username) >= 3)
);

create function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, full_name, avatar_url)
  values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
  return new;
end;
$$ language plpgsql security definer;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
```

### Explanation

One of the most common design patterns in Supabase is to add a trigger to the `auth.users` table. The database role managing authentication (supabase_auth_admin) only has the necessary permissions it needs to perform its duties. So, when a trigger operated by the supabase_auth_admin interacts outside the auth schema, it causes a permission error.

A security definer function retains the privileges of the database user that created it. As long as it is the `postgres` role, your auth triggers should be able to engage with outside tables.

## Solution 2 (Constraint Related)

If you did not create a trigger, check if you created a foreign/primary key relationship between the auth.users table and another table. If you did, then ALTER the [behavior](https://stackoverflow.com/questions/5383612/setting-up-table-relations-what-do-cascade-set-null-and-restrict-do) of the relationship and recreate it with a less [restrictive constraint](https://stackoverflow.com/questions/3359329/how-to-change-the-foreign-key-referential-action-behavior).
