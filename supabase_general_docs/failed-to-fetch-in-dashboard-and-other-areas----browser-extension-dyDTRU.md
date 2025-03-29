# "Failed to Fetch" Error in Dashboard and Applications

## Problem

When using the Supabase Dashboard or your application, you may encounter a "Failed to Fetch" error that prevents you from performing certain actions, particularly when making API requests.

![Failed to Fetch error](https://supabase.com/docs/img/troubleshooting/7fe991ac-40ea-4628-a5e3-181d706225ea.png)

## Common Cause: Browser Extensions

While this error can occur for various reasons, a common cause is browser extensions that modify CORS (Cross-Origin Resource Sharing) behavior. In particular, the "Allow CORS: Access-Control-Allow-Origin" extension for Chrome and other browsers is known to cause issues.

This extension often blocks PATCH requests by default, which interferes with Supabase API calls.

![CORS extension settings](https://github.com/supabase/supabase/assets/54564956/c61b9292-2954-4c68-8129-995941f36210)

## Solutions

1. **Disable Problematic Extensions**:
   - Temporarily disable any CORS-related browser extensions
   - Check particularly for [Allow CORS: Access-Control-Allow-Origin](https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf) or similar extensions

2. **Configure Extension Settings**:
   - If you need to keep the extension active, adjust its settings to allow PATCH requests
   - Ensure the extension's interceptor is not blocking Supabase domains

3. **Try Alternative Browsers**:
   - Use a different browser without the problematic extensions
   - Use an incognito/private window (extensions are typically disabled by default)

4. **Clear Browser Cache and Cookies**:
   - Clear your browser cache and cookies
   - Restart your browser and try again

## Other Potential Causes

If disabling extensions doesn't resolve the issue, consider these other potential causes:

1. **Network Issues**:
   - Check your internet connection
   - Test if other websites or APIs are working correctly

2. **Firewall or Security Software**:
   - Corporate firewalls or security software might block certain requests
   - VPNs may interfere with some API calls

3. **Supabase Service Status**:
   - Check the [Supabase Status page](https://status.supabase.com/) for any ongoing service disruptions

## Prevention

When developing applications that use Supabase:

1. Use a clean browser profile when working with the Supabase Dashboard
2. Be cautious about installing browser extensions that modify web requests
3. Consider using the Supabase CLI for operations that might be affected by browser extensions
