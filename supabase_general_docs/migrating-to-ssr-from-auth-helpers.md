# Migrating to the SSR package from Auth Helpers

The new `ssr` package takes the core concepts of the Auth Helpers and makes them available to any server language or framework. This page will guide you through migrating from the Auth Helpers package to `ssr`.

## Replacing Supabase packages

**Next.js/SvelteKit/Remix**

```bash
npm uninstall @supabase/auth-helpers-nextjs
npm install @supabase/ssr
```

## Creating a client

The new `ssr` package exports two functions for creating a Supabase client:
- The `createBrowserClient` function is used in the client
- The `createServerClient` function is used in the server

Check out the [Creating a client](creating-a-client.md) page for examples of creating a client in your framework.

## Next steps

- Implement [Authentication using Email and Password](https://supabase.com/docs/guides/auth/server-side/email-based-auth-with-pkce-flow-for-ssr)
- Implement [Authentication using OAuth](https://supabase.com/docs/guides/auth/server-side/oauth-with-pkce-flow-for-ssr)
- [Learn more about SSR](https://supabase.com/docs/guides/auth/server-side-rendering)
