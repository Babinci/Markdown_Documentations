# Connecting with pgAdmin

## Introduction

[pgAdmin](https://www.pgadmin.org/) is a GUI tool for managing PostgreSQL databases. You can use it to connect to your Supabase database via SSL.

## Connection Steps

### 1. Register a New Server

Register a new PostgreSQL server in pgAdmin.

![Register a new postgres server.](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Fguides%2Fdatabase%2Fconnecting-to-postgres%2Fpgadmin%2Fregister-server-pgAdmin--light.png&w=3840&q=75&dpl=dpl_2DQMEZHm5P9QNZGKAqcszuVSdHSJ)

### 2. Name Your Server

Give your server a descriptive name.

![Name Postgres Server.](https://supabase.com/docs/img/guides/database/connecting-to-postgres/pgadmin/name-pg-server.png)

### 3. Add Connection Information

Add the connection information from your Supabase project:

1. Go to your [Database Settings](https://supabase.com/dashboard/project/_/settings/database) in the Supabase Dashboard
2. Make sure `Use connection pooling` is enabled 
3. Switch the connection mode to `Session`
4. Copy your connection parameters
5. Fill in your Database password that you created when creating your project (It can be reset in Database Settings if needed)

![Add Connection Info.](https://supabase.com/docs/img/guides/database/connecting-to-postgres/pgadmin/add-pg-server-conn-info.png)

### 4. Configure SSL

1. Download your SSL certificate from the [Database Settings](https://supabase.com/dashboard/project/_/settings/database) page in your Supabase Dashboard
2. In pgAdmin, navigate to the Parameters tab
3. Select connection parameter as Root Certificate
4. Navigate to the Root certificate input (it will open a file-picker modal)
5. Select the certificate you downloaded earlier
6. Save the server details

pgAdmin should now be able to connect to your PostgreSQL database via SSL.

![Add Connection Info.](https://supabase.com/docs/img/guides/database/connecting-to-postgres/pgadmin/database-settings-host.png)
