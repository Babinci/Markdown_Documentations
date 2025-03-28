# Sign in with OAuth

This guide explains how to implement social login in your application using Supabase's `signInWithOAuth()` method.

## Overview

The `signInWithOAuth()` method allows users to log in via a third-party provider. Supabase supports many different third-party providers including Google, GitHub, Facebook, and more.

This method is used for signing in using a third-party provider and supports the PKCE flow for enhanced security, particularly useful for server-side authentication.

## Usage

### Basic OAuth Sign In

```javascript
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'github'
})
```

### Sign In with Redirect

For cases where you want to specify a redirect URL, you can use the `redirectTo` option:

```javascript
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'github',
  options: {
    redirectTo: 'https://example.com/welcome'
  }
})
```

### Sign In with Scopes and Provider Tokens

You can request specific scopes from the OAuth provider to access additional user information or resources:

```javascript
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: {
    scopes: 'profile email',
    queryParams: {
      access_type: 'offline',
      prompt: 'consent',
    }
  }
})
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `provider` | string | The third-party provider to use for authentication (e.g., 'github', 'google', 'facebook') |
| `options` | object | Additional options for the sign-in process |
| `options.redirectTo` | string | The URL to redirect the user to after they authenticate with the third-party provider |
| `options.scopes` | string | A space-separated list of scopes to request from the provider |
| `options.queryParams` | object | Additional query parameters to include with the request to the provider |

## Return Value

The method returns a Promise that resolves to an object containing:

- `data`: An object containing:
  - `provider`: The provider used for authentication
  - `url`: The URL to redirect the user to for authentication (if the method is called on the server)
  - `session`: The session object (if authentication is successful in a browser context)
  - `user`: The user object (if authentication is successful in a browser context)
- `error`: Any error that occurred during the sign-in process

## PKCE Flow for Server-Side Auth

For a PKCE (Proof Key for Code Exchange) flow, which is recommended for server-side authentication, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route.

In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint:

```javascript
await supabase.auth.signInWithOAuth({
  provider: 'github',
  options: {
    redirectTo: `http://example.com/auth/callback`,
  },
})
```

At the callback endpoint, handle the code exchange to save the user session. For example, in a Next.js application:

```javascript
// app/auth/callback/route.ts
import { NextResponse } from 'next/server'
import { createClient } from '@/utils/supabase/server'

export async function GET(request: Request) {
  const { searchParams, origin } = new URL(request.url)
  const code = searchParams.get('code')
  const next = searchParams.get('next') ?? '/'
  
  if (code) {
    const supabase = await createClient()
    const { error } = await supabase.auth.exchangeCodeForSession(code)
    if (!error) {
      const forwardedHost = request.headers.get('x-forwarded-host')
      const isLocalEnv = process.env.NODE_ENV === 'development'
      if (isLocalEnv) {
        return NextResponse.redirect(`${origin}${next}`)
      } else if (forwardedHost) {
        return NextResponse.redirect(`https://${forwardedHost}${next}`)
      } else {
        return NextResponse.redirect(`${origin}${next}`)
      }
    }
  }

  return NextResponse.redirect(`${origin}/auth/auth-code-error`)
}
```

## Additional Resources

- For a complete list of supported providers, visit the [Supabase Auth Providers documentation](https://supabase.com/docs/guides/auth/providers)
- To learn more about implementing server-side authentication, see the [Server-Side Auth guide](https://supabase.com/docs/guides/auth/server-side/creating-a-client)
