# How to Troubleshoot Next.js and Supabase Auth Issues

Last edited: 2/21/2025

Authentication with server-side rendering can be challenging. This guide will help you troubleshoot common issues when implementing Supabase Auth with Next.js. Many of these principles also apply to other SSR frameworks like Nuxt, SvelteKit, and Remix.

## Troubleshooting Checklist

If you're experiencing issues with Supabase Auth and SSR, verify the following:

✅ **Use the latest packages**: Ensure you're using the latest version of `@supabase/ssr`. Note that the `@supabase/auth-helpers` package is being deprecated in favor of `@supabase/ssr`.

✅ **Client utility functions**: Confirm you've implemented all the necessary client utility functions that can be imported into components requiring Supabase auth. Follow the [client creation guide](https://supabase.com/docs/guides/auth/server-side/creating-a-client?queryGroups=framework&framework=nextjs&queryGroups=environment&environment=client-component#creating-a-client) carefully.

✅ **Middleware implementation**: Verify your `middleware.ts` file is correctly implemented to refresh expired sessions before loading server components that require authentication.

## Official Documentation Resources

Use these resources to validate your implementation:

- [Setting up Server-Side Auth for Next.js](https://supabase.com/docs/guides/auth/server-side/nextjs?queryGroups=router&router=app)
- [SSR Advanced Guide](https://supabase.com/docs/guides/auth/server-side/advanced-guide)
- [Creating a Supabase Client for SSR](https://supabase.com/docs/guides/auth/server-side/creating-a-client?queryGroups=framework&framework=nextjs&queryGroups=environment&environment=middleware)

## Compare With Reference Implementation

A reliable way to identify potential issues is to compare your code with the official Supabase Next.js quickstart:

```bash
npx create-next-app -e with-supabase
```

This downloads a working reference implementation to your local machine.

## Video Resources

Our YouTube channel offers helpful tutorials:

- [The Right Way to do Auth with the Next.js App Router](https://youtu.be/v6UvgfSIjQ0?si=TBUN9dD4pmjRg78a)

Also, familiarize yourself with Next.js authentication concepts in the [official Next.js documentation](https://nextjs.org/docs/app/building-your-application/authentication).

## Getting Additional Help

If you encounter edge cases or specific issues:

1. Reach out to our community on [GitHub Discussions](https://github.com/orgs/supabase/discussions) or [Discord](https://discord.gg/rxTfewPvys)
2. Report issues to the [`@supabase/ssr` GitHub repository](https://github.com/supabase/ssr/issues)
3. Contact [Supabase Support](https://supabase.help/) with detailed information:
   - Your specific use case
   - Relevant code snippets
   - Package.json file contents
   - Middleware.ts implementation
   - HAR file (if applicable)
