# Use Supabase with refine

Learn how to create a Supabase project, add sample data to your database, and query the data from a [refine](https://refine.dev/) app.

## Step-by-Step Guide

### 1. Create a Supabase Project

Go to [database.new](https://database.new/) and create a new Supabase project.

When your project is up and running, go to the [Table Editor](https://supabase.com/dashboard/project/_/editor), create a new table and insert some data.

Alternatively, you can run the following snippet in your project's [SQL Editor](https://supabase.com/dashboard/project/_/sql/new). This will create an `instruments` table with some sample data:

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

### 2. Create a refine App

Create a [refine](https://github.com/refinedev/refine) app using the [create refine-app](https://refine.dev/docs/getting-started/quickstart/) command.

The `refine-supabase` preset adds the `@refinedev/supabase` supplementary package that supports Supabase in a refine app. This package includes the Supabase dependency [supabase-js](https://github.com/supabase/supabase-js) out-of-the-box.

```bash
npm create refine-app@latest -- --preset refine-supabase my-app
```

### 3. Open Your refine App in VS Code

You will develop your app, connect to the Supabase backend, and run the refine app in VS Code:

```bash
cd my-app
code .
```

### 4. Start the App

Start the app, go to [http://localhost:5173](http://localhost:5173/) in a browser, and you should be greeted with the refine Welcome page:

```bash
npm run dev
```

![refine welcome page](https://supabase.com/docs/img/refine-qs-welcome-page.png)

### 5. Update `supabaseClient`

Update the `supabaseClient` with your Supabase project's URL and API key. The `supabaseClient` is used in auth provider and data provider methods that allow the refine app to connect to your Supabase backend.

You can find your Project URL and Anon key in your Supabase dashboard under Project Settings > API.

```javascript
import { createClient } from "@refinedev/supabase";

const SUPABASE_URL = "YOUR_SUPABASE_URL";
const SUPABASE_KEY = "YOUR_SUPABASE_KEY";

export const supabaseClient = createClient(SUPABASE_URL, SUPABASE_KEY, {
  db: {
    schema: "public",
  },
  auth: {
    persistSession: true,
  },
});
```

### 6. Add Instruments Resource and Pages

Configure resources and define pages for the `instruments` resource.

Use the following command to automatically add resources and generate code for pages for `instruments` using refine Inferencer:

```bash
npm run refine create-resource instruments
```

This defines pages for `list`, `create`, `show`, and `edit` actions inside the `src/pages/instruments/` directory with the `<HeadlessInferencer />` component.

The `<HeadlessInferencer />` component depends on `@refinedev/react-table` and `@refinedev/react-hook-form` packages. To avoid errors, install them as dependencies:

```bash
npm install @refinedev/react-table @refinedev/react-hook-form
```

The `<HeadlessInferencer />` is a refine Inferencer component that automatically generates necessary code for the pages. More information on [how the Inferencer works is available in the docs](https://refine.dev/docs/packages/documentation/inferencer/).

### 7. Add Routes for Instruments Pages

Add routes for the `list`, `create`, `show`, and `edit` pages. You should remove the `index` route for the Welcome page presented with the `<Welcome />` component.

Update your `App.tsx` file:

```tsx
import { Refine } from "@refinedev/core";
import { RefineKbar, RefineKbarProvider } from "@refinedev/kbar";
import routerBindings, {
  DocumentTitleHandler,
  NavigateToResource,
  UnsavedChangesNotifier,
} from "@refinedev/react-router-v6";
import { dataProvider, liveProvider } from "@refinedev/supabase";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import authProvider from "./authProvider";
import { supabaseClient } from "./utility";
import { 
  InstrumentsCreate, 
  InstrumentsEdit, 
  InstrumentsList, 
  InstrumentsShow 
} from "./pages/instruments";

function App() {
  return (
    <BrowserRouter>
      <RefineKbarProvider>
        <Refine
          dataProvider={dataProvider(supabaseClient)}
          liveProvider={liveProvider(supabaseClient)}
          authProvider={authProvider}
          routerProvider={routerBindings}
          options={{
            syncWithLocation: true,
            warnWhenUnsavedChanges: true,
          }}
          resources={[{
            name: "instruments",
            list: "/instruments",
            create: "/instruments/create",
            edit: "/instruments/edit/:id",
            show: "/instruments/show/:id"
          }]}>
          <Routes>
            <Route 
              index
              element={<NavigateToResource resource="instruments" />}
            />
            <Route path="/instruments">
              <Route index element={<InstrumentsList />} />
              <Route path="create" element={<InstrumentsCreate />} />
              <Route path="edit/:id" element={<InstrumentsEdit />} />
              <Route path="show/:id" element={<InstrumentsShow />} />
            </Route>
          </Routes>
          <RefineKbar />
          <UnsavedChangesNotifier />
          <DocumentTitleHandler />
        </Refine>
      </RefineKbarProvider>
    </BrowserRouter>
  );
}

export default App;
```

### 8. View Instruments Pages

Now you should be able to see the instruments pages along the `/instruments` routes. You can edit and add new instruments using the Inferencer-generated UI.

The Inferencer auto-generated code gives you a good starting point on which to keep building your `list`, `create`, `show`, and `edit` pages. To view the generated code, click the "Show the auto-generated code" buttons in their respective pages.

## Advanced Features

### Adding Authentication

refine comes with built-in authentication that works with Supabase. To enable it, you need to:

1. Configure auth provider in your `authProvider.ts` file
2. Add login/register pages
3. Set up RLS policies for authenticated users

### Real-time Updates

refine supports Supabase Realtime subscriptions. To enable real-time updates:

1. Make sure the `liveProvider` is configured (already done in step 7)
2. Enable Realtime for your tables in the Supabase dashboard
3. Add `live={true}` to your components to enable real-time features

### Custom Queries

If you need to perform custom queries beyond the basic CRUD operations:

```typescript
// Custom query example
const { data } = await supabaseClient
  .from("instruments")
  .select("*")
  .order("name", { ascending: true })
  .limit(5);
```

## Troubleshooting

- **404 Not Found**: Make sure your routes are correctly configured in `App.tsx`
- **Auth Issues**: Check your Supabase URL and API key
- **Permission Denied**: Ensure your Row Level Security (RLS) policies are correctly set up
- **Inferencer Errors**: Install all required dependencies for the Inferencer components
