# Connecting to Supabase with Drizzle ORM

[Drizzle ORM](https://github.com/drizzle-team/drizzle-orm) is a TypeScript ORM for SQL databases designed with maximum type safety in mind. This guide shows how to connect your Supabase PostgreSQL database with Drizzle ORM.

## Quick Start

Follow these steps to set up Drizzle with your Supabase project:

### 1. Install Dependencies

First, install Drizzle and related packages:

```bash
npm i drizzle-orm postgres
npm i -D drizzle-kit
```

### 2. Create Your Schema

Create a `schema.ts` file and define your database models:

```typescript
import { pgTable, serial, text, varchar } from "drizzle-orm/pg-core";

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  fullName: text('full_name'),
  phone: varchar('phone', { length: 256 }),
});
```

### 3. Connect to Your Database

Connect to your Supabase database using the Connection Pooler:

```typescript
import 'dotenv/config'
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

const connectionString = process.env.DATABASE_URL

// Disable prefetch as it is not supported for "Transaction" pool mode
export const client = postgres(connectionString, { prepare: false })
export const db = drizzle(client);
```

## Connection String

In your [Database Settings](https://supabase.com/dashboard/project/_/settings/database), make sure "Use connection pooler" is checked, then copy the URI and save it as the `DATABASE_URL` environment variable. Remember to replace the password placeholder with your actual database password.

## Additional Configuration

If you plan on solely using Drizzle instead of the Supabase Data API (PostgREST), you can disable the latter in the [API Settings](https://supabase.com/dashboard/project/_/settings/api) to save resources.

## Query Examples

Once connected, you can perform queries using Drizzle's API:

```typescript
// Insert a user
const newUser = await db.insert(users).values({
  fullName: "John Doe",
  phone: "+1234567890"
}).returning();

// Select users
const allUsers = await db.select().from(users);

// Update a user
await db.update(users)
  .set({ fullName: "Jane Doe" })
  .where(eq(users.id, 1));
```

For more information on using Drizzle ORM, refer to the [official documentation](https://orm.drizzle.team/docs/overview).