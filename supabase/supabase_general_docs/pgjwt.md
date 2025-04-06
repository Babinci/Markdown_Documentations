# pgjwt: JSON Web Tokens

## Introduction

The [`pgjwt`](https://github.com/michelp/pgjwt) (PostgreSQL JSON Web Token) extension allows you to create and parse [JSON Web Tokens (JWTs)](https://en.wikipedia.org/wiki/JSON_Web_Token) within a PostgreSQL database. JWTs are commonly used for authentication and authorization in web applications and services.

## Enable the Extension

### Using the Dashboard

1. Go to the [Database](https://supabase.com/dashboard/project/_/database/tables) page in the Dashboard
2. Click on **Extensions** in the sidebar
3. Search for `pgjwt` and enable the extension

### Using SQL

```sql
CREATE EXTENSION pgjwt;
```

## API Functions

- **`sign(payload json, secret text, algorithm text default 'HSA256')`**: Signs a JWT containing _payload_ with _secret_ using _algorithm_.
- **`verify(token text, secret text, algorithm text default 'HSA256')`**: Decodes a JWT _token_ that was signed with _secret_ using _algorithm_.

Where:

- `payload` is an encrypted JWT represented as a string
- `secret` is the private/secret passcode which is used to sign the JWT and verify its integrity
- `algorithm` is the method used to sign the JWT using the secret
- `token` is an encrypted JWT represented as a string

## Usage Examples

Once the extension is installed, you can use its functions to create and parse JWTs. Here's an example of how to use the `sign` function to create a JWT:

```sql
SELECT extensions.sign(
    payload   := '{"sub":"1234567890","name":"John Doe","iat":1516239022}',
    secret    := 'secret',
    algorithm := 'HS256'
);
```

The `sign` function returns a string that represents the JWT, which can then be safely transmitted between parties:

```
sign
---------------------------------
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o
(1 row)
```

To parse a JWT and extract its claims, you can use the `verify` function:

```sql
SELECT extensions.verify(
    token     := 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiRm9vIn0.Q8hKjuadCEhnCPuqIj9bfLhTh_9QSxshTRsA5Aq4IuM',
    secret    := 'secret',
    algorithm := 'HS256'
);
```

Which returns the decoded contents and some associated metadata:

```
header                    |    payload     | valid
-------------------------+----------------+-------
{"alg":"HS256","typ":"JWT"} | {"name":"Foo"} | t
(1 row)
```

## Resources

- [Official `pgjwt` documentation](https://github.com/michelp/pgjwt)
