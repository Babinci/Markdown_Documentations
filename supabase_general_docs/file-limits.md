# Storage File Limits

This guide explains how to set and manage file size limits in Supabase Storage, both globally and at the bucket level.

## Global File Size Limits

Supabase allows you to set a maximum file size that applies across all storage buckets. This global limit can be configured in the [Storage Settings](https://supabase.com/dashboard/project/_/settings/storage) section of your Supabase dashboard.

### Plan-Specific Limits

Your maximum global file size depends on your Supabase subscription plan:

| Plan | Maximum File Size |
|------|-------------------|
| Free | 50 MB |
| Pro | 50 GB |
| Team | 50 GB |
| Enterprise | Custom (contact support) |

If you're on the Pro plan or higher and need to upload files larger than 50 GB, please [contact Supabase support](https://supabase.com/dashboard/support/new) to discuss your requirements.

### Setting the Global Limit

1. Navigate to your project's [Storage Settings](https://supabase.com/dashboard/project/_/settings/storage)
2. Find the "File Size Limit" section
3. Set your desired maximum file size (up to the plan-specific limit)
4. Save your changes

As a best practice, set the global limit to the largest file size your application needs to accept, then use bucket-specific limits for more granular control.

## Per-Bucket Restrictions

In addition to the global limit, you can set more specific restrictions at the individual bucket level. These per-bucket restrictions allow you to:

1. **Limit file sizes**: Set a maximum file size for a specific bucket (must be equal to or smaller than the global limit)
2. **Restrict file types**: Allow only certain file formats in a bucket (e.g., only PDFs, only images, etc.)

### Configuring Bucket-Specific Limits

You can set these restrictions when creating a new bucket or by editing an existing one:

#### When Creating a New Bucket:

1. Go to Storage in your Supabase dashboard
2. Click "Create a new bucket"
3. In the creation dialog, check "Restrict file upload types" and/or "Restrict file size"
4. Configure your specific restrictions
5. Complete the bucket creation process

#### For Existing Buckets:

1. Navigate to the bucket in your Storage dashboard
2. Click the settings icon next to the bucket name
3. Edit the file type or size restrictions as needed
4. Save your changes

For detailed instructions on bucket-specific restrictions, see the [Creating Buckets](https://supabase.com/docs/guides/storage/buckets/creating-buckets#restricting-uploads) documentation.

## Implementation Best Practices

1. **Global limits**: Set to the absolute maximum file size your application will ever need
2. **Bucket organization**: Create separate buckets for different file types or use cases
3. **Bucket-specific limits**:
   - For image uploads, restrict to image formats and appropriate sizes
   - For document storage, limit to document formats like PDF, DOCX, etc.
   - For video storage, set appropriate size limits based on your needs
4. **Client-side validation**: In addition to server-side limits, implement client-side validation to provide immediate feedback to users
5. **Progressive uploads**: For large files, consider implementing resumable uploads to improve user experience

## Monitoring and Adjusting Limits

Regularly review your storage usage patterns and adjust limits as needed. If you find that users frequently upload files close to your limits, consider increasing them to improve user experience.
