# Supabase Auth with Remix

This guide covers how to implement Supabase Auth in a Remix application.

## Recommended Approach

We recommend using the newer `@supabase/ssr` package for integrating Supabase Auth with Remix applications. This package provides a more flexible and framework-agnostic approach to server-side authentication.

### Benefits of `@supabase/ssr`

- Works with any server framework, not just Remix
- Simpler API with fewer abstractions
- Better type safety
- More consistent behavior across frameworks
- Actively maintained and updated

## Getting Started with `@supabase/ssr`

### 1. Install Dependencies

```bash
npm install @supabase/supabase-js @supabase/ssr
```

### 2. Create Your Supabase Client

Create a file, such as `lib/supabase.ts`:

```typescript
import { createServerClient } from '@supabase/ssr'
import { type LoaderFunctionArgs, type ActionFunctionArgs } from '@remix-run/node'

// Server-side client creation
export function createClient(request: Request) {
  const cookies = Object.fromEntries(
    request.headers.get('cookie')?.split('; ')?.map(c => c.split('=')) || []
  )
  
  return createServerClient(
    process.env.SUPABASE_URL!,
    process.env.SUPABASE_ANON_KEY!,
    {
      cookies: {
        get: (key) => cookies[key],
        set: (key, value, options) => {
          // Will need to implement a set-cookie header manipulator here
          // to work with Remix response
        },
        remove: (key, options) => {
          // Will need to implement a set-cookie header manipulator here
          // to work with Remix response
        },
      },
    }
  )
}

// Helper for loader functions
export async function getSession(args: LoaderFunctionArgs) {
  const { request } = args
  const supabase = createClient(request)
  
  const { data: { session } } = await supabase.auth.getSession()
  return { supabase, session }
}
```

### 3. Use in Loader Functions

```typescript
import { json } from '@remix-run/node'
import { getSession } from '~/lib/supabase'
import type { LoaderFunctionArgs } from '@remix-run/node'

export async function loader(args: LoaderFunctionArgs) {
  const { session, supabase } = await getSession(args)
  
  if (!session) {
    return json({ error: 'Unauthorized' }, { status: 401 })
  }
  
  const { data } = await supabase.from('profiles').select('*').single()
  
  return json({ profile: data })
}
```

### 4. Sign In and Sign Out

```typescript
import { createClient } from '~/lib/supabase'
import type { ActionFunctionArgs } from '@remix-run/node'

export async function action(args: ActionFunctionArgs) {
  const { request } = args
  const formData = await request.formData()
  const email = formData.get('email') as string
  const password = formData.get('password') as string
  
  const supabase = createClient(request)
  
  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password
  })
  
  if (error) {
    return json({ error: error.message }, { status: 400 })
  }
  
  // Handle setting the auth cookie in the response
  // and redirect the user
}
```

## Migrating from Auth Helpers

If you're currently using the `@supabase/auth-helpers-remix` package, we recommend migrating to `@supabase/ssr`. For detailed migration instructions, please refer to the [Migration Guide](https://supabase.com/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers).

Key differences to be aware of:

1. Different method names and signature
2. Different cookie handling approach
3. No built-in context providers (you may need to create your own)

## Authentication Patterns in Remix

### Protected Routes

```typescript
// app/routes/dashboard.tsx
import { json, redirect } from '@remix-run/node'
import { getSession } from '~/lib/supabase'
import type { LoaderFunctionArgs } from '@remix-run/node'

export async function loader(args: LoaderFunctionArgs) {
  const { session, supabase } = await getSession(args)
  
  if (!session) {
    return redirect('/login')
  }
  
  // Fetch protected data
  const { data } = await supabase.from('protected_table').select('*')
  
  return json({ data })
}
```

### Handling Auth State in Components

```tsx
// app/routes/index.tsx
import { useLoaderData } from '@remix-run/react'

export default function Index() {
  const { session } = useLoaderData<typeof loader>()
  
  return (
    <div>
      {session ? (
        <p>Logged in as: {session.user.email}</p>
      ) : (
        <p>Not logged in</p>
      )}
    </div>
  )
}
```

## Additional Resources

- [Supabase SSR Documentation](https://supabase.com/docs/guides/auth/server-side)
- [Remix Documentation](https://remix.run/docs/en/main)
- [Complete Remix Example on GitHub](https://github.com/supabase/supabase/tree/master/examples/auth/remix)
