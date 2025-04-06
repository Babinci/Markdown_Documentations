# Self-Hosting with Docker

This guide explains how to configure and deploy Supabase with Docker, which is the easiest way to get started with self-hosted Supabase.

## Before You Begin

You need the following installed on your system:
- [Git](https://git-scm.com/downloads) 
- Docker ([Windows](https://docs.docker.com/desktop/install/windows-install/), [macOS](https://docs.docker.com/desktop/install/mac-install/), or [Linux](https://docs.docker.com/desktop/install/linux-install/))

## Installing and Running Supabase

Follow these steps to start Supabase on your machine:

```bash
# Get the code
git clone --depth 1 https://github.com/supabase/supabase

# Go to the docker folder
cd supabase/docker

# Copy the environment variables
cp .env.example .env

# Pull the latest images
docker compose pull

# Start the services (in detached mode)
docker compose up -d
```

If you are using rootless Docker, edit `.env` and set `DOCKER_SOCKET_LOCATION` to your Docker socket location (e.g., `/run/user/1000/docker.sock`).

After all services have started, you can view them running in the background:

```bash
docker compose ps
```

All services should have a status of `running (healthy)`. If any service has a status of `created` but not `running`, try starting that service manually with `docker compose start <service-name>`.

> **Important**: Your app is now running with default credentials. Be sure to [secure your services](#securing-your-services) as soon as possible.

## Accessing Your Services

### Accessing Supabase Studio

You can access Supabase Studio through the API gateway on port `8000`:
- URL: `http://<your-ip>:8000` or [localhost:8000](http://localhost:8000/) if running Docker locally
- Default credentials:
  - Username: `supabase`
  - Password: `this_password_is_insecure_and_should_be_updated`

Change these credentials as soon as possible using the [dashboard authentication](#dashboard-authentication) instructions.

### Accessing the APIs

Each API is available through the same API gateway:

- REST: `http://<your-ip>:8000/rest/v1/`
- Auth: `http://<your-ip>:8000/auth/v1/`
- Storage: `http://<your-ip>:8000/storage/v1/`
- Realtime: `http://<your-ip>:8000/realtime/v1/`

### Accessing Your Edge Functions

Edge Functions are stored in `volumes/functions`. The default setup has a `hello` function that you can invoke at `http://<your-ip>:8000/functions/v1/hello`.

To add new functions, create files in `volumes/functions/<FUNCTION_NAME>/index.ts`. Restart the `functions` service to apply changes:

```bash
docker compose restart functions --no-deps
```

### Accessing Postgres

By default, Supabase uses the [Supavisor](https://supabase.github.io/supavisor/) connection pooler to manage database connections.

Connect to the Postgres database using:

1. For session-based connections (equivalent to direct Postgres connections):
   ```bash
   psql 'postgres://postgres.your-tenant-id:your-super-secret-and-long-postgres-password@localhost:5432/postgres'
   ```

2. For pooled transactional connections:
   ```bash
   psql 'postgres://postgres.your-tenant-id:your-super-secret-and-long-postgres-password@localhost:6543/postgres'
   ```

The default tenant ID is `your-tenant-id`, and the default password is `your-super-secret-and-long-postgres-password`. Change these as soon as possible using the [update secrets](#update-secrets) instructions.

By default, the database is not accessible from outside the local machine, but the pooler is. You can [change this](#exposing-your-postgres-database) by updating the `docker-compose.yml` file.

## Updating Your Services

For security reasons, service versions are "pinned" in the docker-compose file (updated ~monthly). To update any service immediately:

1. Update the version number in the docker-compose file
2. Run `docker compose pull`
3. Restart the services to apply changes

You should update services frequently to get the latest features, bug fixes, and security patches.

**Example: Updating Supabase Studio**
1. Visit the [supabase/studio](https://hub.docker.com/r/supabase/studio/tags) image on Docker Hub
2. Find the latest version (tag) number (e.g., `20241029-46e1e40`)
3. Update the `image` field in `docker-compose.yml` to the new version
4. Run `docker compose pull` and then `docker compose up -d` to restart with the new version

## Securing Your Services

Never deploy your Supabase setup using the default credentials. Follow these steps to secure your installation.

### Generate API Keys

1. Generate a secure JWT secret (40-character random string)
2. Use the JWT secret to generate new `anon` and `service` API keys
3. Replace the values in `./docker/.env`:
   - `ANON_KEY` - replace with an `anon` key
   - `SERVICE_ROLE_KEY` - replace with a `service` key
   - `JWT_SECRET` - replace with your JWT secret

### Update Secrets

Update the `./docker/.env` file with your own secrets, including:

- `POSTGRES_PASSWORD`: the password for the `postgres` role
- `JWT_SECRET`: used by PostgREST and GoTrue
- `SITE_URL`: the base URL of your site
- `SMTP_*`: mail server credentials
- `POOLER_TENANT_ID`: the tenant-id for Supavisor pooler connection string

### Dashboard Authentication

Update the following values in `./docker/.env`:

- `DASHBOARD_USERNAME`: The username for the Dashboard
- `DASHBOARD_PASSWORD`: The password for the Dashboard

For multiple users, add credentials in `./docker/volumes/api/kong.yml`:

```yaml
basicauth_credentials:
  - consumer: DASHBOARD
    username: user_one
    password: password_one
  - consumer: DASHBOARD
    username: user_two
    password: password_two
```

To enable all dashboard features outside of `localhost`, update:

- `SUPABASE_PUBLIC_URL`: The URL or IP used to access the dashboard

### Restarting All Services

Apply configuration changes by restarting all services:

```bash
# Stop and remove the containers
docker compose down

# Recreate and start the containers
docker compose up -d
```

Be aware that this will cause temporary downtime.

## Managing Your System

### Stopping All Services

```bash
docker compose stop
```

### Uninstalling

```bash
# Stop docker and remove volumes:
docker compose down -v

# Remove Postgres data:
rm -rf volumes/db/data/
```

Warning: This will destroy all data in the database and storage volumes!

## Managing Your Secrets

For production deployments, we strongly recommend using a secrets manager instead of plain text files. Options include:

- [Doppler](https://www.doppler.com/)
- [Infisical](https://infisical.com/)
- [Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview) by Azure
- [Secrets Manager](https://aws.amazon.com/secrets-manager/) by AWS
- [Secrets Manager](https://cloud.google.com/secret-manager) by GCP
- [Vault](https://www.hashicorp.com/products/vault) by HashiCorp

## Advanced Configuration

### Architecture

Supabase combines several open-source tools, each chosen for enterprise readiness:

- [Kong](https://github.com/Kong/kong) - Cloud-native API gateway
- [GoTrue](https://github.com/supabase/gotrue) - JWT-based API for user management
- [PostgREST](http://postgrest.org/) - RESTful API server for PostgreSQL
- [Realtime](https://github.com/supabase/realtime) - WebSocket server for PostgreSQL changes
- [Storage](https://github.com/supabase/storage-api) - RESTful interface for S3 file management
- [postgres-meta](https://github.com/supabase/postgres-meta) - RESTful API for PostgreSQL management
- [PostgreSQL](https://www.postgresql.org/) - Reliable, feature-rich database system
- [Supavisor](https://github.com/supabase/supavisor) - Scalable connection pooler for PostgreSQL

### Common Configuration Options

#### Configuring an Email Server

Configure a production-ready SMTP server by setting:

```bash
SMTP_ADMIN_EMAIL=
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=
SMTP_SENDER_NAME=
```

AWS SES is recommended for its reliability and low cost.

#### Configuring S3 Storage

Configure Storage to use S3 instead of local files:

```yaml
storage:
  environment:
    STORAGE_BACKEND: s3
    GLOBAL_S3_BUCKET: name-of-your-s3-bucket
    REGION: region-of-your-s3-bucket
```

#### Configuring Supabase AI Assistant

Enable AI services by adding an OpenAI API key:

```yaml
studio:
  environment:
    OPENAI_API_KEY: ${OPENAI_API_KEY:-}
```

#### Exposing Your Postgres Database

For direct access to the PostgreSQL database (bypassing Supavisor):

```yaml
# Comment or remove the supavisor section
# supavisor:
#   ports:
# ...

db:
  ports:
    - ${POSTGRES_PORT}:${POSTGRES_PORT}
```

Note: This is less secure, so ensure you have proper firewall protection.

## Additional Resources

For more specific configuration options, refer to the documentation for each component:
- [Postgres](https://hub.docker.com/_/postgres/)
- [PostgREST](https://postgrest.org/en/stable/configuration.html)
- [Realtime](https://github.com/supabase/realtime#server)
- [Auth](https://github.com/supabase/auth)
- [Storage](https://github.com/supabase/storage-api)
- [Kong](https://docs.konghq.com/gateway/latest/install/docker/)
- [Supavisor](https://supabase.github.io/supavisor/development/docs/)