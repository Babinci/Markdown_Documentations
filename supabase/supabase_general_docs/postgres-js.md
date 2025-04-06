# Postgres.js

[Postgres.js](https://github.com/porsager/postgres) is a full-featured Postgres client for Node.js and Deno.

## Connecting with Postgres.js

### 1. Install

Install Postgres.js and related dependencies.

```bash
npm i postgres
```

### 2. Connect

Create a `db.js` file with the connection details.

To get your connection details, go to your [`Database Settings`](https://supabase.com/dashboard/project/_/settings/database). Make sure `Use connection pooling` is enabled. Choose `Transaction Mode` if you're on a platform with transient connections, such as a serverless function, and `Session Mode` if you have a long-lived connection. Copy the URI and save it as the environment variable `DATABASE_URL`.

```javascript
// db.js
import postgres from 'postgres'

const connectionString = process.env.DATABASE_URL
const sql = postgres(connectionString)

export default sql
```

### 3. Execute commands

Use the connection to execute commands.

```javascript
import sql from './db.js'

async function getUsersOver(age) {
  const users = await sql`
    select name, age
    from users
    where age > ${age}
  `
  // users = Result [{ name: "Walter", age: 80 }, { name: 'Murray', age: 68 }, ...]
  return users
}
```
