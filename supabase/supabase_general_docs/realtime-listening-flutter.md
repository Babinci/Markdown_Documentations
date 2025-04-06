# Listening to Postgres Changes with Flutter

The Postgres Changes extension enables you to listen for database changes and receive them in real-time within your Flutter applications.

## Overview

Supabase Realtime allows you to subscribe to changes in your PostgreSQL database and receive those changes instantly in your Flutter application. This is useful for building real-time features such as:

- Live notifications
- Chat applications
- Collaborative editing
- Live dashboards
- Real-time updates to UI

## Implementation

To listen to Postgres Changes in your Flutter application:

1. Enable the Realtime feature for your table
2. Set up the Supabase client in your Flutter app
3. Subscribe to the changes using the Supabase client

## Video Tutorial

For a detailed walkthrough, check out this tutorial:

<iframe width="560" height="315" src="https://www.youtube.com/embed/gboTC2lcgzw" title="Listening to real-time changes on the database with Flutter and Supabase" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Watch on YouTube](https://www.youtube.com/watch?v=gboTC2lcgzw)

## Example Code

Here's a basic example of how to listen to Postgres Changes in a Flutter application:

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

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final _future = Supabase.instance.client
      .from('messages')
      .select()
      .order('created_at', ascending: false)
      .limit(10)
      .execute();

  List<Map<String, dynamic>> _messages = [];
  RealtimeSubscription? _subscription;

  @override
  void initState() {
    super.initState();
    _subscription = Supabase.instance.client
        .from('messages')
        .on(SupabaseEventTypes.insert, (payload) {
          setState(() {
            _messages = [payload.newRecord as Map<String, dynamic>, ..._messages];
          });
        })
        .subscribe();
  }

  @override
  void dispose() {
    _subscription?.unsubscribe();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Realtime Messages')),
        body: FutureBuilder(
          future: _future,
          builder: (context, snapshot) {
            if (!snapshot.hasData) {
              return const Center(child: CircularProgressIndicator());
            }
            final response = snapshot.data as PostgrestResponse;
            _messages = response.data;
            return ListView.builder(
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final message = _messages[index];
                return ListTile(
                  title: Text(message['content']),
                  subtitle: Text('From: ${message['username']}'),
                );
              },
            );
          },
        ),
      ),
    );
  }
}
```

## Enabling Realtime for Tables

Before you can listen to changes, you need to enable Realtime for your database tables:

1. Go to the [Supabase Dashboard](https://app.supabase.io)
2. Navigate to Database > Replication
3. Enable the tables you want to track with Realtime
4. You can also enable Realtime programmatically using SQL:

```sql
-- Enable replication for a specific table
ALTER PUBLICATION supabase_realtime ADD TABLE messages;

-- Enable Row Level Security for the table
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;

-- Create a policy that allows everyone to select messages
CREATE POLICY "Allow selecting messages" 
  ON messages FOR SELECT 
  USING (true);
```

## Advanced Usage

### Filtering Events

You can filter the events you receive by specifying event types:

```dart
_subscription = Supabase.instance.client
  .from('messages')
  .on(SupabaseEventTypes.insert | SupabaseEventTypes.update, (payload) {
    // Handle only inserts and updates
  })
  .subscribe();
```

### Subscribing to Specific Rows

You can subscribe to changes for specific rows using filters:

```dart
_subscription = Supabase.instance.client
  .from('messages')
  .on(SupabaseEventTypes.update, (payload) {
    // Handle update events
  })
  .eq('room_id', roomId) // Only listen to messages in this room
  .subscribe();
```

### Getting Old and New Record Values

When handling update events, you can access both the old and new values:

```dart
_subscription = Supabase.instance.client
  .from('messages')
  .on(SupabaseEventTypes.update, (payload) {
    final oldMessage = payload.oldRecord as Map<String, dynamic>;
    final newMessage = payload.newRecord as Map<String, dynamic>;
    print('Message changed from "${oldMessage['content']}" to "${newMessage['content']}"');
  })
  .subscribe();
```
