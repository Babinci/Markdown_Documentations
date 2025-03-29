# Customizing Emails by Language

## Using user metadata to create multi-language email templates

When you register a user, you can create meta-data about them using the JS-Client's [signUp function](https://supabase.com/docs/reference/javascript/auth-signup?example=sign-up-with-additional-user-metadata):

```javascript
const { data, error } = await supabase.auth.signUp({
  email: 'email@example.com',
  password: 'example-password',
  options: {
    data: {
      first_name: 'John',
      last_name: 'Doe',
      age: 27,
      language: 'en'
    },
  },
})
```

The above example creates a user entry that includes information about their name, age, and language preference. The data is stored in the auth.users table in the `auth.raw_user_meta_data` column. You can view it in the auth schema with the [SQL Editor](https://supabase.com/dashboard/project/_/editor).

This metadata can be accessed in a project's [Email Templates](https://supabase.com/dashboard/project/_/auth/templates). 

If you need to update a user's meta-data, you can do so with the [`updateUser`](https://supabase.com/docs/reference/javascript/auth-updateuser?example=update-the-users-metadata) function.

## Creating multi-language templates

You can use the metadata to store a user's language preferences. You can then use "if statements" in the email template to set the content for a specific language:

```html
{{if eq .Data.language "en" }}
<h1>Welcome!</h1>
{{ else if eq .Data.language "pl" }}
<h1>Witamy!</h1>
{{ else }}
<h1>chuS'ugh, tera' je (Klingon)</h1>
{{end}}
```

Supabase uses the [Go Templating Language](https://pkg.go.dev/text/template) to render emails. It has advanced features for conditions that you may want to [explore](https://gohugo.io/templates/introduction/). 

For more complex examples and discussions about advanced language templates, you can refer to this [GitHub discussion](https://github.com/supabase/gotrue/issues/80#issuecomment-1552264148).
