# Use Supabase with Vue

Learn how to create a Supabase project, add some sample data to your database, and query the data from a Vue app.

## 1. Create a Supabase Project

Go to [database.new](https://database.new/) and create a new Supabase project.

When your project is up and running, go to the [Table Editor](https://supabase.com/dashboard/project/_/editor), create a new table and insert some data.

Alternatively, you can run the following snippet in your project's [SQL Editor](https://supabase.com/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data:

```sql
-- Create the table
create table instruments (
  id bigint primary key generated always as identity,
  name text not null
);

-- Insert some sample data into the table
insert into instruments (name)
values
  ('violin'),
  ('viola'),
  ('cello');

alter table instruments enable row level security;
```

Make the data in your table publicly readable by adding an RLS policy:

```sql
create policy "public can read instruments"
on public.instruments
for select to anon
using (true);
```

## 2. Create a Vue App

Create a Vue app using the `npm init` command:

```bash
npm init vue@latest my-app
```

## 3. Install the Supabase Client Library

The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a Vue app.

Navigate to the Vue app and install `supabase-js`:

```bash
cd my-app && npm install @supabase/supabase-js
```

## 4. Create the Supabase Client

Create a `/src/lib` directory in your Vue app, create a file called `supabaseClient.js` and add the following code to initialize the Supabase client with your project URL and public API (anon) key:

```javascript
import { createClient } from '@supabase/supabase-js'

export const supabase = createClient('https://<project>.supabase.co', '<your-anon-key>')
```

## 5. Query Data from the App

Replace the existing content in your `App.vue` file with the following code:

```vue
<script setup>
  import { ref, onMounted } from 'vue'
  import { supabase } from './lib/supabaseClient'

  const instruments = ref([])

  async function getInstruments() {
    const { data } = await supabase.from('instruments').select()
    instruments.value = data
  }

  onMounted(() => {
    getInstruments()
  })
</script>

<template>
  <ul>
    <li v-for="instrument in instruments" :key="instrument.id">{{ instrument.name }}</li>
  </ul>
</template>
```

## 6. Start the App

Start the app and go to [http://localhost:5173](http://localhost:5173/) in a browser to see the list of instruments:

```bash
npm run dev
```
