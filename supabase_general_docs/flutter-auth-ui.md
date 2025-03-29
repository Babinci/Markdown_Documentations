# Flutter Auth UI

Flutter Auth UI is a pre-built, customizable authentication UI package for Flutter applications that integrate with Supabase Auth. It provides ready-to-use widgets for multiple authentication methods while being flexible enough to match your brand's design.

![Flutter Auth UI Screenshot](https://raw.githubusercontent.com/supabase-community/flutter-auth-ui/main/screenshots/supabase_auth_ui.png)

## Installation

Add the latest version of the package to your Flutter project:

```bash
flutter pub add supabase_auth_ui
```

## Initialization

Before using the Auth UI components, initialize Supabase in your Flutter application:

```dart
import 'package:flutter/material.dart';
import 'package:supabase_auth_ui/supabase_auth_ui.dart';

void main() async {
  await Supabase.initialize(
    url: dotenv.get('SUPABASE_URL'),
    anonKey: dotenv.get('SUPABASE_ANON_KEY'),
  );
  
  runApp(const MyApp());
}
```

## Authentication Components

### Email Authentication

Use the `SupaEmailAuth` widget to create email and password sign-in and sign-up forms:

```dart
SupaEmailAuth(
  redirectTo: kIsWeb ? null : 'io.mydomain.myapp://callback',
  onSignInComplete: (response) {
    // Handle successful sign in
  },
  onSignUpComplete: (response) {
    // Handle successful sign up
  },
  metadataFields: [
    MetaDataField(
      prefixIcon: const Icon(Icons.person),
      label: 'Username',
      key: 'username',
      validator: (val) {
        if (val == null || val.isEmpty) {
          return 'Please enter something';
        }
        return null;
      },
    ),
  ],
)
```

The `metadataFields` parameter allows you to collect additional user information during signup, which will be stored in the user's metadata.

### Magic Link Authentication

Use the `SupaMagicAuth` widget to create a passwordless email magic link form:

```dart
SupaMagicAuth(
  redirectUrl: kIsWeb ? null : 'io.mydomain.myapp://callback',
  onSuccess: (Session response) {
    // Handle successful authentication
  },
  onError: (error) {
    // Handle error
  },
)
```

### Password Reset

Use the `SupaResetPassword` widget to create a password reset form:

```dart
SupaResetPassword(
  accessToken: supabase.auth.currentSession?.accessToken,
  onSuccess: (UserResponse response) {
    // Handle successful password reset
  },
  onError: (error) {
    // Handle error
  },
)
```

### Phone Authentication

Use the `SupaPhoneAuth` widget for phone-based authentication:

```dart
SupaPhoneAuth(
  authAction: SupaAuthAction.signUp,  // or SupaAuthAction.signIn
  onSuccess: (AuthResponse response) {
    // Handle successful authentication
  },
),
```

### Social Authentication

Use the `SupaSocialsAuth` widget to display buttons for social login providers:

```dart
SupaSocialsAuth(
  socialProviders: [
    OAuthProvider.apple,
    OAuthProvider.google,
  ],
  colored: true,  // Use provider brand colors
  redirectUrl: kIsWeb
    ? null
    : 'io.mydomain.myapp://callback',
  onSuccess: (Session response) {
    // Handle successful authentication
  },
  onError: (error) {
    // Handle error
  },
)
```

## Theming

The Flutter Auth UI package uses standard Flutter components, allowing you to use your application's theme to style the authentication forms. This makes it easy to match your brand's aesthetic without customizing individual components.

Key theming considerations:
- Use your app's `ThemeData` to control colors, typography, and shapes
- Flutter Auth UI respects your app's `InputDecoration` theme for form fields
- Button styles follow your app's `ElevatedButton` and `TextButton` themes
- Text styling is derived from your app's `TextTheme`

## Deep Linking Setup

For mobile applications using OAuth or magic links, configure deep linking to handle redirect URLs:

### Android Setup

In your `android/app/src/main/AndroidManifest.xml` file:

```xml
<manifest ...>
    <application ...>
        ...
        <activity ...>
            ...
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="io.mydomain.myapp" android:host="callback" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

### iOS Setup

In your `ios/Runner/Info.plist` file:

```xml
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleTypeRole</key>
        <string>Editor</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>io.mydomain.myapp</string>
        </array>
    </dict>
</array>
```

## Advanced Usage

### Custom Validators

You can provide custom validation logic for form fields:

```dart
SupaEmailAuth(
  // ... other properties
  emailValidator: (value) {
    if (!value.contains('@mycompany.com')) {
      return 'Only company emails allowed';
    }
    return null;
  },
  passwordValidator: (value) {
    if (value.length < 12) {
      return 'Password must be at least 12 characters';
    }
    return null;
  },
)
```

### Handling Auth State Changes

To respond to authentication state changes, use Supabase's auth state listener:

```dart
@override
void initState() {
  super.initState();
  supabase.auth.onAuthStateChange.listen((data) {
    final AuthChangeEvent event = data.event;
    if (event == AuthChangeEvent.signedIn) {
      // User has signed in
    } else if (event == AuthChangeEvent.signedOut) {
      // User has signed out
    }
  });
}
```

## Resources

- [Supabase Flutter Auth Documentation](https://supabase.com/docs/guides/auth/flutter)
- [Flutter Auth UI Package on pub.dev](https://pub.dev/packages/supabase_auth_ui)
- [Supabase Auth Documentation](https://supabase.com/docs/guides/auth)
