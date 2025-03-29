# GitHub Actions for Edge Functions

This guide shows how to use GitHub Actions to automatically deploy Supabase Edge Functions.

## Deploying Edge Functions with GitHub Actions

You can use the Supabase CLI together with GitHub Actions to automatically deploy your Supabase Edge Functions when you push to your repository. Here's an example workflow configuration:

```yaml
name: Deploy Function
on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    env:
      SUPABASE_ACCESS_TOKEN: YOUR_SUPABASE_ACCESS_TOKEN
      PROJECT_ID: YOUR_SUPABASE_PROJECT_ID
    steps:
      - uses: actions/checkout@v4
      - uses: supabase/setup-cli@v1
        with:
          version: latest
      - run: supabase functions deploy --project-ref $PROJECT_ID
```

## Deploying All Functions

Since Supabase CLI [v1.62.0](https://github.com/supabase/cli/releases/tag/v1.62.0), you can deploy all functions with a single command.

Individual function configuration like [JWT verification](https://supabase.com/docs/guides/cli/config#functions.function_name.verify_jwt) and [import map location](https://supabase.com/docs/guides/cli/config#functions.function_name.import_map) can be set via the `config.toml` file:

```toml
[functions.hello-world]
verify_jwt = false
```

## Additional Resources

- [Example repository](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/github-action-deploy) with GitHub Actions deployment
- [Video tutorial](https://www.youtube.com/watch?v=l2KlzGrhB6w) demonstrating the deployment process
