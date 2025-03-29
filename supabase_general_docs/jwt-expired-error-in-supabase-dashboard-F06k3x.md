# Resolving "JWT Expired" Error in Supabase Dashboard

When you encounter "JWT Expired" errors in the Supabase Dashboard, it usually means your computer's time is not properly synchronized with the actual time.

## Problem

The error occurs because JSON Web Tokens (JWTs) have an expiration timestamp. If your computer's clock is incorrect, the token might appear expired to your system even when it's still valid.

## Solution

1. Go to [https://time.is/](https://time.is/) to compare your computer's clock with the actual time.
2. If your computer's time is inaccurate, sync it to resolve the issue using the instructions below.

### Windows
1. Right-click on the time in the taskbar
2. Select "Adjust date/time"
3. Toggle "Set time automatically" to On
4. Click "Sync now"

### macOS
1. Open System Preferences
2. Go to "Date & Time"
3. Make sure "Set date and time automatically" is checked
4. Select a suitable time server from the dropdown

### Linux
1. Open a terminal and run `sudo timedatectl set-ntp true`
2. Verify with `timedatectl status`

After synchronizing your computer's time, refresh the Supabase Dashboard and the error should be resolved.

## Prevention

Ensure your system is configured to regularly synchronize time with internet time servers to prevent this issue from recurring.
