# Supabase Multi-Factor Authentication (MFA)

## Table of Contents
- [Introduction](#introduction)
- [Enroll a Factor](#enroll-a-factor)
- [Create a Challenge](#create-a-challenge)
- [Verify a Challenge](#verify-a-challenge)
- [Create and Verify a Challenge](#create-and-verify-a-challenge)
- [Unenroll a Factor](#unenroll-a-factor)
- [Get Authenticator Assurance Level](#get-authenticator-assurance-level)
- [Other Documentation Files](#other-documentation-files)

## Introduction

This section contains methods commonly used for Multi-Factor Authentication (MFA) and are invoked behind the `supabase.auth.mfa` namespace.

Currently, Supabase only supports time-based one-time password (TOTP) as the 2nd factor. They don't support recovery codes but allow users to enroll more than 1 TOTP factor, with an upper limit of 10.

Having a 2nd TOTP factor for recovery frees the user of the burden of having to store their recovery codes somewhere. It also reduces the attack surface since multiple recovery codes are usually generated compared to just having 1 backup TOTP factor.

## Enroll a Factor

- Currently, `totp` is the only supported `factor_type`. The returned `id` should be used to create a challenge.
- To create a challenge, see [`mfa.challenge()`](#create-a-challenge).
- To verify a challenge, see [`mfa.verify()`](#verify-a-challenge).
- To create and verify a challenge in a single step, see [`mfa.challenge_and_verify()`](#create-and-verify-a-challenge).

### Example

```python
response = supabase.auth.mfa.enroll(
    {
        "factor_type": "totp",
        "friendly_name": "your_friendly_name",
    }
)
```

## Create a Challenge

- An [enrolled factor](#enroll-a-factor) is required before creating a challenge.
- To verify a challenge, see [`mfa.verify()`](#verify-a-challenge).

### Example

```python
response = supabase.auth.mfa.challenge(
    {"factor_id": "34e770dd-9ff9-416c-87fa-43b31d7ef225"}
)
```

## Verify a Challenge

- To verify a challenge, please [create a challenge](#create-a-challenge) first.

### Example

```python
response = supabase.auth.mfa.verify(
    {
        "factor_id": "34e770dd-9ff9-416c-87fa-43b31d7ef225",
        "challenge_id": "4034ae6f-a8ce-4fb5-8ee5-69a5863a7c15",
        "code": "123456",
    }
)
```

## Create and Verify a Challenge

- An [enrolled factor](#enroll-a-factor) is required before invoking `challengeAndVerify()`.
- Executes [`mfa.challenge()`](#create-a-challenge) and [`mfa.verify()`](#verify-a-challenge) in a single step.

### Example

```python
response = supabase.auth.mfa.challenge_and_verify(
    {
        "factor_id": "34e770dd-9ff9-416c-87fa-43b31d7ef225",
        "code": "123456",
    }
)
```

## Unenroll a Factor

### Example

```python
response = supabase.auth.mfa.unenroll(
    {"factor_id": "34e770dd-9ff9-416c-87fa-43b31d7ef225"}
)
```

## Get Authenticator Assurance Level

- Authenticator Assurance Level (AAL) is the measure of the strength of an authentication mechanism.
- In Supabase, having an AAL of `aal1` refers to having the 1st factor of authentication such as an email and password or OAuth sign-in while `aal2` refers to the 2nd factor of authentication such as a time-based, one-time-password (TOTP).
- If the user has a verified factor, the `next_level` field will return `aal2`, else, it will return `aal1`.

### Example

```python
response = supabase.auth.mfa.get_authenticator_assurance_level()
```

## Other Documentation Files

- [Overview](./supabase_overview.md)
- [Database Operations](./supabase_database.md)
- [Query Filters](./supabase_filters.md)
- [Authentication Basics](./supabase_auth_basics.md)
- [OAuth Authentication](./supabase_auth_oauth.md)
- [Admin Authentication Methods](./supabase_auth_admin.md)
- [Realtime](./supabase_realtime.md)
- [Storage](./supabase_storage.md)
- [Edge Functions](./supabase_edge_functions.md)
