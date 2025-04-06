# Edge Functions

Supabase Edge Functions are server-side TypeScript functions that are distributed globally at the edge—close to your users. They enable you to run server-side code without having to deploy or manage your own servers.

## Overview

Edge Functions provide a versatile way to extend your Supabase projects with custom server-side logic. They're particularly useful for:

- Handling webhooks from third-party services
- Integrating with external APIs
- Processing data before it reaches your database
- Implementing custom authentication flows
- Running operations that shouldn't happen on the client

Edge Functions are built on [Deno](https://deno.com/), which offers several benefits:

- **Open Source**: Deno is fully open source and community-driven
- **Portable**: Functions run locally during development and on any Deno-compatible platform in production
- **TypeScript Native**: First-class TypeScript support without configuration
- **Secure by Default**: No file, network, or environment access unless explicitly enabled
- **WebAssembly Support**: Run code compiled to WASM for high-performance computing
- **Globally Distributed**: Deploy once, run in multiple regions for low-latency responses

## Getting Started

To begin working with Edge Functions, follow the [quickstart guide](https://supabase.com/docs/guides/functions/quickstart) which walks you through creating, testing, and deploying your first function.

## Example Use Cases

### API Integrations

Edge Functions are perfect for interacting with third-party APIs like payment processors, messaging services, or AI platforms:

- Process Stripe payments and handle webhooks
- Integrate with messaging platforms like Discord or Telegram
- Connect to AI services like OpenAI or Hugging Face
- Send emails through providers like Resend or SendGrid

### Data Processing

Transform, validate, or process data before it reaches your database:

- Clean and validate form submissions
- Process uploaded files before storing them
- Generate thumbnails or transform images
- Convert data formats (CSV to JSON, etc.)

### Custom Authentication

Implement specialized authentication flows:

- Create custom sign-up processes
- Handle social login providers
- Implement multi-factor authentication logic
- Generate custom JWT tokens

### Backend-for-Frontend

Create tailored APIs for your frontend applications:

- Aggregate data from multiple sources
- Implement rate limiting and request validation
- Create RESTful or GraphQL interfaces

## Example Function Gallery

Here are some examples to help you get started:

### Authentication and Security

- [Using supabase-js with Auth](https://supabase.com/docs/guides/functions/auth) - Access auth context and use Supabase client
- [Protecting forms with Cloudflare Turnstile](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile) - Implement CAPTCHA protection
- [Rate limiting](https://supabase.com/docs/guides/functions/examples/rate-limiting) - Control request frequency using Upstash Redis

### Database Integration

- [Connect to Postgres](https://supabase.com/docs/guides/functions/connect-to-postgres) - Direct database access from Edge Functions
- [Type-safe SQL with Kysely](https://supabase.com/docs/guides/functions/kysely-postgres) - Strongly typed database interactions
- [Working with Supabase Storage](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/read-storage/index.ts) - Read and write files

### External Services

- [OpenAI Integration](https://supabase.com/docs/guides/ai/examples/openai) - Connect to OpenAI APIs
- [Hugging Face Models](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning) - Access 100,000+ ML models
- [Amazon Bedrock Image Generator](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator) - Generate images with Amazon's AI
- [Stripe Webhooks](https://supabase.com/docs/guides/functions/examples/stripe-webhooks) - Process payments and handle Stripe events
- [Send Emails with Resend](https://supabase.com/docs/guides/functions/examples/send-emails) - Email delivery

### Bots and Automation

- [Discord Bot](https://supabase.com/docs/guides/functions/examples/discord-bot) - Create slash command bots
- [Telegram Bot](https://supabase.com/docs/guides/functions/examples/telegram-bot) - Build messaging bots
- [Slack Bot Mention](https://supabase.com/docs/guides/functions/examples/slack-bot-mention) - Respond to Slack mentions

### Content Generation

- [Open Graph Image Generation](https://supabase.com/docs/guides/functions/examples/og-image) - Create dynamic social images
- [OG Images with Storage CDN Caching](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/og-image-with-storage-cdn) - Cache generated images
- [Screenshots with Puppeteer](https://supabase.com/docs/guides/functions/examples/screenshots) - Capture website screenshots

### Architecture Patterns

- [RESTful Service API](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/restful-tasks/index.ts) - Build REST endpoints
- [Oak Server Middleware](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/oak-server) - Request routing
- [Server-Sent Events](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/streams) - Real-time data streaming
- [File Uploads](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/file-upload-storage) - Process multipart/form-data

### Operations

- [GitHub Actions Deployment](https://supabase.com/docs/guides/functions/examples/github-actions) - CI/CD pipelines
- [Monitoring with Sentry](https://supabase.com/docs/guides/functions/examples/sentry-monitoring) - Error tracking
- [User Geolocation](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/location) - Get location from IP

### Storage and Caching

- [Upstash Redis Counter](https://supabase.com/docs/guides/functions/examples/upstash-redis) - Distributed counters and caching

## Development Features

Edge Functions support:

- **TypeScript and JavaScript**: Write in either language
- **NPM Compatibility**: Use thousands of npm packages
- **ES Modules**: Modern JavaScript module system
- **CORS Support**: Configure cross-origin resource sharing
- **Environment Variables**: Securely store configuration
- **Local Development**: Test functions before deployment
- **File System Access**: Read and write files with permission
- **Background Tasks**: Run operations after response is sent

## Learn More

- [Edge Functions Quickstart](https://supabase.com/docs/guides/functions/quickstart)
- [Local Development](https://supabase.com/docs/guides/functions/local-development)
- [Deploy Edge Functions](https://supabase.com/docs/guides/functions/deploy)
- [Debugging Tools](https://supabase.com/docs/guides/functions/debugging)
- [CORS Configuration](https://supabase.com/docs/guides/functions/cors)
- [Environment Variables](https://supabase.com/docs/guides/functions/secrets)
