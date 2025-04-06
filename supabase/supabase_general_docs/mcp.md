# Model Context Protocol (MCP)

The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is a standard for connecting Large Language Models (LLMs) to external services. This guide shows how to connect Supabase to AI tools using MCP for natural language database interactions.

## Supported AI Tools

You can connect Supabase to these AI tools using MCP:

- [Cursor](https://www.cursor.com/)
- [Windsurf](https://docs.codeium.com/windsurf) (Codium)
- [Cline](https://github.com/cline/cline) (VS Code extension)
- [Claude desktop](https://claude.ai/download)
- [Claude code](https://claude.ai/code)

Once connected, you can use natural language commands to run read-only database queries directly in your AI tool.

## Connect to Supabase using MCP

Supabase uses the [Postgres MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) to provide MCP access to your database. For security, the MCP server runs all queries as read-only transactions.

### Step 1: Find your database connection string

First, retrieve your database connection string based on whether you're using a hosted or local Supabase instance.

#### For a hosted Supabase instance

1. Navigate to your project's [Connection settings](https://supabase.com/dashboard/project/_/settings/database?showConnect=true)
2. Copy the connection string found under **Session pooler**

#### For a local Supabase instance

Run the following command in your terminal where you're running the [Supabase CLI](https://supabase.com/docs/reference/cli/introduction):

```bash
supabase status
```

or with npx:

```bash
npx supabase status
```

Copy the `DB URL` field from the output.

### Step 2: Configure in your AI tool

Set up the connection in your preferred AI tool using the instructions below:

#### Cursor

1. Create a `.cursor` directory in your project root (if it doesn't exist)
2. Create a `.cursor/mcp.json` file with the following:

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "<connection-string>"]
    }
  }
}
```

3. Replace `<connection-string>` with your actual connection string
4. Open Cursor and go to **Settings/MCP** to verify the connection (you should see a green active status)

#### Windsurf

1. Open Windsurf and navigate to the Cascade assistant
2. Tap the hammer (MCP) icon, then **Configure** to open the configuration file
3. Add the following configuration:

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "<connection-string>"]
    }
  }
}
```

4. Replace `<connection-string>` with your actual connection string
5. Save the file and tap **Refresh** in the Cascade assistant
6. Verify the connection (you should see a green active status)

#### Cline (VS Code extension)

1. Open the Cline extension in VS Code and tap the **MCP Servers** icon
2. Tap **Configure MCP Servers** to open the configuration file
3. Add the following configuration:

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "<connection-string>"]
    }
  }
}
```

4. Replace `<connection-string>` with your actual connection string
5. Save the file (Cline should automatically reload the configuration)
6. Verify the connection (you should see a green active status)

#### Claude desktop

1. Open Claude desktop and navigate to **Settings**
2. Under the **Developer** tab, tap **Edit Config** to open the configuration file
3. Add the following configuration:

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "<connection-string>"]
    }
  }
}
```

4. Replace `<connection-string>` with your actual connection string
5. Save the file and restart Claude desktop
6. From the new chat screen, verify the connection (you should see a hammer icon with the new MCP server available)

#### Claude code

1. Create a `.mcp.json` file in your project root
2. Add the following configuration:

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "<connection-string>"]
    }
  }
}
```

3. Replace `<connection-string>` with your actual connection string
4. Save the file and restart Claude code to apply the configuration

## Next steps

With your AI tool now connected to Supabase using MCP, try asking it to run database queries using natural language commands. For example:

- "Show me the schema of my database"
- "List all users in my database"
- "Find products with prices greater than $50"
- "Show me the most recent orders"

The AI tool will translate your natural language requests into SQL and execute the queries against your Supabase database.
