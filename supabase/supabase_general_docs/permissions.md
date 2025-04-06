# Permissions

## Introduction

The Supabase platform offers additional services (e.g., Storage) on top of the PostgreSQL database that comes with each project. These services default to storing their operational data within your database, to ensure that you retain complete control over it.

## Service Ownership Requirements

These services assume a base level of access to their data in order to be able to run migrations and function properly. Breaking these assumptions runs the risk of rendering these services inoperational for your project:

- All entities under the `storage` schema are owned by `supabase_storage_admin`
- All entities under the `auth` schema are owned by `supabase_auth_admin`

## Long-term Implications

It is possible for violations of these ownership assumptions to not cause an immediate outage, but take effect at a later time when a newer migration becomes available. Therefore, it's important to maintain the correct ownership structure for Supabase service schemas.

## Best Practices

When working with Supabase services:

1. Do not change ownership of tables, functions, or other database objects in the `storage` or `auth` schemas
2. Do not drop or recreate these schemas
3. Use Row Level Security (RLS) policies to control access to the data instead of changing ownership
4. If you need to extend functionality, consider creating your own schemas rather than modifying the existing service schemas
