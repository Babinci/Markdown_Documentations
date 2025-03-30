# Vercel Marketplace

Vercel Marketplace allows you to manage Supabase resources directly from the Vercel platform, offering unified billing, streamlined authentication, and easy team access management.

## Overview

The Vercel Marketplace integration provides:
- Unified billing through your Vercel account
- Management of Supabase resources from Vercel dashboard or CLI
- Automatic environment variable synchronization for connected projects

When you create organizations and projects through Vercel Marketplace, they function identically to those created directly within Supabase, but with the convenience of Vercel platform integration.

## Quickstart

### Via Template

You can quickly deploy a Next.js app with Supabase using the Next.js Supabase Starter Template:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world)

### Via Vercel Marketplace

*Details coming soon...*

## Connecting to Supabase Projects

Supabase Projects created via Vercel Marketplace are automatically synchronized with connected Vercel projects. This includes essential environment variables:

```
POSTGRES_URL
POSTGRES_PRISMA_URL
POSTGRES_URL_NON_POOLING
POSTGRES_USER
POSTGRES_HOST
POSTGRES_PASSWORD
POSTGRES_DATABASE
SUPABASE_SERVICE_ROLE_KEY
SUPABASE_ANON_KEY
SUPABASE_URL
SUPABASE_JWT_SECRET
NEXT_PUBLIC_SUPABASE_ANON_KEY
NEXT_PUBLIC_SUPABASE_URL
```

These variables ensure your applications can connect securely to the database and interact with Supabase APIs.

## Studio Support

You can access Supabase Studio easily through the Vercel dashboard from either:
- The Integration installation page
- The Vercel Storage page

Depending on your entry point, you'll either land on the Supabase dashboard homepage or be redirected to the corresponding Supabase Project.

Supabase Studio provides tools including:
- SQL Editor for running queries
- Table Editor for managing database structure
- Log Explorer for real-time log inspection
- Postgres and Compute upgrade options

## Permissions

There is a one-to-one relationship between a Supabase Organization and a Vercel team:
- Installing the integration or launching your first Supabase Project creates a corresponding Supabase Organization if needed
- Vercel users are assigned Supabase accounts automatically
- The user creating a Vercel Storage database receives the `owner` role in the new Supabase organization
- Subsequent users receive roles based on their Vercel role (`developer` for Vercel `member`, `owner` for Vercel `owner`)
- Role management is handled in the Vercel dashboard and synchronized with Supabase

Note: Non-Vercel users can be invited to your Supabase Organization, but their permissions won't be synchronized with Vercel.

## Pricing

Pricing for databases created through Vercel Marketplace is identical to those created directly within Supabase. Your usage is tracked on the [Supabase usage page](https://supabase.com/dashboard/org/_/usage) and sent to Vercel for billing, appearing on your Vercel invoice.

Note that the Supabase Organization billing cycle is separate from Vercel's. Plan changes reset the billing cycle to the date of the change, with the initial billing cycle starting when you install the integration.

## Limitations

When using Vercel Marketplace, the following limitations apply:
- Projects can only be created or removed via the Vercel dashboard
- Organizations can only be removed by uninstalling the Vercel Marketplace Integration
- Owners cannot be added manually within the Supabase dashboard
- Invoices and payments must be managed through the Vercel dashboard, not the Supabase dashboard
