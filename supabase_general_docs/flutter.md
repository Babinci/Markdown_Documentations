# Getting Started with Supabase and Flutter

This guide demonstrates how to use Supabase in a Flutter application, covering project setup, data querying, and authentication.

## Step 1: Create a Supabase Project

1. Go to [database.new](https://database.new/) and create a new Supabase project.
2. Once your project is running, create a table with sample data.

You can use this SQL in the [SQL Editor](https://supabase.com/dashboard/project/_/sql/new) to create an `instruments` table with sample data:

```sql
-- Create the table
CREATE TABLE instruments (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name TEXT NOT NULL
);

-- Insert some sample data into the table
INSERT INTO instruments (name)
VALUES
  ('violin'),
  ('viola'),
  ('cello');

-- Enable Row Level Security
ALTER TABLE instruments ENABLE ROW LEVEL SECURITY;

-- Create a policy to make the data publicly readable
CREATE POLICY "public can read instruments"
ON public.instruments
FOR SELECT TO anon
USING (true);
```

## Step 2: Create a Flutter App

Create a new Flutter app if you don't already have one:

```bash
flutter create my_app
```

## Step 3: Install the Supabase Client Library

Add the Supabase Flutter package to your project by editing your `pubspec.yaml` file:

```yaml
dependencies:
  flutter:
    sdk: flutter
  supabase_flutter: ^2.0.0
```

Then run:

```bash
flutter pub get
```

## Step 4: Initialize the Supabase Client

Open `lib/main.dart` and initialize the Supabase client with your project URL and anonymous key:

```dart
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  await Supabase.initialize(
    url: 'YOUR_SUPABASE_URL',
    anonKey: 'YOUR_SUPABASE_ANON_KEY',
  );
  
  runApp(MyApp());
}
```

Replace `YOUR_SUPABASE_URL` and `YOUR_SUPABASE_ANON_KEY` with your project's URL and anonymous key from your Supabase dashboard.

## Step 5: Query Data from the App

Create a simple app to fetch and display data from your Supabase database:

```dart
class MyApp extends StatelessWidget {
  const MyApp({super.key});
  
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Instruments',
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});
  
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final _future = Supabase.instance.client
      .from('instruments')
      .select();
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Musical Instruments'),
      ),
      body: FutureBuilder(
        future: _future,
        builder: (context, snapshot) {
          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }
          final instruments = snapshot.data!;
          return ListView.builder(
            itemCount: instruments.length,
            itemBuilder: ((context, index) {
              final instrument = instruments[index];
              return ListTile(
                title: Text(instrument['name']),
              );
            }),
          );
        },
      ),
    );
  }
}
```

## Step 6: Run Your App

Launch your app with:

```bash
flutter run
```

The app should display a list of instruments fetched from your Supabase database.

## Setting Up Deep Links

Many authentication methods require deep links to redirect users back to your app after authentication. Follow these steps to configure deep links for your application:

### Android Setup

Edit your `android/app/src/main/AndroidManifest.xml`:

```xml
<manifest ...>
    <application ...>
        <activity ...>
            <!-- ... -->
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="io.supabase.flutterquickstart" android:host="login-callback" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

### iOS Setup

Edit your `ios/Runner/Info.plist`:

```xml
<!-- ... -->
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleTypeRole</key>
        <string>Editor</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>io.supabase.flutterquickstart</string>
        </array>
    </dict>
</array>
<!-- ... -->
```

## Production Considerations

### Android 

Add internet permission to your AndroidManifest.xml:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
  <!-- Required to fetch data from the internet. -->
  <uses-permission android:name="android.permission.INTERNET" />
  <!-- ... -->
</manifest>
```

### macOS

For macOS apps, additional configuration is required to set up entitlements:

1. Edit the `macos/Runner/DebugProfile.entitlements` and `macos/Runner/Release.entitlements` files:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<!-- ... -->
	<key>com.apple.security.network.client</key>
	<true/>
</dict>
</plist>
```

## Next Steps

- [Add Authentication](https://supabase.com/docs/guides/auth/flutter)
- [Implement Row Level Security](https://supabase.com/docs/guides/auth/row-level-security)
- [Build a complete Flutter app with Supabase](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter)
- [Explore Flutter Auth UI components](flutter-auth-ui.md)
