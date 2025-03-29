# Deprecated RLS Features

Last edited: 3/27/2025

## The `auth.role()` function is now deprecated

The `auth.role()` function has been deprecated in favor of using the `TO` field, natively supported within Postgres:

```sql
-- DEPRECATED
create policy "Public profiles are viewable by everyone."
on profiles for select using (
  auth.role() = 'authenticated' or auth.role() = 'anon'
);

-- RECOMMENDED
create policy "Public profiles are viewable by everyone."
on profiles for select
to authenticated, anon
using (
  true
);
```

## The `auth.email()` function is now deprecated

The `auth.email()` function has been deprecated in favor of a more generic function to return the full JWT:

```sql
-- DEPRECATED
create policy "User can view their profile."
on profiles for select using (
  auth.email() = email
);

-- RECOMMENDED
create policy "User can view their profile."
on profiles for select using (
  (auth.jwt() ->> 'email') = email
);
```
