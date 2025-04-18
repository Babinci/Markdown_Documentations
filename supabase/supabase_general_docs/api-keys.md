# Understanding API Keys

Supabase provides two default keys when you create a project: an `anon` key, and a `service_role` key. You can find both keys in the [API Settings](https://supabase.com/dashboard/project/_/settings/api).

The data APIs are designed to work with Postgres Row Level Security (RLS). These keys both map to Postgres roles. You can find an `anon` user and a `service_role` user in the [Roles](http://supabase.com/dashboard/project/_/database/roles) section of the dashboard.

The keys are both long-lived JWTs. If you decode these keys, you will see that they contain the "role", an "issued date", and an "expiry date" ~10 years in the future.

```json
{
  "role": "anon",
  "iat": 1625137684,
  "exp": 1940713684
}
```

## The `anon` key

The `anon` key has very few privileges. You can use it in your [RLS policies](https://supabase.com/docs/guides/database/postgres/row-level-security) to allow unauthenticated access. For example, this policy will allow unauthenticated access to the `profiles` table:

```sql
create policy "Allow public access" on profiles to anon for
select using (true);
```

And similarly for disallowing access:

```sql
create policy "Disallow public access" on profiles to anon for
select using (false);
```

If you are using [Supabase Auth](https://supabase.com/docs/guides/auth/overview), then the `anon` role will automatically update to `authenticated` once a user is logged in:

```sql
create policy "Allow access to authenticated users" on profiles to authenticated for
select using (true);
```

## The `service_role` key

The "service_role" is a predefined Postgres role with elevated privileges, designed to perform various administrative and service-related tasks. It can bypass Row Level Security, so it should only be used on a private server.

Never expose the `service_role` key in a browser or anywhere where a user can see it.

A common use case for the `service_role` key is running data analytics jobs on the backend. To support joins on user id, it is often useful to grant the service role read access to `auth.users` table.

```sql
grant select on table auth.users to service_role;
```

We have [partnered with GitHub](https://github.blog/changelog/2022-03-28-supabase-is-now-a-github-secret-scanning-partner/) to scan for Supabase `service_role` keys pushed to public repositories.
If they detect any keys with service_role privileges being pushed to GitHub, they will forward the API key to us, so that we can automatically revoke the detected secrets and notify you, protecting your data against malicious actors.
