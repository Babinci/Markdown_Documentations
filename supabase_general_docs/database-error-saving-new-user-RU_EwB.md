# Database Error Saving New User

## Problem

You may encounter a "Database error saving new user" message when:
- Inviting a new user from the dashboard
- Trying to insert a user into a table using the table editor in the Supabase dashboard

This error is normally associated with a side effect of a database transaction.

## Common Causes

- You have a trigger/trigger function setup on the `auth.users` table
- You have added a constraint on the `auth.users` table which isn't being met
- You are using Prisma and it has broken all the permissions on the `auth.users` table

## Debugging the Error

To find more detailed information about the error:
- Use the [Auth logs explorer](https://app.supabase.com/project/_/logs/auth-logs) to find the issue with more information
- Check the [Postgres logs explorer](https://app.supabase.com/project/_/logs/postgres-logs) for specific database errors

## Solution Strategies

1. If you have triggers on the `auth.users` table, make sure they use the `security definer` attribute and have proper error handling
2. Review any constraints added to the `auth.users` table
3. If using Prisma, you may need to reset permissions on the `auth.users` table

Remember that the `auth` schema is managed by Supabase, and modifications to its tables should be done carefully to avoid disrupting the authentication system.
