# Deploy to Production

## Deploy your Edge Functions to your remote Supabase Project

Once you have developed your Edge Functions locally, you can deploy them to your Supabase project.

## Login to the CLI

Log in to the Supabase CLI if necessary:

```bash
supabase login
```

> **CLI not installed?**
> See the [CLI Docs](https://supabase.com/docs/guides/cli) to learn how to install the Supabase CLI on your local machine.

## Get your project ID

Get the project ID associated with your function by running:

```bash
supabase projects list
```

> **Need a new project?**
> If you haven't yet created a Supabase project, you can do so by visiting [database.new](https://database.new/).

## Link your local project

[Link](https://supabase.com/docs/reference/cli/usage#supabase-link) your local project to your remote Supabase project using the ID you just retrieved:

```bash
supabase link --project-ref your-project-id
```

## Deploy your Edge Functions

> **Docker required**
> Since Supabase CLI version 1.123.4, you must have [Docker Desktop](https://docs.docker.com/desktop/) installed to deploy Edge Functions.

You can deploy all of your Edge Functions with a single command:

```bash
supabase functions deploy
```

You can deploy individual Edge Functions by specifying the name of the function in the deploy command:

```bash
supabase functions deploy hello-world
```

By default, Edge Functions require a valid JWT in the authorization header. If you want to use Edge Functions without Authorization checks (commonly used for Stripe webhooks), you can pass the `--no-verify-jwt` flag when deploying your Edge Functions.

```bash
supabase functions deploy hello-world --no-verify-jwt
```

Be careful when using this flag, as it will allow anyone to invoke your Edge Function without a valid JWT. The Supabase client libraries automatically handle authorization.

## Invoking remote functions

You can now invoke your Edge Function using the project's `ANON_KEY`, which can be found in the [API settings](https://supabase.com/dashboard/project/_/settings/api) of the Supabase Dashboard.

### cURL

```bash
curl --request POST 'https://<project_id>.supabase.co/functions/v1/hello-world' \
  --header 'Authorization: Bearer ANON_KEY' \
  --header 'Content-Type: application/json' \
  --data '{ "name":"Functions" }'
```

### JavaScript

```javascript
async function callFunction() {
  const SUPABASE_URL = 'https://<project_id>.supabase.co'
  const SUPABASE_ANON_KEY = 'ANON_KEY'
  
  const response = await fetch(`${SUPABASE_URL}/functions/v1/hello-world`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: 'Functions' })
  })
  
  const data = await response.json()
  console.log(data)
}
```

You should receive the response `{ "message":"Hello Functions!" }`.
