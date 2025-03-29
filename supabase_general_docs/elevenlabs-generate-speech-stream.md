# Streaming Speech with ElevenLabs

This tutorial shows how to build an Edge Function API that generates, streams, stores, and caches speech using Supabase Edge Functions, Supabase Storage, and the ElevenLabs text-to-speech API.

## Introduction

With this implementation, you can:
- Generate speech from text using ElevenLabs
- Stream audio directly to the browser
- Store generated audio in Supabase Storage for caching
- Serve cached audio through Supabase's CDN

Find the [example project on GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/supabase/stream-and-cache-storage).

## Requirements

- An [ElevenLabs](https://elevenlabs.io/text-to-speech) account with an API key
- A [Supabase](https://supabase.com/) account (sign up via [database.new](https://database.new/))
- The [Supabase CLI](https://supabase.com/docs/guides/local-development) installed
- The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed

## Setup

### Create a Supabase Project Locally

After installing the Supabase CLI, run:

```bash
supabase init
```

### Configure the Storage Bucket

Add this configuration to your `config.toml` file:

```toml
[storage.buckets.audio]
public = false
file_size_limit = "50MiB"
allowed_mime_types = ["audio/mp3"]
objects_path = "./audio"
```

Upon running `supabase start`, this will create a new storage bucket in your local Supabase project. To deploy this to your hosted Supabase project, run `supabase seed buckets --linked`.

### Configure Background Tasks for Edge Functions

To use background tasks in Edge Functions when developing locally, add this to your `config.toml` file:

```toml
[edge_runtime]
policy = "per_worker"
```

When running with `per_worker` policy, Function won't auto-reload on edits. You'll need to manually restart it with `supabase functions serve`.

### Create an Edge Function for Speech Generation

Create a new Edge Function:

```bash
supabase functions new text-to-speech
```

Choose `y` when prompted "Generate VS Code settings for Deno?" if you're using VS Code or Cursor.

### Set Up Environment Variables

In the `supabase/functions` directory, create a `.env` file with:

```
# Find/create an API key at https://elevenlabs.io/app/settings/api-keys
ELEVENLABS_API_KEY=your_api_key
```

## Dependencies

The project uses:
- `@supabase/supabase-js` to interact with Supabase
- ElevenLabs JavaScript SDK for text-to-speech
- `object-hash` to generate request parameter hashes

Since Supabase Edge Functions use the Deno runtime, import dependencies using the `npm:` prefix.

## Implementation

Add this code to your `supabase/functions/text-to-speech/index.ts` file:

```typescript
// Setup type definitions for built-in Supabase Runtime APIs
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { createClient } from 'jsr:@supabase/supabase-js@2'
import { ElevenLabsClient } from 'npm:elevenlabs@1.52.0'
import * as hash from 'npm:object-hash'

const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
)

const client = new ElevenLabsClient({
  apiKey: Deno.env.get('ELEVENLABS_API_KEY'),
})

// Upload audio to Supabase Storage in a background task
async function uploadAudioToStorage(stream: ReadableStream, requestHash: string) {
  const { data, error } = await supabase.storage
    .from('audio')
    .upload(`${requestHash}.mp3`, stream, {
      contentType: 'audio/mp3',
    })
  console.log('Storage upload result', { data, error })
}

Deno.serve(async (req) => {
  // To secure your function for production, you can for example validate the request origin,
  // or append a user access token and validate it with Supabase Auth.
  console.log('Request origin', req.headers.get('host'))
  
  const url = new URL(req.url)
  const params = new URLSearchParams(url.search)
  const text = params.get('text')
  const voiceId = params.get('voiceId') ?? 'JBFqnCBsd6RMkjVDRZzb'
  const requestHash = hash.MD5({ text, voiceId })
  console.log('Request hash', requestHash)

  // Check storage for existing audio file
  const { data } = await supabase.storage.from('audio').createSignedUrl(`${requestHash}.mp3`, 60)
  if (data) {
    console.log('Audio file found in storage', data)
    const storageRes = await fetch(data.signedUrl)
    if (storageRes.ok) return storageRes
  }

  if (!text) {
    return new Response(JSON.stringify({ error: 'Text parameter is required' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    })
  }

  try {
    console.log('ElevenLabs API call')
    const response = await client.textToSpeech.convertAsStream(voiceId, {
      output_format: 'mp3_44100_128',
      model_id: 'eleven_multilingual_v2',
      text,
    })

    const stream = new ReadableStream({
      async start(controller) {
        for await (const chunk of response) {
          controller.enqueue(chunk)
        }
        controller.close()
      },
    })

    // Branch stream to Supabase Storage
    const [browserStream, storageStream] = stream.tee()
    
    // Upload to Supabase Storage in the background
    EdgeRuntime.waitUntil(uploadAudioToStorage(storageStream, requestHash))
    
    // Return the streaming response immediately
    return new Response(browserStream, {
      headers: {
        'Content-Type': 'audio/mpeg',
      },
    })
  } catch (error) {
    console.log('error', { error })
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
  }
})
```

## Running Locally

Start the local Supabase stack:

```bash
supabase start
```

Then start the Edge Function:

```bash
supabase functions serve
```

### Try It Out

Navigate to `http://127.0.0.1:54321/functions/v1/text-to-speech?text=hello%20world` to hear the function in action.

Afterwards, check `http://127.0.0.1:54323/project/default/storage/buckets/audio` to see the audio file in your local Supabase Storage bucket.

## Deployment to Supabase

Link your local project to your Supabase account:

```bash
supabase link
```

Deploy the function:

```bash
supabase functions deploy
```

### Set Function Secrets

Set your environment variables in your Supabase project:

```bash
supabase secrets set --env-file supabase/functions/.env
```

## Testing the Deployed Function

The function can be used directly as a source for an `<audio>` element:

```html
<audio
  src="https://${SUPABASE_PROJECT_REF}.supabase.co/functions/v1/text-to-speech?text=Hello%2C%20world!&voiceId=JBFqnCBsd6RMkjVDRZzb"
  controls
/>
```

Find a complete frontend implementation in the [GitHub example](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/text-to-speech/supabase/stream-and-cache-storage/src/pages/Index.tsx).

## How It Works

The Edge Function:

1. Receives a text query parameter
2. Generates a hash based on the text and voice ID
3. Checks if the audio file already exists in Storage
4. If found, returns the cached audio file
5. If not found, calls the ElevenLabs API to generate speech
6. Streams the audio back to the client while simultaneously uploading it to Storage for future requests
7. Uses background tasks to handle the Storage upload without delaying the response

This approach provides fast responses for repeated requests while minimizing API calls to ElevenLabs.