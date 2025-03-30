# pg_jsonschema: JSON Schema Validation

## Introduction

[JSON Schema](https://json-schema.org/) is a language for annotating and validating JSON documents. [`pg_jsonschema`](https://github.com/supabase/pg_jsonschema) is a PostgreSQL extension that adds the ability to validate PostgreSQL's built-in `json` and `jsonb` data types against JSON Schema documents.

## Enable the Extension

### Using the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for `pg_jsonschema` and enable the extension

### Using SQL

```sql
CREATE EXTENSION pg_jsonschema;
```

## API Functions

- **`json_matches_schema(schema json, instance json)`**: Checks if a `json` _instance_ conforms to a JSON Schema _schema_
- **`jsonb_matches_schema(schema json, instance jsonb)`**: Checks if a `jsonb` _instance_ conforms to a JSON Schema _schema_

## Usage Examples

Since `pg_jsonschema` exposes its utilities as functions, we can execute them with a SELECT statement:

```sql
SELECT extensions.json_matches_schema(
  schema := '{"type": "object"}',
  instance := '{}'
);
```

`pg_jsonschema` is generally used in tandem with a [check constraint](https://www.postgresql.org/docs/current/ddl-constraints.html) as a way to constrain the contents of a json/b column to match a JSON Schema:

```sql
CREATE TABLE customer(
  id serial primary key,
  metadata json,
  CHECK (
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
  )
);

-- Example: Valid Payload
INSERT INTO customer(metadata)
VALUES ('{"tags": ["vip", "darkmode-ui"]}');
-- Result:
--   INSERT 0 1

-- Example: Invalid Payload
INSERT INTO customer(metadata)
VALUES ('{"tags": [1, 3]}');
-- Result:
--   ERROR:  new row for relation "customer" violates check constraint "customer_metadata_check"
--   DETAIL:  Failing row contains (2, {"tags": [1, 3]}).
```

## Benefits of JSON Schema Validation

1. **Data Integrity**: Ensure all JSON data stored in your database adheres to a specific structure
2. **Error Prevention**: Catch data validation issues at the database level rather than in application code
3. **Self-documenting**: JSON Schema acts as documentation for the expected JSON structure
4. **Type Safety**: Add type checking to otherwise schema-less JSON data
5. **Complexity Handling**: Validate nested structures, arrays, and complex relationships

## Resources

- [Official pg_jsonschema documentation](https://github.com/supabase/pg_jsonschema)
- [JSON Schema specification](https://json-schema.org/)
