# Migrating from Firebase Firestore to Supabase Database

This guide explains how to migrate your data from a Firebase Firestore database to a Supabase PostgreSQL database using community-provided migration tools.

## Overview

The migration process involves:
1. Extracting data from Firestore collections into JSON files
2. Optionally transforming the data structure with custom hooks
3. Importing the JSON data into Supabase PostgreSQL tables

During this process, Firestore collections are "flattened" and converted to PostgreSQL tables with basic column types: `text`, `numeric`, `boolean`, or `jsonb`. For complex data structures, you can write custom hooks to split nested data into multiple related tables.

## Setting Up the Migration Tool

1. Clone the migration repository:
   ```bash
   git clone https://github.com/supabase-community/firebase-to-supabase.git
   ```

2. Navigate to the Firestore directory:
   ```bash
   cd firebase-to-supabase/firestore
   ```

3. Create a Supabase connection configuration:
   Create a file named `supabase-service.json` with the following content:
   ```json
   {
     "host": "database.server.com",
     "password": "secretpassword",
     "user": "postgres",
     "database": "postgres",
     "port": 5432
   }
   ```

4. Configure with your Supabase credentials:
   - Go to your project's [Database settings](https://supabase.com/dashboard/project/_/settings/database)
   - Under **Connection parameters**, enable **Use connection pooling** and set the mode to **Session**
   - Replace the `host` and `user` fields in your `supabase-service.json` with the values shown
   - Update the `password` with the password you used when you created your Supabase project

## Generating a Firebase Private Key

1. Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project

2. Access your project settings:
   - Click the gear icon next to **Project Overview** in the sidebar
   - Select **Project Settings**

3. Generate a service account key:
   - Click the **Service Accounts** tab
   - Select **Firebase Admin SDK**
   - Click **Generate new private key**
   - Save the downloaded file as `firebase-service.json` in your project directory

## Command Line Operations

### Listing All Firestore Collections

To view all collections in your Firestore database:

```bash
node collections.js
```

### Exporting a Firestore Collection to JSON

To extract a collection to a JSON file:

```bash
node firestore2json.js <collectionName> [<batchSize>] [<limit>]
```

Parameters:
- `<collectionName>`: Name of the Firestore collection to export
- `<batchSize>`: (Optional) Number of documents to process in one batch (default: 1000)
- `<limit>`: (Optional) Maximum number of documents to export (default: 0, meaning no limit)

The output file will be named `<collectionName>.json`.

### Importing JSON Data to Supabase (PostgreSQL)

After exporting your collection to JSON, import it to Supabase:

```bash
node json2supabase.js <path_to_json_file> [<primary_key_strategy>] [<primary_key_name>]
```

Parameters:
- `<path_to_json_file>`: Path to the JSON file (e.g., `./my_collection.json`)
- `<primary_key_strategy>`: (Optional) Strategy for creating primary keys:
  - `none` (default): No primary key is added
  - `smallserial`: Creates a key using `(id SMALLSERIAL PRIMARY KEY)` (2-byte autoincrementing integer)
  - `serial`: Creates a key using `(id SERIAL PRIMARY KEY)` (4-byte autoincrementing integer)
  - `bigserial`: Creates a key using `(id BIGSERIAL PRIMARY KEY)` (8-byte autoincrementing integer)
  - `uuid`: Creates a key using `(id UUID PRIMARY KEY DEFAULT gen_random_uuid())` (random UUID)
  - `firestore_id`: Creates a key using `(id TEXT PRIMARY KEY)` (uses existing `firestore_id` as key)
- `<primary_key_name>`: (Optional) Name for the primary key column (default: "id")

## Using Custom Hooks for Data Transformation

Custom hooks allow you to transform your data during the export process. This is particularly useful for:
- Customizing or modifying fields
- Calculating derived data
- Flattening nested documents into related tables

### Creating a Custom Hook

1. Create a JavaScript file named after your collection. For example, if your collection is named `users`, create a file named `users.js`.

2. The basic format of a hook file:
   ```javascript
   module.exports = (collectionName, doc, recordCounters, writeRecord) => {
     // Modify the document here
     return doc;
   }
   ```

   Parameters:
   - `collectionName`: Name of the collection being processed
   - `doc`: Current document (JSON object) being processed
   - `recordCounters`: Object tracking processed records count
   - `writeRecord`: Function for writing data to other JSON files (for creating related tables)

### Hook Examples

#### Adding a Unique Numeric Key

```javascript
module.exports = (collectionName, doc, recordCounters, writeRecord) => {
  doc.unique_key = recordCounters[collectionName] + 1;
  return doc;
}
```

#### Adding a Timestamp

```javascript
module.exports = (collectionName, doc, recordCounters, writeRecord) => {
  doc.dump_time = new Date().toISOString();
  return doc;
}
```

#### Flattening Nested Arrays into Separate Tables

For a `users` collection with nested weapon arrays:

```javascript
module.exports = (collectionName, doc, recordCounters, writeRecord) => {
  // Create related records for each weapon
  for (let i = 0; i < doc.weapons.length; i++) {
    const weapon = {
      uid: doc.uid,
      weapon: doc.weapons[i],
    };
    writeRecord('weapons', weapon, recordCounters);
  }
  
  // Remove the weapons array from the main document
  delete doc.weapons;
  
  return doc;
}
```

This will create two tables: one for users and one for weapons, with a relationship based on the `uid` field.

## Best Practices

1. **Start small**: Test with a single small collection before migrating your entire database.

2. **Plan your data model**: Consider how to best represent your Firestore collections as PostgreSQL tables.

3. **Write custom hooks**: For complex data structures, create custom hooks to properly normalize your data.

4. **Verify data integrity**: After migration, verify that all your data was correctly transferred.

5. **Update your application code**: Remember to update your client-side code to use Supabase APIs.

## Additional Resources

- [Supabase vs Firebase comparison](https://supabase.com/alternatives/supabase-vs-firebase)
- [Firebase Storage Migration guide](https://supabase.com/docs/guides/migrations/firebase-storage)
- [Firebase Auth Migration guide](https://supabase.com/docs/guides/migrations/firebase-auth)

## Enterprise Support

For larger migrations or if you need additional assistance, [contact the Supabase Enterprise team](https://forms.supabase.com/enterprise) for professional migration support.
