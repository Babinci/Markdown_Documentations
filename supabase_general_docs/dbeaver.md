# Connecting with DBeaver

If you do not have DBeaver, you can download it from its [website](https://dbeaver.io/download/).

## Connection Steps

### 1. Create a new database connection

Click the "New Database Connection" button or use the menu to create a new connection.

![new database connection](https://supabase.com/docs/img/guides/database/connecting-to-postgres/dbeaver/new_database_connection.png)

### 2. Select PostgreSQL

In the database selection dialog, choose PostgreSQL.

![Selection Menu](https://supabase.com/docs/img/guides/database/connecting-to-postgres/dbeaver/select_postgres.png)

### 3. Get Your Credentials

Inside the Dashboard's [Database Settings](https://supabase.com/dashboard/project/_/settings/database), note your session mode's:
- host
- username

You will also need your database's password. If you forgot it, you can generate a new one in the settings.

If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.

![database credentials](https://supabase.com/docs/img/guides/database/connecting-to-postgres/dbeaver/session_mode.png)

### 4. Fill out credentials

In DBeaver's Main menu, add your host, username, and password.

![filling out form](https://supabase.com/docs/img/guides/database/connecting-to-postgres/dbeaver/filling_credentials.png)

### 5. Download certificate

In the [Database Settings](https://supabase.com/dashboard/project/_/settings/database), download your SSL certificate.

![filling out form](https://supabase.com/docs/img/guides/database/connecting-to-postgres/dbeaver/certificate.png)

### 6. Secure your connection

In DBeaver's SSL tab, add your SSL certificate.

![filling out form](https://supabase.com/docs/img/guides/database/connecting-to-postgres/dbeaver/ssl_tab.png)

### 7. Connect

Test your connection and then click finish. You should now be able to interact with your database with DBeaver.

![connected dashboard](https://supabase.com/docs/img/guides/database/connecting-to-postgres/dbeaver/finished.png)
