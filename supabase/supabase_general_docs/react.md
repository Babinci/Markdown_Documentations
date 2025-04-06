# Use Supabase Auth with React

Learn how to use Supabase Auth with React.js to add authentication to your web application.

## Getting Started

### 1. Create a new Supabase project

[Launch a new project](https://supabase.com/dashboard) in the Supabase Dashboard.

Your new database has a table for storing your users. You can see that this table is currently empty by running some SQL in the [SQL Editor](https://supabase.com/dashboard/project/_/sql).

```sql
select * from auth.users;
```

### 2. Create a React app

Create a React app using the `create-react-app` command.

```bash
npx create-react-app my-app
```

### 3. Install the Supabase client library

The fastest way to get started is to use Supabase's `auth-ui-react` library which provides a convenient interface for working with Supabase Auth from a React app.

Navigate to the React app and install the Supabase libraries.

```bash
cd my-app && npm install @supabase/supabase-js @supabase/auth-ui-react @supabase/auth-ui-shared
```

## Setting Up Authentication

### 4. Set up your login component

In `App.js`, create a Supabase client using your [Project URL and public API (anon) key](https://supabase.com/dashboard/project/_/settings/api).

You can configure the Auth component to display whenever there is no session inside `supabase.auth.getSession()`.

```jsx
import './index.css'
import { useState, useEffect } from 'react'
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient('https://<project>.supabase.co', '<your-anon-key>')

export default function App() {
  const [session, setSession] = useState(null)

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session)
    })

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setSession(session)
    })

    return () => subscription.unsubscribe()
  }, [])

  if (!session) {
    return (<Auth supabaseClient={supabase} appearance={{ theme: ThemeSupa }} />)
  }
  else {
    return (<div>Logged in!</div>)
  }
}
```

### 5. Start the app

Start the app, go to [http://localhost:3000](http://localhost:3000/) in a browser, and open the browser console and you should be able to log in.

```bash
npm start
```

## Customizing the Auth UI

You can customize the Auth UI by passing additional props to the `Auth` component:

```jsx
<Auth
  supabaseClient={supabase}
  appearance={{ theme: ThemeSupa }}
  providers={['google', 'github']}
  socialLayout="horizontal"
  redirectTo="http://localhost:3000/auth/callback"
/>
```

## Next Steps

After implementing basic authentication, consider adding:

1. **Protected routes** - Restrict access to certain pages based on authentication status
2. **User profiles** - Create and manage user profiles in your database
3. **Role-based access control** - Implement different permissions for different user types
4. **Password reset** - Allow users to reset their passwords
5. **Email verification** - Verify user emails before granting full access
