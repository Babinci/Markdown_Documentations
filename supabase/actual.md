# Auth

## Use Supabase to authenticate and authorize your users.

# Auth architecture

## The architecture behind Supabase Auth.

---

There are four major layers to Supabase Auth:

1. [Client layer](#client-layer) This can be one of the Supabase client SDKs, or manually made HTTP requests using the HTTP client of your choice.
2. Kong API gateway. This is shared between all Supabase products.
3. [Auth service](#auth-service) (formerly known as GoTrue).
4. [Postgres database](#postgres) This is shared between all Supabase products.

## Client layer

The client layer runs in your app. This could be running in many places, including:

* Your frontend browser code
* Your backend server code
* Your native application

The client layer provides the functions that you use to sign in and manage users. We recommend using the Supabase client SDKs, which handle:

* Configuration and authentication of HTTP calls to the Supabase Auth backend
* Persistence, refresh, and removal of Auth Tokens in your app's storage medium
* Integration with other Supabase products

But at its core, this layer manages the making of HTTP calls, so you could write your own client layer if you wanted to.

See the Client SDKs for more information:

* JavaScript
* Flutter
* Swift
* Python
* C#
* Kotlin

## Auth service

The Auth service is an Auth API server written and maintained by Supabase. It is a fork of the GoTrue project, originally created by Netlify.

When you deploy a new Supabase project, we deploy an instance of this server alongside your database, and inject your database with the required Auth schema.

The Auth service is responsible for:

* Validating, issuing, and refreshing JWTs
* Serving as the intermediary between your app and Auth information in the database
* Communicating with external providers for Social Login and SSO

## Postgres

Supabase Auth uses the `auth` schema in your Postgres database to store user tables and other information. For security, this schema is not exposed on the auto-generated API.

You can connect Auth information to your own objects using database triggers and foreign keys. Make sure that any views you create for Auth data are adequately protected by enabling RLS or revoking grants.

Make sure any views you create for Auth data are protected.

Starting in Postgres version 15, views inherit the RLS policies of the underlying tables if created with `security_invoker`. Views in earlier versions, or those created without `security_invoker`, inherit the permissions of the owner, who can bypass RLS policies.

# Users

---

A **user** in Supabase Auth is someone with a user ID, stored in the Auth schema. Once someone is a user, they can be issued an Access Token, which can be used to access Supabase endpoints. The token is tied to the user, so you can restrict access to resources via [RLS policies].

## Permanent and anonymous users

Supabase distinguishes between permanent and anonymous users.

* **Permanent users** are tied to a piece of Personally Identifiable Information (PII), such as an email address, a phone number, or a third-party identity. They can use these identities to sign back into their account after signing out.
* **Anonymous users** aren't tied to any identities. They have a user ID and a personalized Access Token, but they have no way of signing back in as the same user if they are signed out.

Anonymous users are useful for:

* E-commerce applications, to create shopping carts before checkout
* Full-feature demos without collecting personal information
* Temporary or throw-away accounts

See the Anonymous Signins guide to learn more about anonymous users.

##### Anonymous users do not use the anon role

Just like permanent users, anonymous users use the **authenticated** role for database access.

The **anon** role is for those who aren't signed in at all and are not tied to any user ID. We refer to these as unauthenticated or public users.

## The user object

The user object stores all the information related to a user in your application. The user object can be retrieved using one of these methods:

1. `supabase.auth.getUser()`
2. Retrieve a user object as an admin using `supabase.auth.admin.getUserById()`

A user can sign in with one of the following methods:

* Password-based method (with email or phone)
* Passwordless method (with email or phone)
* OAuth
* SAML SSO

An identity describes the authentication method that a user can use to sign in. A user can have multiple identities. These are the types of identities supported:

* Email
* Phone
* OAuth
* SAML

A user with an email or phone identity will be able to sign in with either a password or passwordless method (e.g. use a one-time password (OTP) or magic link). By default, a user with an unverified email or phone number will not be able to sign in.

The user object contains the following attributes:

| Attributes | Type | Description |
| --- | --- | --- |
| id | `string` | The unique id of the identity of the user. |
| aud | `string` | The audience claim. |
| role | `string` | The role claim used by Postgres to perform Row Level Security (RLS) checks. |
| email | `string` | The user's email address. |
| email\_confirmed\_at | `string` | The timestamp that the user's email was confirmed. If null, it means that the user's email is not confirmed. |
| phone | `string` | The user's phone number. |
| phone\_confirmed\_at | `string` | The timestamp that the user's phone was confirmed. If null, it means that the user's phone is not confirmed. |
| confirmed\_at | `string` | The timestamp that either the user's email or phone was confirmed. If null, it means that the user does not have a confirmed email address and phone number. |
| last\_sign\_in\_at | `string` | The timestamp that the user last signed in. |
| app\_metadata | `object` | The `provider` attribute indicates the first provider that the user used to sign up with. The `providers` attribute indicates the list of providers that the user can use to login with. |
| user\_metadata | `object` | Defaults to the first provider's identity data but can contain additional custom user metadata if specified. |
| identities | `UserIdentity[]` | Contains an object array of identities linked to the user. |
| created\_at | `string` | The timestamp that the user was created. |
| updated\_at | `string` | The timestamp that the user was last updated. |
| is\_anonymous | `boolean` | Is true if the user is an anonymous user. |

## Resources

* User Management guide

# Identities

---

An identity is an authentication method associated with a user. Supabase Auth supports the following types of identity:

* Email
* Phone
* OAuth
* SAML

A user can have more than one identity. Anonymous users have no identity until they link an identity to their user.

## The user identity object

The user identity object contains the following attributes:

| Attributes | Type | Description |
| --- | --- | --- |
| provider\_id | `string` | The provider id returned by the provider. If the provider is an OAuth provider, the id refers to the user's account with the OAuth provider. If the provider is `email` or `phone`, the id is the user's id from the `auth.users` table. |
| user\_id | `string` | The user's id that the identity is linked to. |
| identity\_data | `object` | The identity metadata. For OAuth and SAML identities, this contains information about the user from the provider. |
| id | `string` | The unique id of the identity. |
| provider | `string` | The provider name. |
| email | `string` | The email is a generated column that references the optional email property in the identity\_data |
| created\_at | `string` | The timestamp that the identity was created. |
| last\_sign\_in\_at | `string` | The timestamp that the identity was last used to sign in. |
| updated\_at | `string` | The timestamp that the identity was last updated. |

# User sessions

---

Supabase Auth provides fine-grained control over your user's sessions.

Some security sensitive applications, or those that need to be SOC 2, HIPAA, PCI-DSS or ISO27000 compliant will require some sort of additional session controls to enforce timeouts or provide additional security guarantees. Supabase Auth makes it easy to build compliant applications.

## What is a session?

A session is created when a user signs in. By default, it lasts indefinitely and a user can have an unlimited number of active sessions on as many devices.

A session is represented by the Supabase Auth access token in the form of a JWT, and a refresh token which is a unique string.

Access tokens are designed to be short lived, usually between 5 minutes and 1 hour while refresh tokens never expire but can only be used once. You can exchange a refresh token only once to get a new access and refresh token pair.

This process is called **refreshing the session.**

A session terminates, depending on configuration, when:

* The user clicks sign out.
* The user changes their password or performs a security sensitive action.
* It times out due to inactivity.
* It reaches its maximum lifetime.
* A user signs in on another device.

## Access token (JWT) claims

Every access token contains a `session_id` claim, a UUID, uniquely identifying the session of the user. You can correlate this ID with the primary key of the `auth.sessions` table.

## Initiating a session

A session is initiated when a user signs in. The session is stored in the `auth.sessions` table, and your app should receive the access and refresh tokens.

There are two flows for initiating a session and receiving the tokens:

* Implicit flow
* PKCE flow

## Limiting session lifetime and number of allowed sessions per user

This feature is only available on Pro Plans and up.

Supabase Auth can be configured to limit the lifetime of a user's session. By default, all sessions are active until the user signs out or performs some other action that terminates a session.

In some applications, it's useful or required for security to ensure that users authenticate often, or that sessions are not left active on devices for too long.

There are three ways to limit the lifetime of a session:

* Time-boxed sessions, which terminate after a fixed amount of time.
* Set an inactivity timeout, which terminates sessions that haven't been refreshed within the timeout duration.
* Enforce a single-session per user, which only keeps the most recently active session.

To make sure that users are required to re-authenticate periodically, you can set a positive value for the **Time-box user sessions** option in the Auth settings for your project.

To make sure that sessions expire after a period of inactivity, you can set a positive duration for the **Inactivity timeout** option in the Auth settings.

You can also enforce only one active session per user per device or browser. When this is enabled, the session from the most recent sign in will remain active, while the rest are terminated. Enable this via the *Single session per user* option in the Auth settings.

Sessions are not proactively destroyed when you change these settings, but rather the check is enforced whenever a session is refreshed next. This can confuse developers because the actual duration of a session is the configured timeout plus the JWT expiration time. For single session per user, the effect will only be noticed at intervals of the JWT expiration time. Make sure you adjust this setting depending on your needs. We do not recommend going below 5 minutes for the JWT expiration time.

Otherwise sessions are progressively deleted from the database 24 hours after they expire, which prevents you from causing a high load on your project by accident and allows you some freedom to undo changes without adversely affecting all users.

## Frequently asked questions

### What are recommended values for access token (JWT) expiration?

Most applications should use the default expiration time of 1 hour. This can be customized in your project's Auth settings in the Advanced Settings section.

Setting a value over 1 hour is generally discouraged for security reasons, but it may make sense in certain situations.

Values below 5 minutes, and especially below 2 minutes, should not be used in most situations because:

* The shorter the expiration time, the more frequently refresh tokens are used, which increases the load on the Auth server.
* Time is not absolute. Servers can often be off sync for tens of seconds, but user devices like laptops, desktops or mobile devices can sometimes be off by minutes or even hours. Having too short expiration time can cause difficult-to-debug errors due to clock skew.
* Supabase's client libraries always try to refresh the session ahead of time, which won't be possible if the expiration time is too short.
* Access tokens should generally be valid for at least as long as the longest running request in your application. This helps you avoid issues where the access token becomes invalid midway through processing.

### What is refresh token reuse detection and what does it protect from?

As your users continue using your app, refresh tokens are being constantly exchanged for new access tokens.

The general rule is that a refresh token can only be used once. However, strictly enforcing this can cause certain issues to arise. There are two exceptions to this design to prevent the early and unexpected termination of user's sessions:

* A refresh token can be used more than once within a defined reuse interval. By default this is 10 seconds and we do not recommend changing this value. This exception is granted for legitimate situations such as:
  + Using server-side rendering where the same refresh token needs to be reused on the server and soon after on the client
  + To allow some leeway for bugs or issues with serializing access to the refresh token request
* If the parent of the currently active refresh token for the user's session is being used, the active token will be returned. This exception solves an important and often common situation:
  + All clients such as browsers, mobile or desktop apps, and even some servers are inherently unreliable due to network issues. A request does not indicate that they received a response or even processed the response they received.
  + If a refresh token is revoked after being used only once, and the response wasn't received and processed by the client, when the client comes back online, it will attempt to use the refresh token that was already used. Since this might happen outside of the reuse interval, it can cause sudden and unexpected session termination.

Should the reuse attempt not fall under these two exceptions, the whole session is regarded as terminated and all refresh tokens belonging to it are marked as revoked. You can disable this behavior in the Advanced Settings of the Auth settings page, though it is generally not recommended.

The purpose of this mechanism is to guard against potential security issues where a refresh token could have been stolen from the user, for example by exposing it accidentally in logs that leak (like logging cookies, request bodies or URL params) or via vulnerable third-party servers. It does not guard against the case where a user's session is stolen from their device.

### What are the benefits of using access and refresh tokens instead of traditional sessions?

Traditionally user sessions were implemented by using a unique string stored in cookies that identified the authorization that the user had on a specific browser. Applications would use this unique string to constantly fetch the attached user information on every API call.

This approach has some tradeoffs compared to using a JWT-based approach:

* If the authentication server or its database crashes or is unavailable for even a few seconds, the whole application goes down. Scheduling maintenance or dealing with transient errors becomes very challenging.
* A failing authentication server can cause a chain of failures across other systems and APIs, paralyzing the whole application system.
* All requests that require authentication has to be routed through the authentication, which adds an additional latency overhead to all requests.

Supabase Auth prefers a JWT-based approach using access and refresh tokens because session information is encoded within the short-lived access token, enabling transfer across APIs and systems without dependence on a central server's availability or performance. This approach enhances an application's tolerance to transient failures or performance issues. Furthermore, proactively refreshing the access token allows the application to function reliably even during significant outages.

It's better for cost optimization and scaling as well, as the authentication system's servers and database only handle traffic for this use case.

### How to ensure an access token (JWT) cannot be used after a user signs out

Most applications rarely need such strong guarantees. Consider adjusting the JWT expiry time to an acceptable value. If this is still necessary, you should try to use this validation logic only for the most sensitive actions within your application.

When a user signs out, the sessions affected by the logout are removed from the database entirely. You can check that the `session_id` claim in the JWT corresponds to a row in the `auth.sessions` table. If such a row does not exist, it means that the user has logged out.

Note that sessions are not proactively terminated when their maximum lifetime (time-box) or inactivity timeout are reached. These sessions are cleaned up progressively 24 hours after reaching that status. This allows you to tweak the values or roll back changes without causing unintended user friction.

### Using HTTP-only cookies to store access and refresh tokens

This is possible, but only for apps that use the traditional server-only web app approach where all of the application logic is implemented on the server and it returns rendered HTML only.

If your app uses any client side JavaScript to build a rich user experience, using HTTP-Only cookies is not feasible since only your server will be able to read and refresh the session of the user. The browser will not have access to the access and refresh tokens.

Because of this, the Supabase JavaScript libraries provide only limited support. You can override the `storage` option when creating the Supabase client **on the server** to store the values in cookies or your preferred storage choice, for example:

```
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
  auth: {
    storage: customStorageObject,
  },
})
```

The `customStorageObject` should implement the `getItem`, `setItem`, and `removeItem` methods from the `Storage` interface. Async versions of these methods are also supported.

When using cookies to store access and refresh tokens, make sure that the `Expires` or `Max-Age` attributes of the cookies is set to a timestamp very far into the future. Browsers will clear the cookies, but the session will remain active in Supabase Auth. Therefore it's best to let Supabase Auth control the validity of these tokens and instruct the browser to always store the cookies indefinitely.

# Password-based Auth

## Allow users to sign in with a password connected to their email or phone number.

---

Users often expect to sign in to your site with a password. Supabase Auth helps you implement password-based auth safely, using secure configuration options and best practices for storing and verifying passwords.

Users can associate a password with their identity using their email address or a phone number.

## With email

### Enabling email and password-based authentication

Email authentication is enabled by default.

You can configure whether users need to verify their email to sign in. On hosted Supabase projects, this is true by default. On self-hosted projects or in local development, this is false by default.

Change this setting on the Auth Providers page for hosted projects, or in the configuration file for self-hosted projects.

### Signing up with an email and password

There are two possible flows for email signup: implicit flow and PKCE flow. If you're using SSR, you're using the PKCE flow. If you're using client-only code, the default flow depends upon the client library. The implicit flow is the default in JavaScript and Dart, and the PKCE flow is the default in Swift.

The instructions in this section assume that email confirmations are enabled.

#### Implicit flow

The implicit flow only works for client-only apps. Your site directly receives the access token after the user confirms their email.

To sign up the user, call `signUp()` with their email address and password.

You can optionally specify a URL to redirect to after the user clicks the confirmation link. This URL must be configured as a Redirect URL, which you can do in the dashboard for hosted projects, or in the configuration file for self-hosted projects.

If you don't specify a redirect URL, the user is automatically redirected to your site URL. This defaults to `localhost:3000`, but you can also configure this.

```javascript
async function signUpNewUser() {
  const { data, error } = await supabase.auth.signUp({
    email: 'valid.email@supabase.io',
    password: 'example-password',
    options: {
      emailRedirectTo: 'https://example.com/welcome',
    },
  })
}
```

### Signing in with an email and password

When your user signs in, call `signInWithPassword()` with their email address and password:

```javascript
async function signInWithEmail() {
  const { data, error } = await supabase.auth.signInWithPassword({
    email: 'valid.email@supabase.io',
    password: 'example-password',
  })
}
```

### Resetting a password

#### Step 1: Create a reset password page

Create a **reset password** page. This page should be publicly accessible.

Collect the user's email address and request a password reset email. Specify the redirect URL, which should point to the URL of a **change password** page. This URL needs to be configured in your redirect URLs.

```javascript
await supabase.auth.resetPasswordForEmail('valid.email@supabase.io', {
  redirectTo: 'http://example.com/account/update-password',
})
```

#### Step 2: Create a change password page

Create a **change password** page at the URL you specified in the previous step. This page should be accessible only to authenticated users.

Collect the user's new password and call `updateUser` to update their password.

```javascript
await supabase.auth.updateUser({ password: new_password })
```

### Email sending

The signup confirmation and password reset flows require an SMTP server to send emails.

The Supabase platform comes with a default email-sending service for you to try out. The service has a rate limit of 2 emails per hour, and availability is on a best-effort basis. For production use, you should consider configuring a custom SMTP server.

Consider configuring a custom SMTP server for production.

See the Custom SMTP guide for instructions.

#### Local development with Inbucket

You can test email flows on your local machine. The Supabase CLI automatically captures emails sent locally by using Inbucket.

In your terminal, run `supabase status` to get the Inbucket URL. Go to this URL in your browser, and follow the instructions to find your emails.

## With phone

You can use a user's mobile phone number as an identifier, instead of an email address, when they sign up with a password.

This practice is usually discouraged because phone networks recycle mobile phone numbers. Anyone receiving a recycled phone number gets access to the original user's account. To mitigate this risk, implement MFA.

Protect users who use a phone number as a password-based auth identifier by enabling MFA.

### Enabling phone and password-based authentication

Enable phone authentication on the Auth Providers page for hosted Supabase projects.

For self-hosted projects or local development, use the configuration file. See the configuration variables namespaced under `auth.sms`.

If you want users to confirm their phone number on signup, you need to set up an SMS provider. Each provider has its own configuration. Supported providers include MessageBird, Twilio, Vonage, and TextLocal (community-supported).

### Signing up with a phone number and password

To sign up the user, call `signUp()` with their phone number and password:

```javascript
const { data, error } = await supabase.auth.signUp({
  phone: '+13334445555',
  password: 'some-password',
})
```

If you have phone verification turned on, the user receives an SMS with a 6-digit pin that you must verify within 60 seconds:

You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyOtp`:

```javascript
const {
  data: { session },
  error,
} = await supabase.auth.verifyOtp({
  phone: '+13334445555',
  token: '123456',
  type: 'sms',
})
```

### Signing in a with a phone number and password

Call the function to sign in with the user's phone number and password:

```javascript
const { data, error } = await supabase.auth.signInWithPassword({
  phone: '+13334445555',
  password: 'some-password',
})
```

# Self-Hosting with Docker

## Learn how to configure and deploy Supabase with Docker.

---

Docker is the easiest way to get started with self-hosted Supabase. It should only take you a few minutes to get up and running. This guide assumes you are running the command from the machine you intend to host from.

## Contents

1. [Before you begin](#before-you-begin)
2. [Installing and running Supabase](#installing-and-running-supabase)
3. [Accessing your services](#accessing-supabase-studio)
4. [Updating your services](#updating-your-services)
5. [Securing your services](#securing-your-services)

## Before you begin

You need the following installed in your system: Git and Docker (Windows, macOS, or Linux).

## Installing and running Supabase

Follow these steps to start Supabase on your machine:

```bash
# Get the code
git clone --depth 1 https://github.com/supabase/supabase

# Go to the docker folder
cd supabase/docker

# Copy the fake env vars
cp .env.example .env

# Pull the latest images
docker compose pull

# Start the services (in detached mode)
docker compose up -d
```

If you are using rootless docker, edit `.env` and set `DOCKER_SOCKET_LOCATION` to your docker socket location. For example: `/run/user/1000/docker.sock`. Otherwise, you will see an error like `container supabase-vector exited (0)`.

After all the services have started you can see them running in the background:

```bash
docker compose ps
```

All of the services should have a status `running (healthy)`. If you see a status like `created` but not `running`, try starting that service manually with `docker compose start <service-name>`.

Your app is now running with default credentials.
[Secure your services](#securing-your-services) as soon as possible using the instructions below.

### Accessing Supabase Studio

You can access Supabase Studio through the API gateway on port `8000`. For example: `http://<your-ip>:8000`, or localhost:8000 if you are running Docker locally.

You will be prompted for a username and password. By default, the credentials are:

* Username: `supabase`
* Password: `this_password_is_insecure_and_should_be_updated`

You should change these credentials as soon as possible using the [instructions](#dashboard-authentication) below.

### Accessing the APIs

Each of the APIs are available through the same API gateway:

* REST: `http://<your-ip>:8000/rest/v1/`
* Auth: `http://<your-domain>:8000/auth/v1/`
* Storage: `http://<your-domain>:8000/storage/v1/`
* Realtime: `http://<your-domain>:8000/realtime/v1/`

### Accessing your Edge Functions

Edge Functions are stored in `volumes/functions`. The default setup has a `hello` Function that you can invoke on `http://<your-domain>:8000/functions/v1/hello`.

You can add new Functions as `volumes/functions/<FUNCTION_NAME>/index.ts`. Restart the `functions` service to pick up the changes: `docker compose restart functions --no-deps`

### Accessing Postgres

By default, the Supabase stack runs the Supavisor connection pooler. Supavisor provides efficient management of database connections.

You can connect to the Postgres database using the following methods:

1. For session-based connections (equivalent to direct Postgres connections):

```bash
psql 'postgres://postgres.your-tenant-id:your-super-secret-and-long-postgres-password@localhost:5432/postgres'
```

2. For pooled transactional connections:

```bash
psql 'postgres://postgres.your-tenant-id:your-super-secret-and-long-postgres-password@localhost:6543/postgres'
```

The default tenant ID is `your-tenant-id`, and the default password is `your-super-secret-and-long-postgres-password`. You should change these as soon as possible using the instructions below.

By default, the database is not accessible from outside the local machine but the pooler is. You can change this by updating the `docker-compose.yml` file.

## Updating your services

For security reasons, we "pin" the versions of each service in the docker-compose file (these versions are updated ~monthly). If you want to update any services immediately, you can do so by updating the version number in the docker compose file and then running `docker compose pull`. You can find all the latest docker images in the Supabase Docker Hub.

You should update your services frequently to get the latest features and bug fixes and security patches. Note that you will need to restart the services to pick up the changes, which will result in some downtime for your services.

**Example**
You'll want to update the Studio(Dashboard) frequently to get the latest features and bug fixes. To update the Dashboard:

1. Visit the supabase/studio image in the Supabase Docker Hub
2. Find the latest version (tag) number. It will look something like `20241029-46e1e40`
3. Update the `image` field in the `docker-compose.yml` file to the new version. It should look like this: `image: supabase/studio:20241028-a265374`
4. Run `docker compose pull` and then `docker compose up -d` to restart the service with the new version.

## Securing your services

While we provided you with some example secrets for getting started, you should NEVER deploy your Supabase setup using the defaults we have provided. Follow all of the steps in this section to ensure you have a secure setup, and then restart all services to pick up the changes.

### Generate API keys

We need to generate secure keys for accessing your services. We'll use the `JWT Secret` to generate `anon` and `service` API keys using the form below.

1. **Obtain a Secret**: Use the 40-character secret provided, or create your own. If creating, ensure it's a strong, random string of 40 characters.
2. **Store Securely**: Save the secret in a secure location on your local machine. Don't share this secret publicly or commit it to version control.
3. **Generate a JWT**: Use the form below to generate a new `JWT` using your secret.

### Update API keys

Run this form twice to generate new `anon` and `service` API keys. Replace the values in the `./docker/.env` file:

* `ANON_KEY` - replace with an `anon` key
* `SERVICE_ROLE_KEY` - replace with a `service` key

You will need to restart the services for the changes to take effect.

### Update secrets

Update the `./docker/.env` file with your own secrets. In particular, these are required:

* `POSTGRES_PASSWORD`: the password for the `postgres` role.
* `JWT_SECRET`: used by PostgREST and GoTrue, among others.
* `SITE_URL`: the base URL of your site.
* `SMTP_*`: mail server credentials. You can use any SMTP server.
* `POOLER_TENANT_ID`: the tenant-id that will be used by Supavisor pooler for your connection string

You will need to restart the services for the changes to take effect.

### Dashboard authentication

The Dashboard is protected with basic authentication. The default user and password MUST be updated before using Supabase in production.
Update the following values in the `./docker/.env` file:

* `DASHBOARD_USERNAME`: The default username for the Dashboard
* `DASHBOARD_PASSWORD`: The default password for the Dashboard

You can also add more credentials for multiple users in `./docker/volumes/api/kong.yml`. For example:

```yaml
basicauth_credentials:
  - consumer: DASHBOARD
    username: user_one
    password: password_one
  - consumer: DASHBOARD
    username: user_two
    password: password_two
```

To enable all dashboard features outside of `localhost`, update the following value in the `./docker/.env` file:

* `SUPABASE_PUBLIC_URL`: The URL or IP used to access the dashboard

You will need to restart the services for the changes to take effect.

## Restarting all services

You can restart services to pick up any configuration changes by running:

```bash
# Stop and remove the containers
docker compose down
# Recreate and start the containers
docker compose up -d
```

Be aware that this will result in downtime. Simply restarting the services does not apply configuration changes.

## Stopping all services

You can stop Supabase by running `docker compose stop` in same directory as your `docker-compose.yml` file.

## Uninstalling

You can stop Supabase by running the following in same directory as your `docker-compose.yml` file:

```bash
# Stop docker and remove volumes:
docker compose down -v
# Remove Postgres data:
rm -rf volumes/db/data/
```

This will destroy all data in the database and storage volumes, so be careful!

---

Supabase Auth makes it easy to implement authentication and authorization in your app. We provide client SDKs and API endpoints to help you create and manage users.

Your users can use many popular Auth methods, including password, magic link, one-time password (OTP), social login, and single sign-on (SSO).

## About authentication and authorization

Authentication and authorization are the core responsibilities of any Auth system.

* **Authentication** means checking that a user is who they say they are.
* **Authorization** means checking what resources a user is allowed to access.

Supabase Auth uses [JSON Web Tokens (JWTs)] for authentication. Auth integrates with Supabase's database features, making it easy to use [Row Level Security (RLS)] for authorization.

## The Supabase ecosystem

You can use Supabase Auth as a standalone product, but it's also built to integrate with the Supabase ecosystem.

Auth uses your project's Postgres database under the hood, storing user data and other Auth information in a special schema. You can connect this data to your own tables using triggers and foreign key references.

Auth also enables access control to your database's automatically generated [REST API]. When using Supabase SDKs, your data requests are automatically sent with the user's Auth Token. The Auth Token scopes database access on a row-by-row level when used along with [RLS policies].

## Providers

Supabase Auth works with many popular Auth methods, including Social and Phone Auth using third-party providers. See the following sections for a list of supported third-party providers.

### Social Auth

- Apple
- Azure (Microsoft)
- Bitbucket
- Discord
- Facebook
- Figma
- GitHub
- GitLab
- Google
- Kakao
- Keycloak
- LinkedIn
- Notion
- Slack
- Spotify
- Twitter
- Twitch
- WorkOS
- Zoom

### Phone Auth

- MessageBird
- Twilio
- Vonage

## Pricing

Charges apply to Monthly Active Users (MAU), Monthly Active Third-Party Users (Third-Party MAU), and Monthly Active SSO Users (SSO MAU) and Advanced MFA Add-ons. For a detailed breakdown of how these charges are calculated, refer to the following pages:

* [Pricing MAU]
* [Pricing Third-Party MAU]
* [Pricing SSO MAU]
* [Advanced MFA - Phone]
