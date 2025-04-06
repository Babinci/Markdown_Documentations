# Use Supabase with RedwoodJS

Learn how to create a Supabase project, add sample data to your database using Prisma migration and seeds, and query the data from a RedwoodJS app.

## Step-by-Step Guide

### 1. Setup Your New Supabase Project

[Create a new project](https://supabase.com/dashboard) in the Supabase Dashboard.

Be sure to make note of the Database Password you used as you will need this later to connect to your database.

![New project for redwoodjs](https://supabase.com/docs/img/guides/getting-started/quickstarts/redwoodjs/new-project.png)

### 2. Gather Database Connection Strings

Go to the [database settings page](https://supabase.com/dashboard/project/_/settings/database). In this quickstart, we are going to connect via the connection pooler. If your network supports IPv6, you can connect to the database directly without using the connection pooler.

We will use the pooler both in `Transaction` and `Session` mode:
- **Transaction mode**: Used for application queries
- **Session mode**: Used for running migrations with Prisma

To do this:
1. Set the connection mode to `Transaction` in the database settings page
2. Copy the connection string and append `?pgbouncer=true&&connection_limit=1`
   - `pgbouncer=true` disables Prisma from generating prepared statements (required since the connection pooler does not support prepared statements in transaction mode yet)
   - `connection_limit=1` parameter is only required if you are using Prisma from a serverless environment

To get the Session mode connection pooler string, change the port of the connection string from the dashboard to 5432.

You will need both the Transaction mode and Session mode connection strings to set up environment variables in Step 5.

![pooled connection for redwoodjs](https://supabase.com/docs/img/guides/getting-started/quickstarts/redwoodjs/pooled-connection-strings.png)

### 3. Create a RedwoodJS App

Create a RedwoodJS app with TypeScript.

The [`yarn` package manager](https://yarnpkg.com/) is required to create a RedwoodJS app. You will use it to run RedwoodJS commands later.

While TypeScript is recommended, if you want a JavaScript app, omit the `--ts` flag.

```bash
yarn create redwood-app my-app --ts
```

### 4. Open Your RedwoodJS App in VS Code

You'll develop your app, manage database migrations, and run your app in VS Code.

```bash
cd my-app
code .
```

### 5. Configure Environment Variables

In your `.env` file, add the following environment variables for your database connection:

- The `DATABASE_URL` should use the Transaction mode connection string you copied in Step 2.
- The `DIRECT_URL` should use the Session mode connection string you copied in Step 2.

```
# Transaction mode connection string used for migrations
DATABASE_URL="postgres://postgres.[project-ref]:[db-password]@xxx.pooler.supabase.com:6543/postgres?pgbouncer=true&connection_limit=1"

# Session mode connection string — used by Prisma Client
DIRECT_URL="postgres://postgres.[project-ref]:[db-password]@xxx.pooler.supabase.com:5432/postgres"
```

### 6. Update Your Prisma Schema

By default, RedwoodJS ships with a SQLite database, but we want to use Postgres.

Update your Prisma schema file `api/db/schema.prisma` to use your Supabase Postgres database connection environment variables you set up in Step 5:

```prisma
datasource db {
  provider  = "postgresql"
  url       = env("DATABASE_URL")
  directUrl = env("DIRECT_URL")
}
```

### 7. Create the Instrument Model and Apply a Schema Migration

Create the Instrument model in `api/db/schema.prisma` and then run `yarn rw prisma migrate dev` from your terminal to apply the migration:

```prisma
model Instrument {
  id   Int    @id @default(autoincrement())
  name String @unique
}
```

After updating the schema, run the migration:

```bash
yarn rw prisma migrate dev
```

### 8. Update Seed Script

Let's seed the database with a few instruments.

Update the file `scripts/seeds.ts` to contain the following code:

```typescript
import type { Prisma } from '@prisma/client'
import { db } from 'api/src/lib/db'

export default async () => {
  try {
    const data: Prisma.InstrumentCreateArgs['data'][] = [
      { name: 'dulcimer' },
      { name: 'harp' },
      { name: 'guitar' },
    ]
    
    console.log('Seeding instruments ...')
    const instruments = await db.instrument.createMany({ data })
    console.log('Done.', instruments)
  } catch (error) {
    console.error(error)
  }
}
```

### 9. Seed Your Database

Run the seed database command to populate the `Instrument` table with the instruments you just created.

```bash
yarn rw prisma db seed
```

The reset database command `yarn rw prisma db reset` will recreate the tables and will also run the seed script.

### 10. Scaffold the Instrument UI

Now, we'll use RedwoodJS generators to scaffold a CRUD UI for the `Instrument` model:

```bash
yarn rw g scaffold instrument
```

### 11. Start the App

Start the app via `yarn rw dev`. A browser will open to the RedwoodJS Splash page.

![RedwoodJS Splash Page](https://supabase.com/docs/img/redwoodjs-qs-splash.png)

### 12. View Instruments UI

Click on `/instruments` to visit [http://localhost:8910/instruments](http://localhost:8910/instruments) where you should see the list of instruments.

You may now edit, delete, and add new instruments using the scaffolded UI.

## Next Steps

- Add authentication with Supabase Auth
- Create more complex data models and relationships
- Deploy your RedwoodJS application
- Add real-time features with Supabase Realtime

## Troubleshooting

### Connection Issues

If you're having trouble connecting to your Supabase database:

1. Check that your connection strings in the `.env` file are correct
2. Verify that you've added `?pgbouncer=true&connection_limit=1` to the `DATABASE_URL`
3. Ensure your IP address is allowed in the Supabase dashboard (Database settings > Network)

### Migration Issues

If Prisma migrations are failing:

1. Make sure you're using the correct `DIRECT_URL` for the Session mode
2. Check for any unique constraints or data type issues in your schema
3. Try running `yarn rw prisma migrate reset` to start fresh
