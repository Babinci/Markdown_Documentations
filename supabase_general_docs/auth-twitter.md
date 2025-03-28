# Login with Twitter

To enable Twitter Auth for your project, you need to set up a Twitter OAuth application and add the application credentials in the Supabase Dashboard.

## Overview

Setting up Twitter logins for your application consists of 3 parts:

1. Create and configure a Twitter Project and App on the [Twitter Developer Dashboard](https://developer.twitter.com/en/portal/dashboard).
2. Add your Twitter `API Key` and `API Secret Key` to your [Supabase Project](https://supabase.com/dashboard).
3. Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js).

## Access your Twitter Developer Account

1. Go to [developer.twitter.com](https://developer.twitter.com/).
2. Click on `Sign in` at the top right to log in.

## Find your Callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

1. Go to your [Supabase Project Dashboard](https://supabase.com/dashboard)
2. Click on the `Authentication` icon in the left sidebar
3. Click on [`Providers`](https://supabase.com/dashboard/project/_/auth/providers) under the Configuration section
4. Click on **Twitter** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

For testing OAuth locally with the Supabase CLI see the [local development docs](https://supabase.com/docs/guides/cli/local-development#use-auth-locally).

## Create a Twitter OAuth App

1. Click `+ Create Project`.
   - Enter your project name, click `Next`.
   - Select your use case, click `Next`.
   - Enter a description for your project, click `Next`.
   - Enter a name for your app, click `Next`.
   - Copy and save your `API Key` (this is your `client_id`).
   - Copy and save your `API Secret Key` (this is your `client_secret`).
   - Click on `App settings` to proceed to next steps.
2. At the bottom, you will find `User authentication settings`. Click on `Set up`.
3. Under `User authentication settings`, you can configure `App permissions`.
4. Make sure you turn ON `Request email from users`.
5. Select `Web App...` as the `Type of App`.
6. Under `App info` configure the following:
   - Enter your `Callback URL`. Check the **Find your callback URL** section above to learn how to obtain your callback URL.
   - Enter your `Website URL` (tip: try `http://127.0.0.1:port` or `http://www.localhost:port` during development)
   - Enter your `Terms of service URL`.
   - Enter your `Privacy policy URL`.
7. Click `Save`.

## Enter your Twitter Credentials into your Supabase Project

1. Go to your [Supabase Project Dashboard](https://supabase.com/dashboard)
2. In the left sidebar, click the `Authentication` icon (near the top)
3. Click on [`Providers`](https://supabase.com/dashboard/project/_/auth/providers) under the Configuration section
4. Click on **Twitter** from the accordion list to expand and turn **Twitter Enabled** to ON
5. Enter your **Twitter Client ID** and **Twitter Client Secret** saved in the previous step
6. Click `Save`

## Add Login Code to your Client App

Make sure you're using the right `supabase` client in the following code.

If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](https://supabase.com/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.

When your user signs in, call [`signInWithOAuth()`](https://supabase.com/docs/reference/javascript/auth-signinwithoauth) with `twitter` as the `provider`:

```javascript
async function signInWithTwitter() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'twitter',
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
- [Twitter Developer Dashboard](https://developer.twitter.com/en/portal/dashboard)
