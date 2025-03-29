# Managing Enums in PostgreSQL

This guide explains how to create and manage enumerated types (enums) in PostgreSQL databases.

## What Are Enums?

Enums in PostgreSQL are custom data types that allow you to define a fixed set of possible values for a column. They're useful when you need to constrain a column to a predetermined list of options.

## Creating Enums

You can define a PostgreSQL enum using the `CREATE TYPE` statement:

```sql
CREATE TYPE mood AS ENUM (
  'happy',
  'sad',
  'excited',
  'calm'
);
```

In this example, we've created an enum called "mood" with four possible values.

## When to Use Enums

There's overlap between enums and foreign keys, as both can restrict a column to specific values. Here are some considerations:

### Advantages of Enums

- **Performance**: Queries only need to access a single table instead of joining with a lookup table
- **Simplicity**: SQL is generally easier to read and write
- **Type Safety**: PostgreSQL enforces the constraint at the database level

### Disadvantages of Enums

- **Limited Flexibility**: Adding or removing values requires schema modifications (via migrations)
- **Maintenance Overhead**: Enums require schema updates when values change
- **Internationalization Challenges**: Enum labels can't be easily translated

**Best Practice**: Use enums when the list of values is small, fixed, and unlikely to change often. Good candidates include:
- Continents
- Departments
- Status codes with fixed meanings
- Card suits

## Using Enums in Tables

To use an enum in a table, define a column with the enum type:

```sql
CREATE TABLE person (
  id SERIAL PRIMARY KEY,
  name TEXT,
  current_mood mood
);
```

Here, the `current_mood` column can only contain values from the "mood" enum.

### Inserting Data with Enums

Insert data by specifying one of the enum values:

```sql
INSERT INTO person
  (name, current_mood)
VALUES
  ('Alice', 'happy');
```

### Querying Data with Enums

Filter and compare enum values as you would with other data types:

```sql
SELECT * FROM person WHERE current_mood = 'sad';
```

## Managing Enums

You can manage your enums using the `ALTER TYPE` statement.

### Updating Enum Values

Update the value of an enum column:

```sql
UPDATE person
SET current_mood = 'excited'
WHERE name = 'Alice';
```

### Adding Enum Values

Add new values to an existing enum:

```sql
ALTER TYPE mood ADD VALUE 'content';
```

**Important**: New values can only be added to the end of an enum's list by default. To add values at specific positions, use `ALTER TYPE mood ADD VALUE 'content' BEFORE 'happy'` or `AFTER 'sad'`.

### Removing Enum Values

It is **unsafe** to remove enum values once they have been created. It's better to leave unused enum values in place.

As noted in the [PostgreSQL mailing list](https://www.postgresql.org/message-id/21012.1459434338%40sss.pgh.pa.us), there is no `ALTER TYPE DELETE VALUE` command in PostgreSQL. Even if you delete every occurrence of an enum value within tables, the value could still exist in index pages, which would break if you removed the `pg_enum` entry.

### Getting a List of Enum Values

Query your existing enum values using the `enum_range` function:

```sql
SELECT enum_range(NULL::mood);
```

This returns an array of all values in the enum.

## Resources

- Official PostgreSQL Documentation: [Enumerated Types](https://www.postgresql.org/docs/current/datatype-enum.html)