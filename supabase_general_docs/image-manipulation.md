# Custom Image Manipulation with Edge Functions

While Supabase Storage offers [built-in image transformations](https://supabase.com/docs/guides/storage/serving/image-transformations) for common needs, you can use Edge Functions to create custom image processing pipelines beyond what's available out-of-the-box.

This guide demonstrates how to use the [`magick-wasm`](https://github.com/dlemstra/magick-wasm) library, a WebAssembly port of ImageMagick, to perform advanced image manipulations in Supabase Edge Functions.

## Library Compatibility

Edge Functions currently only support WebAssembly-based image processing libraries. Native libraries that require system dependencies (like `Sharp`) are not compatible. The WebAssembly port of ImageMagick (`magick-wasm`) is a good choice because it supports over 100 file formats and provides comprehensive image manipulation capabilities.

## Prerequisites

Before starting, ensure you have:

1. The latest version of the [Supabase CLI](https://supabase.com/docs/guides/cli#installation) installed
2. A Supabase project (local or hosted)
3. Basic knowledge of TypeScript and Deno

## Creating an Image Blur Function

Let's create a function that accepts an uploaded image and returns a blurred thumbnail.

### Step 1: Create the Edge Function

Create a new function locally using the Supabase CLI:

```bash
supabase functions new image-blur
```

### Step 2: Implement the Function

Add the following code to the `index.ts` file:

```typescript
// This is an example showing how to use Magick WASM to do image manipulations in Edge Functions.
import {
  ImageMagick,
  initializeImageMagick,
  MagickFormat,
} from "npm:@imagemagick/magick-wasm@0.0.30";

const wasmBytes = await Deno.readFile(
  new URL(
    "magick.wasm",
    import.meta.resolve("npm:@imagemagick/magick-wasm@0.0.30"),
  ),
);

await initializeImageMagick(
  wasmBytes,
);

Deno.serve(async (req) => {
  const formData = await req.formData();
  const content = await formData.get("file").bytes();

  let result = ImageMagick.read(
    content,
    (img): Uint8Array => {
      // resize the image
      img.resize(500, 300);
      
      // add a blur of 60x5
      img.blur(60, 5);
      
      return img.write(
        (data) => data,
      );
    },
  );

  return new Response(
    result,
    { headers: { "Content-Type": "image/png" } },
  );
});
```

This function:
1. Initializes the ImageMagick WebAssembly module
2. Accepts an image upload via a form submission
3. Resizes the image to 500x300 pixels
4. Applies a blur effect with radius 60 and sigma 5
5. Returns the processed image with the appropriate content type

### Step 3: Test Locally

Start your local Supabase development environment and serve the function:

```bash
supabase start
supabase functions serve --no-verify-jwt
```

Test the function using cURL or any API testing tool:

```bash
curl --location 'http://localhost:54321/functions/v1/image-blur' \
--form 'file=@"/path/to/image.png"' \
--output '/path/to/output.png'
```

If everything works correctly, you should find a blurred, resized version of your original image at the specified output path.

### Step 4: Deploy to Production

Once you're satisfied with the function, deploy it to your hosted Supabase project:

```bash
supabase link
supabase functions deploy image-blur
```

## Performance Considerations

Hosted Edge Functions have [resource limits](https://supabase.com/docs/guides/functions/limits) on memory and CPU usage. Keep these limitations in mind when processing images:

- Complex image operations may exceed the resource limits
- Large images (>5MB) may cause timeout errors
- Consider implementing progressive enhancement or fallbacks for intensive operations

## Extending the Function

You can extend this example to implement other image manipulations:

- **Watermarking**: Add text or image overlays
- **Format conversion**: Convert between image formats
- **Filters and effects**: Apply artistic filters or photo effects
- **Composite operations**: Combine multiple images
- **Metadata handling**: Extract or modify image metadata

## Resources

- [ImageMagick Documentation](https://imagemagick.org/script/command-line-options.php)
- [magick-wasm GitHub Repository](https://github.com/dlemstra/magick-wasm)
- [Supabase Edge Functions Limits](https://supabase.com/docs/guides/functions/limits)
- [Example Source Code](https://github.com/supabase/supabase/blob/641940e5464f0f894b0cf5b427a85e1686b9259b/examples/edge-functions/supabase/functions/image-manipulation/index.ts)
