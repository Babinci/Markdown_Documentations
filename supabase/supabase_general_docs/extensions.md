# PostgreSQL Extensions Overview

Extensions expand your PostgreSQL database with functionality beyond the core offering. Supabase has pre-installed many useful open source extensions, making it easy to add advanced features to your projects.

## Managing Extensions

### Enable and Disable Extensions

You can manage extensions through the Supabase Dashboard or SQL:

**Using the Dashboard:**
1. Navigate to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click **Extensions** in the sidebar
3. Toggle extensions on or off as needed

**Using SQL:**
```sql
-- Enable an extension
CREATE EXTENSION IF NOT EXISTS "extension_name";

-- Disable an extension
DROP EXTENSION IF EXISTS "extension_name";
```

### Extension Schema Management

Most extensions are installed under the `extensions` schema, which is accessible to public by default. To maintain clean organization:

- Do not create other entities in the `extensions` schema
- If you need to restrict user access to extension tables, create a separate schema for that specific extension
- Be aware that some extensions require specific schema names (e.g., `postgis_tiger_geocoder` creates a schema named `tiger`)
- Check for schema name conflicts before enabling such extensions

### Custom Extensions

In addition to the pre-configured extensions, you can install your own SQL extensions directly in the database using Supabase's SQL editor, including plpgsql extensions.

### Upgrading Extensions

When a new version of an extension becomes available on Supabase:
- Initiate a software upgrade in the [Infrastructure Settings](https://supabase.com/dashboard/project/_/settings/infrastructure)
- Alternatively, restart your server in the [General Settings](https://supabase.com/dashboard/project/_/settings/general)

## Extension Categories

Supabase offers extensions in various categories to extend your database capabilities:

- **AI & Machine Learning**: Vector, embeddings, and AI-related functionality
- **Admin**: Database administration and management tools
- **Audit**: Tracking and auditing database operations
- **Cryptography**: Encryption, hashing, and security functions
- **Data Types**: Additional specialized data types
- **Geo**: Geographic information systems and spatial data
- **Indexing**: Advanced indexing methods
- **Language Support**: Additional programming languages for stored procedures
- **Notifications**: Event handling and notification systems
- **Search**: Full-text search and information retrieval
- **Testing**: Database testing frameworks
- **Time Series**: Time-series data handling
- **Utility**: General utility functions and tools

## Available Extensions

Supabase is pre-configured with over 50 extensions, including:

| Extension | Description | Category |
|-----------|-------------|----------|
| address_standardizer | Parse addresses into constituent elements | Geo |
| amcheck | Verify relation integrity | Admin |
| btree_gin | GIN indexing for common datatypes | Index |
| citext | Case-insensitive character strings | Data Type |
| hypopg | Hypothetical indexes | Index |
| http | HTTP client for PostgreSQL | Utility |
| index_advisor | Automatic index recommendation | Admin |
| pg_cron | Job scheduler | Utility |
| pg_graphql | GraphQL support | API |
| pg_hashids | Hash IDs for obfuscating numeric identifiers | Utility |
| pg_jsonschema | JSON Schema validation | Data Type |
| pg_net | Asynchronous HTTP requests | Utility |
| pg_stat_statements | SQL execution statistics tracking | Admin |
| pgaudit | Audit logging | Audit |
| pgcrypto | Cryptographic functions | Cryptography |
| pgjwt | JSON Web Token API | Authentication |
| pgroonga | Full-text search for all languages | Search |
| pgrouting | Routing algorithms extension | Geo |
| pgsodium | Libsodium cryptographic functions | Cryptography |
| pgtap | Unit testing for PostgreSQL | Testing |
| plv8 | JavaScript procedural language | Language |
| postgis | Geometry and geography spatial types | Geo |
| postgres_fdw | Foreign-data wrapper for remote PostgreSQL | Connectivity |
| rum | GIN-like index for text search | Search |
| timescaledb | Time-series data management | Time Series |
| uuid-ossp | UUID generation | Utility |
| vector | Vector data type with similarity search | AI |
| pg_repack | Storage optimization and bloat removal | Admin |

For the complete list of extensions and detailed documentation, visit the [Supabase Extensions documentation](https://supabase.com/docs/guides/database/extensions).

## Using Extensions

Each extension provides different functionality to solve specific problems. Refer to the individual extension documentation for usage examples and best practices. Many extensions include their own SQL functions, data types, and operators that can be used in your queries.

## Performance Considerations

- Some extensions can be resource-intensive, so enable only what you need
- Monitor database performance after enabling extensions, especially on smaller compute tiers
- Consider upgrading your compute resources if using multiple resource-intensive extensions
- Extensions with background workers (like pg_cron or timescaledb) consume additional resources
