# User Identities in Supabase Auth

An identity is an authentication method associated with a user in Supabase Auth. Understanding identities is important for implementing flexible authentication strategies, especially when supporting multiple login methods for the same user.

## Identity Types

Supabase Auth supports the following identity types:

- **Email**: Traditional email and password authentication
- **Phone**: Phone number authentication (with SMS verification)
- **OAuth**: Authentication using third-party providers like Google, GitHub, etc.
- **SAML**: Enterprise authentication using Security Assertion Markup Language

## Multiple Identities

A key feature of Supabase Auth is that a user can have more than one identity. This enables scenarios such as:

- A user linking both email and social login methods to the same account
- A user adding a phone number as an alternative login method
- Enterprise users authenticating via both SAML and email

Anonymous users have no identity until they link an identity to their user account.

## The User Identity Object

When working with Supabase Auth APIs or database tables, you'll encounter the user identity object with the following attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `provider_id` | `string` | The provider ID returned by the authentication provider. For OAuth providers, this refers to the user's account with the OAuth provider. For `email` or `phone` providers, this is the user's ID from the `auth.users` table. |
| `user_id` | `string` | The ID of the user that the identity is linked to. |
| `identity_data` | `object` | Identity metadata. For OAuth and SAML identities, this contains information about the user from the provider. |
| `id` | `string` | The unique ID of the identity. |
| `provider` | `string` | The provider name (e.g., "google", "github", "email", "phone"). |
| `email` | `string` | A generated column that references the optional email property in the `identity_data`. |
| `created_at` | `string` | The timestamp when the identity was created. |
| `last_sign_in_at` | `string` | The timestamp when the identity was last used to sign in. |
| `updated_at` | `string` | The timestamp when the identity was last updated. |

## Working with Identities

### Viewing User Identities

You can view a user's identities in the Supabase Dashboard:

1. Navigate to Authentication → Users
2. Select a user to view their details
3. The Identities section shows all linked authentication methods

### Managing Identities Programmatically

You can work with identities using the Supabase Auth API, for example:

- Linking new identities to an existing user
- Unlink identities from a user
- Check which identities are associated with a user

### Database Tables

Identities are stored in the `auth.identities` table, which you can query directly if you have appropriate permissions.

## Common Use Cases

- **Social Login + Email**: Allow users to sign up with email and then link social accounts
- **Account Recovery**: Add alternative login methods to help users recover access
- **Progressive Profiling**: Start with anonymous users who later add identities
- **Identity Merging**: Consolidate multiple accounts into a single user profile
