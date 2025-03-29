# Creating Buckets

This guide explains how to create storage buckets in Supabase and configure upload restrictions.

## Overview

You can create a bucket using the Supabase Dashboard. Since storage is interoperable with your Postgres database, you can also use SQL or our client libraries.

Here are different ways to create a bucket called "avatars":

### Using JavaScript

```javascript
// Use the JS library to create a bucket.
const { data, error } = await supabase.storage.createBucket('avatars', {
  public: true, // default: false
})
```

### Using Dart

```dart
final StorageBucketResponse res = await supabase.storage.createBucket('avatars',
  const BucketOptions(public: true));
```

### Using Swift

```swift
let response = try await supabase.storage.createBucket(
  id: "avatars",
  options: .init(public: true)
)
```

### Using Python

```python
# Use the Python library to create a bucket.
bucket = supabase.storage.create_bucket("avatars", {"public": True})
```

### Using SQL

```sql
-- Use SQL to create a bucket
insert into storage.buckets (id, name, public)
values ('avatars', 'avatars', true);
```

## Restricting Uploads

When creating a bucket you can add additional configurations to restrict the type or size of files you want this bucket to contain.

For example, imagine you want to allow your users to upload only images to the `avatars` bucket and the size must not be greater than 1MB.

You can achieve this by providing: `allowedMimeTypes` and `maxFileSize`:

```javascript
// Use the JS library to create a bucket.
const { data, error } = await supabase.storage.createBucket('avatars', {
  public: true,
  allowedMimeTypes: ['image/*'],
  fileSizeLimit: '1MB',
})
```

If an upload request doesn't meet the above restrictions it will be rejected.

For more information, check the [File Limits](https://supabase.com/docs/guides/storage/uploads/file-limits) section.
