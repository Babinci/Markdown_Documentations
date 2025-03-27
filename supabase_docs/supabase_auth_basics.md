# Supabase Authentication Basics

## Table of Contents
- [Introduction](#introduction)
- [Create a New User](#create-a-new-user)
- [Create an Anonymous User](#create-an-anonymous-user)
- [Sign In a User](#sign-in-a-user)
- [Sign In with ID Token](#sign-in-with-id-token)
- [Sign In a User Through OTP](#sign-in-a-user-through-otp)
- [Sign Out a User](#sign-out-a-user)
- [Send a Password Reset Request](#send-a-password-reset-request)
- [Verify and Log In Through OTP](#verify-and-log-in-through-otp)
- [Retrieve a Session](#retrieve-a-session)
- [Retrieve a New Session](#retrieve-a-new-session)
- [Retrieve a User](#retrieve-a-user)
- [Update a User](#update-a-user)
- [Send a Password Reauthentication Nonce](#send-a-password-reauthentication-nonce)
- [Resend an OTP](#resend-an-otp)
- [Set the Session Data](#set-the-session-data)
- [Exchange an Auth Code for a Session](#exchange-an-auth-code-for-a-session)
- [Other Documentation Files](#other-documentation-files)

## Introduction

- The auth methods can be accessed via the `supabase.auth` namespace.
- By default, the supabase client sets `persist_session` to true and attempts to store the session in memory.
- Any email links and one-time passwords (OTPs) sent have a default expiry of 24 hours. We have the following [rate limits](https://supabase.com/docs/guides/platform/going-into-prod#auth-rate-limits) in place to guard against brute force attacks.
- The expiry of an access token can be set in the "JWT expiry limit" field in [your project's auth settings](https://supabase.com/dashboard/project/_/settings/auth). A refresh token never expires and can only be used once.

## Create a New User

- By default, the user needs to verify their email address before logging in. To turn this off, disable **Confirm email** in [your project](https://supabase.com/dashboard/project/_/auth/providers).
- **Confirm email** determines if users need to confirm their email address after signing up.
  - If **Confirm email** is enabled, a `user` is returned but `session` is null.
  - If **Confirm email** is disabled, both a `user` and a `session` are returned.
- By default, when the user confirms their email address, they are redirected to the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls). You can modify your `SITE_URL` or add additional redirect URLs in [your project](https://supabase.com/dashboard/project/_/auth/url-configuration).
- If sign_up() is called for an existing confirmed user:
  - When both **Confirm email** and **Confirm phone** (even when phone provider is disabled) are enabled in [your project](https://supabase.com/dashboard/project/_/auth/providers), an obfuscated/fake user object is returned.
  - When either **Confirm email** or **Confirm phone** (even when phone provider is disabled) is disabled, the error message, `User already registered` is returned.
- To fetch the currently logged-in user, refer to [`get_user()`](#retrieve-a-user).

### Parameters

- **credentials** *Required* `SignUpWithPasswordCredentials`

### Example

```python
response = supabase.auth.sign_up(
    {
        "email": "email@example.com", 
        "password": "password",
    }
)
```

## Create an Anonymous User

- Returns an anonymous user
- It is recommended to set up captcha for anonymous sign-ins to prevent abuse. You can pass in the captcha token in the `options` param.

### Parameters

- **credentials** *Required* `SignInAnonymouslyCredentials`

### Example

```python
response = supabase.auth.sign_in_anonymously(
    {"options": {"captcha_token": ""}}
)
```

## Sign In a User

Log in an existing user with an email and password or phone and password.

- Requires either an email and password or a phone number and password.

### Parameters

- **credentials** *Required* `SignInWithPasswordCredentials`

### Example

```python
response = supabase.auth.sign_in_with_password(
    {
        "email": "email@example.com", 
        "password": "example-password",
    }
)
```

## Sign In with ID Token

Allows signing in with an OIDC ID token. The authentication provider used should be enabled and configured.

### Parameters

- **credentials** *Required* `SignInWithIdTokenCredentials`

### Example

```python
response = supabase.auth.sign_in_with_id_token(
    {
        "provider": "google", 
        "token": "your-id-token",
    }
)
```

## Sign In a User Through OTP

- Requires either an email or phone number.
- This method is used for passwordless sign-ins where a OTP is sent to the user's email or phone number.
- If the user doesn't exist, `sign_in_with_otp()` will signup the user instead. To restrict this behavior, you can set `should_create_user` in `SignInWithPasswordlessCredentials.options` to `false`.
- If you're using an email, you can configure whether you want the user to receive a magiclink or a OTP.
- If you're using phone, you can configure whether you want the user to receive a OTP.
- The magic link's destination URL is determined by the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls).
- See [redirect URLs and wildcards](https://supabase.com/docs/guides/auth/redirect-urls#use-wildcards-in-redirect-urls) to add additional redirect URLs to your project.
- Magic links and OTPs share the same implementation. To send users a one-time code instead of a magic link, [modify the magic link email template](https://supabase.com/dashboard/project/_/auth/templates) to include `{{ .Token }}` instead of `{{ .ConfirmationURL }}`.

### Parameters

- **credentials** *Required* `SignInWithOtpCredentials`

### Example

```python
response = supabase.auth.sign_in_with_otp(
    {
        "email": "email@example.com",
        "options": {
            "email_redirect_to": "https://example.com/welcome",
        },
    }
)
```

## Sign Out a User

- In order to use the `sign_out()` method, the user needs to be signed in first.
- By default, `sign_out()` uses the global scope, which signs out all other sessions that the user is logged into as well.
- Since Supabase Auth uses JWTs for authentication, the access token JWT will be valid until it's expired. When the user signs out, Supabase revokes the refresh token and deletes the JWT from the client-side. This does not revoke the JWT and it will still be valid until it expires.

### Parameters

- **options** *Optional* `SignOutOptions`

### Example

```python
response = supabase.auth.sign_out()
```

## Send a Password Reset Request

- The password reset flow consist of 2 broad steps: (i) Allow the user to login via the password reset link; (ii) Update the user's password.
- The `reset_password_for_email()` only sends a password reset link to the user's email. To update the user's password, see [`update_user()`](#update-a-user).
- When the user clicks the reset link in the email they are redirected back to your application. You can configure the URL that the user is redirected to with the `redirectTo` parameter. See [redirect URLs and wildcards](https://supabase.com/docs/reference/python/docs/guides/auth/redirect-urls#use-wildcards-in-redirect-urls) to add additional redirect URLs to your project.
- After the user has been redirected successfully, prompt them for a new password and call `update_user()`:

```python
response = supabase.auth.update_user(
    {"password": new_password}
)
```

### Parameters

- **email** *Required* `string`  
  The email address of the user.

- **options** *Optional* `object`

### Example

```python
supabase.auth.reset_password_for_email(
    email,
    {
        "redirect_to": "https://example.com/update-password",
    }
)
```

## Verify and Log In Through OTP

- The `verify_otp` method takes in different verification types. If a phone number is used, the type can either be `sms` or `phone_change`. If an email address is used, the type can be one of the following: `email`, `recovery`, `invite` or `email_change` (`signup` and `magiclink` types are deprecated).
- The verification type used should be determined based on the corresponding auth method called before `verify_otp` to sign up / sign-in a user.
- The `TokenHash` is contained in the [email templates](https://supabase.com/docs/guides/auth/auth-email-templates) and can be used to sign in. You may wish to use the hash with Magic Links for the PKCE flow for Server Side Auth. See [this guide](https://supabase.com/docs/guides/auth/server-side/email-based-auth-with-pkce-flow-for-ssr) for more details.

### Parameters

- **params** *Required* `VerifyOtpParams`

### Example

```python
response = supabase.auth.verify_otp(
    {
        "email": "email@example.com", 
        "token": "123456", 
        "type": "email",
    }
)
```

## Retrieve a Session

- This method retrieves the current local session (i.e in memory).
- The session contains a signed JWT and unencoded session data.
- Since the unencoded session data is retrieved from the local storage medium, **do not** rely on it as a source of trusted data on the server. It could be tampered with by the sender. If you need verified, trustworthy user data, call [`get_user`](#retrieve-a-user) instead.
- If the session has an expired access token, this method will use the refresh token to get a new session.

### Example

```python
response = supabase.auth.get_session()
```

## Retrieve a New Session

Returns a new session, regardless of expiry status. Takes in an optional refresh token. If not passed in, then refresh_session() will attempt to retrieve it from get_session(). If the current session's refresh token is invalid, an error will be thrown.

- This method will refresh the session whether the current one is expired or not.

### Parameters

- **refresh_token** *Optional* `string`

### Example

```python
response = supabase.auth.refresh_session()
```

## Retrieve a User

- This method fetches the user object from the database instead of local session.
- This method is useful for checking if the user is authorized because it validates the user's access token JWT on the server.

### Parameters

- **jwt** *Optional* `string`  
  Takes in an optional access token JWT. If no JWT is provided, the JWT from the current session is used.

### Example

```python
response = supabase.auth.get_user()
```

## Update a User

- In order to use the `update_user()` method, the user needs to be signed in first.
- By default, email updates sends a confirmation link to both the user's current and new email. To only send a confirmation link to the user's new email, disable **Secure email change** in your project's [email auth provider settings](https://supabase.com/dashboard/project/_/auth/providers).

### Example

```python
response = supabase.auth.update_user(
    {"email": "new@email.com"}
)
```

## Send a Password Reauthentication Nonce

- This method is used together with `updateUser()` when a user's password needs to be updated.
- If you require your user to reauthenticate before updating their password, you need to enable the **Secure password change** option in your [project's email provider settings](https://supabase.com/dashboard/project/_/auth/providers).
- A user is only require to reauthenticate before updating their password if **Secure password change** is enabled and the user **hasn't recently signed in**. A user is deemed recently signed in if the session was created in the last 24 hours.
- This method will send a nonce to the user's email. If the user doesn't have a confirmed email address, the method will send the nonce to the user's confirmed phone number instead.

### Example

```python
response = supabase.auth.reauthenticate()
```

## Resend an OTP

- Resends a signup confirmation, email change or phone change email to the user.
- Passwordless sign-ins can be resent by calling the `sign_in_with_otp()` method again.
- Password recovery emails can be resent by calling the `reset_password_for_email()` method again.
- This method will only resend an email or phone OTP to the user if there was an initial signup, email change or phone change request being made.
- You can specify a redirect url when you resend an email link using the `email_redirect_to` option.

### Parameters

- **credentials** *Required* `ResendCredentials`

### Example

```python
response = supabase.auth.resend(
    {
        "type": "signup",
        "email": "email@example.com",
        "options": {
            "email_redirect_to": "https://example.com/welcome",
        },
    }
)
```

## Set the Session Data

Sets the session data from the current session. If the current session is expired, setSession will take care of refreshing it to obtain a new session. If the refresh token or access token in the current session is invalid, an error will be thrown.

- This method sets the session using an `access_token` and `refresh_token`.
- If successful, a `SIGNED_IN` event is emitted.

### Parameters

- **access_token** *Required* `string`

- **refresh_token** *Required* `string`

### Example

```python
response = supabase.auth.set_session(access_token, refresh_token)
```

## Exchange an Auth Code for a Session

Log in an existing user by exchanging an Auth Code issued during the PKCE flow.

- Used when `flow_type` is set to `pkce` in client options.

### Parameters

- **auth_code** *Required* `string`

### Example

```python
response = supabase.auth.exchange_code_for_session(
    {"auth_code": "34e770dd-9ff9-416c-87fa-43b31d7ef225"}
)
```

## Other Documentation Files

- [Overview](./supabase_overview.md)
- [Database Operations](./supabase_database.md)
- [Query Filters](./supabase_filters.md)
- [OAuth Authentication](./supabase_auth_oauth.md)
- [Multi-factor Authentication](./supabase_auth_mfa.md)
- [Admin Authentication Methods](./supabase_auth_admin.md)
- [Realtime](./supabase_realtime.md)
- [Storage](./supabase_storage.md)
- [Edge Functions](./supabase_edge_functions.md)
