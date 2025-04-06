# pg_hashids: Short UIDs

## Introduction

[pg_hashids](https://github.com/iCyberon/pg_hashids) provides a secure way to generate short, unique, non-sequential IDs from numbers. The hashes are intended to be small, easy-to-remember identifiers that can be used to obfuscate data (optionally) with a password, alphabet, and salt.

This extension is useful when you want to hide data like user IDs, order numbers, or tracking codes in favor of unique identifiers that don't expose sequential numeric patterns.

## Enable the Extension

### Using the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for "pg_hashids" and enable the extension

### Using SQL

```sql
CREATE EXTENSION pg_hashids;
```

## Usage Example

Suppose we have a table that stores order information, and we want to give customers a unique identifier without exposing the sequential `id` column. To do this, we can use pg_hashids' `id_encode` function:

```sql
CREATE TABLE orders (
  id serial primary key,
  description text,
  price_cents bigint
);

INSERT INTO orders (description, price_cents)
VALUES ('a book', 9095);

SELECT
  id,
  id_encode(id) as short_id,
  description,
  price_cents
FROM
  orders;
```

This would produce a result like:

```
 id | short_id | description | price_cents
----+----------+-------------+-------------
  1 | jR       | a book      |        9095
(1 row)
```

## API Functions

- **`id_encode(id integer)`**: Converts a numeric ID into a short, non-sequential string
- **`id_decode(hash text)`**: Converts a hashid back into its original numeric ID

## Customizing Hashids

You can customize the hashids with salt, minimum length, and alphabet:

```sql
-- Set a custom salt (default: '')
SELECT hashids_salt('my-salt');

-- Set a minimum hash length (default: 0)
SELECT hashids_min_length(8);

-- Set a custom alphabet (default: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
SELECT hashids_alphabet('abcdefghijklmnopqrstuvwxyz');
```

## Resources

- [Official pg_hashids documentation](https://github.com/iCyberon/pg_hashids)
