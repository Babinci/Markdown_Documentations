# Use Supabase with Hono

Learn how to create a Supabase project, add some sample data to your database, secure it with auth, and query the data from a Hono app.

## Quick Start Guide

### 1. Create a Hono App

Bootstrap the Hono example app from the Supabase Samples using the CLI:

```bash
npx supabase@latest bootstrap hono
```

### 2. Install the Supabase Client Library

The `package.json` file in the project includes the necessary dependencies, including `@supabase/supabase-js` and `@supabase/ssr` to help with server-side auth:

```bash
npm install
```

### 3. Set Up Required Environment Variables

Copy the `.env.example` file to `.env` and update the values with your Supabase project URL and anon key:

```bash
cp .env.example .env
```

Make sure to [enable anonymous sign-ins](https://supabase.com/dashboard/project/_/settings/auth) in the Auth settings of your Supabase project.

### 4. Start the App

Start the app and navigate to [http://localhost:5173](http://localhost:5173/):

```bash
npm run dev
```

## Next Steps

- Learn how [server-side auth](https://supabase.com/docs/guides/auth/server-side/creating-a-client?queryGroups=framework&framework=hono) works with Hono
- [Insert more data](https://supabase.com/docs/guides/database/import-data) into your database
- Upload and serve static files using [Storage](https://supabase.com/docs/guides/storage)
