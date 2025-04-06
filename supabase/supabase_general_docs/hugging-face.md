# Hugging Face Inference API

[Hugging Face](https://huggingface.co/) is an open-source hub for AI/ML models and tools. With over 100,000 machine learning models available, it provides a powerful way to integrate specialized AI & ML tasks into your Supabase applications.

## Integration Methods

There are three ways to use Hugging Face models with Supabase:

1. Use the [Transformers](https://huggingface.co/docs/transformers/index) Python library to perform inference in a Python backend
2. [Generate embeddings](https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings) directly in Edge Functions using Transformers.js
3. Use Hugging Face's hosted [Inference API](https://huggingface.co/inference-api) to execute AI tasks remotely on Hugging Face servers

This guide focuses on the third approach, using the hosted Inference API with Supabase Edge Functions.

## Supported AI Tasks

### Natural Language Processing
- **Summarization**: Condense long text into key points
- **Text Classification**: Categorize text into predefined groups
- **Text Generation**: Create human-like text from prompts
- **Translation**: Convert text between languages
- **Fill in the Blank**: Complete missing words in text

### Computer Vision
- **Image to Text**: Generate captions or descriptions from images
- **Text to Image**: Create images from text descriptions
- **Image Classification**: Identify what's in an image
- **Video Classification**: Categorize video content
- **Object Detection**: Locate and identify objects in images
- **Image Segmentation**: Precisely outline objects in images

### Audio Processing
- **Text to Speech**: Convert text into natural-sounding speech
- **Speech to Text**: Transcribe spoken words
- **Audio Classification**: Identify sounds or speech in audio

See the [full list of tasks](https://huggingface.co/tasks) on the Hugging Face website.

## Setup Instructions

### 1. Generate an Access Token

First, create a Hugging Face access token for your application:

1. Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Name your token based on the app and environment (e.g., "Image Generator (Dev)")
3. Select the `read` role for the Inference API
4. Copy your token for later use

While it's possible to use the Inference API without a token, you may be rate-limited. Using a token ensures reliable service for your application.

### 2. Create an Edge Function

Edge Functions are server-side TypeScript functions that run on-demand, perfect for securely handling API calls with tokens.

First, install the [Supabase CLI](https://supabase.com/docs/guides/cli) if you haven't already. Then:

1. Initialize Supabase in your project directory:
   ```bash
   supabase init
   ```

2. Create a new Edge Function:
   ```bash
   supabase functions new text-to-image
   ```

3. Create a `.env.local` file to store your token:
   ```
   HUGGING_FACE_ACCESS_TOKEN=<your-token-here>
   ```

### 3. Implement the Edge Function

Replace the default code in your new Edge Function with this text-to-image example:

```typescript
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { HfInference } from 'https://esm.sh/@huggingface/inference@2.3.2'

const hf = new HfInference(Deno.env.get('HUGGING_FACE_ACCESS_TOKEN'))

serve(async (req) => {
  const { prompt } = await req.json()
  
  const image = await hf.textToImage(
    {
      inputs: prompt,
      model: 'stabilityai/stable-diffusion-2',
    },
    {
      use_cache: false,
    }
  )
  
  return new Response(image)
})
```

This function:
- Creates a new instance of `HfInference` using your access token
- Accepts a JSON request with a `prompt` parameter
- Calls the text-to-image API with the provided prompt
- Returns the generated image directly in the response

### 4. Test Locally

Run your Edge Function locally:

```bash
supabase functions serve --env-file .env.local --no-verify-jwt
```

The `--no-verify-jwt` flag makes testing easier, but in production, you should use proper authentication.

Test with cURL:

```bash
curl --output result.jpg --location --request POST 'http://localhost:54321/functions/v1/text-to-image' \
  --header 'Content-Type: application/json' \
  --data '{"prompt":"Llama wearing sunglasses"}'
```

The generated image will save as `result.jpg`.

### 5. Deploy to Production

When you're ready to deploy:

```bash
supabase functions deploy text-to-image --project-ref your-project-ref
```

Don't forget to set the environment variable in the Supabase Dashboard.

## Next Steps

You can modify the Edge Function to use different Hugging Face models or task types:

- Try other [AI tasks](https://huggingface.co/tasks)
- Explore different models for the same task
- Implement error handling and input validation
- Add authentication to protect your API

## Resources

- [Hugging Face official website](https://huggingface.co/)
- [Hugging Face JS documentation](https://huggingface.co/docs/huggingface.js)
- [Generate image captions](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning) using Hugging Face
- [Edge Functions documentation](https://supabase.com/docs/guides/functions)
