# Login with Figma

This guide explains how to set up Figma Authentication for your Supabase project.

## Overview

Setting up Figma logins for your application consists of 3 parts:

1. Create and configure a Figma App on the [Figma Developers page](https://www.figma.com/developers)
2. Add your Figma `client_id` and `client_secret` to your [Supabase Project](https://app.supabase.com/)
3. Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)

## Access the Figma Developers page

- Go to the [Figma Developers page](https://www.figma.com/developers)
- Click on `My apps` at the top right
- Log in (if necessary)

![Figma Developers page](https://supabase.com/docs/img/guides/auth-figma/figma_developers_page.png)

## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

- Go to your [Supabase Project Dashboard](https://supabase.com/dashboard)
- Click on the `Authentication` icon in the left sidebar
- Click on [`Providers`](https://supabase.com/dashboard/project/_/auth/providers) under the Configuration section
- Click on **Figma** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

For testing OAuth locally with the Supabase CLI see the [local development docs](https://supabase.com/docs/guides/cli/local-development#use-auth-locally).

## Create a Figma OAuth app

- Enter your `App name`, `Website URL` and upload your app logo
- Click on `Add callback`
- Add your `Callback URL`
- Click on `Save`

![Create Figma app](https://supabase.com/docs/img/guides/auth-figma/figma_create_app.png)

- Copy and save your newly-generated `Client ID`
- Copy and save your newly-generated `Client Secret`

![Get Figma app credentials](https://supabase.com/docs/img/guides/auth-figma/figma_app_credentials.png)

## Enter your Figma credentials into your Supabase project

- Go to your [Supabase Project Dashboard](https://supabase.com/dashboard)
- In the left sidebar, click the `Authentication` icon (near the top)
- Click on [`Providers`](https://supabase.com/dashboard/project/_/auth/providers) under the Configuration section
- Click on **Figma** from the accordion list to expand and turn **Figma Enabled** to ON
- Enter your **Figma Client ID** and **Figma Client Secret** saved in the previous step
- Click `Save`

## Add login code to your client app

### JavaScript Client

Make sure you're using the right `supabase` client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](https://supabase.com/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.

When your user signs in, call [`signInWithOAuth()`](https://supabase.com/docs/reference/javascript/auth-signinwithoauth) with `figma` as the `provider`:

```javascript
async function signInWithFigma() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'figma',
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
- [Figma Developers page](https://www.figma.com/developers)
