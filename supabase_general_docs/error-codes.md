# Supabase Storage Error Codes

This guide explains the error codes you might encounter when working with Supabase Storage, along with troubleshooting steps for resolving them.

## Standard Error Format

Storage error codes are returned in the response body, helping you debug and understand what went wrong with your request. The errors follow this format:

```json
{
  "code": "error_code",
  "message": "error_message"
}
```

## Error Codes Reference

| Error Code | Description | Status Code | Resolution |
| --- | --- | --- | --- |
| `NoSuchBucket` | The specified bucket does not exist | 404 | Verify the bucket name exists or check permissions |
| `NoSuchKey` | The specified key does not exist | 404 | Check if the object exists or verify permissions |
| `NoSuchUpload` | The specified upload does not exist | 404 | Verify upload ID or check if upload was aborted |
| `InvalidJWT` | The provided JWT is invalid | 401 | JWT might be expired or malformed; provide a valid token |
| `InvalidRequest` | Request is not properly formed | 400 | Review request parameters (error message has details) |
| `TenantNotFound` | Specified tenant does not exist | 404 | Storage service provisioning issue - contact support |
| `EntityTooLarge` | Uploaded entity is too large | 413 | Check max-file-limit in project settings |
| `InternalError` | Internal server error occurred | 500 | Check logs or contact support for assistance |
| `ResourceAlreadyExists` | Resource already exists | 409 | Use a different name or use `x-upsert:true` header |
| `InvalidBucketName` | Bucket name is invalid | 400 | Follow bucket naming conventions |
| `InvalidKey` | Key is invalid | 400 | Ensure key follows naming conventions |
| `InvalidRange` | Range is not valid | 416 | Range must be within file size and follow HTTP Range spec |
| `InvalidMimeType` | MIME type is not valid | 400 | Provide valid MIME type in standard format |
| `InvalidUploadId` | Upload ID is invalid | 400 | Provide a valid active upload ID |
| `KeyAlreadyExists` | Key already exists | 409 | Use different key or `x-upsert:true` header |
| `BucketAlreadyExists` | Bucket already exists | 409 | Choose a unique bucket name |
| `DatabaseTimeout` | Database timeout occurred | 504 | Increase pool size or upgrade instance |
| `InvalidSignature` | Signature doesn't match | 403 | Check signature format (see SignatureV4 docs) |
| `SignatureDoesNotMatch` | Request signature mismatch | 403 | Verify credentials (key ID, secret key, region) |
| `AccessDenied` | Access to resource denied | 403 | Check RLS policy permissions |
| `ResourceLocked` | Resource is locked | 423 | Wait and retry request |
| `DatabaseError` | Database error occurred | 500 | Investigate database logs |
| `MissingContentLength` | Content-Length header missing | 411 | Include Content-Length header |
| `MissingParameter` | Required parameter missing | 400 | Provide all required parameters |
| `InvalidUploadSignature` | Upload signature invalid | 403 | Do not alter MultiPartUpload record during upload |
| `LockTimeout` | Lock timeout occurred | 423 | Wait and retry request |
| `S3Error` | S3-related error occurred | - | Check S3 documentation or contact support |
| `S3InvalidAccessKeyId` | AWS access key ID invalid | 403 | Verify access key ID |
| `S3MaximumCredentialsLimit` | Max credentials limit reached | 400 | Manage credentials within limits |
| `InvalidChecksum` | Entity checksum mismatch | 400 | Recalculate and verify checksum |
| `MissingPart` | Entity part is missing | 400 | Include all parts before completing operation |
| `SlowDown` | Request rate too high | 503 | Reduce request rate or implement backoff |

## Legacy Error Format

You may still encounter the older error format during the transition to the new system:

```json
{
  "httpStatusCode": 400,
  "code": "error_code",
  "message": "error_message"
}
```

## Common Error Scenarios and Solutions

### 404 `not_found`

Indicates the resource is not found or you lack permissions to access it.

**Resolution:**
- Add an RLS policy to grant permission to the resource (see [Access Control docs](https://supabase.com/docs/guides/storage/uploads/access-control))
- Include the user `Authorization` header in your request
- Verify the object exists in Storage

### 409 `already_exists`

Indicates the resource already exists.

**Resolution:**
- Use the `upsert` functionality to overwrite the file by setting the `x-upsert:true` header (see [Standard Uploads](https://supabase.com/docs/guides/storage/uploads/standard-uploads#overwriting-files))

### 403 `unauthorized`

You don't have permission for the requested action.

**Resolution:**
- Add or modify RLS policies to grant the necessary permissions (see [Access Control docs](https://supabase.com/docs/guides/storage/security/access-control))
- Ensure you include the user `Authorization` header
- Check that the authenticated user has the required permissions

### 429 `too many requests`

This occurs when many clients are concurrently using Storage and the pooler has reached its `max_clients` limit.

**Resolution:**
- Increase the `max_clients` limit of the pooler
- Upgrade to a larger compute instance through [project add-ons](https://supabase.com/dashboard/project/_/settings/addons)

### 544 `database_timeout`

This happens when Postgres doesn't have enough available connections to efficiently handle Storage requests.

**Resolution:**
- Increase the `pool_size` limit of the pooler
- Upgrade to a larger compute instance through [project add-ons](https://supabase.com/dashboard/project/_/settings/addons)

### 500 `internal_server_error`

An unhandled error occurred in the Storage service.

**Resolution:**
- File a support ticket through the [support portal](https://supabase.com/dashboard/support/new)