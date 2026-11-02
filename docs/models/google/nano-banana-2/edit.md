# Nano Banana 2 Edit API: pricing, parameters and code examples

`google/nano-banana-2/edit` · image generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.045 to $0.165 per run, depending on parameters · **Modes:** async

Nano Banana 2 is Google's new state-of-the-art image generation and editing model

## Pricing

- Depends on parameters (`params.enable_image_search`, `params.enable_web_search`, `params.resolution`).

| parameters | USD |
|---|---|
| enable_image_search=false, enable_web_search=false, resolution="0.5K" | 0.045 |
| enable_image_search=false, enable_web_search=false, resolution="1K" | 0.067 |
| enable_image_search=false, enable_web_search=false, resolution="2K" | 0.101 |
| enable_image_search=false, enable_web_search=false, resolution="4K" | 0.151 |
| enable_image_search=false, enable_web_search=true, resolution="0.5K" | 0.059 |
| enable_image_search=false, enable_web_search=true, resolution="1K" | 0.081 |
| enable_image_search=false, enable_web_search=true, resolution="2K" | 0.115 |
| enable_image_search=false, enable_web_search=true, resolution="4K" | 0.165 |
| enable_image_search=true, enable_web_search=false, resolution="0.5K" | 0.059 |
| enable_image_search=true, enable_web_search=false, resolution="1K" | 0.081 |
| enable_image_search=true, enable_web_search=false, resolution="2K" | 0.115 |
| enable_image_search=true, enable_web_search=false, resolution="4K" | 0.165 |
| enable_image_search=true, enable_web_search=true, resolution="0.5K" | 0.059 |
| enable_image_search=true, enable_web_search=true, resolution="1K" | 0.081 |
| enable_image_search=true, enable_web_search=true, resolution="2K" | 0.115 |
| enable_image_search=true, enable_web_search=true, resolution="4K" | 0.165 |

Formula: `((params.resolution ?? "1K") == "0.5K" ? 0.045 : (params.resolution ?? "1K") == "2K" ? 0.101 : (params.resolution ?? "1K") == "4K" ? 0.151 : 0.067) + (((params.enable_web_search ?? false) || (params.enable_image_search ?? false)) ? 0.014 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/nano-banana-2/edit", "aspect_ratio": "3:2", "images": ["https://static.sandbase.ai/examples/c260ffa3-a68a-4042-83e9-22e3edc8e209/input/1473477b-62f4-4256-98a0-f5ad17c3b13f.jpg"], "prompt": "Make a 3 panel comic in a gritty, noir art style with high-contrast black and white inks. Put the character in a humorous scene."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/nano-banana-2/edit', {'aspect_ratio': '3:2', 'images': ['https://static.sandbase.ai/examples/c260ffa3-a68a-4042-83e9-22e3edc8e209/input/1473477b-62f4-4256-98a0-f5ad17c3b13f.jpg'], 'prompt': 'Make a 3 panel comic in a gritty, noir art style with high-contrast black and white inks. Put the character in a humorous scene.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/nano-banana-2/edit", {
  "aspect_ratio": "3:2",
  "images": [
    "https://static.sandbase.ai/examples/c260ffa3-a68a-4042-83e9-22e3edc8e209/input/1473477b-62f4-4256-98a0-f5ad17c3b13f.jpg"
  ],
  "prompt": "Make a 3 panel comic in a gritty, noir art style with high-contrast black and white inks. Put the character in a humorous scene."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/nano-banana-2/edit", sandbase.Params{
	"aspect_ratio": "3:2",
	"images": []any{"https://static.sandbase.ai/examples/c260ffa3-a68a-4042-83e9-22e3edc8e209/input/1473477b-62f4-4256-98a0-f5ad17c3b13f.jpg"},
	"prompt": "Make a 3 panel comic in a gritty, noir art style with high-contrast black and white inks. Put the character in a humorous scene.",
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
| `prompt` | string | yes | The text prompt to generate an image from. default `"Make a 3 panel comic in a gritty, noir art style with high-contrast black and white inks. Put the character in a humurous scene."` |
| `resolution` | string |  | The resolution of the image to generate. one of: `0.5K`, `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. Leave empty to keep the aspect ratio of the input image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`, `4:1`, `1:4` … |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `enable_web_search` | boolean |  | Enable Google web search grounding to provide background context for image generation. default `false` |
| `enable_image_search` | boolean |  | Enable Google image search to retrieve web images as visual background reference for generation. default `false` |

## Details

Edit or combine images with Nano Banana 2, Google's fast image model. Send images with an instruction to restyle, retouch, swap objects, or merge several inputs into one scene.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URL[], required | — | Images to edit or combine, Image 1, Image 2, … |
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` / `4:1` / `1:4` / `8:1` / `1:8` | — | Omit to follow the first input image. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `resolution` | `0.5K` / `1K` / `2K` / `4K` | `1K` | Sets the per-image rate. |
| `enable_web_search` | boolean | false | Ground the edit in Google Search results. |
| `enable_image_search` | boolean | false | Use image search results as visual references. |

### Billing

$0.045 at 0.5K, $0.067 at 1K, $0.101 at 2K, and $0.151 at 4K per image, Google's list price. Input images are not metered. Turning on `enable_web_search` or `enable_image_search` adds $0.014 per request (charged once even if both are on).

| Request | 0.5K | 1K | 2K | 4K |
|---|---|---|---|---|
| One image | $0.045 | $0.067 | $0.101 | $0.151 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other Nano Banana endpoints: `google/nano-banana-pro`, `google/nano-banana-pro/edit`, `google/nano-banana-2`, `google/nano-banana-2-lite`, `google/nano-banana-2-lite/edit`.

---
Machine-readable: [`catalog/models/google/nano-banana-2/edit.json`](../../../../catalog/models/google/nano-banana-2/edit.json) · Store page: https://www.sandbase.ai/model/google/nano-banana-2/edit
