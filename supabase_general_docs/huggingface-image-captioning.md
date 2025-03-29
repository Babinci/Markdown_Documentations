# Generate Image Captions Using Hugging Face

This guide demonstrates how to use the Hugging Face Inference API with Supabase Edge Functions to automatically generate captions for images uploaded to Supabase Storage.

## About Hugging Face

[Hugging Face](https://huggingface.co/) is a collaboration platform for the machine learning community, hosting over 100,000 machine learning models. [Huggingface.js](https://huggingface.co/docs/huggingface.js/index) provides a convenient way to make calls to these models, making it easy to incorporate AI functionality into Supabase Edge Functions.

In this tutorial, we'll combine Hugging Face with Supabase Storage and Database Webhooks to automatically generate captions for any image uploaded to a storage bucket.

## Project Setup

1. **Create Storage Bucket**:
   - Open your Supabase project dashboard (or [create a new project](https://supabase.com/dashboard/projects))
   - [Create a new bucket](https://supabase.com/dashboard/project/_/storage/buckets) called `images`

2. **Create Database Table**:
   - Create a new table called `image_caption` with the following columns:
     - `id` (type: `uuid`, references `storage.objects.id`)
     - `caption` (type: `text`)

3. **Generate TypeScript Types**:
   - First, generate types for your database schema:
     ```bash
     supabase gen types typescript --project-id=your-project-ref --schema=storage,public > supabase/functions/huggingface-image-captioning/types.ts
     ```

4. **Create Edge Function**:
   - Create a new directory for your function:
     ```bash
     mkdir -p supabase/functions/huggingface-image-captioning
     ```
   - Create the function file (code provided below)

5. **Deploy the Function**:
   ```bash
   supabase functions deploy huggingface-image-captioning
   ```

6. **Set Up Hugging Face Token**:
   - Create an account on [Hugging Face](https://huggingface.co/) if you don't have one
   - Generate an access token from your [settings page](https://huggingface.co/settings/tokens)
   - Add the token to your Edge Function environment variables:
     ```bash
     supabase secrets set HUGGINGFACE_ACCESS_TOKEN=your-token-here
     ```

7. **Create Database Webhook**:
   - Navigate to the [Database Webhooks section](https://supabase.com/dashboard/project/_/database/hooks) in your Supabase Dashboard
   - Create a new webhook that triggers the `huggingface-image-captioning` function whenever a record is added to the `storage.objects` table

## Edge Function Code

```typescript
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { HfInference } from 'https://esm.sh/@huggingface/inference@2.3.2'
import { createClient } from 'jsr:@supabase/supabase-js@2'
import { Database } from './types.ts'

console.log('Hello from `huggingface-image-captioning` function!')

const hf = new HfInference(Deno.env.get('HUGGINGFACE_ACCESS_TOKEN'))

type SoRecord = Database['storage']['Tables']['objects']['Row']

interface WebhookPayload {
  type: 'INSERT' | 'UPDATE' | 'DELETE'
  table: string
  record: SoRecord
  schema: 'public'
  old_record: null | SoRecord
}

serve(async (req) => {
  const payload: WebhookPayload = await req.json()
  const soRecord = payload.record

  const supabaseAdminClient = createClient<Database>(
    // Supabase API URL - env var exported by default when deployed.
    Deno.env.get('SUPABASE_URL') ?? '',
    // Supabase API SERVICE ROLE KEY - env var exported by default when deployed.
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
  )

  // Construct image url from storage
  const { data, error } = await supabaseAdminClient.storage
    .from(soRecord.bucket_id!)
    .createSignedUrl(soRecord.path_tokens!.join('/'), 60)

  if (error) throw error
  const { signedUrl } = data

  // Run image captioning with Huggingface
  const imgDesc = await hf.imageToText({
    data: await (await fetch(signedUrl)).blob(),
    model: 'nlpconnect/vit-gpt2-image-captioning',
  })

  // Store image caption in Database table
  await supabaseAdminClient
    .from('image_caption')
    .insert({ id: soRecord.id!, caption: imgDesc.generated_text })
    .throwOnError()

  return new Response('ok')
})
```

## How It Works

1. When a new image is uploaded to your `images` bucket, a record is created in the `storage.objects` table
2. This triggers the Database Webhook, which calls your Edge Function
3. The function:
   - Retrieves the image details from the webhook payload
   - Creates a signed URL to access the image
   - Sends the image to Hugging Face's image-to-text model
   - Stores the generated caption in the `image_caption` table with a reference to the original image

## Additional Configuration

- **Model Selection**: The example uses `nlpconnect/vit-gpt2-image-captioning`, but you can replace it with any other image-to-text model from Hugging Face
- **Bucket Filtering**: You might want to modify the function to only process images from specific buckets
- **Error Handling**: Consider adding more robust error handling for production usage

## Resources

- [Complete Code on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/huggingface-image-captioning)
- [Video Tutorial](https://www.youtube.com/watch?v=OgnYxRkxEUw)
- [Hugging Face Documentation](https://huggingface.co/docs)
- [Supabase Edge Functions Documentation](https://supabase.com/docs/guides/functions)
