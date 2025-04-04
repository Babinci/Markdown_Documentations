# Resumable Uploads

## Learn how to upload files to Supabase Storage

The resumable upload method is recommended when:

- Uploading large files that may exceed 6MB in size
- Network stability is a concern
- You want to have progress events for your uploads

Supabase Storage implements the [TUS protocol](https://tus.io/) to enable resumable uploads. TUS stands for The Upload Server and is an open protocol for supporting resumable uploads. The protocol allows the upload process to be resumed from where it left off in case of interruptions. This method can be implemented using the [`tus-js-client`](https://github.com/tus/tus-js-client) library, or other client-side libraries like [Uppy](https://uppy.io/docs/tus/) that support the TUS protocol.

## Implementation Example

Here's an example of how to upload a file using `tus-js-client`:

```javascript
const tus = require('tus-js-client')
const projectId = ''

async function uploadFile(bucketName, fileName, file) {
    const { data: { session } } = await supabase.auth.getSession()
    
    return new Promise((resolve, reject) => {
        var upload = new tus.Upload(file, {
            endpoint: `https://${projectId}.supabase.co/storage/v1/upload/resumable`,
            retryDelays: [0, 3000, 5000, 10000, 20000],
            headers: {
                authorization: `Bearer ${session.access_token}`,
                'x-upsert': 'true', // optionally set upsert to true to overwrite existing files
            },
            uploadDataDuringCreation: true,
            removeFingerprintOnSuccess: true, // Important if you want to allow re-uploading the same file
            metadata: {
                bucketName: bucketName,
                objectName: fileName,
                contentType: 'image/png',
                cacheControl: 3600,
            },
            chunkSize: 6 * 1024 * 1024, // NOTE: it must be set to 6MB (for now) do not change it
            onError: function (error) {
                console.log('Failed because: ' + error)
                reject(error)
            },
            onProgress: function (bytesUploaded, bytesTotal) {
                var percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2)
                console.log(bytesUploaded, bytesTotal, percentage + '%')
            },
            onSuccess: function () {
                console.log('Download %s from %s', upload.file.name, upload.url)
                resolve()
            },
        })
        
        // Check if there are any previous uploads to continue.
        return upload.findPreviousUploads().then(function (previousUploads) {
            // Found previous uploads so we select the first one.
            if (previousUploads.length) {
                upload.resumeFromPreviousUpload(previousUploads[0])
            }
            // Start the upload
            upload.start()
        })
    })
}
```

## Upload URL

When uploading using the resumable upload endpoint, the storage server creates a unique URL for each upload, even for multiple uploads to the same path. All chunks will be uploaded to this URL using the `PATCH` method.

This unique upload URL will be valid for **up to 24 hours**. If the upload is not completed within 24 hours, the URL will expire and you'll need to start the upload again. TUS client libraries typically create a new URL if the previous one expires.

## Concurrency

When two or more clients upload to the same upload URL only one of them will succeed. The other clients will receive a `409 Conflict` error. Only 1 client can upload to the same upload URL at a time which prevents data corruption.

When two or more clients upload a file to the same path using different upload URLs, the first client to complete the upload will succeed and the other clients will receive a `409 Conflict` error.

If you provide the `x-upsert` header the last client to complete the upload will succeed instead.

## Uppy Example

You can check a [full example using Uppy](https://github.com/supabase/supabase/tree/master/examples/storage/resumable-upload-uppy).

Uppy has integrations with different frameworks:

- [React](https://uppy.io/docs/react/)
- [Svelte](https://uppy.io/docs/svelte/)
- [Vue](https://uppy.io/docs/vue/)
- [Angular](https://uppy.io/docs/angular/)

## Overwriting Files

When uploading a file to a path that already exists, the default behavior is to return a `400 Asset Already Exists` error.
If you want to overwrite a file on a specific path you can set the `x-upsert` header to `true`.

We do advise against overwriting files when possible, as the CDN will take some time to propagate the changes to all the edge nodes leading to stale content.
Uploading a file to a new path is the recommended way to avoid propagation delays and stale content.

To learn more, see the [CDN](https://supabase.com/docs/guides/storage/cdn/fundamentals) guide.
