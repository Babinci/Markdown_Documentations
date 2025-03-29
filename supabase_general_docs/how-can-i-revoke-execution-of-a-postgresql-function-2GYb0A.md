# How to Revoke Execution of a PostgreSQL Function

All function access is PUBLIC by default in PostgreSQL, which means that any role can execute functions. To restrict execution permissions, you need to follow these steps:

## Revoking Function Execution

### Step 1: Revoke Execution from PUBLIC

First, revoke execution permissions from the PUBLIC role to remove the default access:

```sql
REVOKE EXECUTE ON FUNCTION function_name FROM PUBLIC;
```

### Step 2: Revoke Execution from Specific Roles

Next, revoke execution permissions from specific roles that should not have access:

```sql
REVOKE EXECUTE ON FUNCTION function_name FROM role_name;
```

## Example

For a function named `foo`, you would run:

```sql
REVOKE EXECUTE ON FUNCTION foo FROM PUBLIC;
REVOKE EXECUTE ON FUNCTION foo FROM anon;
```

After executing these commands, the `anon` role should receive a permission error when trying to execute the function:

```sql
BEGIN;
SET LOCAL ROLE anon;
SELECT foo();
-- ERROR: permission denied for function foo
```

## Verification

You can verify the permissions by trying to execute the function as the restricted role:

```sql
BEGIN;
SET LOCAL ROLE role_name;
SELECT function_name();
ROLLBACK;
```

If the permission changes were successful, you should see an error message stating "permission denied for function."
