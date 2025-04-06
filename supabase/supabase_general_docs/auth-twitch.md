# Login with Twitch

To enable Twitch Auth for your project, you need to set up a Twitch Application and add the Application OAuth credentials to your Supabase Dashboard.

## Overview

Setting up Twitch logins for your application consists of 3 parts:

1. Create and configure a Twitch Application in the [Twitch Developer Console](https://dev.twitch.tv/console)
2. Add your Twitch OAuth Consumer keys to your [Supabase Project](https://supabase.com/dashboard)
3. Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)

## Access your Twitch Developer Account

1. Go to [dev.twitch.tv](https://dev.twitch.tv/).
2. Click on `Log in with Twitch` at the top right to log in.
3. If you have not already enabled 2-Factor Authentication for your Twitch Account, you will need to do that at [Twitch Security Settings](https://www.twitch.tv/settings/security) before you can continue.
4. Once logged in, go to the [Twitch Developer Console](https://dev.twitch.tv/console).

## Find your Callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

1. Go to your [Supabase Project Dashboard](https://supabase.com/dashboard)
2. Click on the `Authentication` icon in the left sidebar
3. Click on [`Providers`](https://supabase.com/dashboard/project/_/auth/providers) under the Configuration section
4. Click on **Twitch** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

For testing OAuth locally with the Supabase CLI, see the [local development docs](https://supabase.com/docs/guides/cli/local-development#use-auth-locally).

## Create a Twitch Application

1. Click on `+ Register Your Application` at the top right of the Developer Console.
2. Enter the name of your application.
3. Type or paste your `OAuth Redirect URL` (the callback URL from the previous step).
4. Select a category for your app.
5. Check the CAPTCHA box and click `Create`.

## Retrieve your Twitch OAuth Client ID and Client Secret

1. Click `Manage` at the right of your application entry in the list.
2. Copy your Client ID.
3. Click `New Secret` to create a new Client Secret.
4. Copy your Client Secret.

## Add your Twitch Credentials into your Supabase Project

1. Go to your [Supabase Project Dashboard](https://supabase.com/dashboard)
2. In the left sidebar, click the `Authentication` icon (near the top)
3. Click on [`Providers`](https://supabase.com/dashboard/project/_/auth/providers) under the Configuration section
4. Click on **Twitch** from the accordion list to expand and turn **Twitch Enabled** to ON
5. Enter your **Twitch Client ID** and **Twitch Client Secret** saved in the previous step
6. Click `Save`

## Add Login Code to your Client App

Make sure you're using the right `supabase` client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](https://supabase.com/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.

When your user signs in, call [`signInWithOAuth()`](https://supabase.com/docs/reference/javascript/auth-signinwithoauth) with `twitch` as the `provider`:

```javascript
async function signInWithTwitch() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'twitch',
  })
}
```

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](https://supabase.com/docs/guides/auth/redirect-urls).

In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint:

```javascript
await supabase.auth.signInWithOAuth({
  provider,
  options: {
    redirectTo: `http://example.com/auth/callback`,
  },
})
```

At the callback endpoint, handle the code exchange to save the user session. For example, in Next.js, create a new file at `app/auth/callback/route.ts` and populate with the following:

```javascript
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
- [Twitch Account](https://twitch.tv/)
- [Twitch Developer Console](https://dev.twitch.tv/console)
