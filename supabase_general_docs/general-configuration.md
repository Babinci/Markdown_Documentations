# General Auth Configuration

This guide covers the general configuration options for Supabase Auth that control user sign-up, email verification, and identity linking.

## Configuration Overview

Supabase Auth provides several global configuration options that apply across all authentication methods. These settings can be found in the [Auth Settings](https://supabase.com/dashboard/project/_/settings/auth) section of your Supabase Dashboard.

## Core Settings

### Allow New User Sign-ups

Controls whether new users can register for your application.

- **Enabled**: Anyone can create a new account through your sign-up workflows
- **Disabled**: Only existing users can sign in; new registrations are blocked

This setting is useful when you want to:
- Close registrations temporarily
- Create a private or invite-only application
- Manually create all user accounts through the admin interface

### Confirm Email

Determines whether users need to verify their email address before they can sign in.

> Note: This option is configured in the Email provider settings under the provider-specific configuration.

- **Enabled**: Users receive a verification email and must confirm their address before signing in
- **Disabled**: Users can sign in immediately without verification; the system implicitly confirms the email in the database

Consider email confirmation to:
- Ensure users provide valid email addresses
- Reduce spam or bot registrations
- Comply with security policies requiring verified contact information

### Allow Anonymous Sign-ins

Controls whether your application supports anonymous authentication.

- **Enabled**: Users can access your application without registering, receiving a temporary anonymous account
- **Disabled**: All users must explicitly authenticate with credentials

Anonymous authentication is useful for:
- Allowing users to try your application before registering
- Collecting data or user actions before a formal sign-up
- Creating seamless onboarding experiences

### Allow Manual Linking

Determines whether users can manually link multiple authentication methods to their account.

- **Enabled**: Users can connect multiple sign-in methods (email, social providers, etc.) to a single account
- **Disabled**: Each authentication method creates a separate user account

Account linking helps:
- Provide users with alternative login methods
- Consolidate user data under a single account
- Improve account recovery options

## Related Configuration Sections

Supabase Auth offers additional configuration options in specialized sections:

1. **[Provider-specific Configuration](https://supabase.com/dashboard/project/_/auth/providers)**: Settings for individual authentication providers (Google, GitHub, email, etc.)

2. **[Rate Limits](https://supabase.com/dashboard/project/_/auth/rate-limits)**: Controls for limiting authentication attempts to prevent abuse

3. **[Email Templates](https://supabase.com/dashboard/project/_/auth/templates)**: Customization of emails sent for verification, password reset, etc.

4. **[Redirect URLs](https://supabase.com/dashboard/project/_/auth/url-configuration)**: Allowed URLs for redirecting users after authentication events

5. **[Auth Hooks](https://supabase.com/dashboard/project/_/auth/hooks)**: Custom functions to run during authentication workflows

## Security Considerations

When configuring your authentication settings:

- **Disabling email confirmation** may make your application more vulnerable to spam accounts or users entering incorrect email addresses
- **Enabling anonymous access** requires careful consideration of what resources anonymous users can access
- **Account linking** should be implemented with appropriate security controls to prevent unauthorized account takeovers

## Implementation Impact

Changes to these settings may affect:

- Your application's user registration flow
- The authentication experience for new and existing users
- Your database's user management tables
- Any custom authentication logic you've implemented

Consider testing authentication flows thoroughly after changing these settings, especially in production environments where existing users might be affected.
