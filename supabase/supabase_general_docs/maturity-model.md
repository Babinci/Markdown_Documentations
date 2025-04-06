# Supabase Maturity Model

Supabase is designed for both rapid prototyping and enterprise-scale production. This guide outlines best practices as your application matures from prototype to production and your team expands.

## Prototyping Stage

During the prototyping phase, the Supabase Dashboard provides a quick and easy way to build applications. However, we strongly recommend:

- Using [Migrations](https://supabase.com/docs/guides/deployment/database-migrations) to manage your database changes
- Using our CLI to [capture any changes](https://supabase.com/docs/reference/cli/supabase-db-diff) made on the Dashboard
- Committing changes to a version control system like Git

## Collaboration Stage

As soon as you start collaborating with team members, all project changes should be tracked in version control. At this point:

- Move away from using the Dashboard for schema changes
- Use migrations to manage your database
- Check all changes into your version control system
- Establish clear access controls for team members

### Resources:

- [Database migrations](https://supabase.com/docs/guides/deployment/database-migrations)
- [Managing access on the Dashboard](https://supabase.com/docs/guides/platform/access-control)
- [PGAudit for Postgres](https://supabase.com/docs/guides/database/extensions/pgaudit)

## Production Stage

Once your application is live, it's critical to establish proper development workflows. Key considerations:

1. **Never change your database using the Dashboard** - everything should be done with [Migrations](https://supabase.com/docs/guides/cli/managing-environments#create-a-new-migration)
2. **Use Dashboard access controls** to prevent unauthorized changes via the UI
3. **Implement multiple environments** (`local` → `staging` → `prod`) as part of your development workflow
4. **Secure production credentials** - never share production passwords with your team, especially the `postgres` password
5. **Use a CI/CD pipeline** for database changes through version-controlled migrations
6. **Implement network restrictions** to limit database access
7. **Enable Point-in-Time Recovery** for safer backups with less impact on database performance

### Resources:

- [Database migrations](https://supabase.com/docs/guides/deployment/database-migrations)
- [Managing access on the Dashboard](https://supabase.com/docs/guides/platform/access-control)
- [PGAudit for Postgres](https://supabase.com/docs/guides/database/extensions/pgaudit)
- [Managing environments](https://supabase.com/docs/guides/cli/managing-environments)
- [Production Checklist](https://supabase.com/docs/guides/platform/going-into-prod)
- [Shared Responsibility Model](https://supabase.com/docs/guides/platform/shared-responsibility-model)

## Enterprise Stage

For enterprise-level security, consider:

- Running workloads across several organizations
- Creating a dedicated Production organization with limited access
- Restricting direct production database access to only qualified team members
- Implementing comprehensive audit logging and security controls

If you need help designing a secure development workflow for your organization, reach out to [Supabase Enterprise](https://forms.supabase.com/enterprise).
