# How to Check GoTrue/API Version of a Supabase Project

When troubleshooting authentication issues or ensuring compatibility with specific features, it's helpful to know which version of GoTrue (Supabase's auth service) is running in your project.

## Using the Health Check Endpoint

You can make a `GET` request to the health check endpoint to retrieve this information. Here's an example using `curl`:

```bash
curl -X GET 'https://project-ref.supabase.co/auth/v1/health' -H 'apikey: ANON_KEY'
```

Replace `project-ref` with your actual Supabase project reference and `ANON_KEY` with your project's anon key.

## Sample Response

The response will look like this:

```json
{
    "version": "v2.60.7",
    "name": "GoTrue",
    "description": "GoTrue is a user registration and authentication API"
}
```

This information is particularly useful when:

- Debugging authentication issues that might be version-specific
- Verifying that your project has a version that supports specific features
- Reporting issues to Supabase support
- Ensuring compatibility between client libraries and the server version

## Using in JavaScript/TypeScript

If you prefer to use JavaScript/TypeScript instead of curl:

```javascript
async function checkGoTrueVersion() {
  const response = await fetch('https://project-ref.supabase.co/auth/v1/health', {
    headers: {
      'apikey': 'ANON_KEY'
    }
  });
  const data = await response.json();
  console.log('GoTrue version:', data.version);
  return data;
}
```
