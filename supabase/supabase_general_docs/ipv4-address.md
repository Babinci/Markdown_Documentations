# Dedicated IPv4 Address for Ingress

## Attach an IPv4 address to your database

The Supabase IPv4 add-on provides a dedicated IPv4 address for your Postgres database connection. It can be configured in the [Add-ons Settings](https://supabase.com/dashboard/project/_/settings/addons).

## Understanding IP addresses

The Internet Protocol (IP) addresses devices on the internet. There are two main versions:

- **IPv4**: The older version, with a limited address space.
- **IPv6**: The newer version, offering a much larger address space and the future-proof option.

## When you need the IPv4 add-on

IPv4 addresses are guaranteed to be static for ingress traffic. If your database is making outbound connections, the outbound IP address is not static and cannot be guaranteed.

You may need the IPv4 add-on:
- When using the direct connection string in an IPv6-incompatible network instead of Supavisor or client libraries.
- When you need a dedicated IP address for your direct connection string

## Enabling the IPv4 add-on

You can enable the IPv4 add-on in your project's [add-ons settings](https://supabase.com/dashboard/project/_/settings/addons).

Note that direct database connections can experience a short amount of downtime when toggling the
add-on due to DNS reconfiguration and propagation. Generally, this should be less than a minute.

## Read replicas and IPv4 add-on

When using the add-on, each database (including read replicas) receives an IPv4 address. Each replica adds to the total IPv4 cost.

## Changes and updates

While the IPv4 address generally remains the same, actions like pausing/unpausing the project or enabling/disabling the add-on can lead to a new IPv4 address.

## Supabase and IPv6 compatibility

By default, Supabase Postgres use IPv6 addresses. If your system doesn't support IPv6, you have the following options:

1. **Supavisor Connection Strings**: The Supavisor connection strings are IPv4-compatible alternatives to direct connections
2. **Supabase Client Libraries**: These libraries are compatible with IPv4
3. **Dedicated IPv4 Add-On (Pro Plans+)**: For a guaranteed IPv4 and static database address for the direct connection, enable this paid add-on.

### Checking your network IPv6 support

Most services are IPv6 compatible, but some exceptions exist (listed below). To verify your personal network supports it, run this command on your server:

```bash
curl -6 https://ifconfig.co/ip
```

If it returns an IPv6 address then your system is compatible. An example IPv6 address might look like: `2a05:d014:1c06:5f0c:d7a9:8616:bee2:30df`.

### Checking platforms for IPv6 support

The majority of services are IPv6 compatible. However, there are a few prominent ones that only accept IPv4 connections:

- [Retool](https://retool.com/)
- [Vercel](https://vercel.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Render](https://render.com/)

## Finding your database's IP address

Use an IP lookup website or this command (replace `<PROJECT_REF>`):

```bash
nslookup db.<PROJECT_REF>.supabase.co
```

## Identifying your connections

The pooler and direct connection strings can be found in the [database settings](https://supabase.com/dashboard/project/_/settings/database):

### Direct connection

IPv6 unless IPv4 Add-On is enabled

```
# Example direct connection string
postgresql://postgres:[YOUR-PASSWORD]@db.ajrbwkcuthywfihaarmflo.supabase.co:5432/postgres
```

### Supavisor in transaction mode (port 6543)

Always uses an IPv4 address

```
# Example transaction string
postgresql://postgres.ajrbwkcuthywddfihrmflo:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```

### Supavisor in session mode (port 5432)

Always uses an IPv4 address

```
# Example session string
postgresql://postgres.ajrbwkcuthywfddihrmflo:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:5432/postgres
```

## Pricing

For a detailed breakdown of how charges are calculated, refer to [Manage IPv4 usage](ipv4.md).
