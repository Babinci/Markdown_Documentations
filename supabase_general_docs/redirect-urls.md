# Redirect URLs

Learn how to set up and configure redirect URLs with Supabase Auth.

## Overview

When using [passwordless sign-ins](https://supabase.com/docs/reference/javascript/auth-signinwithotp) or [third-party providers](https://supabase.com/docs/reference/javascript/auth-signinwithoauth#sign-in-using-a-third-party-provider-with-redirect), the Supabase client library methods provide a `redirectTo` parameter to specify where to redirect the user after authentication. 

By default, the user will be redirected to the `SITE_URL`, but you can modify the `SITE_URL` or add additional redirect URLs to the allow list. Once you've added necessary URLs to the allow list, you can specify the URL you want the user to be redirected to in the `redirectTo` parameter.

To edit the allow list:
- Hosted projects: Go to the [URL Configuration](https://supabase.com/dashboard/project/_/auth/url-configuration) page in the dashboard.
- Local development or self-hosted projects: Use the [configuration file](https://supabase.com/docs/guides/cli/config#auth.additional_redirect_urls).

## Use Wildcards in Redirect URLs

Supabase allows you to specify wildcards when adding redirect URLs to the [allow list](https://supabase.com/dashboard/project/_/auth/url-configuration). You can use wildcard match patterns to support preview URLs from providers like Netlify and Vercel.

| Wildcard | Description |
| --- | --- |
| `*` | Matches any sequence of non-separator characters |
| `**` | Matches any sequence of characters |
| `?` | Matches any single non-separator character |
| `c` | Matches character c (c != `*`, `**`, `?`, `\`, `[`, `{`, `}`) |
| `\c` | Matches character c |
| `[!{ character-range }]` | Matches any sequence of characters not in the `{ character-range }`. For example, `[!a-z]` will not match any characters ranging from a-z. |

The separator characters in a URL are defined as `.` and `/`. You can use [this tool](https://www.digitalocean.com/community/tools/glob?comments=true&glob=http%3A%2F%2Flocalhost%3A3000%2F%2A%2A&matches=false&tests=http%3A%2F%2Flocalhost%3A3000&tests=http%3A%2F%2Flocalhost%3A3000%2F&tests=http%3A%2F%2Flocalhost%3A3000%2F%3Ftest%3Dtest&tests=http%3A%2F%2Flocalhost%3A3000%2Ftest-test%3Ftest%3Dtest&tests=http%3A%2F%2Flocalhost%3A3000%2Ftest%2Ftest%3Ftest%3Dtest) to test your patterns.

> **Recommendation**: While the "globstar" (`**`) is useful for local development and preview URLs, we recommend setting the exact redirect URL path for your site URL in production.

### Redirect URL Examples with Wildcards

| Redirect URL | Description |
| --- | --- |
| `http://localhost:3000/*` | Matches `http://localhost:3000/foo`, `http://localhost:3000/bar` but not `http://localhost:3000/foo/bar` or `http://localhost:3000/foo/` (note the trailing slash) |
| `http://localhost:3000/**` | Matches `http://localhost:3000/foo`, `http://localhost:3000/bar` and `http://localhost:3000/foo/bar` |
| `http://localhost:3000/?` | Matches `http://localhost:3000/a` but not `http://localhost:3000/foo` |
| `http://localhost:3000/[!a-z]` | Matches `http://localhost:3000/1` but not `http://localhost:3000/a` |

## Netlify Preview URLs

For deployments with Netlify, set the `SITE_URL` to your official site URL. Add the following additional redirect URLs for local development and deployment previews:

- `http://localhost:3000/**`
- `https://**--my_org.netlify.app/**`

## Vercel Preview URLs

For deployments with Vercel, set the `SITE_URL` to your official site URL. Add the following additional redirect URLs for local development and deployment previews:

- `http://localhost:3000/**`
- `https://*-<team-or-account-slug>.vercel.app/**`

Vercel provides an environment variable for the URL of the deployment called `NEXT_PUBLIC_VERCEL_URL`. See the [Vercel docs](https://vercel.com/docs/concepts/projects/environment-variables#system-environment-variables) for more details. You can use this variable to dynamically redirect depending on the environment. 

You should also set the value of the environment variable called `NEXT_PUBLIC_SITE_URL`. This should be set to your site URL in the production environment to ensure that redirects function correctly.

```javascript
const getURL = () => {
  let url =
    process?.env?.NEXT_PUBLIC_SITE_URL ?? // Set this to your site URL in production env.
    process?.env?.NEXT_PUBLIC_VERCEL_URL ?? // Automatically set by Vercel.
    'http://localhost:3000/'
  
  // Make sure to include `https://` when not localhost.
  url = url.startsWith('http') ? url : `https://${url}`
  
  // Make sure to include a trailing `/`.
  url = url.endsWith('/') ? url : `${url}/`
  
  return url
}

const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'github',
  options: {
    redirectTo: getURL(),
  },
})
```

## Email Templates When Using `redirectTo`

When using a `redirectTo` option, you may need to replace the `{{ .SiteURL }}` with `{{ .RedirectTo }}` in your email templates. See the [Email Templates guide](https://supabase.com/docs/guides/auth/auth-email-templates) for more information.

For example, change the following:

```html
<!-- Old -->
<a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email">Confirm your mail</a>

<!-- New -->
<a href="{{ .RedirectTo }}/auth/confirm?token_hash={{ .TokenHash }}&type=email">Confirm your mail</a>
```

## Mobile Deep Linking URIs

For mobile applications, you can use deep linking URIs. For example, for your `SITE_URL` you can specify something like `com.supabase://login-callback/` and for additional redirect URLs something like `com.supabase.staging://login-callback/` if needed.

Read more about deep linking and find code examples for different frameworks in the [Native Mobile Deep Linking guide](https://supabase.com/docs/guides/auth/native-mobile-deep-linking).

## Error Handling

When authentication fails, the user will still be redirected to the redirect URL provided. However, the error details will be returned as query fragments in the URL. You can parse these query fragments and show a custom error message to the user. For example:

```javascript
const params = new URLSearchParams(window.location.hash.slice(1))

if (params.get('error_code') && params.get('error_code').startsWith('4')) {
  // Show error message if error is a 4xx error
  window.alert(params.get('error_description'))
}
```

## Common Issues

### Missing URL in Allow List

If you get an error that the redirect URL is not allowed, make sure to:
1. Check if the URL is properly added to the allow list
2. Verify there are no typos in the URL
3. Check if you're using HTTPS in production but HTTP in your code

### Trailing Slash Issues

Pay close attention to trailing slashes in your URLs. Make sure they match exactly or use wildcards to handle both cases.

### URL Encoding

If your redirect URL contains special characters or parameters, ensure they are properly URL encoded when passing to the `redirectTo` parameter.
