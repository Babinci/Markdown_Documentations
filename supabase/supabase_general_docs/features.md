# Supabase Features

This is a comprehensive overview of the features that Supabase provides for all projects, both hosted and self-hosted.

## Database

### Postgres Database
Every Supabase project is powered by a full PostgreSQL database, giving you access to one of the world's most advanced open-source relational databases.
[Documentation on Postgres Database](https://supabase.com/docs/guides/database)

### Vector Database
Store and query vector embeddings directly within your PostgreSQL database using pgvector, enabling AI and machine learning applications.
[Documentation on Vector Database](https://supabase.com/docs/guides/ai)

### Auto-generated REST API
A RESTful API is automatically generated from your database schema, allowing you to interact with your data without writing any server-side code.
[Documentation on REST API](https://supabase.com/docs/guides/api#rest-api-overview)

### Auto-generated GraphQL API
Create powerful GraphQL APIs using the pg_graphql extension, providing a flexible query language for your applications.
[Documentation on GraphQL API](https://supabase.com/docs/guides/graphql/api)

### Database Webhooks
Send database changes to external services using webhooks, allowing for event-driven architectures.
[Documentation on Webhooks](https://supabase.com/docs/guides/database/webhooks)

### Secrets and Encryption
Encrypt sensitive data and store secrets securely using Vault, Supabase's PostgreSQL extension for managing encrypted data.
[Documentation on Vault](https://supabase.com/docs/guides/database/vault)

## Platform

### Database Backups
All projects include daily backups with options to upgrade to Point-in-Time Recovery for continuous protection.
[Documentation on Backups](https://supabase.com/docs/guides/platform/backups)

### Custom Domains
White-label the Supabase APIs with your own domain to create a branded experience for your users.
[Documentation on Custom Domains](https://supabase.com/docs/guides/platform/custom-domains)

### Network Restrictions
Restrict access to your database by specifying allowed IP ranges, enhancing security.
[Documentation on Network Restrictions](https://supabase.com/docs/guides/platform/network-restrictions)

### SSL Enforcement
Force all Postgres clients to connect via SSL to enhance database connection security.
[Documentation on SSL Enforcement](https://supabase.com/docs/guides/platform/ssl-enforcement)

### Branching
Test and preview changes using Supabase Branches before deploying to production.
[Documentation on Branching](https://supabase.com/docs/guides/platform/branching)

### Terraform Provider
Manage your Supabase infrastructure using Terraform, following Infrastructure as Code principles.
[Documentation on Terraform](https://supabase.com/docs/guides/platform/terraform)

### Read Replicas
Deploy read-only database replicas across multiple regions to reduce latency and improve resource management.
[Documentation on Read Replicas](https://supabase.com/docs/guides/platform/read-replicas)

### Log Drains
Export Supabase logs to third-party providers and external monitoring tools.
[Documentation on Log Drains](https://supabase.com/docs/guides/platform/log-drains)

## Studio

### Studio Single Sign-On
Access the Supabase dashboard through Single Sign-On (SSO) using your organization's identity provider.
[Documentation on Studio SSO](https://supabase.com/docs/guides/platform/sso)

## Realtime

### Postgres Changes
Receive database changes in real-time through WebSockets, enabling reactive applications.
[Documentation on Postgres Changes](https://supabase.com/docs/guides/realtime/postgres-changes)

### Broadcast
Send messages between connected users in real-time using WebSockets.
[Documentation on Broadcast](https://supabase.com/docs/guides/realtime/broadcast)

### Presence
Synchronize shared state across users, enabling features like online status indicators and typing notifications.
[Documentation on Presence](https://supabase.com/docs/guides/realtime/presence)

## Auth

### Email Login
Build secure email authentication flows for your applications.
[Documentation on Email Auth](https://supabase.com/docs/guides/auth/auth-email)

### Social Login
Integrate social authentication providers such as Google, Facebook, GitHub, and more.
[Documentation on Social Login](https://supabase.com/docs/guides/auth/social-login)

### Phone Logins
Enable phone-based authentication using SMS verification.
[Documentation on Phone Auth](https://supabase.com/docs/guides/auth/phone-login)

### Passwordless Login
Implement secure, passwordless authentication using magic links sent via email.
[Documentation on Passwordless Login](https://supabase.com/docs/guides/auth/auth-magic-link)

### Authorization via Row Level Security
Control data access at the row level using PostgreSQL's built-in security policies.
[Documentation on Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)

### CAPTCHA Protection
Add CAPTCHA verification to your authentication forms to prevent automated attacks.
[Documentation on CAPTCHA](https://supabase.com/docs/guides/auth/auth-captcha)

### Server-Side Auth
Leverage server-side authentication helpers for popular frameworks like Next.js, SvelteKit, and Remix.
[Documentation on Server-Side Auth](https://supabase.com/docs/guides/auth/server-side)

## Storage

### File Storage
Store and serve files with granular access controls.
[Documentation on Storage](https://supabase.com/docs/guides/storage)

### Content Delivery Network
Leverage Supabase's CDN to cache large files and reduce load times.
[Documentation on CDN](https://supabase.com/docs/guides/storage/cdn/fundamentals)

### Smart Content Delivery Network
Automatically revalidate assets at the edge for optimal performance.
[Documentation on Smart CDN](https://supabase.com/docs/guides/storage/cdn/smart-cdn)

### Image Transformations
Transform images on-the-fly to fit your application needs.
[Documentation on Image Transformations](https://supabase.com/docs/guides/storage/serving/image-transformations)

### Resumable Uploads
Enable large file uploads with the ability to resume interrupted transfers.
[Documentation on Resumable Uploads](https://supabase.com/docs/guides/storage/uploads/resumable-uploads)

### S3 Compatibility
Interact with Supabase Storage using any tool that supports the S3 protocol.
[Documentation on S3 Compatibility](https://supabase.com/docs/guides/storage/s3/compatibility)

## Edge Functions

### Deno Edge Functions
Deploy globally distributed TypeScript functions for custom business logic.
[Documentation on Edge Functions](https://supabase.com/docs/guides/functions)

### Regional Invocations
Execute Edge Functions in regions close to your database for reduced latency.
[Documentation on Regional Invocation](https://supabase.com/docs/guides/functions/regional-invocation)

### NPM Compatibility
Use NPM modules and Node.js built-in APIs in your Edge Functions.
[Read more about NPM support](https://supabase.com/blog/edge-functions-node-npm)

## Project Management

### CLI
Develop locally and deploy to Supabase using the command line interface.
[Documentation on CLI](https://supabase.com/docs/reference/cli)

### Management API
Programmatically manage your Supabase projects and resources.
[Documentation on Management API](https://supabase.com/docs/reference/api)

## Client Libraries

Supabase provides official client libraries for:
- [JavaScript](https://supabase.com/docs/reference/javascript/start)
- [Flutter](https://supabase.com/docs/reference/dart/initializing)
- [Swift](https://supabase.com/docs/reference/swift/introduction)

Additional community-supported libraries are available for other languages.

## Feature Status

Supabase features are in one of four states - each with different stability and support guarantees:

### Private Alpha
Initial limited access for community feedback. To join the early access program, email [product-ops@supabase.io](mailto:product-ops@supabase.io).

### Public Alpha
Accessible to all but with potential API changes. The service is stable but not covered by the uptime SLA.

### Beta
Security-tested features with stable APIs and clear communication for any breaking changes.

### Generally Available (GA)
Features in GA are fully supported and covered by the [uptime SLA](https://supabase.com/sla).

## Feature Availability Matrix

| Product | Feature | Stage | Available on self-hosted |
| --- | --- | --- | --- |
| Database | Postgres | `GA` | ✅ |
| Database | Vector Database | `GA` | ✅ |
| Database | Auto-generated Rest API | `GA` | ✅ |
| Database | Auto-generated GraphQL API | `GA` | ✅ |
| Database | Webhooks | `beta` | ✅ |
| Database | Vault | `public alpha` | ✅ |
| Platform |  | `GA` | ✅ |
| Platform | Point-in-Time Recovery | `GA` | 🚧 [wal-g](https://github.com/wal-g/wal-g) |
| Platform | Custom Domains | `GA` | N/A |
| Platform | Network Restrictions | `beta` | N/A |
| Platform | SSL enforcement | `GA` | N/A |
| Platform | Branching | `public alpha` | N/A |
| Platform | Terraform Provider | `public alpha` | N/A |
| Platform | Read Replicas | `private alpha` | N/A |
| Platform | Log Drains | `public alpha` | ✅ |
| Studio |  | `GA` | ✅ |
| Studio | SSO | `GA` | ✅ |
| Realtime | Postgres Changes | `GA` | ✅ |
| Realtime | Broadcast | `GA` | ✅ |
| Realtime | Presence | `GA` | ✅ |
| Realtime | Broadcast Authorization | `public beta` | ✅ |
| Realtime | Presence Authorization | `public beta` | ✅ |
| Storage |  | `GA` | ✅ |
| Storage | CDN | `GA` | 🚧 [Cloudflare](https://www.cloudflare.com/) |
| Storage | Smart CDN | `GA` | 🚧 [Cloudflare](https://www.cloudflare.com/) |
| Storage | Image Transformations | `GA` | ✅ |
| Storage | Resumable Uploads | `GA` | ✅ |
| Storage | S3 compatibility | `public alpha` | ✅ |
| Edge Functions |  | `beta` | ✅ |
| Edge Functions | Regional Invocations | `beta` | ✅ |
| Edge Functions | NPM compatibility | `beta` | ✅ |
| Auth |  | `GA` | ✅ |
| Auth | Email login | `GA` | ✅ |
| Auth | Social login | `GA` | ✅ |
| Auth | Phone login | `GA` | ✅ |
| Auth | Passwordless login | `GA` | ✅ |
| Auth | SSO with SAML | `GA` | ✅ |
| Auth | Authorization via RLS | `GA` | ✅ |
| Auth | CAPTCHA protection | `GA` | ✅ |
| Auth | Server-side Auth | `beta` | ✅ |
| CLI |  | `GA` | ✅ Works with self-hosted |
| Management API |  | `GA` | N/A |
| Client Library | JavaScript | `GA` | N/A |
| Client Library | Flutter | `beta` | N/A |
| Client Library | Swift | `beta` | N/A |

- ✅ = Fully Available
- 🚧 = Available, but requires external tools or configuration
