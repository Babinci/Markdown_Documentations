# Login with Bitbucket

This guide explains how to set up Bitbucket Auth for your Supabase project.

## Overview

Setting up Bitbucket logins for your application consists of 3 parts:

1. Create and configure a Bitbucket OAuth Consumer on [Bitbucket](https://bitbucket.org/)
2. Add your Bitbucket OAuth Consumer keys to your [Supabase Project](https://supabase.com/dashboard)
3. Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)

## Access your Bitbucket account

- Go to [bitbucket.org](https://bitbucket.org/)
- Click on `Login` at the top right to log in

![Bitbucket Developer Portal](https://supabase.com/docs/img/guides/auth-bitbucket/bitbucket-portal.png)

## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

- Go to your [Supabase Project Dashboard](https://supabase.com/dashboard)
- Click on the `Authentication` icon in the left sidebar
- Click on [`Providers`](https://supabase.com/dashboard/project/_/auth/providers) under the Configuration section
- Click on **Bitbucket** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

For testing OAuth locally with the Supabase CLI see the [local development docs](https://supabase.com/docs/guides/cli/local-development#use-auth-locally).

## Create a Bitbucket OAuth app

- Click on your profile icon at the bottom left
- Click on `All Workspaces`
- Select a workspace and click on it to select it
- Click on `Settings` on the left
- Click on `OAuth consumers` on the left under `Apps and Features` (near the bottom)
- Click `Add Consumer` at the top
- Enter the name of your app under `Name`
- In `Callback URL`, type the callback URL of your app
- Check the permissions you need (Email, Read should be enough)
- Click `Save` at the bottom
- Click on your app name (the name of your new OAuth Consumer)
- Copy your `Key` (`client_key`) and `Secret` (`client_secret`) codes

## Add your Bitbucket credentials into your Supabase project

- Go to your [Supabase Project Dashboard](https://supabase.com/dashboard)
- In the left sidebar, click the `Authentication` icon (near the top)
- Click on [`Providers`](https://supabase.com/dashboard/project/_/auth/providers) under the Configuration section
- Click on **BitBucket** from the accordion list to expand and turn **BitBucket Enabled** to ON
- Enter your **BitBucket Client ID** and **BitBucket Client Secret** saved in the previous step
- Click `Save`

## Add login code to your client app

### JavaScript Client

Make sure you're using the right `supabase` client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](https://supabase.com/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.

When your user signs in, call [`signInWithOAuth()`](https://supabase.com/docs/reference/javascript/auth-signinwithoauth) with `bitbucket` as the `provider`:

```javascript
async function signInWithBitbucket() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'bitbucket',
  })
}
```

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](https://supabase.com/docs/guides/auth/redirect-urls).

In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

```javascript
await supabase.auth.signInWithOAuth({
  provider,
  options: {
    redirectTo: `http://example.com/auth/callback`,
  },
})
```

At the callback endpoint, handle the code exchange to save the user session.

#### Next.js Example

Create a new file at `app/auth/callback/route.ts` and populate with the following:

```typescript
import { NextResponse } from 'next/server'
// The client you created from the Server-Side Auth instructions
import { createClient } from '@/utils/supabase/server'

export async function GET(request: Request) {
  const { searchParams, origin } = new URL(request.url)
  const code = searchParams.get('code')
  // if "next" is in param, use it as the redirect URL
  const next = searchParams.get('next') ?? '/'

  if (code) {
    const supabase = await createClient()
    const { error } = await supabase.auth.exchangeCodeForSession(code)
    if (!error) {
      const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer
      const isLocalEnv = process.env.NODE_ENV === 'development'
      if (isLocalEnv) {
        // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host
        return NextResponse.redirect(`${origin}${next}`)
      } else if (forwardedHost) {
        return NextResponse.redirect(`https://${forwardedHost}${next}`)
      } else {
        return NextResponse.redirect(`${origin}${next}`)
      }
    }
  }

  // return the user to an error page with instructions
  return NextResponse.redirect(`${origin}/auth/auth-code-error`)
}
```

When your user signs out, call [signOut()](https://supabase.com/docs/reference/javascript/auth-signout) to remove them from the browser session and any objects from localStorage:

```javascript
async function signOut() {
  const { error } = await supabase.auth.signOut()
}
```

## Resources

- [Supabase - Get started for free](https://supabase.com/)
- [Supabase JS Client](https://github.com/supabase/supabase-js)
- [Bitbucket Account](https://bitbucket.org/)
