# Storage Access Control

Supabase Storage is designed to work perfectly with Postgres [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) (RLS).

You can use RLS to create [Security Access Policies](https://www.postgresql.org/docs/current/sql-createpolicy.html) that are incredibly powerful and flexible, allowing you to restrict access based on your business needs.

## Access Policies

By default Storage does not allow any uploads to buckets without RLS policies. You selectively allow certain operations by creating RLS policies on the `storage.objects` table.

You can find the documentation for the storage schema [here](https://supabase.com/docs/guides/storage/schema/design), and to simplify the process of crafting your policies, you can utilize these [helper functions](https://supabase.com/docs/guides/storage/schema/helper-functions).

The RLS policies required for different operations are documented [here](https://supabase.com/docs/reference/javascript/storage-createbucket)

For example, the only RLS policy required for [uploading](https://supabase.com/docs/reference/javascript/storage-from-upload) objects is to grant the `INSERT` permission to the `storage.objects` table.

To allow overwriting files using the `upsert` functionality you will need to additionally grant `SELECT` and `UPDATE` permissions.

## Policy Examples

An easy way to get started would be to create RLS policies for `SELECT`, `INSERT`, `UPDATE`, `DELETE` operations and restrict the policies to meet your security requirements. For example, one can start with the following `INSERT` policy:

```sql
create policy "policy_name"
ON storage.objects
for insert with check (
  true
);
```

and modify it to only allow authenticated users to upload assets to a specific bucket by changing it to:

```sql
create policy "policy_name"
on storage.objects 
for insert to authenticated 
with check (
    -- restrict bucket
    bucket_id = 'my_bucket_id'
);
```

This example demonstrates how you would allow authenticated users to upload files to a folder called `private` inside `my_bucket_id`:

```sql
create policy "Allow authenticated uploads"
on storage.objects
for insert
to authenticated
with check (
  bucket_id = 'my_bucket_id' and
  (storage.foldername(name))[1] = 'private'
);
```

This example demonstrates how you would allow authenticated users to upload files to a folder called with their `users.id` inside `my_bucket_id`:

```sql
create policy "Allow authenticated uploads"
on storage.objects
for insert
to authenticated
with check (
  bucket_id = 'my_bucket_id' and
  (storage.foldername(name))[1] = (select auth.uid()::text)
);
```

Allow a user to access a file that was previously uploaded by the same user:

```sql
create policy "Individual user Access"
on storage.objects for select
to authenticated
using ( (select auth.uid()) = owner_id::uuid );
```

## Bypassing Access Controls

If you exclusively use Storage from trusted clients, such as your own servers, and need to bypass the RLS policies, you can use the `service key` in the `Authorization` header. Service keys entirely bypass RLS policies, granting you unrestricted access to all Storage APIs.

Remember you should not share the service key publicly.
