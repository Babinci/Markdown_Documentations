# Check Usage for Monthly Active Users (MAU)

This guide explains how to track and understand Monthly Active Users (MAU) usage in your Supabase project.

## Viewing MAU Usage

You can view your MAU usage in your [project's usage page](https://app.supabase.com/project/_/settings/billing/usage).

## How MAU is Calculated

For MAU tracking, Supabase relies on the [Auth Server](https://github.com/supabase/auth) logs. MAU count is relative to your billing cycle and resets whenever your billing cycle resets.

The calculation is based on:
- A distinct count of all user IDs in the current billing cycle
- Auth events include logins, token refreshes, logouts, and other authentication activities
- Each user is counted only once towards MAU in a billing cycle, regardless of how many authentication events they trigger

## Accessing Auth Logs

You can check your Auth logs in your [project's logs & analytics section](https://supabase.com/dashboard/project/_/logs/auth-logs).

## Log Retention Periods

The log retention period (how far back you can access logs) depends on your subscription plan:

| Plan | Log Retention |
|------|---------------|
| Free | 1 day |
| Pro | 7 days |
| Team | 28 days |
| Enterprise | 90 days |

Unless you're on an Enterprise plan, you won't be able to execute queries to determine MAU yourself, as you typically don't have access to logs covering the full billing cycle (approximately 30 days).
