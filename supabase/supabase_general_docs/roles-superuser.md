# Roles, Superuser Access and Unsupported Operations

Supabase provides the default `postgres` role to all instances deployed. Superuser access is not given as it allows destructive operations to be performed on the database.

To ensure you are not impacted by this, additional privileges are granted to the `postgres` user to allow it to run some operations that are normally restricted to superusers.

However, this does mean that some operations, that typically require `superuser` privileges, are not available on Supabase. These are documented below:

## Unsupported operations

- `CREATE SUBSCRIPTION`
- `CREATE EVENT TRIGGER`
- `COPY ... FROM PROGRAM`
- `ALTER USER ... WITH SUPERUSER`
