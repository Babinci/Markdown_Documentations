# Integrating With Supabase Auth

Edge Functions work seamlessly with Supabase Auth, allowing you to access authenticated user information and enforce Row Level Security (RLS) policies.

## Auth Context

When a user makes a request to an Edge Function, you can use the Authorization header to set the Auth context in the Supabase client:

```javascript
import { createClient } from 'jsr:@supabase/supabase-js@2'

Deno.serve(async (req: Request) => {
  const supabaseClient = createClient(
    Deno.env.get('SUPABASE_URL') ?? '',
    Deno.env.get('SUPABASE_ANON_KEY') ?? '',
  );
  
  // Get the session or user object
  const authHeader = req.headers.get('Authorization')!;
  const token = authHeader.replace('Bearer ', '');
  const { data } = await supabaseClient.auth.getUser(token);
})
```

Importantly, this is done _inside_ the `Deno.serve()` callback argument, so that the Authorization header is set for each request.

## Fetching the User

After initializing a Supabase client with the Auth context, you can use `getUser()` to fetch the user object, and run queries in the context of the user with Row Level Security (RLS) policies enforced.

```javascript
import { createClient } from 'jsr:@supabase/supabase-js@2'

Deno.serve(async (req: Request) => {
  const supabaseClient = createClient(
    Deno.env.get('SUPABASE_URL') ?? '',
    Deno.env.get('SUPABASE_ANON_KEY') ?? '',
  )
  
  // Get the session or user object
  const authHeader = req.headers.get('Authorization')!
  const token = authHeader.replace('Bearer ', '')
  const { data } = await supabaseClient.auth.getUser(token)
  const user = data.user
  
  return new Response(JSON.stringify({ user }), {
    headers: { 'Content-Type': 'application/json' },
    status: 200,
  })
})
```

## Row Level Security

After initializing a Supabase client with the Auth context, all queries will be executed with the context of the user. For database queries, this means [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) will be enforced.

```javascript
import { createClient } from 'jsr:@supabase/supabase-js@2'

Deno.serve(async (req: Request) => {
  const supabaseClient = createClient(
    Deno.env.get('SUPABASE_URL') ?? '',
    Deno.env.get('SUPABASE_ANON_KEY') ?? '',
  );
  
  // Get the session or user object
  const authHeader = req.headers.get('Authorization')!;
  const token = authHeader.replace('Bearer ', '');
  const { data: userData } = await supabaseClient.auth.getUser(token);
  
  const { data, error } = await supabaseClient.from('profiles').select('*');
  
  return new Response(JSON.stringify({ data }), {
    headers: { 'Content-Type': 'application/json' },
    status: 200,
  })
})
```

## Example Code

See a full [example on GitHub](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/select-from-table-with-auth-rls/index.ts) for integrating Supabase Auth with Edge Functions.
