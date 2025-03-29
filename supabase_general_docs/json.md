# Managing JSON and Unstructured Data

PostgreSQL supports storing and querying unstructured data through its powerful JSON data types. This guide will show you how to work with JSON data in your Supabase project.

## JSON vs JSONB

PostgreSQL supports two types of JSON columns:

- `json` - Stores an exact copy of the input text. Database functions must reparse the content on each execution.
- `jsonb` - Stores data in a decomposed binary format. While this makes it slightly slower to input due to added conversion overhead, it is significantly faster to process, since no reparsing is needed.

The recommended type is `jsonb` for almost all cases.

## When to use JSON/JSONB

Generally, you should use a `jsonb` column when you have data that is:
- Unstructured
- Has a variable schema
- Needs to be stored as a single unit

For example, if you wanted to store responses for various webhooks, you might not know the format of the response when creating the table. Instead, you could store the `payload` as a `jsonb` object in a single column.

> **Note**: Don't go overboard with `json/jsonb` columns. They are a useful tool, but most of the benefits of a relational database come from the ability to query and join structured data, and the referential integrity that brings.

## Create JSONB columns

`json/jsonb` is just another "data type" for PostgreSQL columns. You can create a `jsonb` column in the same way you would create a `text` or `int` column:

```sql
CREATE TABLE books (
  id serial PRIMARY KEY,
  title text,
  author text,
  metadata jsonb
);
```

## Inserting JSON data

You can insert JSON data in the same way that you insert any other data. The data must be valid JSON.

```sql
INSERT INTO books
  (title, author, metadata)
VALUES
  (
    'The Poky Little Puppy',
    'Janette Sebring Lowrey',
    '{"description":"Puppy is slower than other, bigger animals.","price":5.95,"ages":[3,6]}'
  ),
  (
    'The Tale of Peter Rabbit',
    'Beatrix Potter',
    '{"description":"Rabbit eats some vegetables.","price":4.49,"ages":[2,5]}'
  ),
  (
    'Tootle',
    'Gertrude Crampton',
    '{"description":"Little toy train has big dreams.","price":3.99,"ages":[2,5]}'
  ),
  (
    'Green Eggs and Ham',
    'Dr. Seuss',
    '{"description":"Sam has changing food preferences and eats unusually colored food.","price":7.49,"ages":[4,8]}'
  ),
  (
    'Harry Potter and the Goblet of Fire',
    'J.K. Rowling',
    '{"description":"Fourth year of school starts, big drama ensues.","price":24.95,"ages":[10,99]}'
  );
```

## Querying JSON data

Querying JSON data is similar to querying other data, with a few additional operators to access nested values.

PostgreSQL supports a range of [JSON functions and operators](https://www.postgresql.org/docs/current/functions-json.html). For example:

- The `->` operator returns values as `jsonb` data
- The `->>` operator returns values as `text`

```sql
SELECT
  title,
  metadata ->> 'description' AS description, -- returned as text
  metadata -> 'price' AS price,
  metadata -> 'ages' -> 0 AS low_age,
  metadata -> 'ages' -> 1 AS high_age
FROM books;
```

## Validating JSON data

Supabase provides the [`pg_jsonschema` extension](pg_jsonschema.md) that adds the ability to validate `json` and `jsonb` data types against [JSON Schema](https://json-schema.org/) documents.

Once you have enabled the extension, you can add a "check constraint" to your table to validate the JSON data:

```sql
CREATE TABLE customers (
  id serial PRIMARY KEY,
  metadata json
);

ALTER TABLE customers
ADD CONSTRAINT check_metadata CHECK (
  json_matches_schema(
    '{
        "type": "object",
        "properties": {
            "tags": {
                "type": "array",
                "items": {
                    "type": "string",
                    "maxLength": 16
                }
            }
        }
    }',
    metadata
  )
);
```

## Resources

- [PostgreSQL: JSON Functions and Operators](https://www.postgresql.org/docs/current/functions-json.html)
- [PostgreSQL JSON types](https://www.postgresql.org/docs/current/datatype-json.html)
- [pg_jsonschema Extension](pg_jsonschema.md)
