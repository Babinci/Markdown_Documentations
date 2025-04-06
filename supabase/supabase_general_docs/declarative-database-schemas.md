# Declarative Database Schemas

## Manage your database schemas in one place and generate versioned migrations

## Overview

Declarative schemas allow you to reduce code duplications in managing [schema migrations](https://supabase.com/docs/guides/local-development/overview#database-migrations). As your database schema evolves over time, declaring it in one place will help you iterate faster by referring to a single source of truth.

## Schema migrations

Schema migrations are SQL statements written in Data Definition Language. They are versioned in your `supabase/migrations` directory to ensure schema consistency between local and remote environments.

### Declaring your schema

#### 1. Create your first schema file

Create a SQL file in `supabase/schemas` directory that defines an `employees` table.

```sql
create table "employees" (
  "id" integer not null,
  "name" text
);
```

#### 2. Generate a migration file

Generate a migration file by diffing against your declared schema.

```bash
supabase db diff -f employees_table
```

Make sure your local database is stopped before diffing your schema.

#### 3. Start the local database

The new migration file will be used when starting the database locally so you can validate your schema using the local Dashboard.

```bash
supabase start
```

### Updating your schema

#### 1. Stop the local database

Before updating your schema files, stop the local development environment.

```bash
supabase stop
```

#### 2. Add a new column

Edit `supabase/schemas/employees.sql` file to add a new column to `employees` table.

```sql
create table "employees" (
  "id" integer not null,
  "name" text,
  "age" smallint not null
);
```

Some entities like views and enums expect columns to be declared in a specific order. To avoid messy diffs, always append new columns to the end of the table.

#### 3. Generate a new migration

Diff existing migrations against your declared schema.

```bash
supabase db diff -f add_age
```

#### 4. Review the generated migration

Verify that the generated migration contain a single incremental change.

```sql
alter table "public"."employees" add column "age" smallint not null;
```

#### 5. Apply the pending migration

Start the database locally and apply the pending migration.

```bash
supabase start && supabase migration up
```

### Managing dependencies

As your database schema evolves, you will probably start using more advanced entities like views and functions. These entities are notoriously verbose to manage using plain migrations because the entire body must be recreated whenever there is a change. Using declarative schema, you can now edit them in-place so it's much easier to review.

```sql
create table "employees" (
  "id" integer not null,
  "name" text,
  "age" smallint not null
);

create view "profiles" as
  select id, name from "employees";

create function "get_age"(employee_id integer) RETURNS smallint
  LANGUAGE "sql"
AS $$
  select age
  from employees
  where id = employee_id;
$$;
```

Your schema files are run in lexicographic order by default. The order is important when you have foreign keys between multiple tables as the parent table must be created first. For example, your `supabase` directory may end up with the following structure.

```
.
└── supabase/
    ├── schemas/
    │   ├── employees.sql
    │   └── managers.sql
    └── migrations/
        ├── 20241004112233_employees_table.sql
        ├── 20241005112233_add_employee_age.sql
        └── 20241006112233_add_managers_table.sql
```

For small projects with only a few tables, the default schema order may be sufficient. However, as your project grows, you might need more control over the order in which schemas are applied. To specify a custom order for applying the schemas, you can declare them explicitly in `config.toml`. Any glob patterns will evaluated, deduplicated, and sorted in lexicographic order. For example, the following pattern ensures `employees.sql` is always executed first.

```toml
[db.migrations]
schema_paths = [
  "./schemas/employees.sql",
  "./schemas/*.sql",
]
```

### Pulling in your production schema

To set up declarative schemas on a existing project, you can pull in your production schema by running:

```bash
supabase db dump > supabase/schemas/prod.sql
```

From there, you can start breaking down your schema into smaller files and generate migrations. You can do this all at once, or incrementally as you make changes to your schema.

## Known caveats

The `migra` diff tool used for generating schema diff is capable of tracking most database changes. However, there are edge cases where it can fail.

If you need to use any of the entities below, remember to add them through [versioned migrations](https://supabase.com/docs/guides/deployment/database-migrations) instead.

### Data manipulation language

- DML statements such as `insert`, `update`, `delete`, etc., are not captured by schema diff

### View ownership

- [view owner and grants](https://github.com/djrobstep/migra/issues/160#issuecomment-1702983833)
- [security invoker on views](https://github.com/djrobstep/migra/issues/234)
- [materialized views](https://github.com/djrobstep/migra/issues/194)
- doesn't recreate views when altering column type

### RLS policies

- [alter policy statements](https://github.com/djrobstep/schemainspect/blob/master/schemainspect/pg/obj.py#L228)
- [column privileges](https://github.com/djrobstep/schemainspect/pull/67)

### Other entities

- schema privileges are not tracked because each schema is diffed separately
- [comments are not tracked](https://github.com/djrobstep/migra/issues/69)
- [partitions are not tracked](https://github.com/djrobstep/migra/issues/186)
- [`alter publication ... add table ...`](https://github.com/supabase/cli/issues/883)
- [create domain statements are ignored](https://github.com/supabase/cli/issues/2137)
- [grant statements are duplicated from default privileges](https://github.com/supabase/cli/issues/1864)
