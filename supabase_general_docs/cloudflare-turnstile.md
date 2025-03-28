# CAPTCHA Support with Cloudflare Turnstile

[Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) is a friendly, free CAPTCHA replacement, and it works seamlessly with Supabase Edge Functions to protect your forms.

## Table of Contents

- [Setup](#setup)
- [Code](#code)
- [Deploy the Server-Side Validation Edge Function](#deploy-the-server-side-validation-edge-function)
- [Invoke the Function from Your Site](#invoke-the-function-from-your-site)
- [Resources](#resources)

## Setup

1. Follow these steps to set up a new site: [https://developers.cloudflare.com/turnstile/get-started/](https://developers.cloudflare.com/turnstile/get-started/)
2. Add the Cloudflare Turnstile widget to your site: [https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/)

## Code

Create a new function in your project:

```bash
supabase functions new cloudflare-turnstile
```

And add the code to the `index.ts` file:

```typescript
import { corsHeaders } from '../_shared/cors.ts'

console.log('Hello from Cloudflare Turnstile!')

function ips(req: Request) {
  return req.headers.get('x-forwarded-for')?.split(/\s*,\s*/)
}

Deno.serve(async (req) => {
  // This is needed if you're planning to invoke your function from a browser.
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  const { token } = await req.json()
  const clientIps = ips(req) || ['']
  const ip = clientIps[0]

  // Validate the token by calling the
  // "/siteverify" API endpoint.
  let formData = new FormData()
  formData.append('secret', Deno.env.get('CLOUDFLARE_SECRET_KEY') ?? '')
  formData.append('response', token)
  formData.append('remoteip', ip)

  const url = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'
  const result = await fetch(url, {
    body: formData,
    method: 'POST',
  })

  const outcome = await result.json()
  console.log(outcome)

  if (outcome.success) {
    return new Response('success', { headers: corsHeaders })
  }

  return new Response('failure', { headers: corsHeaders })
})
```

## Deploy the Server-Side Validation Edge Function

Follow the server-side validation guidelines from Cloudflare: [https://developers.cloudflare.com/turnstile/get-started/server-side-validation/](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)

Then deploy your function and set your secret key:

```bash
supabase functions deploy cloudflare-turnstile
supabase secrets set CLOUDFLARE_SECRET_KEY=your_secret_key
```

## Invoke the Function from Your Site

Once deployed, you can invoke the function from your application:

```javascript
const { data, error } = await supabase.functions.invoke('cloudflare-turnstile', {
  body: { token },
})
```

## Resources

- [GitHub Example Code](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/cloudflare-turnstile)
- [Video Guide](https://www.youtube.com/watch?v=OwW0znboh60)

![Video guide preview](https://img.youtube.com/vi/OwW0znboh60/0.jpg)
