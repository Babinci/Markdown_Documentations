# JWTs (JSON Web Tokens)

A [JSON Web Token](https://jwt.io/introduction) is a type of data structure, represented as a string, that usually contains identity and authorization information about a user. It encodes information about its lifetime and is signed with a cryptographic key to make it tamper-resistant.

Supabase Access Tokens are JWTs. The JWT is sent along with every request to Supabase services. By verifying the token and inspecting the included claims, you can allow or deny access to resources. [Row Level Security](row-level-security.md) policies are based on the information present in JWTs.

## Understanding JWTs

### Structure of a JWT

JWTs consist of three parts, separated by dots (`.`):
1. **Header**: Contains metadata about the token type and the signing algorithm
2. **Payload**: Contains the claims (data statements about an entity)
3. **Signature**: Used to verify that the token hasn't been altered

A typical JWT looks like this:
```
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMDAxIiwibmFtZSI6IlNhbSBWaW1lcyIsImlhdCI6MTUxNjIzOTAyMiwiZXhwIjoxNTE4MjM5MDIyfQ.zMcHjKlkGhuVsiPIkyAkB2rjXzyzJsMMgpvEGvGtjvA
```

### JWT Payload

The JSON object inside a JWT typically contains information like this:

```json
{
  "sub": "0001",
  "name": "Sam Vimes",
  "iat": 1516239022,
  "exp": 1518239022
}
```

- `sub` is the "subject", which is usually the UUID of the user
- `iat` is the timestamp at which the token was created (issued at)
- `exp` is the expiration timestamp
- You can include custom claims as needed

## Encoding and Signing JWTs

JWTs are encoded and signed using cryptographic algorithms:

1. The header typically looks like:
   ```json
   {
     "alg": "HS256",
     "typ": "JWT"
   }
   ```

2. The payload contains the claims:
   ```json
   {
     "sub": "0001",
     "name": "Sam Vimes",
     "iat": 1516239022,
     "exp": 1518239022
   }
   ```

3. The signature is created using the formula:
   ```
   HMACSHA256(
     base64UrlEncode(header) + "." +
     base64UrlEncode(payload),
     secret)
   ```

You can test encoding/decoding tokens at [https://jwt.io](https://jwt.io/).

## Benefits of JWTs

JWTs have become popular in microservice architectures because:

- They enable **decentralized authentication** - services can verify a token without querying a central database
- They contain **self-contained information** - claims about the user are included in the token
- They're **stateless** - no need to store session information on the server
- They can be **verified independently** - any service with the secret key can verify the token

> **Note**: Unlike session tokens, JWTs cannot be easily revoked before expiration. If a JWT is compromised, it remains valid until it expires unless you change the signing key (which invalidates all existing tokens).

## JWTs in Supabase

Supabase issues JWTs for three different purposes:

### 1. Anonymous Key (`anon key`)

- Used to bypass the Supabase API gateway
- Can be safely included in client-side code
- Example usage:
  ```bash
  curl 'https://xscduanzzfseqszwzhcy.supabase.co/rest/v1/colors?select=name' \
  -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYxNDIwNTE3NCwiZXhwIjoxOTI5NzgxMTc0fQ.-NBR1WnZyQGpRLdXJfgfpszoZ0EeE6KHatJsDPLIX8c"
  ```

- When decoded, it contains:
  ```json
  {
    "role": "anon",
    "iss": "supabase",
    "iat": 1614205174,
    "exp": 1929781174
  }
  ```

### 2. Service Role Key (`service role key`)

- Has super admin rights and can bypass Row Level Security
- Must be kept private and never used in client-side code
- Should only be used in secure environments (your server)

### 3. User-specific JWTs

- Issued when a user authenticates with your application
- Contains user-specific information
- Used to identify users and enforce permissions
- Example decoded payload:
  ```json
  {
    "aud": "authenticated",
    "exp": 1615824388,
    "sub": "0334744a-f2a2-4aba-8c8a-6e748f62a172",
    "email": "valid.email@supabase.io",
    "app_metadata": {
      "provider": "email"
    },
    "user_metadata": null,
    "role": "authenticated"
  }
  ```

## Using JWTs in API Requests

### For Public Data (with RLS enabled)
```bash
curl 'https://xscduanzzfseqszwzhcy.supabase.co/rest/v1/colors?select=name' \
-H "apikey: YOUR_ANON_KEY"
```

### For Authenticated Users
```bash
curl 'https://xscduanzzfseqszwzhcy.supabase.co/rest/v1/colors?select=name' \
-H "apikey: YOUR_ANON_KEY" \
-H "Authorization: Bearer USER_JWT_TOKEN"
```

### For Server-Side Operations
```bash
curl "$YOUR_PROJECT_URL/rest/v1/colors?select=name" \ 
-H "apikey: $YOUR_SERVICE_ROLE_KEY" \ 
-H "authorization: Bearer $YOUR_SERVICE_ROLE_KEY"
```

## Security Considerations

1. Never expose your service role key in client-side code
2. Always use Row Level Security when exposing your anon key
3. Set appropriate expiration times for your tokens
4. Be aware that JWTs cannot be easily revoked before they expire
5. Store tokens securely to prevent theft or leakage

## Resources

- [JWT Introduction](https://jwt.io/introduction)
- [JWT Debugger](https://jwt.io/)
- [Row Level Security in Supabase](row-level-security.md)
- [Supabase Auth Documentation](auth.md)
