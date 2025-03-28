# Supabase Edge Functions

## Table of Contents
- [Introduction](#introduction)
- [Invoke a Supabase Edge Function](#invoke-a-supabase-edge-function)
- [Other Documentation Files](#other-documentation-files)

## Introduction

Supabase Edge Functions are server-side TypeScript functions that run on Supabase's Edge Function infrastructure. They allow you to execute custom server-side logic in a secure, managed environment. The Python client provides a simple interface to invoke these functions.

## Invoke a Supabase Edge Function

Invoke a Supabase Function.

- Requires an Authorization header.
- When you pass in a body to your function, Supabase automatically attaches the Content-Type header for `Blob`, `ArrayBuffer`, `File`, `FormData` and `String`. If it doesn't match any of these types we assume the payload is `json`, serialise it and attach the `Content-Type` header as `application/json`. You can override this behaviour by passing in a `Content-Type` header of your own.

### Example

```python
response = supabase.functions.invoke(
    "hello-world", 
    invoke_options={
        "body": {"name": "Functions"},
    },
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
- [Storage](./supabase_storage.md)
