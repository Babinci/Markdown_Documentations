# CORS Support for Edge Functions

This guide explains how to implement Cross-Origin Resource Sharing (CORS) support to allow invoking Edge Functions from browsers.

## Overview

To invoke edge functions from the browser, you need to handle [CORS Preflight](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request) requests, which are HTTP OPTIONS requests that check if the actual request is safe to send.

## Recommended Setup

We recommend adding a `cors.ts` file within a [`_shared` folder](https://supabase.com/docs/guides/functions/quickstart#organizing-your-edge-functions) which makes it easy to reuse the CORS headers across functions:

```typescript
export const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}
```

You can then import and use the CORS headers within your functions:

```typescript
import { corsHeaders } from '../_shared/cors.ts'

console.log(`Function "browser-with-cors" up and running!`)

Deno.serve(async (req) => {
  // This is needed if you're planning to invoke your function from a browser.
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const { name } = await req.json()
    const data = {
      message: `Hello ${name}!`,
    }

    return new Response(JSON.stringify(data), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    })
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 400,
    })
  }
})
```

See the [complete example on GitHub](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/browser-with-cors/index.ts) for a fully working implementation.
