# Using Realtime Presence with Flutter

Supabase Presence enables you to track and display which users are currently online in your Flutter application, a common feature for real-time collaborative applications.

## Overview

Presence allows you to:

- Track when users join or leave a session
- Show which users are currently online
- Display user status and activity
- Enable real-time collaboration features

## Implementation

To implement Realtime Presence in your Flutter application, you'll need to:

1. Set up a Supabase project with Realtime enabled
2. Connect to Supabase Realtime from your Flutter app
3. Track user presence using the Presence API
4. Listen to presence changes and update your UI accordingly

## Video Tutorial

For a detailed walkthrough of implementing Presence in a Flutter app, check out this tutorial:

<iframe width="560" height="315" src="https://www.youtube.com/embed/B2NZvZ2uLNs" title="Track online users with Supabase Realtime Presence | Flutter Figma Clone #3" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Watch on YouTube](https://www.youtube.com/watch?v=B2NZvZ2uLNs)

## Example Code

Here's an example implementation of Realtime Presence in a Flutter application:

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

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: PresenceExample(),
    );
  }
}

class PresenceExample extends StatefulWidget {
  @override
  _PresenceExampleState createState() => _PresenceExampleState();
}

class _PresenceExampleState extends State<PresenceExample> {
  final supabase = Supabase.instance.client;
  final channel = Supabase.instance.client.channel('room:123');
  final myUserId = 'user-${DateTime.now().millisecondsSinceEpoch}';
  Map<String, dynamic> presenceState = {};
  
  @override
  void initState() {
    super.initState();
    
    // Subscribe to presence changes
    channel
      .on(RealtimeListenTypes.presence, ChannelFilter(event: 'sync'), 
        (payload, [ref]) {
          setState(() {
            presenceState = channel.presenceState();
          });
        })
      .on(RealtimeListenTypes.presence, ChannelFilter(event: 'join'), 
        (payload, [ref]) {
          setState(() {
            presenceState = channel.presenceState();
          });
        })
      .on(RealtimeListenTypes.presence, ChannelFilter(event: 'leave'), 
        (payload, [ref]) {
          setState(() {
            presenceState = channel.presenceState();
          });
        })
      .subscribe(
        (status, [ref]) async {
          if (status == 'SUBSCRIBED') {
            // Track presence with our own user data
            await channel.track({
              'user_id': myUserId,
              'name': 'User ${myUserId.substring(5, 9)}',
              'online_at': DateTime.now().toIso8601String(),
            });
          }
        }
      );
  }
  
  @override
  void dispose() {
    channel.unsubscribe();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Online Users'),
      ),
      body: ListView(
        children: [
          for (final entry in presenceState.entries)
            for (final presence in entry.value)
              ListTile(
                leading: CircleAvatar(
                  child: Text(presence['name'].substring(5, 6)),
                ),
                title: Text(presence['name']),
                subtitle: Text('Online since ${DateTime.parse(presence['online_at']).toLocal().toString()}'),
                trailing: presence['user_id'] == myUserId
                    ? Chip(label: Text('You'))
                    : null,
              ),
        ],
      ),
    );
  }
}
```

## Advanced Usage

### Custom User Status

You can extend Presence to include custom user status information:

```dart
await channel.track({
  'user_id': myUserId,
  'name': userName,
  'online_at': DateTime.now().toIso8601String(),
  'status': 'away', // or 'active', 'busy', etc.
  'activity': 'viewing document 123',
});
```

### Handling User Activity

You can update a user's presence information to reflect their current activity:

```dart
void updateUserActivity(String documentId) {
  channel.track({
    'user_id': myUserId,
    'name': userName,
    'online_at': DateTime.now().toIso8601String(),
    'status': 'active',
    'activity': 'editing document $documentId',
    'last_activity_at': DateTime.now().toIso8601String(),
  });
}
```

### Tracking Cursor Position

For collaborative editing applications, you can track and share cursor positions:

```dart
void updateCursorPosition(double x, double y) {
  channel.track({
    'user_id': myUserId,
    'name': userName,
    'cursor_x': x,
    'cursor_y': y,
    'last_update': DateTime.now().toIso8601String(),
  });
}
```

## Performance Considerations

- Presence data should be kept small to minimize network overhead
- Consider debouncing updates for high-frequency changes (like cursor movement)
- For very large user counts, consider using pagination or filtering
