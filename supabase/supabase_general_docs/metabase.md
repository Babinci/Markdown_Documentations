# Connecting Supabase to Metabase

[Metabase](https://www.metabase.com/) is a popular open-source data visualization and business intelligence tool. This guide shows how to connect your Supabase Postgres database to Metabase for data exploration and visualization.

## Prerequisites

- A Supabase project
- Metabase (either cloud account or self-hosted)

## Setup Instructions

### 1. Get Metabase

Choose one of these options:

#### Option A: Create a Metabase Cloud Account

Create a [Metabase Cloud account](https://store.metabase.com/checkout) if you prefer a hosted solution.

#### Option B: Deploy Locally with Docker

If you prefer to self-host, you can deploy with Docker:

```bash
# Pull the latest Metabase image
docker pull metabase/metabase:latest

# Run Metabase on port 3000
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

After deployment, access the setup wizard at: [`http://localhost:3000/setup`](http://localhost:3000/setup)

### 2. Connect to Supabase Postgres Database

1. Find your database connection information:
   - Navigate to your project dashboard and click [Settings > Database](https://supabase.com/dashboard/project/_?showConnect=true)
   - View the connection parameters under "Session pooler"

2. Enter your database credentials in Metabase:
   - Database Type: PostgreSQL
   - Name: A descriptive name (e.g., "Supabase Production")
   - Host: Your database host (from connection string)
   - Port: Your database port (usually 6543 for Supavisor)
   - Database name: Your database name (from connection string)
   - Username: Your database username (from connection string)
   - Password: Your database password (from connection string)

   ![Metabase Postgres Server Configuration](https://supabase.com/docs/img/guides/database/connecting-to-postgres/metabase/add-pg-server.png)

#### Connection Notice

If you're in an [IPv6 environment](https://supabase.com/docs/guides/platform/ipv4-address#checking-your-network-ipv6-support) or have the [IPv4 Add-On](https://supabase.com/docs/guides/platform/ipv4-address#understanding-ip-addresses), you can use the direct connection string instead of Supavisor in Session mode.

### 3. Explore Your Data

Once connected, you can:
- Create custom dashboards
- Build visualizations
- Set up automated reports
- Perform SQL queries directly against your Supabase database

![Exploring data in Metabase](https://supabase.com/docs/img/guides/database/connecting-to-postgres/metabase/explore.png)

## Troubleshooting

If you encounter connection issues:

1. **Check network restrictions**: Ensure your Metabase instance's IP address is allowed in your [Supabase network restrictions](https://supabase.com/dashboard/project/_/settings/network)
2. **Verify credentials**: Double-check your connection string details
3. **Connection timeout**: If using Supavisor, try the direct connection string instead
4. **SSL settings**: Ensure SSL is enabled in your Metabase connection settings
