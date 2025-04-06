# Google Auth Fails for Some Users

If you start facing errors like the following when users try to authenticate with Google:

```
error=server_error&error_description=Error+getting+user+email+from+external+provider

Missing required authentication credential. Expected OAuth 2 access token, login cookie or other valid authentication credential. See https://developers.google.com/identity/sign-in/web/devconsole-project.
"status": "UNAUTHENTICATED"

500: Error getting user email from external provider
```

## Solution

This issue occurs because some Google Suite instances require the explicit request of email Auth Scopes. You can fix this by adding the `userinfo.email` scope to your Google OAuth sign-in request:

```javascript
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: {
    scopes: 'https://www.googleapis.com/auth/userinfo.email'
  }
})
```

This explicit scope request ensures that your application has permission to access the user's email address, which is required for authentication with Supabase Auth.
