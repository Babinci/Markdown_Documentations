# Network Restrictions

If you can't find the Network Restrictions section at the bottom of your [Database Settings](https://supabase.com/dashboard/project/_/settings/database), update your version of Postgres in the [Infrastructure Settings](https://supabase.com/dashboard/project/_/settings/infrastructure).

Each Supabase project comes with configurable restrictions on the IP ranges that are allowed to connect to Postgres and its pooler ("your database"). These restrictions are enforced before traffic reaches your database. If a connection is not restricted by IP, it still needs to authenticate successfully with valid database credentials.

If direct connections to your database [resolve to a IPv6 address](https://supabase.com/dashboard/project/_/settings/database), you need to add both IPv4 and IPv6 CIDRs to the list of allowed CIDRs. Network Restrictions will be applied to all database connection routes, whether pooled or direct. You will need to add both the IPv4 and IPv6 networks you want to allow. There are two exceptions: If you have been granted an extension on the IPv6 migration OR if you have purchased the [IPv4 add-on](https://supabase.com/dashboard/project/_/settings/addons), you need only add IPv4 CIDRs.

## To get started via the Dashboard

Network restrictions can be configured in the [Database Settings](https://supabase.com/dashboard/project/_/settings/database) page. Ensure that you have [Owner or Admin permissions](https://supabase.com/docs/guides/platform/access-control#manage-team-members) for the project that you are enabling network restrictions.

## To get started via the CLI

1. [Install](https://supabase.com/docs/guides/cli) the Supabase CLI 1.22.0+.
2. [Log in](https://supabase.com/docs/guides/cli/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.
3. If your project was created before 23rd December 2022, it will need to be [upgraded to the latest Supabase version](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects) before Network Restrictions can be used.
4. Ensure that you have [Owner or Admin permissions](https://supabase.com/docs/guides/platform/access-control#manage-team-members) for the project that you are enabling network restrictions.

### Check restrictions

You can use the `get` subcommand of the CLI to retrieve the restrictions currently in effect.

If restrictions have been applied, the output of the `get` command will reflect the IP ranges allowed to connect:

```
> supabase network-restrictions --project-ref {ref} get --experimental
DB Allowed IPv4 CIDRs: &[183.12.1.1/24]
DB Allowed IPv6 CIDRs: &[2001:db8:3333:4444:5555:6666:7777:8888/64]
Restrictions applied successfully: true
```

If restrictions have never been applied to your project, the list of allowed CIDRs will be empty, but they will also not have been applied ("Restrictions applied successfully: false"). As a result, all IPs are allowed to connect to your database:

```
> supabase network-restrictions --project-ref {ref} get --experimental
DB Allowed IPv4 CIDRs: []
DB Allowed IPv6 CIDRs: []
Restrictions applied successfully: false
```

### Update restrictions

The `update` subcommand is used to apply network restrictions to your project:

```
> supabase network-restrictions --project-ref {ref} update --db-allow-cidr 183.12.1.1/24 --db-allow-cidr 2001:db8:3333:4444:5555:6666:7777:8888/64 --experimental
DB Allowed IPv4 CIDRs: &[183.12.1.1/24]
DB Allowed IPv6 CIDRs: &[2001:db8:3333:4444:5555:6666:7777:8888/64]
Restrictions applied successfully: true
```

The restrictions specified (in the form of CIDRs) replaces any restrictions that might have been applied in the past.
To add to the existing restrictions, you must include the existing restrictions within the list of CIDRs provided to the `update` command.

### Remove restrictions

To remove all restrictions on your project, you can use the `update` subcommand with the CIDR `0.0.0.0/0`:

```
> supabase network-restrictions --project-ref {ref} update --db-allow-cidr 0.0.0.0/0 --db-allow-cidr ::/0 --experimental
DB Allowed IPv4 CIDRs: &[0.0.0.0/0]
DB Allowed IPv6 CIDRs: &[::/0]
Restrictions applied successfully: true
```

## Limitations

- The current iteration of Network Restrictions applies to connections to Postgres and the database pooler; it doesn't currently apply to APIs offered over HTTPS (e.g., PostgREST, Storage, and Auth). This includes using Supabase client libraries like [supabase-js](https://supabase.com/docs/reference/javascript).
- If network restrictions are enabled, direct access to your database from Edge Functions will always be blocked. Using the Supabase client library [supabase-js](https://supabase.com/docs/reference/javascript) is recommended to connect to a database with network restrictions from Edge Functions.
