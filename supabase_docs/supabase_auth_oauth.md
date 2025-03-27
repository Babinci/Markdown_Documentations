# Supabase OAuth Authentication

## Table of Contents
- [Introduction](#introduction)
- [Sign In a User Through OAuth](#sign-in-a-user-through-oauth)
- [Sign In a User Through SSO](#sign-in-a-user-through-sso)
- [Retrieve Identities Linked to a User](#retrieve-identities-linked-to-a-user)
- [Link an Identity to a User](#link-an-identity-to-a-user)
- [Unlink an Identity from a User](#unlink-an-identity-from-a-user)
- [Other Documentation Files](#other-documentation-files)

## Introduction

Supabase Auth supports multiple authentication methods including OAuth and SSO (Single Sign-On). This document covers the OAuth-related functionality provided by the Supabase Python client.

## Sign In a User Through OAuth

- This method is used for signing in using a third-party provider.
- Supabase supports many different [third-party providers](https://supabase.com/docs/guides/auth#configure-third-party-providers).

### Parameters

- **credentials** *Required* `SignInWithOAuthCredentials`

### Example

```python
response = supabase.auth.sign_in_with_oauth(
    {"provider": "github"}
)
```

## Sign In a User Through SSO

- Before you can call this method you need to [establish a connection](https://supabase.com/docs/guides/auth/sso/auth-sso-saml#managing-saml-20-connections) to an identity provider. Use the [CLI commands](https://supabase.com/docs/reference/cli/supabase-sso) to do this.
- If you've associated an email domain to the identity provider, you can use the `domain` property to start a sign-in flow.
- In case you need to use a different way to start the authentication flow with an identity provider, you can use the `provider_id` property. For example:
  - Mapping specific user email addresses with an identity provider.
  - Using different hints to identity the identity provider to be used by the user, like a company-specific page, IP address or other tracking information.

### Parameters

- **params** *Required* `SignInWithSSOCredentials`

### Example

```python
response = supabase.auth.sign_in_with_sso(
    {"domain": "company.com"}
)
```

## Retrieve Identities Linked to a User

Gets all the identities linked to a user.

- The user needs to be signed in to call `get_user_identities()`.

### Example

```python
response = supabase.auth.get_user_identities()
```

## Link an Identity to a User

- The **Enable Manual Linking** option must be enabled from your [project's authentication settings](https://supabase.com/dashboard/project/_/settings/auth).
- The user needs to be signed in to call `link_identity()`.
- If the candidate identity is already linked to the existing user or another user, `link_identity()` will fail.
- If `link_identity` is run on the server, you should handle the redirect.

### Parameters

- **credentials** *Required* `SignInWithOAuthCredentials`

### Example

```python
response = supabase.auth.link_identity(
    {provider: "github"}
)
```

## Unlink an Identity from a User

- The **Enable Manual Linking** option must be enabled from your [project's authentication settings](https://supabase.com/dashboard/project/_/settings/auth).
- The user needs to be signed in to call `unlink_identity()`.
- The user must have at least 2 identities in order to unlink an identity.
- The identity to be unlinked must belong to the user.

### Parameters

- **identity** *Required* `UserIdentity`

### Example

```python
# retrieve all identites linked to a user
response = supabase.auth.get_user_identities()

# find the google identity
google_identity = list(
    filter(lambda identity: identity.provider == "google", res.identities)).pop()

# unlink the google identity
response = supabase.auth.unlink_identity(google_identity)
```

## Other Documentation Files

- [Overview](./supabase_overview.md)
- [Database Operations](./supabase_database.md)
- [Query Filters](./supabase_filters.md)
- [Authentication Basics](./supabase_auth_basics.md)
- [Multi-factor Authentication](./supabase_auth_mfa.md)
- [Admin Authentication Methods](./supabase_auth_admin.md)
- [Realtime](./supabase_realtime.md)
- [Storage](./supabase_storage.md)
- [Edge Functions](./supabase_edge_functions.md)
