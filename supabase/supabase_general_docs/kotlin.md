# Using Supabase with Android Kotlin

This guide will walk you through creating a Supabase project, adding sample data to your database, and querying the data from an Android Kotlin app.

## Prerequisites

- Android Studio installed
- Basic knowledge of Android development
- Basic knowledge of Kotlin and Jetpack Compose

## Step 1: Create a Supabase Project

1. Go to [database.new](https://database.new/) and create a new Supabase project.
2. When your project is up and running, go to the SQL Editor and run the following snippet to create a table with sample data:

```sql
-- Create the table
CREATE TABLE instruments (
  id bigint primary key generated always as identity,
  name text not null
);

-- Insert some sample data into the table
INSERT INTO instruments (name)
VALUES
  ('violin'),
  ('viola'),
  ('cello');

-- Enable Row Level Security
ALTER TABLE instruments ENABLE ROW LEVEL SECURITY;

-- Make the data in the table publicly readable with an RLS policy
CREATE POLICY "public can read instruments"
ON public.instruments
FOR SELECT TO anon
USING (true);
```

## Step 2: Create an Android App

Open Android Studio and create a new Android project with Kotlin and Compose support.

## Step 3: Install the Dependencies

Open your `build.gradle.kts` (app) file and add the serialization plugin, Ktor client, and Supabase client:

```kotlin
plugins {
    // Existing plugins
    id("org.jetbrains.kotlin.android")
    kotlin("plugin.serialization") version "$kotlin_version"
}

dependencies {
    // Existing dependencies
    implementation(platform("io.github.jan-tennert.supabase:bom:$supabase_version"))
    implementation("io.github.jan-tennert.supabase:postgrest-kt")
    implementation("io.ktor:ktor-client-android:$ktor_version")
}
```

> **Note**: Replace `$kotlin_version` with your project's Kotlin version, `$supabase_version` with the [latest supabase-kt version](https://github.com/supabase-community/supabase-kt/releases), and `$ktor_version` with the [latest Ktor version](https://ktor.io/docs/welcome.html).

## Step 4: Add Internet Access Permission

Add the internet permission to your `AndroidManifest.xml` file under the `manifest` tag and outside the `application` tag:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

## Step 5: Initialize the Supabase Client

Create a Supabase client in your `MainActivity.kt` file just below the imports:

```kotlin
val supabase = createSupabaseClient(
    supabaseUrl = "YOUR_SUPABASE_URL",
    supabaseKey = "YOUR_SUPABASE_ANON_KEY"
) {
    install(Postgrest)
}
```

> **Important**: Replace `YOUR_SUPABASE_URL` and `YOUR_SUPABASE_ANON_KEY` with your actual Supabase project URL and anon key from your project dashboard.

## Step 6: Create a Data Model

Create a serializable data class to represent the data from the database:

```kotlin
@Serializable
data class Instrument(
    val id: Int,
    val name: String,
)
```

## Step 7: Query and Display Data

Use `LaunchedEffect` to fetch data from the database and display it in a `LazyColumn`:

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            YourAppTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    InstrumentsList()
                }
            }
        }
    }
}

@Composable
fun InstrumentsList() {
    var instruments by remember { mutableStateOf<List<Instrument>>(listOf()) }
    
    LaunchedEffect(Unit) {
        withContext(Dispatchers.IO) {
            instruments = supabase.from("instruments")
                           .select().decodeList<Instrument>()
        }
    }
    
    LazyColumn {
        items(
            instruments,
            key = { instrument -> instrument.id },
        ) { instrument ->
            Text(
                instrument.name,
                modifier = Modifier.padding(8.dp),
            )
        }
    }
}
```

> **Note**: For production applications, consider using a `ViewModel` to separate UI and data fetching logic.

## Step 8: Run the App

Run the app on an emulator or a physical device by clicking the "Run app" button in Android Studio.

You should see a simple list showing the instruments from your Supabase database.

## Complete Imports

Here's a reference for the imports you'll need:

```kotlin
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import io.github.jan.supabase.createSupabaseClient
import io.github.jan.supabase.postgrest.Postgrest
import io.github.jan.supabase.postgrest.from
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import kotlinx.serialization.Serializable
```

## Next Steps

- Add functionality to create, update, and delete instruments
- Implement user authentication using Supabase Auth
- Add error handling and loading states
- Separate data fetching logic into a Repository or ViewModel

## Resources

- [supabase-kt GitHub Repository](https://github.com/supabase-community/supabase-kt)
- [Supabase Documentation](https://supabase.com/docs)
- [Android Kotlin Documentation](https://developer.android.com/kotlin)
- [Jetpack Compose Documentation](https://developer.android.com/jetpack/compose)
