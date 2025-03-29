# Using Firebase Auth with Supabase

This guide explains how to use Firebase Authentication alongside or instead of Supabase Auth with your Supabase project.

## Getting Started

To integrate Firebase Auth with your Supabase project:

1. **Get your Firebase Project ID**: Find this in the [Firebase Console](https://console.firebase.google.com/u/0/project/_/settings/general) under Project settings.

2. **Add a Third-party Auth integration**: Go to your Supabase project's [Authentication settings](https://supabase.com/dashboard/project/_/settings/auth) and add a new Third-party Auth integration.

3. **Security for self-hosted setups**: If you're self-hosting Supabase, create and attach restrictive Row Level Security (RLS) policies to all tables in your public schema, Storage, and Realtime to prevent unauthorized access from unrelated Firebase projects.

4. **Assign the `role: 'authenticated'` custom claim**: Configure your Firebase Auth setup to assign this claim to all users.

5. **Set up the Supabase client**: Configure your client library to use Firebase Auth tokens.

## Setup the Supabase Client Library

### JavaScript/TypeScript

```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient('https://<supabase-project>.supabase.co', 'SUPABASE_ANON_KEY', {
  accessToken: async () => {
    return await firebase.auth().currentUser?.getIdToken(/* forceRefresh */ false) ?? null
  },
})
```

### Flutter

```dart
import 'package:supabase_flutter/supabase_flutter.dart';

Future<void> setupSupabase() async {
  await Supabase.initialize(
    url: 'https://<supabase-project>.supabase.co',
    anonKey: 'SUPABASE_ANON_KEY',
    authOptions: FlutterAuthClientOptions(
      accessTokenProvider: () async {
        final user = FirebaseAuth.instance.currentUser;
        if (user == null) return null;
        final idTokenResult = await user.getIdToken();
        return idTokenResult;
      },
    ),
  );
}
```

### Swift (iOS)

```swift
import Supabase

let client = SupabaseClient(
    supabaseURL: URL(string: "https://<supabase-project>.supabase.co")!,
    supabaseKey: "SUPABASE_ANON_KEY",
    options: SupabaseClientOptions(
        auth: AuthOptions(
            accessTokenFactory: {
                if let user = Auth.auth().currentUser {
                    return try await user.getIDToken()
                }
                return nil
            }
        )
    )
)
```

### Kotlin (Android)

```kotlin
import io.github.jan.supabase.createSupabaseClient
import io.github.jan.supabase.gotrue.Auth
import io.github.jan.supabase.gotrue.auth

val supabase = createSupabaseClient(
    supabaseUrl = "https://<supabase-project>.supabase.co",
    supabaseKey = "SUPABASE_ANON_KEY"
) {
    install(Auth) {
        accessTokenProvider = {
            FirebaseAuth.getInstance().currentUser?.getIdToken(false)?.await()?.token
        }
    }
}
```

### Kotlin (Multiplatform)

```kotlin
import io.github.jan.supabase.createSupabaseClient
import io.github.jan.supabase.gotrue.Auth
import io.github.jan.supabase.gotrue.auth

expect fun getFirebaseToken(): String?

val supabase = createSupabaseClient(
    supabaseUrl = "https://<supabase-project>.supabase.co",
    supabaseKey = "SUPABASE_ANON_KEY"
) {
    install(Auth) {
        accessTokenProvider = {
            getFirebaseToken()
        }
    }
}
```

**Note:** After user sign-up, you may need to call `getIdToken(/* forceRefresh */ true)` immediately, as the `onCreate` function that adds the required custom claim does not run synchronously.

## Add Third-Party Auth Integration to Your Project

### Using the Dashboard

In the Supabase dashboard, navigate to your project's [Authentication settings](https://supabase.com/dashboard/project/_/settings/auth) and find the Third-Party Auth section to add a new Firebase integration.

### Using the CLI

Add the following configuration to your `supabase/config.toml` file:

```toml
[auth.third_party.firebase]
enabled = true
project_id = "<firebase-project-id>"
```

## Securing Self-Hosted Installations

When self-hosting, it's essential to add restrictive RLS policies to prevent unauthorized access from other Firebase projects. This is because Firebase Auth uses the same JWT signing keys for all projects.

Create a restrictive policy like this for all tables in your public schema:

```sql
create policy "Restrict access to Supabase Auth and Firebase Auth for project ID <firebase-project-id>"
  on table_name
  as restrictive
  to authenticated
  using (
    (auth.jwt()->>'iss' = 'https://<project-ref>.supabase.co/auth/v1')
    or
    (
        auth.jwt()->>'iss' = 'https://securetoken.google.com/<firebase-project-id>'
        and
        auth.jwt()->>'aud' = '<firebase-project-id>'
     )
  );
```

For easier management across many tables, create a reusable function:

```sql
create function public.is_supabase_or_firebase_project_jwt()
  returns bool
  language sql
  stable
  returns null on null input
  return (
    (auth.jwt()->>'iss' = 'https://<project-ref>.supabase.co/auth/v1')
    or
    (
        auth.jwt()->>'iss' = concat('https://securetoken.google.com/<firebase-project-id>')
        and
        auth.jwt()->>'aud' = '<firebase-project-id>'
     )
  );
```

Then use this function in your policies:

```sql
create policy "Restrict access to correct Supabase and Firebase projects"
  on table_name
  as restrictive
  to authenticated
  using ((select public.is_supabase_or_firebase_project_jwt()) is true);
```

Apply similar policies to Storage buckets and Realtime channels.

## Assigning the "role" Custom Claim

Firebase JWTs don't contain a `role` claim by default. You must add a `role: 'authenticated'` custom claim so Supabase can correctly assign the PostgreSQL role.

### Using Firebase Authentication Functions

#### Option 1: Blocking Functions (for Firebase Authentication with Identity Platform)

**Node.js (Blocking Functions Gen 2)**

```javascript
import { beforeUserCreated, beforeUserSignedIn } from 'firebase-functions/v2/identity'

export const beforecreated = beforeUserCreated((event) => {
  return {
    customClaims: {
      // The Supabase project will use this role to assign the `authenticated`
      // Postgres role.
      role: 'authenticated',
    },
  }
})

export const beforesignedin = beforeUserSignedIn((event) => {
  return {
    customClaims: {
      role: 'authenticated',
    },
  }
})
```

**Python (Blocking Functions Gen 2)**

```python
from firebase_functions.identity import before_user_created, before_user_signed_in

@before_user_created()
def before_created(event):
    return {
        "customClaims": {
            "role": "authenticated"
        }
    }

@before_user_signed_in()
def before_signed_in(event):
    return {
        "customClaims": {
            "role": "authenticated"
        }
    }
```

#### Option 2: Cloud Function for New Users

```javascript
import * as functions from 'firebase-functions'
import * as admin from 'firebase-admin'

admin.initializeApp()

export const addAuthenticatedRole = functions.auth
  .user()
  .onCreate(async (user) => {
    try {
      await admin.auth().setCustomUserClaims(user.uid, {
        role: 'authenticated',
      })
      console.log(`Successfully added role claim to user ${user.uid}`)
    } catch (error) {
      console.error(`Error adding role claim to user ${user.uid}:`, error)
    }
  })
```

Deploy your functions:

```bash
firebase deploy --only functions
```

### Updating Existing Users with Admin SDK

For existing users, run a script to add the custom claim:

```javascript
'use strict';
const { initializeApp } = require('firebase-admin/app');
const { getAuth } = require('firebase-admin/auth');

initializeApp();

async function setRoleCustomClaim() {
  let nextPageToken = undefined
  do {
    const listUsersResult = await getAuth().listUsers(1000, nextPageToken)
    nextPageToken = listUsersResult.pageToken
    
    await Promise.all(listUsersResult.users.map(async (userRecord) => {
      try {
        await getAuth().setCustomUserClaims(userRecord.uid, {
          role: 'authenticated'
        })
        console.log(`Added role to user ${userRecord.uid}`)
      } catch (error) {
        console.error('Failed to set custom role for user', userRecord.uid)
      }
    }))
  } while (nextPageToken);
}

setRoleCustomClaim().then(() => process.exit(0))
```

After users receive the `role: 'authenticated'` claim, it will appear in all newly issued ID tokens.
