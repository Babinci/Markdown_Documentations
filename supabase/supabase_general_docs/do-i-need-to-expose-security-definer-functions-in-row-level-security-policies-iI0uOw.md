# Do I Need to Expose "Security Definer" Functions in Row Level Security Policies?

## Overview

When working with Row Level Security (RLS) policies in Supabase, you may wonder if "security definer" functions need to be exposed in PostgREST configuration. This document provides clarification on this common question.

## PostgREST Configuration Parameters

PostgREST supports two relevant configuration parameters:

1. **Exposed Schemas** - Schemas that PostgREST will expose through its API
2. **Extra Search Path** - Additional schemas PostgREST will search for objects

![PostgREST Configuration](https://supabase.com/docs/img/troubleshooting/d756aeb0-515f-425d-b737-75a935935b73.png)

## Key Information

**You do not need to add your "security definer" functions to either of these configurations if you are using them in your Policies.**

PostgREST doesn't need to know about these functions through extra search path or exposed schemas, as long as you explicitly use the schema inside RLS (e.g.: `security.rls_func`).

## Best Practice

When referencing functions in RLS policies, always use the fully qualified name (including schema) for clarity and to ensure proper resolution.