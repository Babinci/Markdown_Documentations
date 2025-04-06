# Supabase Documentation

This repository contains the documentation for Supabase, organized into different sections for easy navigation. Each file has been formatted for proper markdown rendering and is linked from this index page.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Authentication & Authorization](#authentication--authorization)
3. [Database](#database)
4. [Storage](#storage)
5. [Realtime](#realtime)
6. [Edge Functions](#edge-functions)
7. [AI & Vector Search](#ai--vector-search)
8. [Integrations](#integrations)
9. [Deployment & Operations](#deployment--operations)
10. [Security](#security)
11. [Telemetry](#telemetry)
12. [Troubleshooting](#troubleshooting)
13. [Platform Administration](#platform-administration)
14. [Local Development](#local-development)
15. [Migrations](#migrations)
16. [Reference](#reference)
17. [Framework Integrations](#framework-integrations)
18. [Client Libraries and Frameworks](#client-libraries-and-frameworks)

## Getting Started

- [Getting Started with Supabase](getting-started.md) - Overview of how to get started with Supabase with links to quickstarts and tutorials for various frameworks.
- [AI Prompts](ai-prompts.md) - Curated prompts for working with Supabase using AI-powered IDE tools like GitHub Copilot and Cursor.
- [Architecture](architecture.md) - Overview of Supabase architecture, components, and product principles.
- [Features](features.md) - Comprehensive list of Supabase features, their status, and availability for hosted and self-hosted deployments.
- [Flutter Setup](flutter.md) - How to create a Supabase project and integrate it with a Flutter application.
- [iOS and SwiftUI Setup](ios-swiftui.md) - How to create a Supabase project and query data from an iOS app with SwiftUI.
- [Laravel Setup](laravel.md) - How to create a PHP Laravel project, connect it to your Supabase Postgres database, and configure authentication.
- [Model Context Protocol (MCP)](mcp.md) - How to connect Supabase to AI tools like Cursor, Claude, and Cline using the Model Context Protocol.
- [Next.js Setup](nextjs.md) - How to create a Supabase project and integrate it with a Next.js application.
- [Nuxt.js Setup](nuxtjs.md) - How to create a Supabase project and integrate it with a Nuxt.js application.

## Authentication & Authorization

- [Auth with Edge Functions](auth.md) - How to integrate Supabase Auth with Edge Functions for authenticating users and enforcing Row Level Security.
- [Auth Advanced Guide](advanced-guide.md) - Detailed information about SSR Auth flows and implementation for advanced users.
- [Advanced MFA Phone Usage](advanced-mfa-phone.md) - Managing and understanding pricing for the Advanced Multi-Factor Authentication Phone feature.
- [Anonymous Sign-Ins](auth-anonymous.md) - How to create and use anonymous users for authentication in Supabase.
- [Auth General Configuration](general-configuration.md) - Core settings for controlling user sign-up, email verification, and identity linking.
- [Creating a Supabase Client for SSR](creating-a-client.md) - How to configure your Supabase client to use cookies for Server-Side Rendering (SSR) applications.
- [Enterprise Single Sign-On](enterprise-sso.md) - Overview of Supabase Auth's support for enterprise SSO authentication using SAML 2.0.
- [Login with Apple](auth-apple.md) - How to set up and use Sign in with Apple in web and native apps.
- [Login with Azure (Microsoft)](auth-azure.md) - How to set up and use Microsoft Azure authentication for your Supabase project.
- [Login with Bitbucket](auth-bitbucket.md) - How to set up and use Bitbucket authentication for your Supabase project.
- [CAPTCHA Protection](auth-captcha.md) - How to enable and implement CAPTCHA protection for authentication forms.
- [Login with Discord](auth-discord.md) - How to set up and use Discord authentication for your Supabase project.
- [Login with Facebook](auth-facebook.md) - How to set up and use Facebook authentication for your Supabase project.
- [Login with Figma](auth-figma.md) - How to set up and use Figma authentication for your Supabase project.
- [Login with GitHub](auth-github.md) - How to set up and use GitHub authentication for your Supabase project.
- [Login with GitLab](auth-gitlab.md) - How to set up and use GitLab authentication for your Supabase project.
- [Login with Google](auth-google.md) - How to set up and use Google authentication for your Supabase project.
- [Passwordless Email Logins](auth-email-passwordless.md) - How to implement Magic Links and OTP for passwordless authentication.
- [Password Security](password-security.md) - Best practices for password strength, protection against leaked passwords, and how Supabase securely stores passwords.
- [Password-based Authentication](passwords.md) - Implementing password-based authentication with email or phone number verification.
- [Password Verification Hook](password-verification-hook.md) - Custom password verification for enhanced security, including rate limiting and notifications on failed attempts.
- [Email Templates](auth-email-templates.md) - How to customize authentication email templates in Supabase.
- [Customizing Emails by Language](customizing-emails-by-language-KZ_38Q.md) - How to create multi-language email templates using user metadata.
- [Auth Helpers](auth-helpers.md) - Server-side authentication helper libraries for various frameworks (deprecated).
- [Auth Hooks](auth-hooks.md) - Customize authentication flows using HTTP or Postgres Functions.
- [Flutter Auth UI](flutter-auth-ui.md) - Pre-built, customizable authentication UI widgets for Flutter applications.
- [Custom Access Token Hook](custom-access-token-hook.md) - How to customize the access token issued by Supabase Auth with additional claims.
- [Custom Claims & Role-based Access Control (RBAC)](custom-claims-and-role-based-access-control-rbac.md) - How to implement role-based access control using custom claims in JWTs.
- [Identity Linking](auth-identity-linking.md) - How to manage multiple authentication methods for a single user.
- [Identity Management](identities.md) - Detailed guide to user identities in Supabase Auth and how to manage multiple authentication methods.
- [Login with Kakao](auth-kakao.md) - How to set up and use Kakao authentication for your Supabase project.
- [Login with Keycloak](auth-keycloak.md) - How to set up and use Keycloak authentication for your Supabase project.
- [Login with LinkedIn](auth-linkedin.md) - How to set up and use LinkedIn (OIDC) authentication for your Supabase project.
- [Native Mobile Deep Linking](native-mobile-deep-linking.md) - How to set up deep linking for mobile applications to handle auth redirects.
- [Multi-Factor Authentication](auth-mfa.md) - How to implement and enforce MFA/2FA in your Supabase project.
- [MFA Verification Hook](mfa-verification-hook.md) - How to customize MFA verification with hooks for rate limiting, attempt tracking, and more.
- [Phone Authentication](phone.md) - Implementing multi-factor authentication using phone messaging (SMS/WhatsApp) with enrollment and verification flows.
- [Login with Notion](auth-notion.md) - How to set up and use Notion authentication for your Supabase project.
- [OAuth Scopes](oauth-scopes.md) - Understanding and configuring OAuth scopes for different OAuth providers in Supabase Auth.
- [Send Email Hook](send-email-hook.md) - Configure custom email providers for authentication emails using Auth hooks.
- [Send SMS Hook](send-sms-hook.md) - Configure custom SMS providers for authentication messages with message queuing and regional providers.
- [Custom Auth Emails with React Email and Resend](auth-send-email-hook-react-email-resend.md) - How to use Supabase Edge Functions to customize authentication emails with React Email and Resend.
- [Sign in with OAuth](auth-signinwithoauth.md) - How to implement social login in your application using OAuth providers.
- [Social Login](social-login.md) - Overview of social login benefits and available providers in Supabase Auth.
- [Login with Slack](auth-slack.md) - How to set up and use Slack authentication for your Supabase project.
- [Custom SMTP Configuration](auth-smtp.md) - How to set up and configure a custom SMTP server for sending authentication emails.
- [Login with Spotify](auth-spotify.md) - How to set up and use Spotify authentication for your Supabase project.
- [Migrating to SSR from Auth Helpers](migrating-to-ssr-from-auth-helpers.md) - Guide for migrating from the deprecated Auth Helpers package to the new SSR package.
- [Single Sign-On with SAML 2.0](auth-sso-saml.md) - How to implement enterprise-level SSO using SAML 2.0 with various identity providers like Google Workspaces, Okta, Microsoft Active Directory, and more.
- [Login with Twitch](auth-twitch.md) - How to set up and use Twitch authentication for your Supabase project.
- [Login with Twitter](auth-twitter.md) - How to set up and use Twitter authentication for your Supabase project.
- [Auth UI](auth-ui.md) - A pre-built React component for authenticating users with customizable themes and styles.
- [Implicit Flow](implicit-flow.md) - How the implicit flow authentication method works for client-side applications.
- [PKCE Flow](pkce-flow.md) - How the Proof Key for Code Exchange (PKCE) authentication flow works for server-side applications.
- [Redirect URLs](redirect-urls.md) - How to set up and configure redirect URLs with wildcards for authentication flows.
- [Server-Side Rendering](server-side.md) - How to configure Supabase Auth for server-side rendering frameworks like Next.js and SvelteKit.
- [Sessions](sessions.md) - Understanding and managing user sessions, access tokens, and refresh tokens with Supabase Auth.
- [Signing Out](signout.md) - How to sign out users with different scopes for managing user sessions across devices.
- [TOTP Multi-Factor Authentication](totp.md) - How to implement app authenticator (TOTP) multi-factor authentication with enrollment and verification workflows.
- [SSO and Social Login with WorkOS](auth-workos.md) - How to set up and use WorkOS for Social Login and SSO with your Supabase project.
- [Login with Zoom](auth-zoom.md) - How to set up and use Zoom authentication for your Supabase project.
- [Migrate from Auth0 to Supabase Auth](auth0.md) - Guide for migrating users from Auth0 to Supabase Auth.
- [User Management](managing-user-data.md) - How to view, delete, and export user information, create user profiles, and manage user metadata.
- [Users](users.md) - Understanding permanent and anonymous users, user objects, and user identities in Supabase Auth.

### Auth Troubleshooting
- [Checking GoTrue API Version](how-do-i-check-gotrueapi-version-of-a-supabase-project-lQAnOR.md) - How to check which version of the GoTrue authentication API is running in your Supabase project.
- [Error 401: Invalid Claim: Missing Sub](auth-error-401-invalid-claim-missing-sub--AFwMR.md) - How to fix the "missing sub claim" error in Supabase Auth.
- [Google Auth Fails for Some Users](google-auth-fails-for-some-users-XcFXEu.md) - How to fix Google authentication failures by explicitly requesting the email scope.
- [HTTP API Issues](http-api-issues.md) - How to diagnose and resolve common HTTP API issues, including timeouts, 5xx errors, and connection problems.
- [Invalid Response from Upstream Server](an-invalid-response-was-received-from-the-upstream-server-error-when-querying-auth-RI4Vl-.md) - How to fix the "invalid response from upstream server" error related to auth migrations.
- [JWT Expired Error in Dashboard](jwt-expired-error-in-supabase-dashboard-F06k3x.md) - How to fix "JWT Expired" errors in the Supabase Dashboard by syncing your computer's time.
- [Next.js Auth Issues](how-do-you-troubleshoot-nextjs---supabase-auth-issues-riMCZV.md) - Comprehensive guide for troubleshooting authentication issues with Next.js and Supabase.
- [Amazon Cognito (Amplify)](aws-cognito.md) - How to use Amazon Cognito (Amplify) as an authentication provider with your Supabase project.

## Database

- [Tables and Data](tables.md) - Comprehensive guide to managing tables in Postgres, including data types, primary keys, foreign keys, schemas, views, and loading data.
- [REST API](api.md) - Overview of the auto-generated RESTful API that Supabase creates directly from your database schema.
- [Arrays](arrays.md) - Working with PostgreSQL array types in Supabase, including creating tables with array columns and querying array data.
- [Testing Your Database](testing.md) - Guide to writing automated tests for your PostgreSQL database, including client-based testing and SQL testing with pgTAP.
- [Cascade Deletes](cascade-deletes.md) - Guide to different options for handling foreign key constraints when deleting parent records.
- [Column Level Security](column-level-security.md) - How to restrict access to specific columns in your database tables.
- [Connecting with Beekeeper Studio](beekeeper-studio.md) - How to connect to your Supabase PostgreSQL database using Beekeeper Studio GUI.
- [Connecting with pgAdmin](pgadmin.md) - How to connect to your Supabase PostgreSQL database using pgAdmin with SSL.
- [Connecting with DBeaver](dbeaver.md) - Step-by-step guide for connecting to your Supabase PostgreSQL database using DBeaver.
- [Connecting with Drizzle ORM](drizzle.md) - How to connect to and query your Supabase PostgreSQL database using Drizzle ORM with type safety.
- [Database Configuration](configuration.md) - How to update the default configuration for your PostgreSQL database, including timeouts and timezones.
- [Connecting to Postgres from Edge Functions](connect-to-postgres.md) - How to connect to your Postgres database from Edge Functions using supabase-js, Deno Postgres client, or Drizzle.
- [Connect to your database](connecting-to-postgres.md) - Comprehensive guide on connecting to your Supabase Postgres database from different environments, including frontend applications, serverless functions, and Postgres clients.
- [Connection Management](connection-management.md) - How to effectively manage database connections, configure connection pooling, and monitor connection usage.
- [Connection Pool Settings](how-do-i-update-connection-pool-settings-in-my-dashboard-wAxTJ_.md) - How to update PgBouncer or Supavisor connection pool settings in the dashboard.
- [Changing Max Database Connections](how-to-change-max-database-connections-_BQ8P5.md) - How to configure maximum database connections and understand the performance implications.
- [Cron](cron.md) - How to schedule recurring jobs with cron syntax in Postgres using the pg_cron extension.
- [Installing Cron](install.md) - How to install and uninstall the Supabase Cron Postgres Module for scheduling recurring jobs.
- [Custom Postgres Config](custom-postgres-config.md) - How to customize Postgres configuration settings for advanced database control and optimization.
- [Database Advisors](database-advisors.md) - How to use Performance and Security Advisors to check your database for issues like missing indexes and improper RLS policies.
- [Database Migrations](database-migrations.md) - How to manage schema migrations for your Supabase project using the CLI, including creating tables and seeding data.
- [Database Size](database-size.md) - Understanding database and disk size, including monitoring usage, vacuum operations, and managing read-only mode.
- [Debugging Performance](debugging-performance.md) - How to debug slow-running queries using the Postgres execution planner with the explain() method.
- [Detecting Blocked Queries](how-to-check-if-my-queries-are-being-blocked-by-other-queries-NSKtR1.md) - How to identify when your PostgreSQL queries are being blocked by other operations using a lock monitoring view.
- [Deprecated RLS Features](deprecated-rls-features-Pm77Zs.md) - Information about deprecated Row Level Security functions like auth.role() and auth.email() and their recommended replacements.
- [Dropping All Tables in a Schema](dropping-all-tables-in-schema.md) - How to safely drop all tables in a PostgreSQL schema using a PL/pgSQL script.
- [Dropping a PostgreSQL Role](how-to-delete-a-role-in-postgres-8-AvxY.md) - Step-by-step guide to properly remove a role in PostgreSQL by handling dependencies.
- [Extensions](extensions.md) - Comprehensive overview of PostgreSQL extensions available in Supabase for extending database functionality.
- [PGAudit](pgaudit.md) - Using the PostgreSQL audit extension to track database activities for compliance, security, and troubleshooting.
- [PGJWT](pgjwt.md) - Creating and parsing JSON Web Tokens (JWTs) within PostgreSQL for authentication and authorization.
- [pg_cron](pg_cron.md) - Schedule recurring jobs with cron syntax directly within PostgreSQL for database automation.
- [pg_graphql](pg_graphql.md) - Interact with PostgreSQL using GraphQL instead of SQL, with automatic schema reflection.
- [pg_hashids](pg_hashids.md) - Generate short, unique, non-sequential IDs from numbers to obfuscate sequential database IDs.
- [pg_jsonschema](pg_jsonschema.md) - Validate JSON and JSONB data against JSON Schema documents for data integrity.
- [pg_net](pg_net.md) - Make asynchronous HTTP/HTTPS requests directly from PostgreSQL, useful for triggers and database events.
- [pg_plan_filter](pg_plan_filter.md) - Block execution of resource-intensive queries that exceed a specified cost threshold.
- [pg_repack](pg_repack.md) - Remove table and index bloat without exclusive locks, providing online VACUUM FULL functionality.
- [pg_stat_statements](pg_stat_statements.md) - Track execution statistics for all SQL statements, essential for query performance monitoring.
- [TimescaleDB](timescaledb.md) - Time-series data extension for PostgreSQL enabling efficient storage and querying of time-based datasets.
- [Triggers](triggers.md) - How to create and use PostgreSQL triggers to automatically execute functions on table events.
- [UUID-OSSP](uuid-ossp.md) - Extension for generating universally unique identifiers (UUIDs) for use as primary keys and identifiers.
- [PGMQ](pgmq.md) - A lightweight message queue built on PostgreSQL for reliable message processing with "exactly once" delivery semantics.
- [postgres_fdw](postgres_fdw.md) - Foreign Data Wrapper that enables querying tables and views on remote Postgres servers.
- [PGroonga](pgroonga.md) - Multilingual full text search extension for PostgreSQL supporting a wide range of languages including Japanese and Chinese.
- [pgRouting](pgrouting.md) - Geospatial routing extension for PostgreSQL providing path finding algorithms for transportation networks.
- [pgsodium](pgsodium.md) - Encryption features extension (pending deprecation) with information on migration path to Vault.
- [pgTAP](pgtap.md) - Unit testing extension for PostgreSQL databases with functions for testing tables, columns, and RLS policies.
- [pgvector](pgvector.md) - Vector similarity search extension for PostgreSQL enabling AI embeddings storage and semantic search functionality.
- [plpgsql_check](plpgsql_check.md) - Static code analysis tool for PL/pgSQL to identify syntax and semantic errors before execution.
- [plv8](plv8.md) - JavaScript language extension for PostgreSQL, allowing you to write database functions in JavaScript.
- [RUM](rum.md) - Advanced inverted index for full-text search that improves upon GIN indexes for phrase search and ranking capabilities.
- [First Row in Group](first-row-in-group.md) - How to select the first row for each group in PostgreSQL using the DISTINCT ON clause.
- [Full Text Search](full-text-search.md) - How to implement powerful text search functionality in PostgreSQL using tsvectors and tsqueries.
- [Hypothetical Indexes (HypoPG)](hypopg.md) - How to use the HypoPG extension to test index performance without creating actual indexes.
- [HTTP Extension](http.md) - How to use the PostgreSQL HTTP extension to make RESTful API calls directly from your database.
- [Import Data](import-data.md) - Methods for importing data into Supabase, including using CSV import, pgloader, COPY command, and the Supabase API.
- [Indexes](indexes.md) - Comprehensive guide to creating, managing and using PostgreSQL indexes for optimized query performance.
- [Index Advisor](index_advisor.md) - Postgres extension that recommends indexes to improve query performance.
- [Index Selection in PostgreSQL](how-postgres-chooses-which-index-to-use-_JHrf4.md) - Detailed explanation of how PostgreSQL chooses which indexes to use when executing queries.
- [Inspecting and Debugging](inspect.md) - How to inspect, monitor, and debug PostgreSQL performance using CLI and SQL tools.
- [Interpreting PostgreSQL Logs](how-to-interpret-and-explore-the-postgres-logs-OuCIOj.md) - Comprehensive guide to querying, filtering, and interpreting PostgreSQL logs for troubleshooting and compliance.
- [Query Optimization](query-optimization.md) - Guide to improving query performance with strategic indexing of columns used in WHERE, JOIN, and ORDER BY clauses.
- [Joins and Nested Tables](joins-and-nesting.md) - How to query related tables using the Supabase API with one-to-many and many-to-many relationships.
- [JSON and Unstructured Data](json.md) - How to store, query, and validate JSON data in PostgreSQL using json and jsonb data types.
- [Kysely Postgres](kysely-postgres.md) - How to use Kysely (a type-safe SQL query builder) with Deno Postgres for type-safe database interactions in Edge Functions.
- [Managing Enums](enums.md) - How to create, use, and manage enumerated types in PostgreSQL for columns with fixed sets of possible values.
- [Connecting to Metabase](metabase.md) - How to connect your Supabase Postgres database to Metabase for data visualization and exploration.
- [Monitoring Database Metrics](how-to-view-database-metrics-uqf2z_.md) - How to view real-time and historical database performance metrics using Grafana and the Supabase Dashboard.
- [Revoking Function Execution](how-can-i-revoke-execution-of-a-postgresql-function-2GYb0A.md) - Step-by-step guide to restricting execution permissions for PostgreSQL functions.
- [Network Restrictions](network-restrictions.md) - How to secure your Supabase project by restricting access to specific IP addresses.
- [OrioleDB](orioledb.md) - Using OrioleDB, a new PostgreSQL storage engine with improved performance and scalability.
- [Partitioning Tables](partitions.md) - Divide large tables into smaller, more manageable partitions to improve query performance and simplify data management.
- [PostGIS](postgis.md) - Working with geospatial data in PostgreSQL using the PostGIS extension for location-based queries and geographic operations.
- [Postgres.js](postgres-js.md) - How to connect to and query your Supabase PostgreSQL database using Postgres.js client for Node.js and Deno.
- [Prisma](prisma.md) - How to connect your Supabase PostgreSQL database to Prisma ORM, including setting up database users, migrations, and client.
- [Prisma Troubleshooting](prisma-troubleshooting.md) - Solutions for common Prisma errors when working with Supabase, including connection issues, schema drift, and performance problems.
- [PSQL](psql.md) - How to connect to your Supabase PostgreSQL database using the psql command-line tool with SSL.
- [Queues](queues.md) - Using Supabase Queues for durable message queuing with guaranteed delivery based on the pgmq extension.
- [Replication](replication.md) - How to manage PostgreSQL replication for distributing database load and enabling real-time features.
- [External Replication Setup](setup-replication-external.md) - How to replicate your Supabase database to another PostgreSQL database using logical replication.
- [Roles](roles.md) - Comprehensive guide to managing PostgreSQL role-based access, creating users, granting permissions, and understanding Supabase's default roles.
- [Roles and Superuser Access](roles-superuser.md) - Understanding database role limitations and unsupported operations in Supabase that typically require superuser privileges.
- [Row Level Security](row-level-security.md) - How to secure your data using PostgreSQL's Row Level Security with policies for granular access control and performance optimization.
- [Supavisor](supavisor.md) - Troubleshooting common connection pool errors with Supabase's connection pooler.
- [Timeouts](timeouts.md) - How to configure and manage database query timeouts at session, function, role, and global levels.
- [Using Custom Schemas](using-custom-schemas.md) - How to create and expose custom database schemas beyond the default public schema in your Supabase database.
- [Vault](vault.md) - Using Supabase Vault to safely store and encrypt secrets in Postgres with authenticated encryption.
- [Webhooks](webhooks.md) - Trigger external payloads on database events using PostgreSQL database webhooks.

## Storage

- [Storage Overview](storage.md) - Introduction to Supabase Storage features and capabilities for storing and serving files of any size.
- [Access Control](access-control.md) - How to use Row Level Security policies to control access to buckets and files in Supabase Storage.
- [Ownership](ownership.md) - Understanding ownership management for buckets and objects in Supabase Storage, including access control using Row Level Security.
- [Resumable Uploads](resumable-uploads.md) - How to implement resumable file uploads to Supabase Storage using the TUS protocol for large files and unstable networks.
- [S3 Uploads](s3-uploads.md) - How to upload files to Supabase Storage using the S3 protocol for both single requests and multipart uploads.
- [Scaling Storage](scaling.md) - Optimizations for improving performance and reducing costs when scaling Supabase Storage, including egress reduction and query optimization.
- [Smart CDN](smart-cdn.md) - How Supabase's Smart CDN caching works to improve performance by synchronizing asset metadata to the edge.
- [Standard Uploads](standard-uploads.md) - How to upload files to Supabase Storage using the standard multipart/form-data format for files up to 6MB.
- [Storage Caching](storage-caching.md) - How to integrate Edge Functions with Supabase Storage to cache images on the CDN.
- [Image Transformations](storage-image-transformations.md) - How to transform images in Storage with on-the-fly resizing and optimization features.
- [Storage Size](storage-size.md) - Understanding and monitoring Storage size usage, with SQL queries to analyze object sizes.

## Realtime

- [Postgres Changes](postgres-changes.md) - How to listen to database changes in real-time using Supabase Realtime's Postgres Changes feature.
- [Presence](presence.md) - How to track and synchronize state between multiple users in real-time using Realtime Presence.
- [Protocol](protocol.md) - Detailed reference of the WebSocket message formats used for communication between Realtime clients and servers.
- [Subscribing to Database Changes](subscribing-to-database-changes.md) - How to subscribe to real-time database changes using Broadcast and Postgres Changes methods.
- [Quotas](quotas.md) - Understanding Realtime plan limits for connections, messages, channels, and payload sizes.
- [Realtime Listening in Flutter](realtime-listening-flutter.md) - How to listen to Postgres Changes in real-time with Flutter applications.
- [Realtime Messages Usage](realtime-messages.md) - Understanding and managing billing for Realtime Messages usage in Supabase.
- [Realtime Peak Connections Usage](realtime-peak-connections.md) - Understanding and managing billing for Realtime Peak Connections in Supabase.
- [Realtime User Presence with Flutter](realtime-user-presence.md) - Using Realtime Presence to track and display online users in Flutter applications.
- [Realtime with Next.js](realtime-with-nextjs.md) - Implementing Realtime features in Next.js applications with both client and server components.
- [Realtime Overview](realtime.md) - Overview of Supabase Realtime features including Broadcast, Presence, and Postgres Changes.

## Edge Functions

- [Push Notifications](push-notifications.md) - How to send push notifications from Supabase Edge Functions to Expo-based mobile apps.
- [Quickstart](quickstart.md) - Getting started with Edge Functions development, including local setup, writing, running, and best practices.
- [Routing](routing.md) - How to handle multiple endpoints within a single Edge Function using web frameworks to reduce cold starts and improve performance.
- [Scheduling Functions](schedule-functions.md) - How to schedule Edge Functions to run periodically using pg_cron and pg_net extensions with secure token storage.
- [Screenshots](screenshots.md) - Taking screenshots and generating PDFs using Puppeteer with serverless browsers via WebSockets in Edge Functions.
- [Secrets](secrets.md) - Managing environment variables and sensitive information for Edge Functions in both local and production environments.
- [Sentry Monitoring](sentry-monitoring.md) - Track exceptions and monitor performance issues in Edge Functions using the Sentry Deno SDK.
- [Slack Bot Mention](slack-bot-mention.md) - Create a Slack bot that can respond to mentions using Supabase Edge Functions.
- [Status Codes](status-codes.md) - Reference guide for HTTP status codes returned by Edge Functions and their meanings.
- [Stripe Webhooks](stripe-webhooks.md) - How to handle signed Stripe webhooks securely in Edge Functions.
- [Telegram Bot](telegram-bot.md) - How to build a Telegram Bot using Supabase Edge Functions and the grammY framework.
- [Troubleshooting](troubleshooting.md) - How to solve common issues with Edge Functions, including deployment problems, CORS errors, timeouts, and resource limitations.
- [Unit Testing](unit-test.md) - How to write and run unit tests for Edge Functions using Deno's built-in test runner.
- [Upstash Redis Integration](upstash-redis.md) - How to use Upstash Redis with Edge Functions to create a global invocation counter by region.
- [WebAssembly Modules](wasm.md) - How to use WebAssembly (Wasm) modules in Edge Functions for optimized code and low-level manipulation.
- [WebSockets](websockets.md) - How to handle WebSocket connections in Edge Functions for bi-directional communications.

## Deployment & Operations

- [Performance Tuning](performance.md) - Optimizing your Supabase PostgreSQL database performance, including query optimization and connection management.
- [Permissions](permissions.md) - Understanding service ownership requirements and permissions for Supabase services like Auth and Storage.
- [Self-Hosted Feature Availability](are-all-features-available-in-self-hosted-supabase-THPcqw.md) - Comparison of features available in self-hosted Supabase versus the hosted platform.
- [Read Replicas](read-replicas.md) - Deploy read-only databases across multiple regions for lower latency and better resource management.
- [Regions](regions.md) - List of available regions where you can deploy Supabase projects globally.
- [Regional Invocation](regional-invocation.md) - How to execute Edge Functions in specific regions for optimized performance.
- [Shared Responsibility Model](shared-responsibility-model.md) - Understanding the division of responsibilities between Supabase and users for security, workflow, and application architecture.
- [Upgrading Projects](upgrading.md) - How to upgrade your Supabase project using pg_upgrade or pause and restore methods, including caveats and considerations.

## Security

- [Understanding API Keys](api-keys.md) - Details about the different API keys provided by Supabase and how to use them securely.
- [Hardening the Data API](hardening-data-api.md) - How to secure your database by either disabling the Data API or by exposing a custom schema instead of the default `public` schema.
- [HIPAA Compliance](hipaa-compliance.md) - Understanding HIPAA compliance requirements, responsibilities, and implementation when using Supabase for healthcare applications.
- [HIPAA Projects](hipaa-projects.md) - Step-by-step guide for configuring high compliance projects for storing Protected Health Information (PHI).
- [SOC 2 Compliance](soc-2-compliance.md) - Understanding SOC 2 compliance, responsibilities, and implementation when using Supabase for sensitive data.
- [Securing Your Data](secure-data.md) - Best practices for securely connecting to your Supabase database from frontend applications using RLS and proper API key management.
- [Security Definer Functions in RLS](do-i-need-to-expose-security-definer-functions-in-row-level-security-policies-iI0uOw.md) - Clarification on whether "security definer" functions need to be exposed in PostgREST configuration when used in Row Level Security policies.
- [Product Security](product-security.md) - Comprehensive guide to secure configuration of Supabase products, including Auth, Database, Storage, and Realtime.
- [Rate Limiting](rate-limiting.md) - How to implement rate limiting for Edge Functions using Redis and Upstash.
- [Rate Limits](rate-limits.md) - Understanding and customizing rate limits for Supabase Auth endpoints to prevent abuse.
- [Securing Your API](securing-your-api.md) - Best practices for securing your Supabase API, including proper authentication, authorization, and rate limiting.
- [Security Overview](security.md) - General overview of Supabase security features and compliance certifications including SOC 2 and HIPAA.
- [SSL Enforcement](ssl-enforcement.md) - How to enforce SSL/TLS encryption for all connections to your Supabase project.

## AI & Vector Search

- [AI Models](ai-models.md) - Integration with AI models from OpenAI, Anthropic, Cohere, and other providers.
- [AI Features](ai.md) - Overview of AI-related features available in Supabase, including embeddings, vector storage, and integrations.
- [pgvector](pgvector.md) - Vector similarity search extension enabling embeddings storage and semantic search functionality.
- [Amazon Bedrock Image Generator](amazon-bedrock-image-generator.md) - How to generate images using Amazon Bedrock's Titan Image Generator with Supabase Edge Functions.
- [Semantic Image Search with Amazon Titan](semantic-image-search-amazon-titan.md) - Implementing semantic image search using Amazon Titan multimodal model with Python and the Supabase Vector toolkit.
- [Semantic Search](semantic-search.md) - Building semantic search functionality with pgvector, embedding models, and similarity metrics for meaning-based search.
- [Amazon Bedrock Integration](amazon-bedrock.md) - Integrating Amazon Bedrock foundation models with Supabase for AI applications.
- [Automatic Embeddings](automatic-embeddings.md) - Automatically convert text to vector embeddings for AI search with pgvector.
- [ElevenLabs Speech Generation](elevenlabs-generate-speech-stream.md) - Stream text-to-speech audio using ElevenLabs API from Supabase Edge Functions.
- [ElevenLabs Transcription](elevenlabs-transcribe-speech.md) - Transcribe speech using the ElevenLabs Speech-to-Text API from Supabase Edge Functions.
- [Face Similarity Search](face-similarity.md) - Implementation of facial similarity search using AWS Rekognition and Supabase.
- [Generate Text Embeddings](generate-text-embeddings.md) - Generate text embeddings using OpenAI API and store them in Supabase.
- [Hugging Face Text Generation](hugging-face.md) - Running Hugging Face text generation models with Supabase Edge Functions.
- [Hugging Face Image Captioning](huggingface-image-captioning.md) - Generate image captions with Hugging Face models and Supabase Edge Functions.
- [Hybrid Search](hybrid-search.md) - Implement hybrid search combining keyword and semantic search for better results.
- [HNSW Indexes](hnsw-indexes.md) - Create and use Hierarchical Navigable Small World indexes for faster vector searches.
- [Headless Vector Search](headless-vector-search.md) - Implementing headless vector search with Supabase for in-app semantic search.
- [Image Search with OpenAI CLIP](image-search-openai-clip.md) - Implement image similarity search using OpenAI's CLIP model with Supabase.
- [IVF Indexes](ivf-indexes.md) - Creating and using Inverted File indexes for faster vector searches at scale.
- [Keyword Search](keyword-search.md) - Implementing full-text search for keywords using PostgreSQL FTS.
- [LangChain](langchain.md) - Integrating LangChain with Supabase for building LLM applications with memory persistence.
- [LlamaIndex](llamaindex.md) - How to use LlamaIndex (GPT Index) with Supabase for creating and querying document indexes.
- [Mixpeek Video Search](mixpeek-video-search.md) - Creating AI-powered video search functionality with Mixpeek and Supabase.
- [Next.js Vector Search](nextjs-vector-search.md) - Build a chat interface with Next.js, OpenAI, and Supabase Vector storage.
- [OpenAI GPT-3 Completions](openai.md) - Generate GPT text completions using OpenAI and Supabase Edge Functions.
- [Increasing Vector Lookup Speed](increase-vector-lookup-speeds-by-applying-an-hsnw-index-ohLHUM.md) - How to speed up vector queries by applying an HNSW index to pgvector columns.
- [RAG with Permissions](rag-with-permissions.md) - Implementing fine-grained access control for document retrieval in RAG applications using Row Level Security and Foreign Data Wrappers.
- [Roboflow Computer Vision](roboflow.md) - Integrating Roboflow for computer vision tasks including object detection and image classification with CLIP embeddings storage in Supabase.
- [Semantic Image Search with Amazon Titan](semantic-image-search-amazon-titan.md) - Implementing semantic image search using Amazon Titan embeddings.
- [Semantic Search](semantic-search.md) - Building semantic search functionality with pgvector, OpenAI embeddings, and the Supabase Vector toolkit.
- [Structured and Unstructured Data](structured-unstructured.md) - Understanding the differences between structured and unstructured metadata storage approaches with vector embeddings.
- [Text Deduplication](text-deduplication.md) - Using AI text embeddings to identify and remove duplicate content with Supabase Vecs and sentence transformers.
- [Python Clients](python-clients.md) - Guide to choosing the right Python client (Vecs or ORM libraries) for your AI vector workloads.
- [Vecs Python Client](vecs-python-client.md) - Managing unstructured vector stores in PostgreSQL using the Vecs Python client for creating and querying collections.
- [Vector Columns](vector-columns.md) - Create and query vector columns in Postgres for AI feature engineering and semantic search using pgvector.
- [Vector Indexes](vector-indexes.md) - Create indexes for vector columns in Postgres to optimize search performance.

## Integrations

- [Supabase Marketplace](supabase-marketplace.md) - Overview of the Supabase Marketplace, including Experts and Integrations partners.
- [Vercel Marketplace](vercel-marketplace.md) - Manage Supabase resources directly from the Vercel platform with unified billing and streamlined authentication.

## Telemetry

- [Advanced Log Filtering](advanced-log-filtering.md) - Advanced techniques for querying and filtering logs in Supabase.
- [Telemetry](telemetry.md) - Overview of logs, metrics, and traces for monitoring your Supabase application performance and debugging issues.

## Platform Administration

- [Monthly Active Users](monthly-active-users.md) - Understanding and managing billing for standard email/password users in Supabase projects.
- [Monthly Active SSO Users](monthly-active-users-sso.md) - Understanding and managing billing for Single Sign-On users in Supabase projects.
- [Monthly Active Third-Party Users](monthly-active-users-third-party.md) - Understanding and managing billing for users authenticating with third-party providers like Auth0.
- [Multi-factor Authentication](multi-factor-authentication.md) - How to set up and manage MFA for your Supabase dashboard account.
- [Platform Overview](platform.md) - Introduction to the Supabase platform, projects, organizations, and status monitoring options.
- [Point-in-Time Recovery](point-in-time-recovery.md) - Managing and understanding billing for Point-in-Time Recovery (PITR) usage in your projects.
- [Pricing](pricing.md) - Details about Supabase Realtime pricing, including messages and peak connections billing.
- [Project Transfer](project-transfer.md) - How to transfer ownership of a Supabase project to another organization.
- [Organization SSO](sso.md) - Enable and manage Single Sign-On (SAML 2.0) for your Supabase organization.
- [Storage Image Transformations](storage-image-transformations.md) - Understanding billing, quotas, and optimizing usage for image transformation features.
- [Storage Size](storage-size.md) - Managing and understanding billing for storage size usage with quota information and usage monitoring.
- [Understanding Egress](all-about-supabase-egress-a_Sg_e.md) - Comprehensive guide explaining what egress is, what contributes to it, and how to reduce egress usage.
- [Your Monthly Invoice](your-monthly-invoice.md) - Detailed explanation of billing cycles, invoice components, and how to interpret your Supabase invoice.

## Local Development

- [Overview](overview.md) - Introduction to local development workflow with Supabase CLI and schema migrations.
- [Advanced pgTAP Testing](pgtap-extended.md) - Comprehensive guide to advanced database testing techniques with pgTAP, database.dev, and test helper packages.
- [Seeding Your Database](seeding-your-database.md) - How to populate your database with initial data for reproducible environments across local and testing instances.
- [Testing and Linting](testing-and-linting.md) - Using the Supabase CLI to test and lint your Postgres database and Edge Functions, including pgTAP testing and plpgsql_check linting.

## Reference

- [Resources](resources.md) - Collection of helpful resources, migration guides, and PostgreSQL-specific information for using Supabase.

## Migrations

- [Migrating to Supabase](migrating-to-supabase.md) - Comprehensive guide with migration paths from services like Firebase, Auth0, Heroku, AWS RDS, MySQL, and more.
- [Migrating to SSR from Auth Helpers](migrating-to-ssr-from-auth-helpers.md) - Guide for migrating from the deprecated Auth Helpers package to the new SSR package.
- [Migrating within Supabase](migrating-within-supabase.md) - How to migrate data and settings between Supabase projects.
- [Migrate from Amazon RDS](amazon-rds.md) - How to migrate MySQL, MS SQL, or PostgreSQL databases from Amazon RDS to Supabase.
- [Migrate from Neon](neon.md) - Step-by-step guide for migrating a PostgreSQL database from Neon to Supabase using pg_dump and psql.
- [Migrate from Postgres](postgres.md) - How to migrate an existing Postgres database to Supabase using Colab or CLI tools.
- [Migrate from Render](render.md) - How to migrate your Render Postgres database to Supabase.
- [Migrate from Vercel Postgres](vercel-postgres.md) - How to migrate your Vercel Postgres database to Supabase.

## Framework Integrations

- [Flutter](with-flutter.md) - How to build a user management app with Flutter and Supabase for authentication, database, and storage.
- [Ionic Angular](with-ionic-angular.md) - How to build a user management app with Ionic Angular and Supabase for authentication, database, and storage.
- [Ionic React](with-ionic-react.md) - How to build a user management app with Ionic React and Supabase for authentication, database, and storage.
- [Ionic Vue](with-ionic-vue.md) - How to build a user management app with Ionic Vue and Supabase for authentication, database, and storage.
- [Kotlin](with-kotlin.md) - How to build a product management Android app with Jetpack Compose and Supabase for authentication, database, and storage.
- [Next.js](with-nextjs.md) - How to build a user management app with Next.js and Supabase for authentication, database, and storage.
- [Nuxt 3](with-nuxt-3.md) - How to build a user management app with Nuxt 3 and Vue 3 using Supabase for authentication, database, and storage.
- [React](with-react.md) - How to build a user management app with React using Supabase for authentication, database, and storage.
- [RedwoodJS](with-redwoodjs.md) - How to build a user management app with RedwoodJS using Supabase for authentication, database, and storage.
- [Refine](with-refine.md) - How to build a user management app with Refine framework using Supabase for authentication, database, and storage.
- [SolidJS](with-solidjs.md) - How to build a user management app with SolidJS using Supabase for authentication, database, and storage.
- [Swift and SwiftUI](with-swift.md) - How to build a user management app with Swift and SwiftUI using Supabase for authentication, database, and storage.
- [Svelte](with-svelte.md) - How to build a user management app with Svelte using Supabase for authentication, database, and storage.
- [SvelteKit](with-sveltekit.md) - How to build a user management app with SvelteKit using Supabase for authentication, database, and storage.
- [Vue 3](with-vue-3.md) - How to build a user management app with Vue 3 using Supabase for authentication, database, and storage.
- [RedwoodJS](redwoodjs.md) - How to create a Supabase project and connect it to a RedwoodJS application using Prisma.
- [Refine](refine.md) - How to create a Supabase project and connect it to a Refine application with auto-generated UI.
- [SolidJS](solidjs.md) - How to create a Supabase project, add sample data, and query the data from a SolidJS app.
- [SvelteKit](sveltekit.md) - How to implement Supabase Auth in a SvelteKit application using the SSR package.
- [Remix](remix.md) - How to implement Supabase Auth in a Remix application using the SSR package.
- [Ruby on Rails](ruby-on-rails.md) - How to create a Ruby on Rails project and connect it to your Supabase Postgres database.

## Client Libraries and Frameworks

- [React](react.md) - How to use Supabase Auth with React.js to add authentication to your web application.
- [React.js](reactjs.md) - How to create a Supabase project, add sample data, and query it from a React app.
- [React Native](react-native.md) - How to use Supabase Auth with React Native to create secure authentication flows.
- [Vue](vue.md) - How to create a Supabase project, add sample data, and query the data from a Vue app.