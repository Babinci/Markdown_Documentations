# Developing Edge Functions Locally

## Get started with Edge Functions on your local machine

Let's create a basic Edge Function on your local machine and then invoke it using the Supabase CLI.

## Initialize a Project

Create a new Supabase project in a folder on your local machine:

```bash
supabase init
```

> **Note:** If you don't have the CLI installed, check out the [CLI Docs](https://supabase.com/docs/guides/cli) to learn how to install the Supabase CLI on your local machine.

If you're using VS Code, you can have the CLI automatically create helpful Deno settings when running `supabase init`. Select `y` when prompted "Generate VS Code settings for Deno? [y/N]"!

If you're using an IntelliJ IDEA editor such as WebStorm, you can use the `--with-intellij-settings` flag with `supabase init` to create an auto-generated Deno config.

## Create an Edge Function

Let's create a new Edge Function called `hello-world` inside your project:

```bash
supabase functions new hello-world
```

This creates a function stub in your `supabase` folder:

```
└── supabase
    ├── functions
    │   └── hello-world
    │   │   └── index.ts ## Your function code
    └── config.toml
```

## How to Write the Code

The generated function uses native [Deno.serve](https://docs.deno.com/runtime/manual/runtime/http_server_apis) to handle requests. It gives you access to `Request` and `Response` objects.

Here's the generated Hello World Edge Function, that accepts a name in the `Request` and responds with a greeting:

```typescript
Deno.serve(async (req) => {
  const { name } = await req.json()
  const data = {
    message: `Hello ${name}!`,
  }
  return new Response(JSON.stringify(data), { headers: { 'Content-Type': 'application/json' } })
})
```

## Running Edge Functions Locally

You can run your Edge Function locally using [`supabase functions serve`](https://supabase.com/docs/reference/cli/usage#supabase-functions-serve):

```bash
supabase start # start the supabase stack
supabase functions serve # start the Functions watcher
```

The `functions serve` command has hot-reloading capabilities. It will watch for any changes to your files and restart the Deno server.

## Invoking Edge Functions Locally

While serving your local Edge Function, you can invoke it using curl or one of the client libraries.
To call the function from a browser you need to handle CORS requests. See [CORS](https://supabase.com/docs/guides/functions/cors).

### Using cURL

```bash
curl --request POST 'http://localhost:54321/functions/v1/hello-world' \
  --header 'Authorization: Bearer SUPABASE_ANON_KEY' \
  --header 'Content-Type: application/json' \
  --data '{ "name":"Functions" }'
```

> **Note:** Where is my SUPABASE_ANON_KEY? Run `supabase status` to see your local credentials.

You should see the response `{ "message":"Hello Functions!" }`.

If you execute the function with a different payload, the response will change.

Modify the `--data '{"name":"Functions"}'` line to `--data '{"name":"World"}'` and try invoking the command again.

## Next Steps

Check out the [Deploy to Production](https://supabase.com/docs/guides/functions/deploy) guide to make your Edge Function available to the world.

Read on for some common development tips.

## Development Tips

Here are a few recommendations when developing Edge Functions.

### Skipping Authorization Checks

By default, Edge Functions require a valid JWT in the authorization header. If you want to use Edge Functions without Authorization checks (commonly used for Stripe webhooks), you can pass the `--no-verify-jwt` flag when serving your Edge Functions locally.

```bash
supabase functions serve hello-world --no-verify-jwt
```

Be careful when using this flag, as it will allow anyone to invoke your Edge Function without a valid JWT. The Supabase client libraries automatically handle authorization.

### Using HTTP Methods

Edge Functions support `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`. A Function can be designed to perform different actions based on a request's HTTP method. See the [example on building a RESTful service](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/restful-tasks) to learn how to handle different HTTP methods in your Function.

> **Note:** HTML content is not supported. `GET` requests that return `text/html` will be rewritten to `text/plain`.

### Naming Edge Functions

We recommend using hyphens to name functions because hyphens are the most URL-friendly of all the naming conventions (snake_case, camelCase, PascalCase).

### Organizing Your Edge Functions

We recommend developing "fat functions". This means that you should develop few large functions, rather than many small functions. One common pattern when developing Functions is that you need to share code between two or more Functions. To do this, you can store any shared code in a folder prefixed with an underscore (`_`). We also recommend a separate folder for [Unit Tests](https://supabase.com/docs/guides/functions/unit-test) including the name of the function followed by a `-test` suffix.

We recommend this folder structure:

```
└── supabase
    ├── functions
    │   ├── import_map.json # A top-level import map to use across functions.
    │   ├── _shared
    │   │   ├── supabaseAdmin.ts # Supabase client with SERVICE_ROLE key.
    │   │   └── supabaseClient.ts # Supabase client with ANON key.
    │   │   └── cors.ts # Reusable CORS headers.
    │   ├── function-one # Use hyphens to name functions.
    │   │   └── index.ts
    │   └── function-two
    │   │   └── index.ts
    │   └── tests
    │       └── function-one-test.ts
    │       └── function-two-test.ts
    ├── migrations
    └── config.toml
```

### Using config.toml

Individual function configuration like [JWT verification](https://supabase.com/docs/guides/cli/config#functions.function_name.verify_jwt) and [import map location](https://supabase.com/docs/guides/cli/config#functions.function_name.import_map) can be set via the `config.toml` file.

```toml
[functions.hello-world]
verify_jwt = false
import_map = './import_map.json'
```

### Not Using TypeScript

When you create a new Edge Function, it will use TypeScript by default. However, it is possible to write and deploy Edge Functions using pure JavaScript.

Save your Function as a JavaScript file (e.g. `index.js`) and then update the `supabase/config.toml` as follows:

```toml
[functions.hello-world]
# other entries
entrypoint = './functions/hello-world/index.js' # path must be relative to config.toml
```

> **Note:** `entrypoint` is available only in Supabase CLI version 1.215.0 or higher.

You can use any `.ts`, `.js`, `.tsx`, `.jsx` or `.mjs` file as the `entrypoint` for a Function.

### Error Handling

The `supabase-js` library provides several error types that you can use to handle errors that might occur when invoking Edge Functions:

```javascript
import { FunctionsHttpError, FunctionsRelayError, FunctionsFetchError } from '@supabase/supabase-js'

const { data, error } = await supabase.functions.invoke('hello', {
  headers: { 'my-custom-header': 'my-custom-header-value' },
  body: { foo: 'bar' },
})

if (error instanceof FunctionsHttpError) {
  const errorMessage = await error.context.json()
  console.log('Function returned an error', errorMessage)
} else if (error instanceof FunctionsRelayError) {
  console.log('Relay error:', error.message)
} else if (error instanceof FunctionsFetchError) {
  console.log('Fetch error:', error.message)
}
```

### Database Functions vs Edge Functions

For data-intensive operations we recommend using [Database Functions](https://supabase.com/docs/guides/database/functions), which are executed within your database and can be called remotely using the [REST and GraphQL API](https://supabase.com/docs/guides/api).

For use-cases which require low-latency we recommend [Edge Functions](https://supabase.com/docs/guides/functions), which are globally-distributed and can be written in TypeScript.

## Resources

- [Deploy to Production Guide](https://supabase.com/docs/guides/functions/deploy)
- [Unit Testing Edge Functions](https://supabase.com/docs/guides/functions/unit-test)
- [CORS in Edge Functions](https://supabase.com/docs/guides/functions/cors)
- [Edge Functions Examples](https://github.com/supabase/supabase/tree/master/examples/edge-functions)
