# Database Migrations

## How to manage schema migrations for your Supabase project

Database migrations are SQL statements that create, update, or delete your existing database schemas. They are a common way of tracking changes to your database over time.

## Schema migrations

For this guide, we'll create a table called `employees` and see how we can make changes to it.

You will need to [install](https://supabase.com/docs/guides/local-development#quickstart) the Supabase CLI and start the local development stack.

### 1. Create your first migration file

To get started, generate a [new migration](https://supabase.com/docs/reference/cli/supabase-migration-new) to store the SQL needed to create our `employees` table.

```bash
supabase migration new create_employees_table
```

### 2. Add the SQL to your migration file

This creates a new migration file in supabase/migrations directory.

To that file, add the SQL to create this `employees` table.

```sql
create table if not exists employees (
  id bigint primary key generated always as identity,
  name text not null,
  email text,
  created_at timestamptz default now()
);
```

### 3. Apply your first migration

Run this migration to create the `employees` table.

Now you can visit your new `employees` table in the local Dashboard.

```bash
supabase migration up
```

### 4. Modify your employees table

Next, modify your `employees` table by adding a column for `department`.

```bash
supabase migration new add_department_column
```

### 5. Add a new column to your table

To that new migration file, add the SQL to create a new `department` column.

```sql
alter table if exists public.employees
add department text default 'Hooli';
```

### 6. Apply your second migration

Run this migration to update your existing `employees` table.

```bash
supabase migration up
```

Finally, you should see the `department` column added to your `employees` table in the local Dashboard.

View the [complete code](https://github.com/supabase/supabase/tree/master/examples/database/employees) for this example on GitHub.

## Seeding data

Now that you are managing your database with migrations scripts, it would be great have some seed data to use every time you reset the database.

### 1. Populate your table

Create a seed script in supabase/seed.sql.

To that file, add the SQL to insert data into your `employees` table.

```sql
insert into public.employees 
  (name)
values 
  ('Erlich Bachman'),
  ('Richard Hendricks'),
  ('Monica Hall');
```

### 2. Reset your database

Reset your database to reapply migrations and populate with seed data.

```bash
supabase db reset
```

You should now see the `employees` table, along with your seed data in the Dashboard! All of your database changes are captured in code, and you can reset to a known state at any time, complete with seed data.

## Diffing changes

This workflow is great if you know SQL and are comfortable creating tables and columns. If not, you can still use the Dashboard to create tables and columns, and then use the CLI to diff your changes and create migrations.

### 1. Create your table from the Dashboard

Create a new table called `cities`, with columns `id`, `name` and `population`.

Then generate a [schema diff](https://supabase.com/docs/reference/cli/supabase-db-diff).

```bash
supabase db diff -f create_cities_table
```

### 2. Add schema diff as a migration

A new migration file is created for you.

Alternately, you can copy the table definitions directly from the Table Editor.

```sql
create table "public"."cities" (
  "id" bigint primary key generated always as identity,
  "name" text,
  "population" bigint
);
```

### 3. Test your migration

Test your new migration file by resetting your local database.

```bash
supabase db reset
```

The last step is deploying these changes to a live Supabase project.

## Deploy your project

You've been developing your project locally, making changes to your tables via migrations. It's time to deploy your project to the Supabase Platform and start scaling up to millions of users!

Head over to [Supabase](https://supabase.com/dashboard) and create a new project to deploy to.

### 1. Log in to the Supabase CLI

[Login](https://supabase.com/docs/reference/cli/supabase-login) to the Supabase CLI using an auto-generated Personal Access Token.

```bash
supabase login
```

### 2. Link your project

[Link](https://supabase.com/docs/reference/cli/supabase-link) to your remote project by selecting from the on-screen prompt.

```bash
supabase link
```

### 3. Deploy database changes

[Push](https://supabase.com/docs/reference/cli/supabase-db-push) your migrations to the remote database.

```bash
supabase db push
```

Visiting your live project on [Supabase](https://supabase.com/dashboard/project/_), you'll see a new `employees` table, complete with the `department` column you added in the second migration above.
