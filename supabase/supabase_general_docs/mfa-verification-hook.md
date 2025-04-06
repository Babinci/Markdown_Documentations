# MFA Verification Hook

You can enhance the [Supabase Multi-Factor Authentication (MFA)](https://supabase.com/docs/guides/auth/auth-mfa) implementation with custom verification hooks. These hooks allow you to implement additional security measures and business logic during the MFA verification process.

## Common Use Cases

With MFA verification hooks, you can:

- Limit the number of verification attempts within a specific time period
- Sign out users who exceed a threshold of invalid verification attempts
- Implement rate limiting for verification attempts
- Record and analyze verification attempt patterns
- Implement IP-based restrictions during verification

## Hook Payload

### Inputs

When a user attempts MFA verification, Supabase Auth sends the following payload to your hook:

| Field | Type | Description |
| --- | --- | --- |
| `factor_id` | `string` | Unique identifier for the MFA factor being verified |
| `factor_type` | `string` | Type of factor: `totp` (time-based one-time password) or `phone` |
| `user_id` | `string` | Unique identifier for the user attempting verification |
| `valid` | `boolean` | Whether the verification attempt was successful (true) or failed (false) |

Example payload:

```json
{
  "factor_id": "6eab6a69-7766-48bf-95d8-bd8f606894db",
  "factor_type": "totp",
  "user_id": "3919cb6e-4215-4478-a960-6d3454326cec",
  "valid": false
}
```

### Outputs

Your hook should return a response with the following structure:

| Field | Type | Description |
| --- | --- | --- |
| `decision` | `string` | How to proceed with the verification: <br>- `continue`: Allow Supabase Auth to proceed with default behavior<br>- `reject`: Deny the verification attempt and log out the user from all active sessions |
| `message` | `string` | (Optional) Message to display to the user if the decision is `reject` |

Example response to reject a verification attempt:

```json
{
  "decision": "reject",
  "message": "You have exceeded the maximum number of MFA attempts."
}
```

## Implementation Example: Rate Limiting Failed Attempts

This example implements a 2-second cooldown period between failed MFA verification attempts.

### Step 1: Create a table to track failed attempts

```sql
create table public.mfa_failed_verification_attempts (
  user_id uuid not null,
  factor_id uuid not null,
  last_failed_at timestamp not null default now(),
  primary key (user_id, factor_id)
);
```

### Step 2: Create the verification hook function

```sql
create function public.hook_mfa_verification_attempt(event jsonb)
  returns jsonb
  language plpgsql
as $$
  declare
    last_failed_at timestamp;
  begin
    if (event->>'valid')::boolean is true then
      -- code is valid, accept it
      return jsonb_build_object('decision', 'continue');
    end if;

    -- Check when the last failed attempt occurred
    select mfa.last_failed_at into last_failed_at
      from public.mfa_failed_verification_attempts as mfa
      where
        mfa.user_id = (event->>'user_id')::uuid
        and
        mfa.factor_id = (event->>'factor_id')::uuid;

    if last_failed_at is not null and now() - last_failed_at < interval '2 seconds' then
      -- Last attempt was too recent - reject with a 429 (Too Many Requests) error
      return jsonb_build_object(
        'error', jsonb_build_object(
          'http_code', 429,
          'message', 'Please wait a moment before trying again.'
        )
      );
    end if;

    -- Record this failed attempt
    insert into public.mfa_failed_verification_attempts
      (
        user_id,
        factor_id,
        last_failed_at
      )
      values
      (
        (event->>'user_id')::uuid,
        (event->>'factor_id')::uuid,
        now()
      )
      on conflict (user_id, factor_id) do update
        set last_failed_at = now();

    -- Allow Supabase Auth to handle the failed attempt with default behavior
    return jsonb_build_object('decision', 'continue');
  end;
$$;
```

### Step 3: Set appropriate permissions

```sql
-- Grant access to the Auth admin role
grant all
  on table public.mfa_failed_verification_attempts
  to supabase_auth_admin;

-- Revoke access from other roles
revoke all
  on table public.mfa_failed_verification_attempts
  from authenticated, anon, public;
```

### Step 4: Enable the hook in project settings

1. Navigate to Authentication > Hooks in the Supabase Dashboard
2. Enable the "MFA Verification" hook
3. Select your `hook_mfa_verification_attempt` function

## Advanced Use Cases

You can extend the basic example to implement more sophisticated security measures:

- Count and limit total failed attempts within a longer time window (e.g., 5 attempts per hour)
- Implement progressive timeouts that increase with each consecutive failed attempt
- Send notifications to administrators when suspicious verification patterns are detected
- Log verification attempts with IP addresses and device information for security auditing
