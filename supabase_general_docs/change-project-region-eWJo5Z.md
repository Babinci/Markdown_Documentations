# Change Project Region

This guide explains how to change the region of an existing Supabase project.

## Overview

Currently, there is no direct way to change the region of an existing Supabase project. Instead, you need to create a new project in your desired region and migrate your data and settings.

## Migration Process

To change the region of your Supabase project:

1. Create a new Supabase project in your desired region
2. Follow the [migrations guide](https://supabase.com/docs/guides/platform/migrating-within-supabase) to transfer your data and settings

## Important Considerations

When migrating to a new region, keep in mind:

- **Third-party authentication**: If you're using third-party authentication (Facebook, Google, etc.), you'll need to manually copy over your client ID/secret pairs in the dashboard
- **API credentials**: You'll need to update your API URL, Anon key, and/or Service Role key, which is typically done via environment variables on your web host
- **Client applications**: All client applications will need to be updated with the new project credentials
