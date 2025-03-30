# Securing your API

The data APIs are designed to work with Postgres Row Level Security (RLS). If you use [Supabase Auth](https://supabase.com/docs/guides/auth), you can restrict data based on the logged-in user.

To control access to your data, you can use [Policies](https://supabase.com/docs/guides/auth#policies).

## Enabling row level security

Any table you create in the `public` schema will be accessible via the Supabase Data API.

To restrict access, enable Row Level Security (RLS) on all tables, views, and functions in the `public` schema. You can then write RLS policies to grant users access to specific database rows or functions based on their authentication token.

Always enable Row Level Security on tables, views, and functions in the `public` schema to protect your data.

Any table created through the Supabase Dashboard will have RLS enabled by default. If you created the tables via the SQL editor or via another way, enable RLS like so:

### Dashboard

1. Go to the [Authentication > Policies](https://supabase.com/dashboard/project/_/auth/policies) page in the Dashboard.
2. Select **Enable RLS** to enable Row Level Security.

### SQL

```sql
alter table table_name 
enable row level security;
```
