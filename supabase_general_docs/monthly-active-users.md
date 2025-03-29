# Manage Monthly Active Users Usage

## What you are charged for

You are charged for the number of distinct users who log in or refresh their token during the billing cycle. Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "MAUs".

### Example

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single MAU for this billing cycle.

#### 1. Sign User-1 in on January 3

The MAU count increases from 0 to 1.

```javascript
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'user-1@email.com',
  password: 'example-password-1',
})
```

#### 2. Sign User-1 out on January 4

```javascript
const { error } = await supabase.auth.signOut()
```

#### 3. Sign User-1 in again on January 17

The MAU count remains 1.

```javascript
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'user-1@email.com',
  password: 'example-password-1',
})
```

## How charges are calculated

You are charged by MAU.

### Usage on your invoice

Usage is shown as "Monthly Active Users" on your invoice.

## Pricing

$0.00325 per MAU. You are only charged for usage exceeding your subscription plan's quota.

The count resets at the start of each billing cycle.

| Plan | Quota | Over-Usage |
| --- | --- | --- |
| Free | 50,000 | - |
| Pro | 100,000 | $0.00325 per MAU |
| Team | 100,000 | $0.00325 per MAU |
| Enterprise | Custom | Custom |

## Billing examples

### Within quota

The organization's MAU usage for the billing cycle is within the quota, so no charges apply.

| Line Item | Units | Costs |
| --- | --- | --- |
| Pro Plan | 1 | $25 |
| Compute Hours Micro | 744 hours | $10 |
| Monthly Active Users | 23,000 MAU | $0 |
| **Subtotal** |  | **$35** |
| Compute Credits |  | -$10 |
| **Total** |  | **$25** |

### Exceeding quota

The organization's MAU usage for the billing cycle exceeds the quota by 60,000, incurring charges for this additional usage.

| Line Item | Units | Costs |
| --- | --- | --- |
| Pro Plan | 1 | $25 |
| Compute Hours Micro | 744 hours | $10 |
| Monthly Active Users | 160,000 MAU | $195 |
| **Subtotal** |  | **$230** |
| Compute Credits |  | -$10 |
| **Total** |  | **$220** |

## View usage

You can view Monthly Active Users usage on the [organization's usage page](https://supabase.com/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

In the Monthly Active Users section, you can see the usage for the selected time period.
