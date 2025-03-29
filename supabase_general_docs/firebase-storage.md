# Migrating from Firebase Storage to Supabase Storage

This guide explains how to migrate your files from Firebase Storage to Supabase Storage using the community-provided migration tools.

## Overview

The migration process involves two main steps:
1. Downloading files from Firebase Storage to your local filesystem
2. Uploading these files from your local filesystem to Supabase Storage

Supabase provides tools to simplify this migration process, making it straightforward to move your files between services.

## Setting Up the Migration Tool

1. Clone the migration repository:
   ```bash
   git clone https://github.com/supabase-community/firebase-to-supabase.git
   ```

2. Navigate to the storage directory and prepare the Supabase configuration:
   ```bash
   cd firebase-to-supabase/storage
   ```

3. Rename the sample configuration file:
   ```bash
   cp supabase-keys-sample.js supabase-keys.js
   ```

4. Configure your Supabase credentials:
   - Go to your Supabase project's [API settings](https://supabase.com/dashboard/project/_/settings/api)
   - Copy the **Project URL** and update the `SUPABASE_URL` value in `supabase-keys.js`
   - Copy the **service_role** key and update the `SUPABASE_KEY` value in `supabase-keys.js`

## Generating a Firebase Private Key

1. Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project

2. Access your project settings:
   - Click the gear icon next to **Project Overview** in the sidebar
   - Select **Project Settings**

3. Generate a service account key:
   - Click **Service Accounts** tab
   - Select **Firebase Admin SDK**
   - Click **Generate new private key**
   - Save the downloaded file as `firebase-service.json` in your project directory

## Command Line Options

### Downloading from Firebase Storage

Use the download script to fetch files from Firebase Storage:

```bash
node download.js <prefix> [<folder>] [<batchSize>] [<limit>] [<token>]
```

Parameters:
- `<prefix>`: The prefix of files to download (use `""` for the root bucket)
- `<folder>`: (Optional) Local subfolder for downloaded files (default: `downloads`)
- `<batchSize>`: (Optional) Number of files to process in one batch (default: 100)
- `<limit>`: (Optional) Maximum number of files to process (use `0` for no limit)
- `<token>`: (Optional) Page token to continue from a previous batch

For large migrations, you can process files in batches by using the token displayed at the end of each batch to continue where you left off.

### Uploading to Supabase Storage

After downloading the files, use the upload script to move them to Supabase:

```bash
node upload.js <prefix> <folder> <bucket>
```

Parameters:
- `<prefix>`: File prefix filter (use `""` to upload all files)
- `<folder>`: Local folder containing the downloaded files (default: `downloads`)
- `<bucket>`: Supabase Storage bucket name to upload to

If the specified bucket doesn't exist, it will be created as a non-public bucket. You'll need to configure appropriate permissions in the [Supabase Dashboard](https://supabase.com/dashboard/project/_/storage/buckets) after migration.

## Best Practices

1. **Run a test migration first**: Try with a small subset of files before migrating your entire storage.

2. **Preserve folder structure**: The migration tools maintain your original folder hierarchy, but verify this with a test run.

3. **Verify permissions**: After migration, ensure bucket permissions match your security requirements.

4. **Update your application code**: Remember to update your client-side code to use Supabase Storage APIs.

5. **Batch processing**: For large migrations (thousands of files), process in smaller batches to avoid timeouts or memory issues.

6. **Maintain an audit log**: Keep track of which files have been successfully migrated.

## Handling Errors and Resuming Transfers

If the migration process is interrupted or fails:

1. Note the last processed token displayed in the console
2. Re-run the download command with the same parameters, adding the token as the last parameter
3. Continue the upload process with the files that were successfully downloaded

This allows you to resume the migration from where it left off rather than starting over.

## Post-Migration Steps

1. **Verify file integrity**: Spot-check files to ensure they were migrated correctly.

2. **Configure bucket policies**: Set up appropriate access controls for your Supabase Storage buckets.

3. **Update application references**: Update all Firebase Storage references in your codebase to use Supabase Storage.

4. **Test your application**: Thoroughly test your application with the migrated files.

5. **Monitor storage usage**: Check your Supabase Storage usage to ensure everything is working as expected.

## Additional Resources

- [Supabase vs Firebase comparison](https://supabase.com/alternatives/supabase-vs-firebase)
- [Firestore Data Migration guide](https://supabase.com/docs/guides/migrations/firestore-data)
- [Firebase Auth Migration guide](https://supabase.com/docs/guides/migrations/firebase-auth)

## Enterprise Support

For larger migrations or if you need additional assistance, [contact the Supabase Enterprise team](https://forms.supabase.com/enterprise) for professional migration support.
