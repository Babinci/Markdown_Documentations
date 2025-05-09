31 APR - 04 MAR / 7AM PT

Launch Week 14

03d

:

18h

:

04m

:

18s

[Claim ticket](https://supabase.com/launch-week)Dismiss

![](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Flaunchweek%2F14%2Fpromo-banner-bg.png&w=3840&q=100&dpl=dpl_9WgBm3X43HXGqPuPh4vSvQgRaZyZ)

Edge Functions

# Running AI Models

## How to run AI models in Edge Functions.

* * *

[Supabase Edge Runtime](https://github.com/supabase/edge-runtime) has a built-in API for running AI models. You can use this API to generate embeddings, build conversational workflows, and do other AI related tasks in your Edge Functions.

## Setup [\#](https://supabase.com/docs/guides/functions/ai-models\#setup)

There are no external dependencies or packages to install to enable the API.

You can create a new inference session by doing:

```flex

1
const model = new Supabase.ai.Session('model-name')
```

To get type hints and checks for the API you can import types from `functions-js` at the top of your file:

```flex

1
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
```

## Running a model inference [\#](https://supabase.com/docs/guides/functions/ai-models\#running-a-model-inference)

Once the session is instantiated, you can call it with inputs to perform inferences. Depending on the model you run, you may need to provide different options (discussed below).

```flex

1
const output = await model.run(input, options)
```

## How to generate text embeddings [\#](https://supabase.com/docs/guides/functions/ai-models\#how-to-generate-text-embeddings)

Now let's see how to write an Edge Function using the `Supabase.ai` API to generate text embeddings. Currently, `Supabase.ai` API only supports the [gte-small](https://huggingface.co/Supabase/gte-small) model.

`gte-small` model exclusively caters to English texts, and any lengthy texts will be truncated to a maximum of 512 tokens. While you can provide inputs longer than 512 tokens, truncation may affect the accuracy.

```flex

1
2
3
4
5
6
7
8
9
10
11
12
13
const model = new Supabase.ai.Session('gte-small')Deno.serve(async (req: Request) => {  const params = new URL(req.url).searchParams  const input = params.get('input')  const output = await model.run(input, { mean_pool: true, normalize: true })  return new Response(JSON.stringify(output), {    headers: {      'Content-Type': 'application/json',      Connection: 'keep-alive',    },  })})
```

## Using Large Language Models (LLM) [\#](https://supabase.com/docs/guides/functions/ai-models\#using-large-language-models-llm)

Inference via larger models is supported via [Ollama](https://ollama.com/) and [Mozilla Llamafile](https://github.com/Mozilla-Ocho/llamafile). In the first iteration, you can use it with a self-managed Ollama or [Llamafile server](https://www.docker.com/blog/a-quick-guide-to-containerizing-llamafile-with-docker-for-ai-applications/). We are progressively rolling out support for the hosted solution. To sign up for early access, fill up [this form](https://forms.supabase.com/supabase.ai-llm-early-access).

### Running locally [\#](https://supabase.com/docs/guides/functions/ai-models\#running-locally)

OllamaMozilla Llamafile

[Install Ollama](https://github.com/ollama/ollama?tab=readme-ov-file#ollama) and pull the Mistral model

```flex

1
ollama pull mistral
```

Run the Ollama server locally

```flex

1
ollama serve
```

Set a function secret called AI\_INFERENCE\_API\_HOST to point to the Ollama server

```flex

1
echo "AI_INFERENCE_API_HOST=http://host.docker.internal:11434" >> supabase/functions/.env
```

Create a new function with the following code

```flex

1
supabase functions new ollama-test
```

```flex

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'const session = new Supabase.ai.Session('mistral')Deno.serve(async (req: Request) => {  const params = new URL(req.url).searchParams  const prompt = params.get('prompt') ?? ''  // Get the output as a stream  const output = await session.run(prompt, { stream: true })  const headers = new Headers({    'Content-Type': 'text/event-stream',    Connection: 'keep-alive',  })  // Create a stream  const stream = new ReadableStream({    async start(controller) {      const encoder = new TextEncoder()      try {        for await (const chunk of output) {          controller.enqueue(encoder.encode(chunk.response ?? ''))        }      } catch (err) {        console.error('Stream error:', err)      } finally {        controller.close()      }    },  })  // Return the stream to the user  return new Response(stream, {    headers,  })})
```

Serve the function

```flex

1
supabase functions serve --env-file supabase/functions/.env
```

Execute the function

```flex

1
2
3
curl --get "http://localhost:54321/functions/v1/ollama-test" \--data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \-H "Authorization: $ANON_KEY"
```

### Deploying to production [\#](https://supabase.com/docs/guides/functions/ai-models\#deploying-to-production)

Once the function is working locally, it's time to deploy to production.

Deploy an Ollama or Llamafile server and set a function secret called `AI_INFERENCE_API_HOST` to point to the deployed server

```flex

1
supabase secrets set AI_INFERENCE_API_HOST=https://path-to-your-llm-server/
```

Deploy the Supabase function

```flex

1
supabase functions deploy
```

Execute the function

```flex

1
2
3
curl --get "https://project-ref.supabase.co/functions/v1/ollama-test" \ --data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \ -H "Authorization: $ANON_KEY"
```

As demonstrated in the video above, running Ollama locally is typically slower than running it in on a server with dedicated GPUs. We are collaborating with the Ollama team to improve local performance.

In the future, a hosted LLM API, will be provided as part of the Supabase platform. Supabase will scale and manage the API and GPUs for you. To sign up for early access, fill up [this form](https://forms.supabase.com/supabase.ai-llm-early-access).

Watch video guide

![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2Fw4Rr_1whU-U%2F0.jpg&w=3840&q=75&dpl=dpl_9WgBm3X43HXGqPuPh4vSvQgRaZyZ)

### Is this helpful?

NoYes

### On this page

[Setup](https://supabase.com/docs/guides/functions/ai-models#setup) [Running a model inference](https://supabase.com/docs/guides/functions/ai-models#running-a-model-inference) [How to generate text embeddings](https://supabase.com/docs/guides/functions/ai-models#how-to-generate-text-embeddings) [Using Large Language Models (LLM)](https://supabase.com/docs/guides/functions/ai-models#using-large-language-models-llm) [Running locally](https://supabase.com/docs/guides/functions/ai-models#running-locally) [Deploying to production](https://supabase.com/docs/guides/functions/ai-models#deploying-to-production)