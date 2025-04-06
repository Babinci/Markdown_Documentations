# SSO and Social Login with WorkOS

This guide shows how to set up and use WorkOS for Social Login and SSO with your Supabase project.

## Use Social Login with WorkOS

### Step 1: Create a WorkOS Organization

1. Log in to the WorkOS dashboard and visit the Organizations tab to create an organization.
2. Alternatively, you can [create an organization via the WorkOS API](https://workos.com/docs/reference/organization/create).

### Step 2: Obtain your Client ID and API Key Values

Visit the getting started page of the [WorkOS Dashboard](https://dashboard.workos.com/get-started). Copy the following values from the Quickstart panel:

- `WORKOS_CLIENT_ID`
- `WORKOS_API_KEY`

You must be signed in to see these values.

### Step 3: Add your WorkOS Credentials to your Supabase Project

1. Go to your Supabase Project Dashboard.
2. In the left sidebar, click the Authentication icon (near the top).
3. Click on Providers under the Configuration section.
4. Click on WorkOS from the accordion list to expand.
5. Toggle the `WorkOS Enabled` switch to ON.
6. Enter `https://api.workos.com` in the WorkOS URL field.
7. Enter your WorkOS Client ID and WorkOS Client Secret saved in the previous step.
8. Copy the `Callback URL (for OAuth)` value from the form and save it somewhere handy.
9. Click Save.

### Step 4: Set your Supabase Redirect URI in the WorkOS Dashboard

1. Visit the WorkOS dashboard and click the redirects button in the left navigation panel.
2. On the redirects page, enter your Supabase project's `Callback URL (for OAuth)` which you saved in the previous step.

### Step 5: Add Login Code to your Client App

When a user signs in, call `signInWithOAuth` with `workos` as the provider:

```javascript
async function signInWithWorkOS() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'workos',
    options: {
      redirectTo: 'http://example.com/auth/v1/callback', // Make sure your redirect URL is configured in the Supabase Dashboard Auth settings
      queryParams: {
        connection: '<connection_id>',
      },
    },
  })
  
  if (data.url) {
    redirect(data.url) // use the redirect API for your server or framework
  }
}
```

You can find your `connection_id` in the WorkOS dashboard under the Organizations tab. Select your organization and then click View connection.

Within your specified callback URL, you'll exchange the code for a logged-in user profile. For example, in Next.js:

```javascript
import { NextResponse } from 'next/server'
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

## Resources

- [WorkOS Documentation](https://workos.com/docs/sso/guide)
