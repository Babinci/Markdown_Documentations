# Migrate from Render to Supabase

This guide demonstrates how to migrate your Render Postgres database to Supabase to take advantage of Postgres extensions, row-level security, and other Supabase features.

## Overview

Render is a popular web hosting service that offers managed Postgres databases. While Render excels at providing a great developer experience for deploying applications directly from GitHub or GitLab, Supabase offers a more comprehensive solution for working with Postgres databases.

Supabase provides:
- A Postgres database with 40+ extensions
- Built-in authentication and authorization
- Instant APIs
- Edge functions
- Realtime subscriptions
- Storage
- Row-level security

## Migration Process

### 1. Retrieve Your Render Database Credentials

1. Log in to your [Render account](https://render.com/) and select the project you want to migrate.
2. Click **Dashboard** in the menu and click on your **Postgres** database.
3. Scroll down in the **Info** tab.
4. Click on **PSQL Command** and copy the content that appears after `PSQL_COMMAND=`.

![Copying PSQL command from Render dashboard](https://supabase.com/docs/img/guides/resources/migrating-to-supabase/render/render_dashboard.png)

Example:
```bash
%env PSQL_COMMAND=PGPASSWORD=RgaMDfTS_password_FTPa7 psql -h dpg-a_server_in.oregon-postgres.render.com -U my_db_pxl0_user my_db_pxl0
```

### 2. Retrieve Your Supabase Connection String

1. If you're new to Supabase, [create a project](https://supabase.com/dashboard).
   - Make a note of your password, you will need this later.
   - If you forget your password, you can [reset it here](https://supabase.com/dashboard/project/_/settings/database).

2. Go to the [Database settings](https://supabase.com/dashboard/project/_/settings/database) for your project in the Supabase Dashboard.

3. Under **Connection string**, make sure **Use connection pooling** is enabled. Copy the URI and replace the password placeholder with your database password.

### 3. Migrate the Database

#### Option A: Using Google Colab (Recommended)

The fastest way to migrate your database is with the Supabase migration tool on [Google Colab](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Migrate_Postgres_Supabase.ipynb).

1. Open [the Colab notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Migrate_Postgres_Supabase.ipynb).

2. Set the environment variables:
   - `PSQL_COMMAND` - The PSQL command from Render
   - `SUPABASE_HOST` - Your Supabase connection string
   - `SUPABASE_PASSWORD` - Your Supabase database password

3. Run the first two steps in the notebook in order:
   - The first step sets the variables
   - The second step installs PSQL and the migration script

4. Run the third step to start the migration. This will take a few minutes depending on your database size.

#### Option B: Using CLI Tools

If you prefer using command-line tools, you can use `pg_dump` and `psql`, which are included in a full Postgres installation.

1. Extract connection details from your Render PSQL command:
   ```bash
   # Example Render command
   PGPASSWORD=RgaMDfTS_password_FTPa7 psql -h dpg-a_server_in.oregon-postgres.render.com -U my_db_pxl0_user my_db_pxl0
   ```

2. Use `pg_dump` to export your database:
   ```bash
   PGPASSWORD=RgaMDfTS_password_FTPa7 pg_dump -h dpg-a_server_in.oregon-postgres.render.com -U my_db_pxl0_user -d my_db_pxl0 -F c -f render_backup.dump
   ```

3. Restore the database to Supabase:
   ```bash
   pg_restore -h db.your-project-ref.supabase.co -U postgres -d postgres -p 5432 render_backup.dump
   ```
   
   You'll be prompted for your Supabase database password.

## Resource Considerations

- **Database Size < 6 GB**: The free tier should be sufficient.
- **Database Size > 6 GB**: We recommend [upgrading to at least a Large compute add-on](https://supabase.com/docs/guides/platform/compute-add-ons) to ensure you have the necessary resources for migration.
- **Database Size < 150 GB**: You can increase the disk size on paid projects by navigating to [Database Settings](https://supabase.com/dashboard/project/_/settings/database).
- **Database Size > 150 GB**: [Contact our support team](https://supabase.com/dashboard/support/new) for assistance in provisioning the required resources.

## Post-Migration Steps

After migrating your database, you should:

1. **Verify Data Integrity**: Check that all your tables, data, and relationships have been correctly migrated.
2. **Set Up Row-Level Security**: Configure RLS policies to secure your database access.
3. **Configure Authentication**: Set up authentication methods for your application.
4. **Update Connection Strings**: Update your application's connection strings to point to your Supabase database.
5. **Test Your Application**: Thoroughly test your application with the new database.

## Troubleshooting

### Common Issues

- **Connection Issues**: If you're having trouble connecting to either database, check that your IP is allowed in the respective database firewall settings.
- **Permission Errors**: Ensure the database user has sufficient permissions to read from or write to the database.
- **Timeouts**: For large databases, the migration might timeout. Consider breaking down the migration into smaller chunks or [contact support](https://supabase.com/dashboard/support/new).

## Enterprise Support

For enterprise migrations or if you need more help migrating your project, [contact us](https://forms.supabase.com/enterprise).
