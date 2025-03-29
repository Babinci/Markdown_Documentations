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
17. [Client Libraries and Frameworks](#client-libraries-and-frameworks)

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
- [Login with Notion](auth-notion.md) - How to set up and use Notion authentication for your Supabase project.
- [OAuth Scopes](oauth-scopes.md) - Understanding and configuring OAuth scopes for different OAuth providers in Supabase Auth.
- [Custom Auth Emails with React Email and Resend](auth-send-email-hook-react-email-resend.md) - How to use Supabase Edge Functions to customize authentication emails with React Email and Resend.
- [Sign in with OAuth](auth-signinwithoauth.md) - How to implement social login in your application using OAuth providers.
- [Login with Slack](auth-slack.md) - How to set up and use Slack authentication for your Supabase project.
- [Custom SMTP Configuration](auth-smtp.md) - How to set up and configure a custom SMTP server for sending authentication emails.
- [Login with Spotify](auth-spotify.md) - How to set up and use Spotify authentication for your Supabase project.
- [Migrating to SSR from Auth Helpers](migrating-to-ssr-from-auth-helpers.md) - Guide for migrating from the deprecated Auth Helpers package to the new SSR package.
- [Single Sign-On with SAML 2.0](auth-sso-saml.md) - How to implement enterprise-level SSO using SAML 2.0 with various identity providers like Google Workspaces, Okta, Microsoft Active Directory, and more.
- [Login with Twitch](auth-twitch.md) - How to set up and use Twitch authentication for your Supabase project.
- [Login with Twitter](auth-twitter.md) - How to set up and use Twitter authentication for your Supabase project.
- [Auth UI](auth-ui.md) - A pre-built React component for authenticating users with customizable themes and styles.
- [Implicit Flow](implicit-flow.md) - How the implicit flow authentication method works for client-side applications.
- [SSO and Social Login with WorkOS](auth-workos.md) - How to set up and use WorkOS for Social Login and SSO with your Supabase project.
- [Login with Zoom](auth-zoom.md) - How to set up and use Zoom authentication for your Supabase project.
- [Migrate from Auth0 to Supabase Auth](auth0.md) - Guide for migrating users from Auth0 to Supabase Auth.
- [User Management](managing-user-data.md) - How to view, delete, and export user information, create user profiles, and manage user metadata.

### Auth Troubleshooting
- [Checking GoTrue API Version](how-do-i-check-gotrueapi-version-of-a-supabase-project-lQAnOR.md) - How to check which version of the GoTrue authentication API is running in your Supabase project.
- [Error 401: Invalid Claim: Missing Sub](auth-error-401-invalid-claim-missing-sub--AFwMR.md) - How to fix the "missing sub claim" error in Supabase Auth.
- [Google Auth Fails for Some Users](google-auth-fails-for-some-users-XcFXEu.md) - How to fix Google authentication failures by explicitly requesting the email scope.
- [HTTP API Issues](http-api-issues.md) - How to diagnose and resolve common HTTP API issues, including timeouts, 5xx errors, and connection problems.
- [JWT Expired Error in Dashboard](jwt-expired-error-in-supabase-dashboard-F06k3x.md) - How to fix "JWT Expired" errors in the Supabase Dashboard by syncing your computer's time.
- [Next.js Auth Issues](how-do-you-troubleshoot-nextjs---supabase-auth-issues-riMCZV.md) - Comprehensive guide for troubleshooting authentication issues with Next.js and Supabase.
- [Amazon Cognito (Amplify)](aws-cognito.md) - How to use Amazon Cognito (Amplify) as an authentication provider with your Supabase project.

## Database

- [Cascade Deletes](cascade-deletes.md) - Guide to different options for handling foreign key constraints when deleting parent records.
- [Column Level Security](column-level-security.md) - How to restrict access to specific columns in your database tables.
- [Connecting with Beekeeper Studio](beekeeper-studio.md) - How to connect to your Supabase PostgreSQL database using Beekeeper Studio GUI.
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
- [Joins and Nested Tables](joins-and-nesting.md) - How to query related tables using the Supabase API with one-to-many and many-to-many relationships.
- [JSON and Unstructured Data](json.md) - How to store, query, and validate JSON data in PostgreSQL using json and jsonb data types.
- [Kysely Postgres](kysely-postgres.md) - How to use Kysely (a type-safe SQL query builder) with Deno Postgres for type-safe database interactions in Edge Functions.
- [Managing Enums](enums.md) - How to create, use, and manage enumerated types in PostgreSQL for columns with fixed sets of possible values.
- [Connecting to Metabase](metabase.md) - How to connect your Supabase Postgres database to Metabase for data visualization and exploration.
- [Monitoring Database Metrics](how-to-view-database-metrics-uqf2z_.md) - How to view real-time and historical database performance metrics using Grafana and the Supabase Dashboard.
- [Revoking Function Execution](how-can-i-revoke-execution-of-a-postgresql-function-2GYb0A.md) - Step-by-step guide to restricting execution permissions for PostgreSQL functions.
- [Network Restrictions](network-restrictions.md) - How to secure your Supabase project by restricting access to specific IP addresses.
- [OrioleDB](orioledb.md) - Using OrioleDB, a new PostgreSQL storage engine with improved performance and scalability.
- [OrioleDB](orioledb.md) - Using OrioleDB, a new PostgreSQL storage engine with improved performance and scalability.

## Security

- [Understanding API Keys](api-keys.md) - Details about the different API keys provided by Supabase and how to use them securely.
- [Hardening the Data API](hardening-data-api.md) - How to secure your database by either disabling the Data API or by exposing a custom schema instead of the default `public` schema.
- [HIPAA Compliance](hipaa-compliance.md) - Understanding HIPAA compliance requirements, responsibilities, and implementation when using Supabase for healthcare applications.
- [HIPAA Projects](hipaa-projects.md) - Step-by-step guide for configuring high compliance projects for storing Protected Health Information (PHI).
- [Security Definer Functions in RLS](do-i-need-to-expose-security-definer-functions-in-row-level-security-policies-iI0uOw.md) - Clarification on whether "security definer" functions need to be exposed in PostgREST configuration when used in Row Level Security policies.
- [Product Security](product-security.md) - Overview of Supabase's security practices, including physical security, network security, and data encryption.
- [Securing Your API](securing-your-api.md) - Best practices for securing your Supabase API, including proper authentication, authorization, and rate limiting.
- [SSL Enforcement](ssl-enforcement.md) - How to enforce SSL/TLS encryption for all connections to your Supabase project.

## Telemetry

- [Advanced Log Filtering](advanced-log-filtering.md) - Advanced techniques for querying and filtering logs in Supabase.
- [Telemetry](telemetry.md) - Information about what telemetry data Supabase collects and how to opt out if desired.

## Platform Administration

- [Monthly Active Users](monthly-active-users.md) - Understanding and managing billing for standard email/password users in Supabase projects.
- [Monthly Active SSO Users](monthly-active-users-sso.md) - Understanding and managing billing for Single Sign-On users in Supabase projects.
- [Monthly Active Third-Party Users](monthly-active-users-third-party.md) - Understanding and managing billing for users authenticating with third-party providers like Auth0.
- [Multi-factor Authentication](multi-factor-authentication.md) - How to set up and manage MFA for your Supabase dashboard account.
- [Project Transfer](project-transfer.md) - How to transfer ownership of a Supabase project to another organization.

## Migrations

- [Migrating to Supabase](migrating-to-supabase.md) - Comprehensive guide with migration paths from services like Firebase, Auth0, Heroku, AWS RDS, MySQL, and more.
- [Migrating to SSR from Auth Helpers](migrating-to-ssr-from-auth-helpers.md) - Guide for migrating from the deprecated Auth Helpers package to the new SSR package.
- [Migrating within Supabase](migrating-within-supabase.md) - How to migrate data and settings between Supabase projects.
- [Migrate from Neon](neon.md) - Step-by-step guide for migrating a PostgreSQL database from Neon to Supabase using pg_dump and psql.
