# How to Delete a Role in PostgreSQL

Last edited: 2/21/2025

Deleting a role in PostgreSQL can be challenging because of the database's strict dependency management. As the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-droprole.html) states:

> A role cannot be removed if it is still referenced in any database of the cluster; an error will be raised if so. Before dropping the role, you must drop all the objects it owns (or reassign their ownership) and revoke any privileges the role has been granted on other objects.

This guide provides a step-by-step process to properly remove a PostgreSQL role.

## Step 1: Grant the Role to PostgreSQL Superuser

First, ensure that the PostgreSQL superuser has ownership of the role you want to delete:

```sql
GRANT <role> TO "postgres";
```

## Step 2: Reassign Objects Owned by the Role

Transfer ownership of all database objects owned by the role to the PostgreSQL superuser:

```sql
REASSIGN OWNED BY <role> TO postgres;
```

This command changes the ownership of all database objects (tables, functions, schemas, etc.) that are owned by the role.

## Step 3: Drop Objects and Revoke Privileges

Remove all remaining objects owned by the role and revoke its privileges:

```sql
DROP OWNED BY <role>;
```

The [DROP OWNED BY](https://www.postgresql.org/docs/current/sql-drop-owned.html) command removes all database objects that were owned by the role, which should be none after the previous reassignment step. More importantly, it also revokes all privileges the role has been granted on objects not owned by the role.

## Step 4: Drop the Role

Finally, drop the role itself:

```sql
DROP ROLE <role>;
```

## Troubleshooting

If you encounter any errors during this process, they are likely due to:

1. The role still owning objects in databases you haven't checked
2. The role being a member of other roles
3. Other roles being members of this role
4. The role having been granted permissions that can't be easily revoked

For persistent issues, consider [creating a support ticket](https://supabase.com/dashboard/support/new) for assistance from the Supabase team.
