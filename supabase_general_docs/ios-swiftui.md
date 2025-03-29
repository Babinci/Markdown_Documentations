# Use Supabase with iOS and SwiftUI

Learn how to create a Supabase project, add some sample data to your database, and query the data from an iOS app.

## 1. Create a Supabase project

Go to [database.new](https://database.new/) and create a new Supabase project.

When your project is up and running, go to the [Table Editor](https://supabase.com/dashboard/project/_/editor), create a new table and insert some data.

Alternatively, you can run the following snippet in your project's [SQL Editor](https://supabase.com/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.

```sql
-- Create the table
CREATE TABLE instruments (
  id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name text NOT NULL
);

-- Insert some sample data into the table
INSERT INTO instruments (name)
VALUES
  ('violin'),
  ('viola'),
  ('cello');

ALTER TABLE instruments ENABLE ROW LEVEL SECURITY;
```

Make the data in your table publicly readable by adding an RLS policy:

```sql
CREATE POLICY "public can read instruments"
ON public.instruments
FOR SELECT TO anon
USING (true);
```

## 2. Create an iOS SwiftUI app with Xcode

Open Xcode > New Project > iOS > App. You can skip this step if you already have a working app.

## 3. Install the Supabase client library

Install Supabase package dependency using Xcode by following Apple's [tutorial](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app).

Make sure to add `Supabase` product package as dependency to the application.

## 4. Initialize the Supabase client

Create a new `Supabase.swift` file add a new Supabase instance using your project URL and public API (anon) key:

```swift
import Supabase

let supabase = SupabaseClient(
  supabaseURL: URL(string: "YOUR_SUPABASE_URL")!,
  supabaseKey: "YOUR_SUPABASE_ANON_KEY"
)
```

## 5. Create a data model for instruments

Create a decodable struct to deserialize the data from the database.

Add the following code to a new file named `Instrument.swift`.

```swift
struct Instrument: Decodable, Identifiable {
  let id: Int
  let name: String
}
```

## 6. Query data from the app

Use a `task` to fetch the data from the database and display it using a `List`.

Replace the default `ContentView` with the following code.

```swift
struct ContentView: View {
  @State var instruments: [Instrument] = []
  
  var body: some View {
    List(instruments) { instrument in
      Text(instrument.name)
    }
    .overlay {
      if instruments.isEmpty {
        ProgressView()
      }
    }
    .task {
      do {
        instruments = try await supabase.from("instruments").select().execute().value
      } catch {
        dump(error)
      }
    }
  }
}
```

## 7. Start the app

Run the app on a simulator or a physical device by hitting `Cmd + R` on Xcode.
