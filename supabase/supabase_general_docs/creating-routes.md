# Creating API Routes

This guide explains how API routes are automatically created in Supabase and how to use them.

## Overview

API routes are automatically created when you create Postgres Tables, Views, or Functions in your Supabase project.

## Create a Table

Let's create our first API route by creating a table called `todos` to store tasks.
This creates a corresponding route `todos` which can accept `GET`, `POST`, `PATCH`, & `DELETE` requests.

### Using the Dashboard

1. Go to the [Table editor](https://supabase.com/dashboard/project/_/editor) page in the Dashboard.
2. Click **New Table** and create a table with the name `todos`.
3. Click **Save**.
4. Click **New Column** and create a column with the name `task` and type `text`.
5. Click **Save**.

### Using SQL

```sql
CREATE TABLE todos (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  task TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL
);
```

## API URL and Keys

Every Supabase project has a unique API URL. Your API is secured behind an API gateway which requires an API Key for every request.

1. Go to the [Settings](https://supabase.com/dashboard/project/_/settings/general) page in the Dashboard.
2. Click **API** in the sidebar.
3. Find your API `URL`, `anon`, and `service_role` keys on this page.

The REST API is accessible through the URL `https://<project_ref>.supabase.co/rest/v1`

Both of these routes require the `anon` key to be passed through an `apikey` header.

## Using the API

You can interact with your API directly via HTTP requests, or you can use the client libraries which Supabase provides.

Let's see how to make a request to the `todos` table which we created in the first step, using the API URL (`SUPABASE_URL`) and Key (`SUPABASE_ANON_KEY`):

### Using JavaScript

```javascript
// Initialize the JS client
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY)

// Make a request
const { data: todos, error } = await supabase.from('todos').select('*')
```

### Using cURL

```bash
curl 'https://<project_ref>.supabase.co/rest/v1/todos' \
  -H "apikey: SUPABASE_ANON_KEY" \
  -H "Authorization: Bearer SUPABASE_ANON_KEY"
```

## JavaScript Client Reference

- [`select()`](https://supabase.com/docs/reference/javascript/select) - Select data from a table
- [`insert()`](https://supabase.com/docs/reference/javascript/insert) - Insert rows into a table
- [`update()`](https://supabase.com/docs/reference/javascript/update) - Update rows in a table
- [`upsert()`](https://supabase.com/docs/reference/javascript/upsert) - Insert or update rows in a table
- [`delete()`](https://supabase.com/docs/reference/javascript/delete) - Delete rows in a table
- [`rpc()`](https://supabase.com/docs/reference/javascript/rpc) - Call Postgres functions
