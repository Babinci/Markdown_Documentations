# Connect to your database

This guide explains how to connect to your Supabase Postgres database from different environments.

## Quick summary

How you connect to your database depends on where you're connecting from:

- For frontend applications, use the [Data API](#data-apis-and-client-libraries)
- For Postgres clients, use a connection string
  - For single sessions (for example, database GUIs) or Postgres native commands (for example, using client applications like [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html) or specifying connections for [replication](https://supabase.com/docs/guides/database/postgres/setup-replication-external)) use the [direct connection string](#direct-connection) if your environment supports IPv6
  - For persistent clients, and support for both IPv4 and IPv6, use [Supavisor session mode](#supavisor-session-mode)
  - For temporary clients (for example, serverless or edge functions) use [Supavisor transaction mode](#supavisor-transaction-mode)

## Quickstarts

- [Prisma](https://supabase.com/docs/guides/database/prisma)
- [Drizzle](https://supabase.com/docs/guides/database/drizzle)
- [Postgres.js](https://supabase.com/docs/guides/database/postgres-js)
- [pgAdmin](https://supabase.com/docs/guides/database/pgadmin)
- [PSQL](https://supabase.com/docs/guides/database/psql)
- [DBeaver](https://supabase.com/docs/guides/database/dbeaver)
- [Metabase](https://supabase.com/docs/guides/database/metabase)
- [Beekeeper Studio](https://supabase.com/docs/guides/database/beekeeper-studio)

## Data APIs and client libraries

The Data APIs allow you to interact with your database using REST or GraphQL requests. You can use these APIs to fetch and insert data from the frontend, as long as you have [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) enabled.

- [REST](https://supabase.com/docs/guides/api)
- [GraphQL](https://supabase.com/docs/guides/graphql/api)

For convenience, you can also use the Supabase client libraries, which wrap the Data APIs with a developer-friendly interface and automatically handle authentication:

- [JavaScript](https://supabase.com/docs/reference/javascript)
- [Flutter](https://supabase.com/docs/reference/dart)
- [Swift](https://supabase.com/docs/reference/swift)
- [Python](https://supabase.com/docs/reference/python)
- [C#](https://supabase.com/docs/reference/csharp)
- [Kotlin](https://supabase.com/docs/reference/kotlin)

## Direct connection

The direct connection string connects directly to your Postgres instance. It is ideal for persistent servers, such as virtual machines (VMs) and long-lasting containers. Examples include AWS EC2 machines, Fly.io VMs, and DigitalOcean Droplets.

Direct connections use IPv6 by default. If your environment doesn't support IPv6, use [Supavisor session mode](#supavisor-session-mode) or get the [IPv4 add-on](https://supabase.com/docs/guides/platform/ipv4-address).

The connection string looks like this:

```
postgresql://postgres:[YOUR-PASSWORD]@db.apbkobhfnmcqqzqeeqss.supabase.co:5432/postgres
```

Get your project's direct string from the [Database Settings](https://supabase.com/dashboard/project/_/settings/database) page:

1. Go to the `Settings` section.
2. Click `Database`.
3. Under `Connection string`, make sure `Display connection pooler` is unchecked. Copy the URI.

## Shared pooler

Every Supabase project includes a free, shared connection pooler. This is ideal for persistent servers when IPv6 is not supported.

### Supavisor session mode

The session mode connection string connects to your Postgres instance via a proxy.

The connection string looks like this:

```
postgres://postgres.apbkobhfnmcqqzqeeqss:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

Get your project's session mode string from the [Database Settings](https://supabase.com/dashboard/project/_/settings/database) page:

1. Go to the `Settings` section.
2. Click `Database`.
3. Under `Connection string`, make sure `Display connection pooler` is checked and `Session mode` is selected. Copy the URI.

### Supavisor transaction mode

The transaction mode connection string connects to your Postgres instance via a proxy which serves as a connection pooler. This is ideal for serverless or edge functions, which require many transient connections.

Transaction mode does not support [prepared statements](https://postgresql.org/docs/current/sql-prepare.html). To avoid errors, [turn off prepared statements](https://github.com/orgs/supabase/discussions/28239) for your connection library.

The connection string looks like this:

```
postgres://postgres.apbkobhfnmcqqzqeeqss:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres
```

Get your project's transaction mode string from the [Database Settings](https://supabase.com/dashboard/project/_/settings/database) page:

1. Go to the `Settings` section.
2. Click `Database`.
3. Under `Connection string`, make sure `Display connection pooler` is checked and `Transaction mode` is selected. Copy the URI.

## Dedicated pooler

For paying customers, we provision a Dedicated Pooler ([PgBouncer](https://www.pgbouncer.org/)) that's co-located with your Postgres database. This will require you to connect with IPv6 or, if that's not an option, you can use the [IPv4 add-on](https://supabase.com/docs/guides/platform/ipv4-address).

The Dedicated Pooler ensures best performance and latency, while using up more of your project's compute resources. If your network supports IPv6 or you have the IPv4 add-on, we encourage you to use the Dedicated Pooler over the Shared Pooler.

PgBouncer always runs in Transaction mode and the current version does not support prepared statement (will be added in a few weeks).

## More about connection pooling

Connection pooling improves database performance by reusing existing connections between queries. This reduces the overhead of establishing connections and improves scalability.

You can use an application-side pooler or a server-side pooler (Supabase automatically provides one called Supavisor), depending on whether your backend is persistent or serverless.

### Application-side poolers

Application-side poolers are built into connection libraries and API servers, such as Prisma, SQLAlchemy, and PostgREST. They maintain several active connections with Postgres or a server-side pooler, reducing the overhead of establishing connections between queries. When deploying to static architecture, such as long-standing containers or VMs, application-side poolers are satisfactory on their own.

### Serverside poolers

Postgres connections are like a WebSocket. Once established, they are preserved until the client (application server) disconnects. A server might only make a single 10 ms query, but needlessly reserve its database connection for seconds or longer.

Serverside-poolers, such as Supabase's [Supavisor](https://github.com/supabase/supavisor) in transaction mode, sit between clients and the database and can be thought of as load balancers for Postgres connections.

They maintain hot connections with the database and intelligently share them with clients only when needed, maximizing the amount of queries a single connection can service. They're best used to manage queries from auto-scaling systems, such as edge and serverless functions.

## Connecting with SSL

You should connect to your database using SSL wherever possible, to prevent snooping and man-in-the-middle attacks.

You can obtain your connection info and Server root certificate from your application's dashboard in the Database Settings section.

## Resources

- [Connection management](https://supabase.com/docs/guides/database/connection-management)
