# Fetch Requests to API Endpoints Aren't Showing the Session

## Problem

When using server-side code to make fetch requests to API endpoints within your application, you may find that the session information is not being properly passed along. This is a common issue when:

- Making fetch requests from a server component to an API route
- Creating server-side functions that need to maintain the user's authentication state
- Working with frameworks like Next.js, Remix, or other server-rendering solutions

## Cause

The session information is stored in cookies, but fetch requests do not automatically forward cookies between server-side contexts. Unlike browser-based requests which automatically include cookies, server-side fetch requests need to explicitly forward the cookie header.

## Solution

You need to manually pass the cookie header with your fetch request. Here's how to do it:

### For Next.js

```javascript
import { headers } from 'next/headers';

async function makeAuthenticatedRequest() {
  const res = await fetch('http://localhost:3000/api/protected-endpoint', {
    headers: {
      cookie: headers().get('cookie') as string,
    },
  });
  
  return await res.json();
}
```

### For other frameworks

The implementation may vary slightly, but the principle is the same:

```javascript
async function makeAuthenticatedRequest(requestHeaders) {
  const res = await fetch('https://your-api-endpoint.com/data', {
    headers: {
      cookie: requestHeaders.cookie,
      // Include other headers as needed
    },
  });
  
  return await res.json();
}
```

## Alternative Solutions

If you're using Supabase with server-side rendering, consider these approaches:

1. **Use Supabase Auth Helpers**: Frameworks like Next.js have official Supabase Auth Helpers that make session management easier:

   ```javascript
   import { createServerComponentClient } from '@supabase/auth-helpers-nextjs';
   import { cookies } from 'next/headers';

   async function getData() {
     const supabase = createServerComponentClient({ cookies });
     const { data } = await supabase.from('your_table').select();
     return data;
   }
   ```

2. **Pass the access token directly** if you don't need the full cookie context:

   ```javascript
   const token = await getAccessToken(); // Your method to retrieve the token
   const res = await fetch('https://your-api-endpoint.com/data', {
     headers: {
       Authorization: `Bearer ${token}`,
     },
   });
   ```

## Common Pitfalls

- Make sure to check if the cookie exists before forwarding it
- Remember that cookie forwarding only works for same-origin or trusted origins
- If you're getting undefined cookies, make sure the cookies are actually being set in the first place
- Some browsers and environments have security restrictions on cookie access
