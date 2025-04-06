# Rate Limits

Rate limits protect your services from abuse by limiting how frequently certain operations can be performed.

## Auth Rate Limits

Supabase Auth enforces rate limits on endpoints to prevent abuse. Some rate limits are [customizable](https://supabase.com/dashboard/project/_/auth/rate-limits) through the dashboard.

| Endpoint | Path | Limited By | Rate Limit |
| --- | --- | --- | --- |
| All endpoints that send emails | `/auth/v1/signup` `/auth/v1/recover` `/auth/v1/user`[^1] | Sum of combined requests | Defaults to 2 emails per hour (changed from 4 to 2 as of Oct 21, 2023). Only customizable with your own SMTP setup. |
| All endpoints that send One-Time-Passwords (OTP) | `/auth/v1/otp` | Sum of combined requests | Defaults to 30 OTPs per hour. Customizable. |
| Send OTPs or magic links | `/auth/v1/otp` | Last request | Defaults to 60 seconds window before a new request is allowed. Customizable. |
| Signup confirmation request | `/auth/v1/signup` | Last request | Defaults to 60 seconds window before a new request is allowed. Customizable. |
| Password Reset Request | `/auth/v1/recover` | Last request | Defaults to 60 seconds window before a new request is allowed. Customizable. |
| Verification requests | `/auth/v1/verify` | IP Address | 360 requests per hour (with bursts up to 30 requests) |
| Token refresh requests | `/auth/v1/token` | IP Address | 1800 requests per hour (with bursts up to 30 requests) |
| Create or Verify an MFA challenge | `/auth/v1/factors/:id/challenge` `/auth/v1/factors/:id/verify` | IP Address | 15 requests per hour (with bursts up to 5 requests) |
| Anonymous sign-ins | `/auth/v1/signup`[^2] | IP Address | 30 requests per hour (with bursts up to 30 requests) |

## Customizing Rate Limits

To modify your rate limits:

1. Go to your Supabase project dashboard
2. Navigate to Authentication > Rate Limits
3. Adjust the settings as needed
4. Save your changes

Note that some rate limits are not customizable, particularly email limits unless you're using a custom SMTP setup.

## Handling Rate Limit Errors

When a rate limit is exceeded, the server will respond with a `429 Too Many Requests` status code. Your application should handle this gracefully by:

1. Informing users to try again later
2. Implementing exponential backoff for retries
3. Caching successful responses when appropriate

## Footnotes

[^1]: The rate limit is only applied on `/auth/v1/user` if this endpoint is called to update the user's email address.
[^2]: The rate limit is only applied on `/auth/v1/signup` if this endpoint is called without passing in an email or phone number in the request body.
