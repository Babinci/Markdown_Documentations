# User Management

This guide covers how to view, delete, export user information, and manage user metadata in your Supabase project.

## View and Manage Users

You can view your users on the [Users page](https://supabase.com/dashboard/project/_/auth/users) of the Dashboard. You can also view the contents of the Auth schema in the [Table Editor](https://supabase.com/dashboard/project/_/editor).

## Accessing User Data via API

For security reasons, the Auth schema is not exposed in the auto-generated API. If you want to access user data via the API, you need to create your own user tables in the `public` schema.

Make sure to:

1. Protect the table by enabling [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
2. Reference the `auth.users` table to ensure data integrity
3. Specify `on delete cascade` in the reference

### Example Profile Table

```sql
create table public.profiles (
  id uuid not null references auth.users on delete cascade,
  first_name text,
  last_name text,
  primary key (id)
);
alter table public.profiles enable row level security;
```

> **Important**: Only use primary keys as [foreign key references](https://www.postgresql.org/docs/current/tutorial-fk.html) for schemas and tables like `auth.users` which are managed by Supabase. While Postgres lets you specify a foreign key reference for columns backed by a unique index, primary keys are **guaranteed not to change**. Columns, indices, constraints or other database objects managed by Supabase **may change at any time**.

### Automatic Profile Creation

To update your `public.profiles` table every time a user signs up, set up a trigger:

```sql
-- inserts a row into public.profiles
create function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = ''
as $$
begin
  insert into public.profiles (id, first_name, last_name)
  values (new.id, new.raw_user_meta_data ->> 'first_name', new.raw_user_meta_data ->> 'last_name');
  return new;
end;
$$;

-- trigger the function every time a user is created
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
```

> **Note**: If the trigger fails, it could block signups, so test your code thoroughly.

## Adding and Retrieving User Metadata

### Assigning Metadata on Sign Up

You can assign metadata to users when they sign up:

```javascript
const { data, error } = await supabase.auth.signUp({
  email: 'valid.email@supabase.io',
  password: 'example-password',
  options: {
    data: {
      first_name: 'John',
      age: 27,
    },
  },
})
```

### Retrieving User Metadata

User metadata is stored on the `raw_user_meta_data` column of the `auth.users` table. To retrieve the metadata:

```javascript
const {
  data: { user },
} = await supabase.auth.getUser()
let metadata = user.user_metadata
```

## Deleting Users

You may delete users directly or via the management console at Authentication > Users. 

> **Important**: Deleting a user from the `auth.users` table does not automatically sign out that user. Because Supabase uses JSON Web Tokens (JWT), a user's JWT will remain "valid" until it expires. If you need to immediately revoke access, consider implementing a Row Level Security policy.

**Note**: You cannot delete a user if they are the owner of any objects in Supabase Storage. You'll need to first delete all the objects for that user, or reassign ownership to another user.

## Exporting Users

As Supabase is built on top of PostgreSQL, you can query the `auth.users` and `auth.identities` tables via the SQL Editor to extract all users:

```sql
select * from auth.users;
```

You can then export the results as CSV.
