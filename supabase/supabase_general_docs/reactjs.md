# Use Supabase with React

Learn how to create a Supabase project, add some sample data to your database, and query the data from a React app.

## Getting Started

### 1. Create a Supabase project

Go to [database.new](https://database.new/) and create a new Supabase project.

When your project is up and running, go to the [Table Editor](https://supabase.com/dashboard/project/_/editor), create a new table and insert some data.

Alternatively, you can run the following snippet in your project's [SQL Editor](https://supabase.com/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.

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

### 2. Create a React app

Create a React app using a [Vite](https://vitejs.dev/guide/) template.

```bash
npm create vite@latest my-app -- --template react
```

### 3. Install the Supabase client library

The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a React app.

Navigate to the React app and install `supabase-js`.

```bash
cd my-app && npm install @supabase/supabase-js
```

### 4. Query data from the app

In `App.jsx`, create a Supabase client using your project URL and public API (anon) key.

You can find your Project URL and Anon key in your Supabase dashboard under Project Settings > API.

Add a `getInstruments` function to fetch the data and display the query result to the page.

```jsx
import { useEffect, useState } from "react";
import { createClient } from "@supabase/supabase-js";

const supabase = createClient("https://<project>.supabase.co", "<your-anon-key>");

function App() {
  const [instruments, setInstruments] = useState([]);

  useEffect(() => {
    getInstruments();
  }, []);

  async function getInstruments() {
    const { data } = await supabase.from("instruments").select();
    setInstruments(data);
  }

  return (
    <ul>
      {instruments.map((instrument) => (
        <li key={instrument.name}>{instrument.name}</li>
      ))}
    </ul>
  );
}

export default App;
```

### 5. Start the app

Start the app, go to [http://localhost:5173](http://localhost:5173/) in a browser, and open the browser console and you should see the list of instruments.

```bash
npm run dev
```

## Next steps

After setting up your basic Supabase integration with React, you can explore more advanced features:

- Set up [Authentication](https://supabase.com/docs/guides/auth) for your app
- [Insert more data](https://supabase.com/docs/guides/database/import-data) into your database
- Upload and serve static files using [Storage](https://supabase.com/docs/guides/storage)
- Implement [Real-time updates](https://supabase.com/docs/guides/realtime) for your application
- Add server functions with [Edge Functions](https://supabase.com/docs/guides/functions)
