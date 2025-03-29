# Serving Assets from Storage

This guide explains how to serve and download files from Supabase Storage buckets.

## Public Buckets

Assets uploaded to public buckets are accessible to anyone with the URL, without authentication. These files benefit from a high CDN cache hit ratio, improving performance.

### Accessing Public Files

You can access public files using this URL pattern:

```
https://[project_id].supabase.co/storage/v1/object/public/[bucket]/[asset-name]
```

You can also generate this URL using the Supabase SDK:

```javascript
const { data } = supabase.storage.from('bucket').getPublicUrl('filePath.jpg')
console.log(data.publicUrl)
```

### Downloading Files

To trigger an automatic download of the file instead of serving it in the browser, add the `?download` query parameter to the URL:

```
https://[project_id].supabase.co/storage/v1/object/public/[bucket]/[asset-name]?download
```

By default, the download will use the original filename. You can specify a custom filename:

```
https://[project_id].supabase.co/storage/v1/object/public/[bucket]/[asset-name]?download=customname.jpg
```

## Private Buckets

Assets stored in non-public buckets are private and cannot be accessed via a public URL. You can access these files only through:

1. Signing a time-limited URL (server-side approach, e.g., with Edge Functions)
2. Making an authenticated GET request to `https://[project_id].supabase.co/storage/v1/object/authenticated/[bucket]/[asset-name]` with a valid user Authorization header

### Signing URLs

You can create a time-limited signed URL to share with users by using the `createSignedUrl` method:

```javascript
const { data, error } = await supabase.storage
  .from('bucket')
  .createSignedUrl('private-document.pdf', 3600) // URL valid for 1 hour (3600 seconds)

if (data) {
  console.log(data.signedUrl)
}
```

This approach allows you to generate temporary access links to private files without requiring the recipient to be authenticated with your application.