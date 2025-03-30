# Testing and Linting

## Using the CLI to test your Supabase project

The Supabase CLI provides a set of tools to help you test and lint your Postgres database and Edge Functions.

## Testing your database

The Supabase CLI provides Postgres linting using the `supabase test db` command.

```bash
supabase test db --help
Tests local database with pgTAP

Usage:  supabase test db [flags]
```

This is powered by the [pgTAP](https://supabase.com/docs/guides/database/extensions/pgtap) extension. You can find a full guide to writing and running tests in the [Testing your database](https://supabase.com/docs/guides/database/testing) section.

### Test helpers

Our friends at [Basejump](https://usebasejump.com/) have created a useful set of Database [Test Helpers](https://github.com/usebasejump/supabase-test-helpers), with an accompanying [blog post](https://usebasejump.com/blog/testing-on-supabase-with-pgtap).

### Running database tests in CI

Use our GitHub Action to [automate your database tests](https://supabase.com/docs/guides/cli/github-action/testing#testing-your-database).

## Testing your Edge Functions

Edge Functions are powered by Deno, which provides a [native set of testing tools](https://deno.land/manual@v1.35.3/basics/testing). We extend this functionality in the Supabase CLI. You can find a detailed guide in the [Edge Functions section](https://supabase.com/docs/guides/functions/unit-test).

## Testing Auth emails

The Supabase CLI uses [Inbucket](https://github.com/inbucket/inbucket) to capture emails sent from your local machine. This is useful for testing emails sent from Supabase Auth.

### Accessing Inbucket

By default, Inbucket is available at [localhost:54324](http://localhost:54324/) when you run `supabase start`. Open this URL in your browser to view the emails.

### Going into production

The "default" email provided by Supabase is only for development purposes. It is [heavily restricted](https://supabase.com/docs/guides/platform/going-into-prod#auth-rate-limits) to ensure that it is not used for spam. Before going into production, you must configure your own email provider. This is as simple as enabling a new SMTP credentials in your [project settings](https://supabase.com/dashboard/project/_/settings/auth).

## Linting your database

The Supabase CLI provides Postgres linting using the `supabase db lint` command:

```bash
supabase db lint --help
Checks local database for typing error

Usage:  supabase db lint [flags]

Flags:
  --level [ warning | error ] Error level to emit. (default warning)
  --linked Lints the linked project for schema errors.
  -s, --schema strings List of schema to include. (default all)
```

This is powered by [plpgsql_check](https://github.com/okbob/plpgsql_check), which leverages the internal Postgres parser/evaluator so you see any errors that would occur at runtime. It provides the following features:

- Validates you are using the correct types for function parameters
- Identifies unused variables and function arguments
- Detection of dead code (any code after an `RETURN` command)
- Detection of missing `RETURN` commands with your Postgres function
- Identifies unwanted hidden casts, which can be a performance issue
- Checks `EXECUTE` statements against SQL injection vulnerability

Check the Reference Docs for [more information](https://supabase.com/docs/reference/cli/supabase-db-lint).
