# Secure Configuration of Supabase Products

The Supabase [production checklist](https://supabase.com/docs/guides/deployment/going-into-prod) provides detailed advice on preparing an app for production. While our [SOC 2](https://supabase.com/docs/guides/security/soc-2-compliance) and [HIPAA](https://supabase.com/docs/guides/security/hipaa-compliance) compliance documents outline the roles and responsibilities for building a secure and compliant app.

Various products at Supabase have their own hardening and configuration guides. Below is a definitive list of these to help guide your way.

## Auth

- [Password security](https://supabase.com/docs/guides/auth/password-security)
- [Rate limits](https://supabase.com/docs/guides/auth/rate-limits)
- [Bot detection / Prevention](https://supabase.com/docs/guides/auth/auth-captcha)
- [JWTs](https://supabase.com/docs/guides/auth/jwts)

## Database

- [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Column Level Security](https://supabase.com/docs/guides/database/postgres/column-level-security)
- [Hardening the Data API](https://supabase.com/docs/guides/database/hardening-data-api)
- [Additional security controls for the Data API](https://supabase.com/docs/guides/api/securing-your-api)
- [Custom claims and role based access control](https://supabase.com/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac)
- [Managing Postgres roles](https://supabase.com/docs/guides/database/postgres/roles)
- [Managing secrets with Vault](https://supabase.com/docs/guides/database/vault)
- [Superuser access and unsupported operations](https://supabase.com/docs/guides/security/docs/guides/database/postgres/roles-superuser)

## Storage

- [Object ownership](https://supabase.com/docs/guides/storage/security/ownership)
- [Access control](https://supabase.com/docs/guides/storage/security/access-control)
  - The Storage API docs contain hints about required [RLS policy permissions](https://supabase.com/docs/reference/javascript/storage-createbucket)
- [Custom roles with the storage schema](https://supabase.com/docs/guides/storage/schema/custom-roles)

## Realtime

- [Authorization](https://supabase.com/docs/guides/security/docs/guides/realtime/authorization)

## Resources

- [Supabase Production Checklist](https://supabase.com/docs/guides/deployment/going-into-prod)
- [SOC 2 Compliance](https://supabase.com/docs/guides/security/soc-2-compliance)
- [HIPAA Compliance](https://supabase.com/docs/guides/security/hipaa-compliance)
