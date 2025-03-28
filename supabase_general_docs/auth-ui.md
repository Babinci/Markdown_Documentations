# Auth UI

> **Note:** As of February 7th, 2024, the Auth UI repository is no longer maintained by the Supabase Team. The team does not currently have capacity to give the expected level of care to this repository. They may revisit Auth UI in the future but regrettably have to leave it on hold as they focus on other priorities such as improving the Server-Side Rendering (SSR) package and advanced Auth primitives.

Auth UI is a pre-built React component for authenticating users. It supports custom themes and extensible styles to match your brand and aesthetic.

## Set up Auth UI

Install the latest version of [supabase-js](https://supabase.com/docs/reference/javascript) and the Auth UI package:

```bash
npm install @supabase/supabase-js @supabase/auth-ui-react @supabase/auth-ui-shared
```

### Import the Auth Component

Pass `supabaseClient` from `@supabase/supabase-js` as a prop to the component.

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')
const App = () => <Auth supabaseClient={supabase} />
```

This renders the Auth component without any styling. We recommend using one of the predefined themes to style the UI. Import the theme you want to use and pass it to the `appearance.theme` prop.

```jsx
import { Auth } from '@supabase/auth-ui-react'
import {
  // Import predefined theme
  ThemeSupa,
} from '@supabase/auth-ui-shared'

const supabase = createClient(
  '<INSERT PROJECT URL>',
  '<INSERT PROJECT ANON API KEY>'
)

const App = () => (
  <Auth
    supabaseClient={supabase}
    {/* Apply predefined theme */}
    appearance={{ theme: ThemeSupa }}
  />
)
```

### Social Providers

The Auth component also supports login with [official social providers](https://supabase.com/docs/guides/auth#providers).

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{ theme: ThemeSupa }}
    providers={['google', 'facebook', 'twitter']}
  />
)
```

### Options

Options are available via `queryParams`:

```jsx
<Auth
  supabaseClient={supabase}
  providers={['google']}
  queryParams={{
    access_type: 'offline',
    prompt: 'consent',
    hd: 'domain.com',
  }}
  onlyThirdPartyProviders
/>
```

### Provider Scopes

Provider Scopes can be requested through `providerScope`:

```jsx
<Auth
  supabaseClient={supabase}
  providers={['google']}
  queryParams={{
    access_type: 'offline',
    prompt: 'consent',
    hd: 'domain.com',
  }}
  providerScopes={{
    google: 'https://www.googleapis.com/auth/calendar.readonly',
  }}
/>
```

### Supported Views

The Auth component is currently shipped with the following views:

- [Email Login](https://supabase.com/docs/guides/auth/auth-email)
- [Magic Link login](https://supabase.com/docs/guides/auth/auth-magic-link)
- [Social Login](https://supabase.com/docs/guides/auth/social-login)
- Update password
- Forgotten password

## Customization

There are several ways to customize Auth UI:

- Use one of the [predefined themes](#predefined-themes) that comes with Auth UI
- Extend a theme by [overriding the variable tokens](#override-themes) in a theme
- [Create your own theme](#create-your-own-theme)
- [Use your own CSS classes](#custom-css-classes)
- [Use inline styles](#custom-inline-css)
- [Use your own labels](#custom-labels)

### Predefined Themes

Auth UI comes with several themes to customize the appearance. Each predefined theme comes with at least two variations, a `default` variation, and a `dark` variation. You can switch between these themes using the `theme` prop. Import the theme you want to use and pass it to the `appearance.theme` prop.

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient(
  '<INSERT PROJECT URL>',
  '<INSERT PROJECT ANON API KEY>'
)

const App = () => (
  <Auth
    supabaseClient={supabase}
    {/* Apply predefined theme */}
    appearance={{ theme: ThemeSupa }}
  />
)
```

Currently there is only one predefined theme available, but more may be added in the future.

### Switch Theme Variations

Auth UI comes with two theme variations: `default` and `dark`. You can switch between these themes with the `theme` prop.

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient(
  '<INSERT PROJECT URL>',
  '<INSERT PROJECT ANON API KEY>'
)

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{ theme: ThemeSupa }}
    {/* Set theme to dark */}
    theme="dark"
  />
)
```

If you don't pass a value to `theme` it uses the `"default"` theme. You can pass `"dark"` to the theme prop to switch to the `dark` theme. If your theme has other variations, use the name of the variation in this prop.

### Override Themes

Auth UI themes can be overridden using variable tokens.

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{
      theme: ThemeSupa,
      variables: {
        default: {
          colors: {
            brand: 'red',
            brandAccent: 'darkred',
          },
        },
      },
    }}
  />
)
```

If you created your own theme, you may not need to override any of them.

### Create Your Own Theme

You can create your own theme by following the same structure within a `appearance.theme` property.

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const customTheme = {
  default: {
    colors: {
      brand: 'hsl(153 60.0% 53.0%)',
      brandAccent: 'hsl(154 54.8% 45.1%)',
      brandButtonText: 'white',
      // ...
    },
  },
  dark: {
    colors: {
      brandButtonText: 'white',
      defaultButtonBackground: '#2e2e2e',
      defaultButtonBackgroundHover: '#3e3e3e',
      // ...
    },
  },
  // You can also add more theme variations with different names.
  evenDarker: {
    colors: {
      brandButtonText: 'white',
      defaultButtonBackground: '#1e1e1e',
      defaultButtonBackgroundHover: '#2e2e2e',
      // ...
    },
  },
}

const App = () => (
  <Auth
    supabaseClient={supabase}
    theme="default" // can also be "dark" or "evenDarker"
    appearance={{ theme: customTheme }}
  />
)
```

You can switch between different variations of your theme with the ["theme" prop](#switch-theme-variations).

### Custom CSS Classes

You can use custom CSS classes for the following elements:
`"button"`, `"container"`, `"anchor"`, `"divider"`, `"label"`, `"input"`, `"loader"`, `"message"`.

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{
      // If you want to extend the default styles instead of overriding it, set this to true
      extend: false,
      // Your custom classes
      className: {
        anchor: 'my-awesome-anchor',
        button: 'my-awesome-button',
        // ...
      },
    }}
  />
)
```

### Custom Inline CSS

You can use custom CSS inline styles for the following elements:
`"button"`, `"container"`, `"anchor"`, `"divider"`, `"label"`, `"input"`, `"loader"`, `"message"`.

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{
      style: {
        button: { background: 'red', color: 'white' },
        anchor: { color: 'blue' },
        // ...
      },
    }}
  />
)
```

### Custom Labels

You can use custom labels with `localization.variables` like so:

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    localization={{
      variables: {
        sign_in: {
          email_label: 'Your email address',
          password_label: 'Your strong password',
        },
      },
    }}
  />
)
```

#### Sign Up Label Customization

| Label Tag | Default Label |
| --- | --- |
| `email_label` | Email address |
| `password_label` | Create a Password |
| `email_input_placeholder` | Your email address |
| `password_input_placeholder` | Your password |
| `button_label` | Sign up |
| `loading_button_label` | Signing up ... |
| `social_provider_text` | Sign in with `{{provider}}` |
| `link_text` | Don't have an account? Sign up |
| `confirmation_text` | Check your email for the confirmation link |

Currently, translating error messages (e.g. "Invalid credentials") is not supported.

### Hiding Links

You can hide links by setting the `showLinks` prop to `false`

```jsx
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => <Auth supabaseClient={supabase} showLinks={false} />
```

Setting `showLinks` to `false` will hide the following links:

- Don't have an account? Sign up
- Already have an account? Sign in
- Send a magic link email
- Forgot your password?

### Sign In and Sign Up Views

Add `sign_in` or `sign_up` views with the `view` prop:

```jsx
<Auth
  supabaseClient={supabase}
  view="sign_up"
/>
```
