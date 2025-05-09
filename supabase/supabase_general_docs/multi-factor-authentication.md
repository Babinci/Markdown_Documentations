# Multi-factor Authentication

This guide is for adding MFA to your Supabase user account. If you want to enable MFA for users in your Supabase project, refer to the [Auth MFA guide](auth-mfa.md) instead.

Multi-factor authentication (MFA) adds an additional layer of security to your user account, by requiring a second factor to verify your user identity. Supabase allows users to enable MFA on their account and set it as a requirement for subsequent logins.

## Supported authentication factors

Currently, Supabase supports adding a unique time-based one-time password (TOTP) to your user account as an additional security factor. You can manage your TOTP factor using apps such as 1Password, Authy, Google Authenticator or Apple's Keychain.

## Enable MFA

You can enable MFA for your user account under your [Supabase account settings](https://supabase.com/dashboard/account/security). Enabling MFA will result in all other user sessions to be automatically logged out and forced to sign-in again with MFA.

Supabase does not return recovery codes. Instead, we recommend that you register a backup TOTP factor to use in an event that you lose access to your primary TOTP factor. Make sure you use a different device and app, or store the secret in a secure location different than your primary one.

For security reasons, we will not be able to restore access to your account if you lose all your two-factor authentication credentials. Do register a backup factor if necessary.

## Login with MFA

Once you've enabled MFA for your Supabase user account, you will be prompted to enter your second factor challenge code as seen in your preferred TOTP app.

## Disable MFA

You can disable MFA for your user account under your [Supabase account settings](https://supabase.com/dashboard/account/security). On subsequent login attempts, you will not be prompted to enter a MFA code.

We strongly recommend that you do not disable MFA to avoid unauthorized access to your user account.
