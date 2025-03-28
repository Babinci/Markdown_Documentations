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
14. [Reference](#reference)

## Getting Started

- [AI Prompts](ai-prompts.md) - Curated prompts for working with Supabase using AI-powered IDE tools like GitHub Copilot and Cursor.
- [Architecture](architecture.md) - Overview of Supabase architecture, components, and product principles.

## Authentication & Authorization

- [Auth with Edge Functions](auth.md) - How to integrate Supabase Auth with Edge Functions for authenticating users and enforcing Row Level Security.
- [Auth Advanced Guide](advanced-guide.md) - Detailed information about SSR Auth flows and implementation for advanced users.
- [Advanced MFA Phone Usage](advanced-mfa-phone.md) - Managing and understanding pricing for the Advanced Multi-Factor Authentication Phone feature.
- [Anonymous Sign-Ins](auth-anonymous.md) - How to create and use anonymous users for authentication in Supabase.
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
- [Auth Helpers](auth-helpers.md) - Server-side authentication helper libraries for various frameworks (deprecated).
- [Auth Hooks](auth-hooks.md) - Customize authentication flows using HTTP or Postgres Functions.
- [Identity Linking](auth-identity-linking.md) - How to manage multiple authentication methods for a single user.
- [Login with Kakao](auth-kakao.md) - How to set up and use Kakao authentication for your Supabase project.
- [Login with Keycloak](auth-keycloak.md) - How to set up and use Keycloak authentication for your Supabase project.
- [Login with LinkedIn](auth-linkedin.md) - How to set up and use LinkedIn (OIDC) authentication for your Supabase project.
- [Multi-Factor Authentication](auth-mfa.md) - How to implement and enforce MFA/2FA in your Supabase project.
- [Login with Notion](auth-notion.md) - How to set up and use Notion authentication for your Supabase project.
- [Custom Auth Emails with React Email and Resend](auth-send-email-hook-react-email-resend.md) - How to use Supabase Edge Functions to customize authentication emails with React Email and Resend.
- [Sign in with OAuth](auth-signinwithoauth.md) - How to implement social login in your application using OAuth providers.
- [Login with Slack](auth-slack.md) - How to set up and use Slack authentication for your Supabase project.
- [Custom SMTP Configuration](auth-smtp.md) - How to set up and configure a custom SMTP server for sending authentication emails.
- [Login with Spotify](auth-spotify.md) - How to set up and use Spotify authentication for your Supabase project.
- [Single Sign-On with SAML 2.0](auth-sso-saml.md) - How to implement enterprise-level SSO using SAML 2.0 with various identity providers like Google Workspaces, Okta, Microsoft Active Directory, and more.
- [Login with Twitch](auth-twitch.md) - How to set up and use Twitch authentication for your Supabase project.
- [Login with Twitter](auth-twitter.md) - How to set up and use Twitter authentication for your Supabase project.
- [Auth UI](auth-ui.md) - A pre-built React component for authenticating users with customizable themes and styles.
- [SSO and Social Login with WorkOS](auth-workos.md) - How to set up and use WorkOS for Social Login and SSO with your Supabase project.
- [Login with Zoom](auth-zoom.md) - How to set up and use Zoom authentication for your Supabase project.
- [Migrate from Auth0 to Supabase Auth](auth0.md) - Guide for migrating users from Auth0 to Supabase Auth.

### Auth Troubleshooting
- [Error 401: Invalid Claim: Missing Sub](auth-error-401-invalid-claim-missing-sub--AFwMR.md) - How to fix the "missing sub claim" error in Supabase Auth.
- [Amazon Cognito (Amplify)](aws-cognito.md) - How to use Amazon Cognito (Amplify) as an authentication provider with your Supabase project.

## Database

- [Cascade Deletes](cascade-deletes.md) - Guide to different options for handling foreign key constraints when deleting parent records.
- [Column Level Security](column-level-security.md) - How to restrict access to specific columns in your database tables.
- [Connecting with Beekeeper Studio](beekeeper-studio.md) - How to connect to your Supabase PostgreSQL database using Beekeeper Studio GUI.
- [Database Configuration](configuration.md) - How to update the default configuration for your PostgreSQL database, including timeouts and timezones.

## Storage

- [Storage Access Control](access-control.md) - How to configure security and access control for Supabase Storage using Row Level Security (RLS).
- [S3 Authentication](authentication.md) - How to authenticate with Supabase Storage S3 using access keys or session tokens.
- [Bandwidth & Storage Egress](bandwidth.md) - How to monitor, calculate, and optimize bandwidth usage for Storage in Supabase.
- [S3 Compatibility](compatibility.md) - Details about the compatibility of Supabase Storage with the S3 protocol.

## Realtime

- [Realtime Authorization](authorization.md) - How to control client access to Realtime Broadcast and Presence using Row Level Security policies.
- [Benchmarks](benchmarks.md) - Detailed performance benchmarks showing the scalability of Supabase Realtime features including Broadcast, Presence, and Postgres Changes.
- [Broadcast](broadcast.md) - How to send low-latency messages between users using Supabase Realtime Broadcast.
- [Realtime Concepts](concepts.md) - Core concepts and extensions available in Supabase Realtime including Channels, Broadcast, Presence, and Postgres Changes.

## Edge Functions

- [Running AI Models](ai-models.md) - How to run AI models in Edge Functions for generating embeddings and using Large Language Models (LLMs).
- [Generate Images with Amazon Bedrock](amazon-bedrock-image-generator.md) - How to use Amazon Bedrock in Edge Functions to generate images with AI.
- [Background Tasks](background-tasks.md) - How to run background tasks in Edge Functions outside of the request handler.
- [CI/CD Workflow](cicd-workflow.md) - How to automate Edge Function deployments using GitHub Actions, Bitbucket, and GitLab CI.
- [Cloudflare Turnstile](cloudflare-turnstile.md) - How to add CAPTCHA protection to your forms using Cloudflare Turnstile and Edge Functions.
- [Handling Compressed Requests](compression.md) - How to decompress Gzip-compressed request bodies in Edge Functions.

## AI & Vector Search

- [AI & Vectors](ai.md) - Overview of Supabase's AI capabilities including vector store, embeddings, and integrations with AI providers.
- [Automatic Embeddings](automatic-embeddings.md) - How to automate vector embedding generation and updates using Edge Functions, pgmq, pg_net, and pg_cron.
- [Building ChatGPT Plugins](building-chatgpt-plugins.md) - How to use Supabase as a Retrieval Store for your ChatGPT plugin.
- [Choosing Compute Add-on](choosing-compute-addon.md) - Guide to selecting the right Compute Add-on for your vector workload with benchmarks for different embedding dimensions.

## Integrations

- [Amazon Bedrock](amazon-bedrock.md) - How to use Amazon Bedrock with Supabase for creating and storing embeddings.
- [Build a Supabase Integration](build-a-supabase-integration.md) - Guide to building a Supabase Integration using OAuth2 and the management API for managing users' organizations and projects.

## Deployment & Operations

- [All about Supabase Egress](all-about-supabase-egress-a_Sg_e.md) - Understanding, monitoring, and optimizing egress (bandwidth) usage in Supabase.
- [Backup and Restore using the CLI](backup-restore.md) - Comprehensive guide for backing up and restoring Supabase projects using the CLI.
- [Database Backups](backups.md) - In-depth explanation of database backup types, frequency, and restoration processes including Point-in-Time Recovery.
- [Branching](branching.md) - How to use Supabase Branches to safely test and preview changes to your project with Git integration.
- [Change Project Region](change-project-region-eWJo5Z.md) - How to change the region of an existing Supabase project by migration.
- [Compute and Disk](compute-and-disk.md) - Information about compute instance sizes, disk types, and performance characteristics for Supabase projects.
- [Manage Compute Usage](compute.md) - Details about compute billing, pricing, and optimization strategies.

## Security

- [Understanding API Keys](api-keys.md) - Details about the different API keys provided by Supabase and how to use them securely.

## Telemetry

- [Advanced Log Filtering](advanced-log-filtering.md) - Advanced techniques for querying and filtering logs in Supabase.

## Troubleshooting

- [Avoiding Timeouts in Long Running Queries](avoiding-timeouts-in-long-running-queries-6nmbdN.md) - How to handle SQL queries that exceed the Dashboard's 1-minute timeout limit.
- [Canceling Statement Due to Statement Timeout](canceling-statement-due-to-statement-timeout-581wFv.md) - Guidance on handling and resolving statement timeout errors in PostgreSQL.
- [Using Stored Functions for Complex Operations](certain-operations-are-too-complex-to-perform-directly-using-the-client-libraries-8JaphH.md) - How to use PostgreSQL stored functions when client library operations are too complex.

## Platform Administration

- [Set Up SSO with Azure AD](azure.md) - How to set up Single Sign-On with Azure Active Directory for accessing the Supabase dashboard.
- [About Billing on Supabase](billing-on-supabase.md) - Overview of Supabase subscription plans, organization-based billing, costs, and usage quotas.
- [Billing FAQ](billing-faq.md) - Frequently asked questions about Supabase billing, subscriptions, plans, quotas, and payments.
- [Change Email Associated with Supabase Account](change-email-associated-with-supabase-account-T5eHNT.md) - How to change the email address associated with your Supabase dashboard account.
- [Check Usage for Monthly Active Users (MAU)](check-usage-for-monthly-active-users-mau-MwZaBs.md) - How to track and understand Monthly Active Users (MAU) usage in your Supabase project.

## Reference

- [REST API](api.md) - Overview of Supabase's auto-generated RESTful API and its features.
- [Auto-generated Documentation](auto-generated-docs.md) - How to access automatically generated API documentation in the Supabase Dashboard.
- [Automatic Retries in supabase-js](automatic-retries-in-supabase-js.md) - How to add automatic retries to your Supabase API requests using fetch-retry.
- [Client Libraries](client-libs.md) - Overview of official and community-maintained client libraries for different programming languages.

