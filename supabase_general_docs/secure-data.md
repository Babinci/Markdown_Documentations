# Securing Your Data

Supabase helps you control access to your data. With access policies, you can protect sensitive data and make sure users only access what they're allowed to see.

## Connecting your app securely

Supabase allows you to access your database using the auto-generated [Data APIs](https://supabase.com/docs/guides/database/connecting-to-postgres#data-apis). This speeds up the process of building web apps, since you don't need to write your own backend services to pass database queries and results back and forth.

You can keep your data secure while accessing the Data APIs from the frontend, so long as you:

- Turn on [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) (RLS) for your tables
- Use your Supabase **anon key** when you create a Supabase client

Your anon key is safe to expose with RLS enabled, because row access permission is checked against your access policies and the user's [JSON Web Token (JWT)](https://supabase.com/docs/learn/auth-deep-dive/auth-deep-dive-jwts). The JWT is automatically sent by the Supabase client libraries if the user is logged in using Supabase Auth.

> **Never expose your service role key on the frontend**
>
> Unlike your anon key, your **service role key** is **never** safe to expose because it bypasses RLS. Only use your service role key on the backend. Treat it as a secret (for example, import it as a sensitive environment variable instead of hardcoding it).

## More information

Supabase and Postgres provide you with multiple ways to manage security, including but not limited to Row Level Security. See the Access and Security pages for more information:

- [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Column Level Security](https://supabase.com/docs/guides/database/postgres/column-level-security)
- [Hardening the Data API](https://supabase.com/docs/guides/database/hardening-data-api)
- [Managing Postgres roles](https://supabase.com/docs/guides/database/postgres/roles)
- [Managing secrets with Vault](https://supabase.com/docs/guides/database/vault)
