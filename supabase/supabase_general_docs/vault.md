# Vault

## Managing secrets in Postgres

Vault is a Postgres extension and accompanying Supabase UI that makes it safe and easy to store encrypted secrets and other data in your database. This opens up a lot of possibilities to use Postgres in ways that go beyond what is available in a stock distribution.

Under the hood, the Vault is a table of Secrets and Encryption Keys that are stored using [Authenticated Encryption](https://en.wikipedia.org/wiki/Authenticated_encryption) on disk. They are then available in decrypted form through a Postgres view so that the secrets can be used by applications from SQL. Because the secrets are stored on disk encrypted and authenticated, any backups or replication streams also preserve this encryption in a way that can't be decrypted or forged.

Supabase provides a dashboard UI for the Vault that makes storing secrets easy. Click a button, type in your secret, and save. Optionally create your own keys you can use to encrypt your secret. Your secret will then be stored on disk encrypted using the specified key.

There are two main parts to the Vault UI, Secrets and Encryption Keys:

## Secrets

You can use the Vault to store secrets - everything from Environment Variables to API Keys. You can then use these secrets anywhere in your database: Postgres [Functions](https://supabase.com/docs/guides/database/functions), Triggers, and [Webhooks](https://supabase.com/docs/guides/database/webhooks). From a SQL perspective, accessing secrets is as easy as querying a table (or in this case, a view). The underlying secrets tables will be stored in encrypted form.

## Encryption keys

These are keys used to encrypt data inside your database. You can create different Encryption Keys for different purposes, for example: one for encrypting user-data, and another for application-data. Each key is encrypted itself using a root encryption key that lives outside of the database. See **[Encryption key location](#encryption-key-location)** for more details.

## Using the Vault

You can manage secrets and encryption keys from the UI or using SQL.

### Adding secrets

There is also a handy function for creating secrets called `vault.create_secret()`:

```sql
select vault.create_secret('my_s3kre3t');
```

The function returns the UUID of the new secret.

```
-[ RECORD 1 ]-+-------------------------------------
create_secret | c9b00867-ca8b-44fc-a81d-d20b8169be17
```

Secrets can also have an optional _unique_ name and an optional description. These are also arguments to `vault.create_secret()`:

```sql
select vault.create_secret('another_s3kre3t', 'unique_name', 'This is the description');
```

```
-[ RECORD 1 ]-----------------------------------------------------------------
id          | 7095d222-efe5-4cd5-b5c6-5755b451e223
name        | unique_name
description | This is the description
secret      | 3mMeOcoG84a5F2uOfy2ugWYDp9sdxvCTmi6kTeT97bvA8rCEsG5DWWZtTU8VVeE=
key_id      | c62da7a0-b85d-471d-8ea7-52aae21d7354
nonce       | \x9f2d60954ba5eb566445736e0760b0e3
created_at  | 2022-12-14 02:34:23.85159+00
updated_at  | 2022-12-14 02:34:23.85159+00
```

Alternatively, you can create a secret by inserting data into the `vault.secret` table:

```sql
insert into vault.secrets (secret)
values ('s3kre3t_k3y') returning *;
```

```
-[ RECORD 1 ]-------------------------------------------------------------
id          | d91596b8-1047-446c-b9c0-66d98af6d001
name        | 
description | 
secret      | S02eXS9BBY+kE3r621IS8beAytEEtj+dDHjs9/0AoMy7HTbog+ylxcS22A==
key_id      | 7f5ad44b-6bd5-4c99-9f68-4b6c7486f927
nonce       | \x3aa2e92f9808e496aa4163a59304b895
created_at  | 2022-12-14 02:29:21.3625+00
updated_at  | 2022-12-14 02:29:21.3625+00
```

### Viewing secrets

If you look in the `vault.secrets` table, you will see that your data is stored encrypted. To decrypt the data, there is an automatically created view `vault.decrypted_secrets`. This view will decrypt secret data on the fly:

```sql
select * from vault.decrypted_secrets order by created_at desc limit 3;
```

```
-[ RECORD 1 ]----+-----------------------------------------------------------------
id               | 7095d222-efe5-4cd5-b5c6-5755b451e223
name             | unique_name
description      | This is the description
secret           | 3mMeOcoG84a5F2uOfy2ugWYDp9sdxvCTmi6kTeT97bvA8rCEsG5DWWZtTU8VVeE=
decrypted_secret | another_s3kre3t
key_id           | c62da7a0-b85d-471d-8ea7-52aae21d7354
nonce            | \x9f2d60954ba5eb566445736e0760b0e3
created_at       | 2022-12-14 02:34:23.85159+00
updated_at       | 2022-12-14 02:34:23.85159+00
-[ RECORD 2 ]----+-----------------------------------------------------------------
id               | c9b00867-ca8b-44fc-a81d-d20b8169be17
name             | 
description      | 
secret           | a1CE4vXwQ53+N9bllJj1D7fasm59ykohjb7K90PPsRFUd9IbBdxIGZNoSQLIXl4=
decrypted_secret | another_s3kre3t
key_id           | 8c72b05e-b931-4372-abf9-a09cfad18489
nonce            | \x1d3b2761548c4efb2d29ca11d44aa22f
created_at       | 2022-12-14 02:32:50.58921+00
updated_at       | 2022-12-14 02:32:50.58921+00
-[ RECORD 3 ]----+-----------------------------------------------------------------
id               | d91596b8-1047-446c-b9c0-66d98af6d001
name             | 
description      | 
secret           | S02eXS9BBY+kE3r621IS8beAytEEtj+dDHjs9/0AoMy7HTbog+ylxcS22A==
decrypted_secret | s3kre3t_k3y
key_id           | 7f5ad44b-6bd5-4c99-9f68-4b6c7486f927
nonce            | \x3aa2e92f9808e496aa4163a59304b895
created_at       | 2022-12-14 02:29:21.3625+00
updated_at       | 2022-12-14 02:29:21.3625+00
```

Notice how this view has a `decrypted_secret` column that contains the decrypted secrets. Views are not stored on disk, they are only run at query time, so the secret remains encrypted on disk, and in any backup dumps or replication streams.

You should ensure that you protect access to this view with the appropriate SQL privilege settings at all times, as anyone that has access to the view has access to decrypted secrets.

### Updating secrets

A secret can be updated with the `vault.update_secret()` function, this function makes updating secrets easy, just provide the secret UUID as the first argument, and then an updated secret, updated optional unique name, or updated description:

```sql
select 
  vault.update_secret(
    '7095d222-efe5-4cd5-b5c6-5755b451e223',
    'n3w_upd@ted_s3kret',
    'updated_unique_name',
    'This is the updated description'
  );
```

```
-[ RECORD 1 ]-+-
update_secret |

postgres=> select * from vault.decrypted_secrets where id = '7095d222-efe5-4cd5-b5c6-5755b451e223';
-[ RECORD 1 ]----+---------------------------------------------------------------------
id               | 7095d222-efe5-4cd5-b5c6-5755b451e223
name             | updated_unique_name
description      | This is the updated description
secret           | lhb3HBFxF+qJzp/HHCwhjl4QFb5dYDsIQEm35DaZQOovdkgp2iy6UMufTKJGH4ThMrU=
decrypted_secret | n3w_upd@ted_s3kret
key_id           | c62da7a0-b85d-471d-8ea7-52aae21d7354
nonce            | \x9f2d60954ba5eb566445736e0760b0e3
created_at       | 2022-12-14 02:34:23.85159+00
updated_at       | 2022-12-14 02:51:13.938396+00
```

## Deep dive

As we mentioned, the Vault uses `pgsodium`'s Transparent Column Encryption (TCE) to store secrets in an authenticated encrypted form. There are some details around that you may be curious about, what does authenticated mean, and where are encryption keys store? This section explains those details.

### Authenticated encryption with associated data

The first important feature of TCE is that it uses an [Authenticated Encryption with Associated Data](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data_(AEAD)) encryption algorithm (based on `libsodium`).

### Encryption key location

**Authenticated Encryption** means that in addition to the data being encrypted, it is also signed so that it cannot be forged. You can guarantee that the data was encrypted by someone you trust, which you wouldn't get with encryption alone. The decryption function verifies that the signature is valid _before decrypting the value_.

**Associated Data** means that you can include any other columns from the same row as part of the signature computation. This doesn't encrypt those other columns - rather it ensures that your encrypted value is only associated with columns from that row. If an attacker were to copy an encrypted value from another row to the current one, the signature would be rejected (assuming you used a unique column in the associated data).

Another important feature of `pgsodium` is that the encryption keys are never stored in the database alongside the encrypted data. Instead, only a **Key ID** is stored, which is a reference to the key that is only accessible outside of SQL. Even if an attacker can capture a dump of your entire database, they will see only encrypted data and key IDs, _never the raw key itself_.

This is an important safety precaution - there is little value in storing the encryption key in the database itself as this would be like locking your front door but leaving the key in the lock! Storing the key outside the database fixes this issue.

Where are the keys stored? Supabase creates and manages the root keys (from which all key IDs are derived) in our secured backend systems. We keep this root key safe and separate from your data. You remain in control of your keys - a separate API endpoint is available that you can use to access the key if you want to decrypt your data outside of Supabase.

### Internal details

To encrypt data, you need a _key id_. You can use the default key id created automatically for every project, or create your own key ids Using the `pgsodium.create_key()` function. Key ids are used to internally derive the encryption key used to encrypt secrets in the vault. Vault users typically do not have access to the key itself, only the key id.

Both `vault.create_secret()` and `vault.update_secret()` take an optional fourth `new_key_id` argument. This argument can be used to store a different key id for the secret instead of the default value.

```sql
select vault.create_secret(
  'another_s3kre3t_key', 
  'another_unique_name',
  'This is another description',
  (pgsodium.create_key()).id);
```

Result:

```
-[ RECORD 1 ]-+-------------------------------------
create_secret | cec9e005-a44d-4b19-86e1-febf3cd40619
```

Which roles should have access to the `vault.secrets` table should be carefully considered. There are two ways to grant access, the first is that the `postgres` user can explicitly grant access to the vault table itself.

## Resources

- Read more about Supabase Vault in the [blog post](https://supabase.com/blog/vault-now-in-beta)
- [Supabase Vault on GitHub](https://github.com/supabase/vault)
- [Column Encryption](https://supabase.com/docs/guides/database/column-encryption)
