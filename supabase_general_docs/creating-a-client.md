# Creating a Supabase Client for SSR

This guide explains how to configure your Supabase client to use cookies for Server-Side Rendering (SSR) applications.

## Overview

To use Server-Side Rendering with Supabase, you need to configure your Supabase client to use cookies. The `@supabase/ssr` package helps you do this for JavaScript/TypeScript applications.

## Installation

Install the `@supabase/ssr` and `@supabase/supabase-js` packages:

```bash
# npm
npm install @supabase/ssr @supabase/supabase-js

# yarn
yarn add @supabase/ssr @supabase/supabase-js

# pnpm
pnpm add @supabase/ssr @supabase/supabase-js
```

## Set Environment Variables

In your environment variables file, set your Supabase URL and Supabase Anon Key:

### Next.js

```bash
NEXT_PUBLIC_SUPABASE_URL=your_supabase_project_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### SvelteKit

```bash
PUBLIC_SUPABASE_URL=your_supabase_project_url
PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### Astro

```bash
PUBLIC_SUPABASE_URL=your_supabase_project_url
PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### Remix

```bash
SUPABASE_URL=your_supabase_project_url
SUPABASE_ANON_KEY=your_supabase_anon_key
```

### Express

```bash
SUPABASE_URL=your_supabase_project_url
SUPABASE_ANON_KEY=your_supabase_anon_key
```

### Hono

```bash
SUPABASE_URL=your_supabase_project_url
SUPABASE_ANON_KEY=your_supabase_anon_key
```

## Create a Client

You'll need some one-time setup code to configure your Supabase client to use cookies. Once your utility code is set up, you can use your new `createClient` utility functions to get a properly configured Supabase client.

Use the browser client in code that runs on the browser, and the server client in code that runs on the server.

For framework-specific setup instructions, please refer to the official [Supabase Server-Side Auth documentation](https://supabase.com/docs/guides/auth/server-side/creating-a-client).

## Next Steps

- Implement [Authentication using Email and Password](https://supabase.com/docs/guides/auth/server-side/email-based-auth-with-pkce-flow-for-ssr)
- Implement [Authentication using OAuth](https://supabase.com/docs/guides/auth/server-side/oauth-with-pkce-flow-for-ssr)
- [Learn more about SSR](https://supabase.com/docs/guides/auth/server-side-rendering)
