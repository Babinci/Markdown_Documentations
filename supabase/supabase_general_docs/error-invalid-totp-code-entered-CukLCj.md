# Error: "Invalid TOTP code entered"

## Problem

When using Time-based One-Time Password (TOTP) authentication with Supabase Auth, you may encounter the error message "Invalid TOTP code entered" even when you believe you've entered the correct code from your authenticator app.

## Cause

This error typically occurs due to time synchronization issues between your device and the authentication server. TOTP codes are generated based on the current time, so if your device's clock is not accurate, the generated codes will be invalid.

## Solution

To resolve this issue:

1. Check your device's date and time settings:
   - Ensure your device shows the correct local time
   - Verify the date is correct
   - Confirm the time zone is set properly

2. Enable automatic time synchronization:
   - On most devices, you can find this in the Date & Time settings
   - Look for options like "Set automatically" or "Sync with Internet time servers"
   
3. If using a hardware authenticator:
   - Some hardware tokens may need their internal clocks synchronized or reset

4. Try alternative recovery methods:
   - If available, use backup codes provided when you set up MFA
   - Contact your system administrator if you're unable to access your account

## Prevention

- Always ensure your device's time settings are set to update automatically
- Consider using authentication apps that automatically sync their time with servers
- Keep backup authentication methods or recovery codes accessible
