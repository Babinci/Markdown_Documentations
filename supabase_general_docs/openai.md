# Generating OpenAI GPT-3 Completions

Generate GPT text completions using OpenAI and Supabase Edge Functions.

## Overview

OpenAI provides a [completions API](https://platform.openai.com/docs/api-reference/completions) that allows you to use their generative GPT models in your own applications.

OpenAI's API is intended to be used from the server-side. Supabase offers Edge Functions to make it easy to interact with third party APIs like OpenAI.

## Setup Supabase Project

If you haven't already, [install the Supabase CLI](https://supabase.com/docs/guides/cli) and initialize your project:

```bash
supabase init
```

## Create Edge Function

Scaffold a new edge function called `openai` by running:

```bash
supabase functions new openai
```

A new edge function will now exist under `./supabase/functions/openai/index.ts`.

We'll design the function to take your user's query (via POST request) and forward it to OpenAI's API.

```typescript
import OpenAI from 'https://deno.land/x/openai@v4.24.0/mod.ts'

Deno.serve(async (req) => {
  const { query } = await req.json()
  const apiKey = Deno.env.get('OPENAI_API_KEY')
  
  const openai = new OpenAI({
    apiKey: apiKey,
  })
  
  // Documentation here: https://github.com/openai/openai-node
  const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: query }],
    // Choose model from here: https://platform.openai.com/docs/models
    model: 'gpt-3.5-turbo',
    stream: false,
  })
  
  const reply = chatCompletion.choices[0].message.content
  
  return new Response(reply, {
    headers: { 'Content-Type': 'text/plain' },
  })
})
```

Note that we are setting `stream` to `false` which will wait until the entire response is complete before returning. If you wish to stream GPT's response word-by-word back to your client, set `stream` to `true`.

## Create OpenAI Key

You may have noticed we were passing `OPENAI_API_KEY` in the Authorization header to OpenAI. To generate this key, go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) and create a new secret key.

After getting the key, copy it into a new file called `.env.local` in your `./supabase` folder:

```
OPENAI_API_KEY=your-key-here
```

## Run Locally

Serve the edge function locally by running:

```bash
supabase functions serve --env-file ./supabase/.env.local --no-verify-jwt
```

Notice how we are passing in the `.env.local` file.

Use cURL or Postman to make a POST request to [http://localhost:54321/functions/v1/openai](http://localhost:54321/functions/v1/openai).

```bash
curl -i --location --request POST http://localhost:54321/functions/v1/openai \
  --header 'Content-Type: application/json' \
  --data '{"query":"What is Supabase?"}'
```

You should see a GPT response come back from OpenAI!

## Deploy

Deploy your function to the cloud by running:

```bash
supabase functions deploy --no-verify-jwt openai
supabase secrets set --env-file ./supabase/.env.local
```

## Resources

If you're interested in learning how to use this to build your own ChatGPT, read [the blog post](https://supabase.com/blog/chatgpt-supabase-docs) and check out the video:

[ClippyGPT - How I Built Supabase's OpenAI Doc Search (Embeddings)](https://www.youtube.com/watch?v=Yhtjd7yGGGA)
