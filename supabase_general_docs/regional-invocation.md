# Regional Invocations

Learn how to execute an Edge Function in a particular region to optimize performance and reduce latency.

## Overview

By default, Edge Functions are executed in the region closest to the user making the request. This helps to reduce network latency and provide faster responses to the user.

However, if your Function performs lots of database or storage operations, invoking the Function in the same region as your database may provide better performance. Some situations where this might be helpful include:

- Bulk adding and editing records in your database
- Uploading and processing files
- Complex queries that require multiple database operations
- Data processing that requires low latency with your database

## Using the `x-region` Header

Use the `x-region` HTTP header when calling an Edge Function to determine where the Function should be executed:

### cURL Example

```bash
curl --request POST 'https://<project_ref>.supabase.co/functions/v1/hello-world' \
  --header 'Authorization: Bearer ANON_KEY' \
  --header 'Content-Type: application/json' \
  --header 'x-region: eu-west-3' \
  --data '{ "name":"Functions" }'
```

### JavaScript Example

```javascript
const response = await fetch(`https://${PROJECT_REF}.supabase.co/functions/v1/hello-world`, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${ANON_KEY}`,
    'Content-Type': 'application/json',
    'x-region': 'eu-west-3'
  },
  body: JSON.stringify({ name: 'Functions' })
})
```

You can verify the execution region by looking at the `x-sb-edge-region` HTTP header in the response. You can also find it as metadata in [Edge Function Logs](https://supabase.com/docs/guides/functions/logging).

## Available Regions

These are the currently supported region values you can provide for the `x-region` header:

| Region Code | Geographic Location |
|-------------|---------------------|
| `ap-northeast-1` | Tokyo, Japan |
| `ap-northeast-2` | Seoul, South Korea |
| `ap-south-1` | Mumbai, India |
| `ap-southeast-1` | Singapore |
| `ap-southeast-2` | Sydney, Australia |
| `ca-central-1` | Central Canada |
| `eu-central-1` | Frankfurt, Germany |
| `eu-west-1` | Dublin, Ireland |
| `eu-west-2` | London, UK |
| `eu-west-3` | Paris, France |
| `sa-east-1` | São Paulo, Brazil |
| `us-east-1` | Northern Virginia, USA |
| `us-west-1` | Northern California, USA |
| `us-west-2` | Oregon, USA |

## Using the Client Library

You can also specify the region when invoking a Function using the Supabase client library:

```javascript
const { createClient, FunctionRegion } = require('@supabase/supabase-js')

const supabase = createClient('https://your-project.supabase.co', 'your-anon-key')

const { data, error } = await supabase.functions.invoke('my-function-name', {
  headers: { 'Content-Type': 'application/json' },
  method: 'POST',
  body: { name: 'Functions' },
  region: FunctionRegion.UsEast1,
})
```

The `FunctionRegion` enum provides type-safe region codes:

```javascript
enum FunctionRegion {
  ApNortheast1 = 'ap-northeast-1',
  ApNortheast2 = 'ap-northeast-2',
  ApSouth1 = 'ap-south-1',
  // ... and so on for all regions
}
```

## Performance Considerations

When deciding whether to use regional invocation, consider:

1. **Database proximity**: If your function makes multiple database queries, invoking it in the same region as your database can reduce latency.

2. **User location**: For functions that interact minimally with the database but return large responses to users, using the default behavior (nearest to user) may be better.

3. **Global audience**: If your users are globally distributed but your database operations are intensive, consider using regional invocation for database operations and then returning results to users.

## Handling Regional Outages

If you explicitly specify the region via the `x-region` header, requests **will NOT** be automatically re-routed to another region if that region experiences an outage. 

To handle regional outages:

1. Implement monitoring to detect regional failures
2. Have a fallback mechanism to change the region during outages
3. Consider implementing multi-region strategies for mission-critical applications

For applications requiring high availability, you might want to implement retry logic with different regions:

```javascript
async function invokeWithRetry(functionName, body, primaryRegion, fallbackRegions) {
  try {
    return await supabase.functions.invoke(functionName, {
      body,
      region: primaryRegion
    })
  } catch (error) {
    // If primary region fails, try fallback regions
    for (const region of fallbackRegions) {
      try {
        return await supabase.functions.invoke(functionName, {
          body,
          region
        })
      } catch (fallbackError) {
        console.error(`Fallback region ${region} also failed`, fallbackError)
      }
    }
    throw new Error('All regions failed')
  }
}
```
