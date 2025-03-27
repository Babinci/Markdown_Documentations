# Supabase Auth Admin Methods

## Table of Contents
- [Introduction](#introduction)
- [Initial Setup](#initial-setup)
- [Retrieve a User](#retrieve-a-user)
- [List All Users](#list-all-users)
- [Create a User](#create-a-user)
- [Delete a User](#delete-a-user)
- [Send an Email Invite Link](#send-an-email-invite-link)
- [Generate an Email Link](#generate-an-email-link)
- [Update a User](#update-a-user)
- [Delete a Factor for a User](#delete-a-factor-for-a-user)
- [Other Documentation Files](#other-documentation-files)

## Introduction

- Any method under the `supabase.auth.admin` namespace requires a `service_role` key.
- These methods are considered admin methods and should be called on a trusted server. Never expose your `service_role` key in the browser.

## Initial Setup

```python
from supabase import create_client
from supabase.lib.client_options import ClientOptions

supabase = create_client(
    supabase_url,
    service_role_key,
    options=ClientOptions(
        auto_refresh_token=False,
        persist_session=False,
    )
)

# Access auth admin api
admin_auth_client = supabase.auth.admin
```

## Retrieve a User

- Fetches the user object from the database based on the user's id.
- The `get_user_by_id()` method requires the user's id which maps to the `auth.users.id` column.

### Parameters

- **uid** *Required* `string`  
  The user's unique identifier

> This function should only be called on a server. Never expose your `service_role` key in the browser.

### Example

```python
response = supabase.auth.admin.get_user_by_id(1)
```

## List All Users

- Defaults to return 50 users per page.

### Parameters

- **params** *Optional* `PageParams`  
  An object which supports page and per_page as numbers, to alter the paginated results.

### Example

```python
response = supabase.auth.admin.list_users()
```

## Create a User

- To confirm the user's email address or phone number, set `email_confirm` or `phone_confirm` to true. Both arguments default to false.
- `create_user()` will not send a confirmation email to the user. You can use [`invite_user_by_email()`](#send-an-email-invite-link) if you want to send them an email invite instead.
- If you are sure that the created user's email or phone number is legitimate and verified, you can set the `email_confirm` or `phone_confirm` param to `true`.

### Parameters

- **attributes** *Required* `AdminUserAttributes`

### Example

```python
response = supabase.auth.admin.create_user(
    {
        "email": "user@email.com",
        "password": "password",
        "user_metadata": {"name": "Yoda"},
    }
)
```

## Delete a User

Delete a user. Requires a `service_role` key.

- The `delete_user()` method requires the user's ID, which maps to the `auth.users.id` column.

### Parameters

- **id** *Required* `string`  
  The user id you want to remove.

- **should_soft_delete** *Optional* `boolean`  
  If true, then the user will be soft-deleted (setting `deleted_at` to the current timestamp and disabling their account while preserving their data) from the auth schema. Defaults to false for backward compatibility.

> This function should only be called on a server. Never expose your `service_role` key in the browser.

### Example

```python
supabase.auth.admin.delete_user(
    "715ed5db-f090-4b8c-a067-640ecee36aa0"
)
```

## Send an Email Invite Link

Sends an invite link to an email address.

- Sends an invite link to the user's email address.
- The `invite_user_by_email()` method is typically used by administrators to invite users to join the application.
- Note that PKCE is not supported when using `invite_user_by_email`. This is because the browser initiating the invite is often different from the browser accepting the invite which makes it difficult to provide the security guarantees required of the PKCE flow.

### Parameters

- **email** *Required* `string`  
  The email address of the user.

- **options** *Optional* `InviteUserByEmailOptions`

### Example

```python
response = supabase.auth.admin.invite_user_by_email("email@example.com")
```

## Generate an Email Link

- The following types can be passed into `generate_link()`: `signup`, `magiclink`, `invite`, `recovery`, `email_change_current`, `email_change_new`, `phone_change`.
- `generate_link()` only generates the email link for `email_change_email` if the **Secure email change** is enabled in your project's [email auth provider settings](https://supabase.com/dashboard/project/_/auth/providers).
- `generate_link()` handles the creation of the user for `signup`, `invite` and `magiclink`.

### Parameters

- **params** *Required* `GenerateLinkParams`

### Example

```python
response = supabase.auth.admin.generate_link(
    {
        "type": "signup",
        "email": "email@example.com",
        "password": "secret",
    }
)
```

## Update a User

### Parameters

- **uid** *Required* `string`

- **attributes** *Required* `AdminUserAttributes`  
  The data you want to update.

> This function should only be called on a server. Never expose your `service_role` key in the browser.

### Example

```python
response = supabase.auth.admin.update_user_by_id(
    "11111111-1111-1111-1111-111111111111",
    {
        "email": "new@email.com",
    }
)
```

## Delete a Factor for a User

Deletes a factor on a user. This will log the user out of all active sessions if the deleted factor was verified.

### Parameters

- **params** *Required* `AuthMFAAdminDeleteFactorParams`

### Example

```python
response = supabase.auth.admin.mfa.delete_factor(
    {
        "id": "34e770dd-9ff9-416c-87fa-43b31d7ef225",
        "user_id": "a89baba7-b1b7-440f-b4bb-91026967f66b"
    }
)
```

## Other Documentation Files

- [Overview](./supabase_overview.md)
- [Database Operations](./supabase_database.md)
- [Query Filters](./supabase_filters.md)
- [Authentication Basics](./supabase_auth_basics.md)
- [OAuth Authentication](./supabase_auth_oauth.md)
- [Multi-factor Authentication](./supabase_auth_mfa.md)
- [Realtime](./supabase_realtime.md)
- [Storage](./supabase_storage.md)
- [Edge Functions](./supabase_edge_functions.md)
