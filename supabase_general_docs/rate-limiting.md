# Rate Limiting Edge Functions

Rate limiting is an important security and performance feature for controlling the traffic to your Edge Functions.

## Using Redis with Upstash for Rate Limiting

[Redis](https://redis.io/docs/about/) is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. It is optimized for atomic operations like incrementing a value, which makes it perfect for implementing rate limiting functionality.

[Upstash](https://upstash.com/) provides an HTTP/REST based Redis client which is ideal for serverless use-cases and therefore works well with Supabase Edge Functions.

## Implementation

You can implement rate limiting based on various identifiers, such as:

- IP addresses
- User IDs from Supabase Auth
- API keys
- Session IDs

## Example

Check out a complete implementation example on [GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/upstash-redis-ratelimit).

## Video Tutorial

Watch the following tutorial for a step-by-step implementation guide:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/o4ooiE-SdUg" title="Rate Limiting with Redis and Upstash" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Benefits of Rate Limiting

1. **Prevent abuse**: Protect your functions from potential DDoS attacks or abuse
2. **Control costs**: Limit the number of function invocations to prevent unexpected billing
3. **Improve reliability**: Ensure service availability by preventing resource exhaustion
4. **Enhance security**: Add an additional layer of protection against brute force attacks
