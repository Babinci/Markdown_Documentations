# Storage Image Transformations

Supabase Storage offers powerful functionality to optimize and resize images on the fly. Any image stored in your buckets can be transformed and optimized for fast delivery, improving your application's loading times and bandwidth usage.

> Note: Image Transformations are currently enabled for Pro Plan and above.

## Getting Started

### Get a Public URL for a Transformed Image

Our client libraries methods like `getPublicUrl` and `createSignedUrl` support the `transform` option, which returns a URL that serves the transformed image.

```javascript
supabase.storage.from('bucket').getPublicUrl('image.jpg', {
  transform: {
    width: 500,
    height: 600,
  },
})
```

The resulting URL will look something like:
```
https://project_id.supabase.co/storage/v1/render/image/public/bucket/image.jpg?width=500&height=600
```

### Signing URLs with Transformation Options

To share a transformed image in a private bucket for a fixed amount of time, provide the transform option when creating a signed URL:

```javascript
supabase.storage.from('bucket').createSignedUrl('image.jpg', 60000, {
  transform: {
    width: 200,
    height: 200,
  },
})
```

The transformation options are embedded into the token attached to the URL and cannot be changed once signed.

### Downloading Transformed Images

To download a transformed image, pass the `transform` option to the `download` function:

```javascript
supabase.storage.from('bucket').download('image.jpg', {
  transform: {
    width: 800,
    height: 300,
  },
})
```

## Automatic Image Optimization (WebP)

When using the image transformation API, Storage automatically detects the best format supported by the client and returns that format without any code changes. For example, if you're using Chrome to view a JPEG image with transformation options, the images are automatically optimized as WebP images.

This optimization reduces bandwidth usage and improves loading times for your application.

Currently, WebP is the only supported automatic optimization format, with AVIF support planned for the future.

### Disabling Automatic Optimization

If you prefer to maintain the original format of the image, you can opt-out of automatic format detection by passing the `format=origin` parameter:

```javascript
await supabase.storage.from('bucket').download('image.jpeg', {
  transform: {
    width: 200,
    height: 200,
    format: 'origin',
  },
})
```

## Next.js Integration

You can use Supabase Image Transformation with Next.js images by creating a custom loader:

1. Create a `supabase-image-loader.js` file in your Next.js project:

```javascript
const projectId = '' // your supabase project id

export default function supabaseLoader({ src, width, quality }) {
  return `https://${projectId}.supabase.co/storage/v1/render/image/public/${src}?width=${width}&quality=${quality || 75}`
}
```

2. Configure Next.js to use your custom loader in `next.config.js`:

```javascript
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './supabase-image-loader.js',
  },
}
```

3. Use the Next.js Image component as usual:

```javascript
import Image from 'next/image'

const MyImage = (props) => {
  return <Image src="bucket/image.png" alt="Picture of the author" width={500} height={500} />
}
```

## Transformation Options

### Optimizing

Adjust the quality of the returned image by setting a value from 20 to 100 (with 100 being the highest quality):

```javascript
supabase.storage.from('bucket').download('image.jpg', {
  transform: {
    quality: 50,
  },
})
```

The default quality is 80.

### Resizing

Use `width` and `height` parameters to resize an image to specific dimensions:

```javascript
supabase.storage.from('bucket').download('image.jpg', {
  transform: {
    width: 800,
    height: 300,
  },
})
```

If only one parameter is specified, the image will be resized and cropped while maintaining the aspect ratio.

### Resize Modes

Different resizing modes are available through the `resize` parameter:

- `cover` (default): Resizes the image while maintaining aspect ratio to fill the given dimensions, cropping any parts that exceed the bounds
- `contain`: Resizes the image while maintaining aspect ratio to fit within the given dimensions, with no cropping
- `fill`: Resizes the image without maintaining aspect ratio, potentially distorting the image

Example:

```javascript
supabase.storage.from('bucket').download('image.jpg', {
  transform: {
    width: 800,
    height: 300,
    resize: 'contain', // 'cover' | 'fill'
  },
})
```

## Limitations and Support

### Limits

- Width and height must be integers between 1-2500
- Maximum image size: 25MB
- Maximum image resolution: 50MP

### Supported Image Formats

| Format | Extension | Source | Result |
| --- | --- | --- | --- |
| PNG | `png` | ✓ | ✓ |
| JPEG | `jpg` | ✓ | ✓ |
| WebP | `webp` | ✓ | ✓ |
| AVIF | `avif` | ✓ | ✓ |
| GIF | `gif` | ✓ | ✓ |
| ICO | `ico` | ✓ | ✓ |
| SVG | `svg` | ✓ | ✓ |
| HEIC | `heic` | ✓ | ✗ |
| BMP | `bmp` | ✓ | ✓ |
| TIFF | `tiff` | ✓ | ✓ |

## Pricing

$5 per 1,000 origin images. You are only charged for usage exceeding your subscription plan's quota.

| Plan | Quota | Over-Usage |
| --- | --- | --- |
| Pro | 100 | $5 per 1,000 origin images |
| Team | 100 | $5 per 1,000 origin images |
| Enterprise | Custom | Custom |

For a detailed breakdown of how charges are calculated, refer to [Manage Storage Image Transformations usage](https://supabase.com/docs/guides/platform/manage-your-usage/storage-image-transformations).

## Self-Hosting

Supabase's image transformation solution can be self-hosted like other Supabase products. Under the hood, it uses [imgproxy](https://imgproxy.net/).

### imgproxy Configuration

Deploy an imgproxy container with:

```yaml
imgproxy:
  image: darthsim/imgproxy
  environment:
    - IMGPROXY_ENABLE_WEBP_DETECTION=true
    - IMGPROXY_JPEG_PROGRESSIVE=true
```

> Note: Ensure this service is only reachable within an internal network and not exposed to the public internet.

### Storage API Configuration

Configure your self-hosted [`storage-api`](https://github.com/supabase/storage-api) service with these environment variables:

```
ENABLE_IMAGE_TRANSFORMATION=true
IMGPROXY_URL=yourinternalimgproxyurl.internal.com
```

## Resources

- [Video Guide: How to resize images on the fly with Supabase](https://www.youtube.com/watch?v=dLqSmxX3r7I)
- [imgproxy Documentation](https://imgproxy.net/)
- [Storage API GitHub Repository](https://github.com/supabase/storage-api)
