# Supabase Python Client Library Overview

## Table of Contents
- [Overview](#overview)
- [Installing](#installing)
- [Initializing](#initializing)
- [Other Documentation Files](#other-documentation-files)

## Overview

[supabase-py](https://github.com/supabase/supabase-py) is the official Python client library for Supabase. This library helps you interact with your Postgres database, listen to database changes, invoke Deno Edge Functions, build login and user management functionality, and manage large files.

## Installing

### Install with PyPi

You can install supabase-py via the terminal. (for Python > 3.8)

**PIP**
```bash
pip install supabase
```

## Initializing

You can initialize a new Supabase client using the `create_client()` method.

The Supabase client is your entrypoint to the rest of the Supabase functionality and is the easiest way to interact with everything we offer within the Supabase ecosystem.

### Parameters

- **supabase_url** *Required* `string`  
  The unique Supabase URL which is supplied when you create a new project in your project dashboard.

- **supabase_key** *Required* `string`  
  The unique Supabase Key which is supplied when you create a new project in your project dashboard.

- **options** *Optional* `ClientOptions`  
  Options to change the Auth behaviors.

### Example

**create_client()** With timeout option

```python
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
```

## Other Documentation Files

- [Database Operations](./supabase_database.md)
- [Query Filters](./supabase_filters.md)
- [Authentication Basics](./supabase_auth_basics.md)
- [OAuth Authentication](./supabase_auth_oauth.md)
- [Multi-factor Authentication](./supabase_auth_mfa.md)
- [Admin Authentication Methods](./supabase_auth_admin.md)
- [Realtime](./supabase_realtime.md)
- [Storage](./supabase_storage.md)
- [Edge Functions](./supabase_edge_functions.md)
