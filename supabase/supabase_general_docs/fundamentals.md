# Storage Content Delivery Network (CDN)

Supabase Storage uses a Content Delivery Network (CDN) to cache assets globally, improving access speeds for users around the world. This guide explains how the Storage CDN works and how to make the most of it.

## What is a CDN?

A Content Delivery Network is a geographically distributed network of servers that caches content from an origin server. For Supabase Storage, the origin server is located in the same region as your Supabase project.

CDNs provide several key benefits:
- **Performance**: Reduces latency by serving content from locations closer to users
- **Scalability**: Handles high traffic loads by distributing requests across multiple servers
- **Security**: Provides protection against DDoS and other attacks
- **Availability**: Ensures content remains available even if the origin server faces issues

## How Supabase Storage CDN Works

### Request Flow

When a user requests an object from Supabase Storage:

1. The request first goes to the nearest CDN node
2. If the CDN has the object cached (a "cache hit"), it serves the object directly
3. If the CDN does not have the object cached (a "cache miss"), it retrieves the object from the origin server, caches it, and then serves it to the user
4. Subsequent requests for the same object from the same region are served directly from the CDN cache

### Cache Status Headers

Each response includes a `cf-cache-status` header that indicates the cache status:

| Status | Description |
|--------|-------------|
| `HIT` | The object was served from the CDN cache |
| `MISS` | The object was not in the CDN cache and was fetched from the origin |
| `REVALIDATED` | The object was in the cache but had expired and was revalidated with the origin |
| `UPDATING` | The object was served from cache while it was being updated from the origin |
| `DYNAMIC` | The response was not cached because it was configured not to be |

## Example Scenario

Let's walk through an example to understand how the CDN improves performance:

1. A new bucket is created for a Supabase project hosted in Singapore
2. A user from the United States requests an object:
   - The request is routed to the US CDN node
   - The CDN does not have the object cached (cache miss)
   - The CDN retrieves the object from the origin server in Singapore
   - The object is cached in the US CDN node and served to the user

![CDN Cache Miss](https://supabase.com/docs/img/cdn-cache-miss.png)

3. Another user in the United States requests the same object:
   - The request is routed to the US CDN node
   - The CDN already has the object cached (cache hit)
   - The object is served directly from the US CDN node without contacting the origin server in Singapore

![CDN Cache Hit](https://supabase.com/docs/img/cdn-cache-hit.png)

## Public vs. Private Buckets

The bucket privacy settings have a significant impact on CDN caching efficiency:

### Public Buckets

Objects in public buckets:
- Do not require authorization for access
- Can be cached more effectively by the CDN
- Result in better cache hit rates
- Provide optimal performance for public content

When two different users access the same object in a public bucket from the same region, the second user will likely experience a cache hit.

### Private Buckets

Objects in private buckets:
- Require authorization for access
- Are evaluated on a per-user basis
- Have user-specific security policies applied
- Result in more origin requests and lower cache hit rates

When two different users access the same object in a private bucket from the same region, both might experience cache misses because their access permissions may differ.

## Cache Eviction

Even with long cache control durations, CDNs may evict objects from their cache if they haven't been requested for a while from a specific region. This is part of the CDN's resource optimization process.

For example, if no users from Japan request your object for an extended period, it may be removed from the Japanese CDN node's cache, even if users in other regions are actively accessing it.

## Optimizing for CDN Performance

To maximize CDN benefits:

1. **Use public buckets** for content that doesn't need access control
2. **Set appropriate cache control headers** for frequently accessed content
3. **Consider regional access patterns** when designing your application
4. **Monitor cache performance** using the cache status headers
5. **Use the Smart CDN feature** for dynamic content that needs to stay fresh

For dynamic content that requires frequent updates, Supabase offers a [Smart CDN](https://supabase.com/docs/guides/storage/cdn/smart-cdn) feature that automatically revalidates objects when they change.
