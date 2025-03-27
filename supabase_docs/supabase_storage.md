# Supabase Storage

## Table of Contents
- [Introduction](#introduction)
- [Create a Bucket](#create-a-bucket)
- [Retrieve a Bucket](#retrieve-a-bucket)
- [List All Buckets](#list-all-buckets)
- [Update a Bucket](#update-a-bucket)
- [Delete a Bucket](#delete-a-bucket)
- [Empty a Bucket](#empty-a-bucket)
- [Upload a File](#upload-a-file)
- [Download a File](#download-a-file)
- [List All Files in a Bucket](#list-all-files-in-a-bucket)
- [Replace an Existing File](#replace-an-existing-file)
- [Move an Existing File](#move-an-existing-file)
- [Copy an Existing File](#copy-an-existing-file)
- [Delete Files in a Bucket](#delete-files-in-a-bucket)
- [Create a Signed URL](#create-a-signed-url)
- [Create Signed URLs](#create-signed-urls)
- [Create Signed Upload URL](#create-signed-upload-url)
- [Upload to a Signed URL](#upload-to-a-signed-url)
- [Retrieve Public URL](#retrieve-public-url)
- [Other Documentation Files](#other-documentation-files)

## Introduction

Supabase Storage provides a convenient way to store and serve files, including static assets like images, videos, and documents. This document covers operations for managing buckets (containers for files) and files themselves.

## Create a Bucket

Creates a new Storage bucket

- RLS policy permissions required:
  - `buckets` table permissions: `insert`
  - `objects` table permissions: none
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **id** *Required* `string`  
  A unique identifier for the bucket you are creating.

- **options** *Required* `CreateOrUpdateBucketOptions`

### Example

```python
response = (
    supabase.storage
    .create_bucket(
        "avatars",
        options={
            "public": False,
            "allowed_mime_types": ["image/png"],
            "file_size_limit": 1024,
        }
    )
)
```

## Retrieve a Bucket

Retrieves the details of an existing Storage bucket.

- RLS policy permissions required:
  - `buckets` table permissions: `select`
  - `objects` table permissions: none
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **id** *Required* `string`  
  The unique identifier of the bucket you would like to retrieve.

### Example

```python
response = supabase.storage.get_bucket("avatars")
```

## List All Buckets

Retrieves the details of all Storage buckets within an existing project.

- RLS policy permissions required:
  - `buckets` table permissions: `select`
  - `objects` table permissions: none
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Example

```python
response = supabase.storage.list_buckets()
```

## Update a Bucket

Updates a Storage bucket

- RLS policy permissions required:
  - `buckets` table permissions: `select` and `update`
  - `objects` table permissions: none
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **id** *Required* `string`  
  A unique identifier for the bucket you are creating.

- **options** *Required* `CreateOrUpdateBucketOptions`

### Example

```python
response = (
    supabase.storage
    .update_bucket(
        "avatars",
        options={
            "public": False,
            "allowed_mime_types": ["image/png"],
            "file_size_limit": 1024,
        }
    )
)
```

## Delete a Bucket

Deletes an existing bucket. A bucket can't be deleted with existing objects inside it. You must first `empty()` the bucket.

- RLS policy permissions required:
  - `buckets` table permissions: `select` and `delete`
  - `objects` table permissions: none
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **id** *Required* `string`  
  The unique identifier of the bucket you would like to delete.

### Example

```python
response = supabase.storage.delete_bucket("avatars")
```

## Empty a Bucket

Removes all objects inside a single bucket.

- RLS policy permissions required:
  - `buckets` table permissions: `select`
  - `objects` table permissions: `select` and `delete`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **id** *Required* `string`  
  The unique identifier of the bucket you would like to empty.

### Example

```python
response = supabase.storage.empty_bucket("avatars")
```

## Upload a File

Uploads a file to an existing bucket.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: only `insert` when you are uploading new files and `select`, `insert` and `update` when you are upserting files
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works
- Please specify the appropriate content [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) if you are uploading images or audio. If no `file_options` are specified, the MIME type defaults to `text/html`.

### Parameters

- **path** *Required* `string`  
  The file path, including the file name. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to upload.

- **file** *Required* `BufferedReader | bytes | FileIO | string | Path`  
  The body of the file to be stored in the bucket.

- **file_options** *Required* `FileOptions`

### Example

```python
with open("./public/avatar1.png", "rb") as f:
    response = (
        supabase.storage
        .from_("avatars")
        .upload(
            file=f,
            path="public/avatar1.png",
            file_options={"cache-control": "3600", "upsert": "false"}
        )
    )
```

## Download a File

Downloads a file from a private bucket. For public buckets, make a request to the URL returned from `get_public_url` instead.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `select`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **path** *Required* `string`  
  The full path and file name of the file to be downloaded. For example `folder/image.png`.

- **options** *Required* `DownloadOptions`

### Example

```python
with open("./myfolder/avatar1.png", "wb+") as f:
    response = (
        supabase.storage
        .from_("avatars")
        .download("folder/avatar1.png")
    )
    f.write(response)
```

## List All Files in a Bucket

Lists all the files within a bucket.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `select`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **path** *Optional* `string`  
  The folder path.

- **options** *Optional* `SearchOptions`

### Example

```python
response = (
    supabase.storage
    .from_("avatars")
    .list(
        "folder",
        {
            "limit": 100,
            "offset": 0,
            "sortBy": {"column": "name", "order": "desc"},
        }
    )
)
```

## Replace an Existing File

Replaces an existing file at the specified path with a new one.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `update` and `select`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **path** *Required* `string`  
  The file path, including the file name. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to upload.

- **file** *Required* `BufferedReader | bytes | FileIO | string | Path`  
  The body of the file to be stored in the bucket.

- **file_options** *Required* `FileOptions`

### Example

```python
with open("./public/avatar1.png", "rb") as f:
    response = (
        supabase.storage
        .from_("avatars")
        .update(
            file=f,
            path="public/avatar1.png",
            file_options={"cache-control": "3600", "upsert": "true"}
        )
    )
```

## Move an Existing File

Moves an existing file to a new path in the same bucket.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `update` and `select`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **from_path** *Required* `string`  
  The original file path, including the current file name. For example `folder/image.png`.

- **to_path** *Required* `string`  
  The new file path, including the new file name. For example `folder/image-new.png`.

### Example

```python
response = (
    supabase.storage
    .from_("avatars")
    .move(
        "public/avatar1.png", 
        "private/avatar2.png"
    )
)
```

## Copy an Existing File

Copies an existing file to a new path in the same bucket.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `update` and `select`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **from_path** *Required* `string`  
  The original file path, including the current file name. For example `folder/image.png`.

- **to_path** *Required* `string`  
  The new file path, including the new file name. For example `folder/image-new.png`.

### Example

```python
response = (
    supabase.storage
    .from_("avatars")
    .copy(
        "public/avatar1.png", 
        "private/avatar2.png"
    )
)
```

## Delete Files in a Bucket

Deletes files within the same bucket

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `delete` and `select`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **paths** *Required* `list[string]`  
  An array of files to delete, including the path and file name. For example `["folder/image.png"]`.

### Example

```python
response = (
    supabase.storage
    .from_("avatars")
    .remove(["folder/avatar1.png"])
)
```

## Create a Signed URL

Creates a signed URL for a file. Use a signed URL to share a file for a fixed amount of time.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `select`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **path** *Required* `string`  
  The file path, including the file name. For example `"folder/image.png"`.

- **expires_in** *Required* `number`  
  The number of seconds until the signed URL expires. For example, `60` for URLs which are valid for one minute.

- **options** *Optional* `URLOptions`

### Example

```python
response = (
    supabase.storage
    .from_("avatars")
    .create_signed_url(
        "folder/avatar1.png", 
        60
    )
)
```

## Create Signed URLs

Creates multiple signed URLs. Use a signed URL to share a file for a fixed amount of time.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `select`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **paths** *Required* `list[string]`  
  The file paths to be downloaded, including the current file names. For example `["folder/image.png", "folder2/image2.png"]`.

- **expires_in** *Required* `number`  
  The number of seconds until the signed URLs expire. For example, `60` for URLs which are valid for one minute.

- **options** *Optional* `CreateSignedURLsOptions`

### Example

```python
response = (
    supabase.storage
    .from_("avatars")
    .create_signed_urls(
        ["folder/avatar1.png", "folder/avatar2.png"], 
        60
    )
)
```

## Create Signed Upload URL

Creates a signed upload URL. Signed upload URLs can be used to upload files to the bucket without further authentication. They are valid for 2 hours.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: `insert`
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **path** *Required* `string`  
  The file path, including the current file name. For example `"folder/image.png"`.

### Example

```python
response = (
    supabase.storage
    .from_("avatars")
    .create_signed_upload_url("folder/avatar1.png")
)
```

## Upload to a Signed URL

Upload a file with a token generated from `create_signed_upload_url`.

- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: none
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **path** *Required* `string`  
  The file path, including the file name. Should be of the format `folder/subfolder/filename.png`. The bucket must already exist before attempting to upload.

- **token** *Required* `string`  
  The token generated from `create_signed_upload_url`

- **file** *Required* `BufferedReader | bytes | FileIO | string | Path`  
  The body of the file to be stored in the bucket.

- **options** *Required* `FileOptions`

### Example

```python
with open("./public/avatar1.png", "rb") as f:
    response = (
        supabase.storage
        .from_("avatars")
        .upload_to_signed_url(
            path="folder/cat.jpg",
            token="token-from-create_signed_upload_url",
            file=f,
        )
    )
```

## Retrieve Public URL

A simple convenience function to get the URL for an asset in a public bucket. If you do not want to use this function, you can construct the public URL by concatenating the bucket URL with the path to the asset. This function does not verify if the bucket is public. If a public URL is created for a bucket which is not public, you will not be able to download the asset.

- The bucket needs to be set to public, either via [update_bucket()](#update-a-bucket) or by going to Storage on [supabase.com/dashboard](https://supabase.com/dashboard), clicking the overflow menu on a bucket and choosing "Make public"
- RLS policy permissions required:
  - `buckets` table permissions: none
  - `objects` table permissions: none
- Refer to the [Storage guide](https://supabase.com/docs/guides/storage/security/access-control) on how access control works

### Parameters

- **path** *Required* `string`  
  The path and name of the file to generate the public URL for. For example `folder/image.png`.

- **options** *Optional* `URLOptions`

### Example

```python
response = (
    supabase.storage
    .from_("avatars")
    .get_public_url("folder/avatar1.jpg")
)
```

## Other Documentation Files

- [Overview](./supabase_overview.md)
- [Database Operations](./supabase_database.md)
- [Query Filters](./supabase_filters.md)
- [Authentication Basics](./supabase_auth_basics.md)
- [OAuth Authentication](./supabase_auth_oauth.md)
- [Multi-factor Authentication](./supabase_auth_mfa.md)
- [Admin Authentication Methods](./supabase_auth_admin.md)
- [Realtime](./supabase_realtime.md)
- [Edge Functions](./supabase_edge_functions.md)
