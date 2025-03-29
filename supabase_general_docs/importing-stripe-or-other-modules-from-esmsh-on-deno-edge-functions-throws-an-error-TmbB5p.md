# Importing Stripe or Other Modules from esm.sh on Deno Edge Functions

If you encounter errors when importing Stripe or other modules from esm.sh in your Deno Edge Functions, you can resolve this by adding `?target=deno` to the import path of the module.

For Stripe, use the following updated import:

```typescript
import Stripe from "https://esm.sh/stripe@11.2.0?target=deno";
```

This parameter instructs esm.sh to provide a version of the module that's compatible with the Deno runtime environment used by Supabase Edge Functions.
