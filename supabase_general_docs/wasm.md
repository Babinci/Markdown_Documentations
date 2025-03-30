# Using WebAssembly Modules

Edge Functions supports running [WebAssembly (Wasm)](https://developer.mozilla.org/en-US/docs/WebAssembly) modules. WebAssembly is useful if you want to optimize code that's slower to run in JavaScript or require low-level manipulation.

It also gives you the option to port existing libraries written in other languages to be used with JavaScript. For example, [magick-wasm](https://supabase.com/docs/guides/functions/examples/image-manipulation), which does image manipulation and transforms, is a port of an existing C library to WebAssembly.

## Writing a Wasm Module

You can use different languages and SDKs to write Wasm modules. For this tutorial, we will write a simple Wasm module in Rust that adds two numbers.

Follow this [guide on writing Wasm modules in Rust](https://developer.mozilla.org/en-US/docs/WebAssembly/Rust_to_Wasm) to setup your dev environment.

Create a new Edge Function called `wasm-add`:

```bash
supabase functions new wasm-add
```

Create a new Cargo project for the Wasm module inside the function's directory:

```bash
cd supabase/functions/wasm-add
cargo new --lib add-wasm
```

Add the following code to `add-wasm/src/lib.rs`:

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn add(a: u32, b: u32) -> u32 {
    a + b
}
```

Update the `add-wasm/Cargo.toml` to include the `wasm-bindgen` dependency:

```toml
[package]
name = "add-wasm"
version = "0.1.0"
description = "A simple wasm module that adds two numbers"
license = "MIT/Apache-2.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
wasm-bindgen = "0.2"
```

After that we can build the package by running:

```bash
wasm-pack build --target deno
```

This will produce a Wasm binary file inside `add-wasm/pkg` directory.

## Calling the Wasm Module from the Edge Function

Now let's update the Edge Function to call `add` from the Wasm module:

```typescript
import { add } from "./add-wasm/pkg/add_wasm.js";

Deno.serve(async (req) => {
  const { a, b } = await req.json();
  return new Response(
    JSON.stringify({ result: add(a, b) }),
    { headers: { "Content-Type": "application/json" } },
  );
});
```

Supabase Edge Functions currently use Deno 1.46. From [Deno 2.1, importing Wasm modules](https://deno.com/blog/v2.1) will require even less boilerplate code.

## Bundle and Deploy the Edge Function

Before deploying the Edge Function, we need to ensure it bundles the Wasm module with it. We can do this by defining it in the `static_files` for the function in `supabase/config.toml`.

You will need to update Supabase CLI to 2.7.0 or higher for the `static_files` support:

```toml
[functions.wasm-add]
static_files = [ "./functions/wasm-add/add-wasm/pkg/*"]
```

Deploy the function by running:

```bash
supabase functions deploy wasm-add
```
