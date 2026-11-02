# Nano Banana Pro Edit API: pricing, parameters and code examples

`google/nano-banana-pro/edit` · image generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.1362 to $0.2422 per run, depending on parameters · **Modes:** async

Nano Banana Pro is Google's new state-of-the-art image generation and editing model

## Pricing

- Depends on parameters (`params.images`, `params.resolution`).

| parameters | USD |
|---|---|
| resolution="1K" | 0.1362 |
| resolution="2K" | 0.1362 |
| resolution="4K" | 0.2422 |

Formula: `((params.resolution ?? "1K") == "4K" ? 0.24 : 0.134) + len(params.images ?? []) * 0.0011`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/nano-banana-pro/edit", "aspect_ratio": "2:3", "images": ["https://static.sandbase.ai/examples/a24d699f-ac6b-4c57-b162-f6073c15d031/input/80b3b8e7-87db-4487-ab30-a844b4f22b96.png", "https://static.sandbase.ai/examples/a24d699f-ac6b-4c57-b162-f6073c15d031/input/7c80d815-ad38-457a-9664-bf7371a876b5.png"], "prompt": "Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/nano-banana-pro/edit', {'aspect_ratio': '2:3', 'images': ['https://static.sandbase.ai/examples/a24d699f-ac6b-4c57-b162-f6073c15d031/input/80b3b8e7-87db-4487-ab30-a844b4f22b96.png', 'https://static.sandbase.ai/examples/a24d699f-ac6b-4c57-b162-f6073c15d031/input/7c80d815-ad38-457a-9664-bf7371a876b5.png'], 'prompt': 'Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/nano-banana-pro/edit", {
  "aspect_ratio": "2:3",
  "images": [
    "https://static.sandbase.ai/examples/a24d699f-ac6b-4c57-b162-f6073c15d031/input/80b3b8e7-87db-4487-ab30-a844b4f22b96.png",
    "https://static.sandbase.ai/examples/a24d699f-ac6b-4c57-b162-f6073c15d031/input/7c80d815-ad38-457a-9664-bf7371a876b5.png"
  ],
  "prompt": "Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/nano-banana-pro/edit", sandbase.Params{
	"aspect_ratio": "2:3",
	"images": []any{"https://static.sandbase.ai/examples/a24d699f-ac6b-4c57-b162-f6073c15d031/input/80b3b8e7-87db-4487-ab30-a844b4f22b96.png", "https://static.sandbase.ai/examples/a24d699f-ac6b-4c57-b162-f6073c15d031/input/7c80d815-ad38-457a-9664-bf7371a876b5.png"},
	"prompt": "Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | The URLs of the images to use for image-to-image generation or image editing.  |
| `prompt` | string | yes | The text prompt to generate an image from. default `"Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."` |
| `resolution` | string |  | The resolution of the image to generate. one of: `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. Leave empty to keep the aspect ratio of the input image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Edit or combine images with Nano Banana Pro. Send one or more images with an instruction; the model keeps identity and layout where you do not ask for changes, and can render new text accurately.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URL[], required | — | Images to edit or combine, Image 1, Image 2, … |
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Omit to follow the first input image. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `resolution` | `1K` / `2K` / `4K` | `1K` | Sets the per-image rate. |

### Billing

$0.134 per output image at 1K or 2K and $0.24 at 4K, plus $0.0011 per input image, Google's list price.

| Inputs | 1K | 2K | 4K |
|---|---|---|---|
| 1 input image | $0.1351 | $0.1351 | $0.2411 |
| 3 input images | $0.1373 | $0.1373 | $0.2433 |
| 6 input images | $0.1406 | $0.1406 | $0.2466 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other Nano Banana endpoints: `google/nano-banana-pro`, `google/nano-banana-2`, `google/nano-banana-2/edit`, `google/nano-banana-2-lite`, `google/nano-banana-2-lite/edit`.

---
Machine-readable: [`catalog/models/google/nano-banana-pro/edit.json`](../../../../catalog/models/google/nano-banana-pro/edit.json) · Store page: https://www.sandbase.ai/model/google/nano-banana-pro/edit
