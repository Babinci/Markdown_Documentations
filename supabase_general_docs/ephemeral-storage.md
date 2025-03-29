# Using Ephemeral Storage in Edge Functions

Supabase Edge Functions provides ephemeral file storage capabilities, allowing you to read and write files to the `/tmp` directory during function execution.

## Understanding Ephemeral Storage

Ephemeral storage resets on each function invocation. This means:

- Files you write during one invocation can only be read within the same invocation
- All data is lost when the function execution completes
- Each function instance has its own isolated storage space

## Use Cases

Ephemeral storage is useful for scenarios that require temporary file processing:

- **File Transformation**: Unzipping archives and processing their contents
- **Data Processing**: Reading and transforming CSV files before uploading to the database
- **Image Manipulation**: Custom image processing workflows using libraries like [`magick-wasm`](https://supabase.com/docs/guides/functions/examples/image-manipulation)
- **Temporary Storage**: Holding uploaded files for validation before storing them permanently

For processing tasks that might exceed the function timeout, consider using [Background Tasks](https://supabase.com/docs/guides/functions/background-tasks) to handle file operations asynchronously.

## How to Use

You can work with ephemeral storage using either:

1. [Deno File System APIs](https://docs.deno.com/api/deno/file-system)
2. The [`node:fs` module](https://docs.deno.com/api/node/fs/)

All file operations should target the `/tmp` directory.

### Example: Processing an Uploaded ZIP File

```typescript
Deno.serve(async (req) => {
  if (req.headers.get('content-type') !== 'application/zip') {
    return new Response('file must be a zip file', {
      status: 400,
    })
  }

  const uploadId = crypto.randomUUID()
  await Deno.writeFile('/tmp/' + uploadId, req.body)
  
  // do something with the written zip file
  
  return new Response('ok')
})
```

### Example: Reading and Writing Text Files

```typescript
Deno.serve(async (req) => {
  const data = await req.text();
  
  // Write to a temporary file
  const filePath = `/tmp/data-${Date.now()}.txt`;
  await Deno.writeTextFile(filePath, data);
  
  // Read from the temporary file
  const fileContent = await Deno.readTextFile(filePath);
  
  return new Response(`File processed: ${fileContent.length} characters`);
})
```

## API Limitations

There are some limitations to be aware of when working with ephemeral storage:

- **Synchronous Write APIs Not Supported**: Functions like `Deno.writeFileSync` or `Deno.mkdirSync` are not available
- **Synchronous Read APIs Are Available**: You can use functions like `Deno.readFileSync`
- **No Persistence Between Invocations**: Data is lost between function calls

## Storage Limits

Storage capacity depends on your Supabase project tier:

| Project Type | Storage Limit |
|--------------|---------------|
| Free         | 256MB         |
| Paid         | 512MB         |

These limits apply to the total amount of data you can write to ephemeral storage during a single function invocation.

## Best Practices

- Use unique filenames (e.g., with UUIDs or timestamps) to avoid conflicts
- Clean up files when done to free up memory, although this isn't strictly necessary
- For larger files, consider streaming the data rather than loading it all into memory
- Remember that ephemeral storage is not meant for persistent data storage - use Supabase Storage for permanent files