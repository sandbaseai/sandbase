# Qwen Image 3 Text to Image

`alibaba/qwen-image-3/text-to-image` · image · Alibaba

Qwen Image 3 by Alibaba - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- Depends on parameters (`params.num_images`, `params.resolution`).

| parameters | USD |
|---|---|
| num_images=1, resolution="1K" | 0.04 |
| num_images=1, resolution="2K" | 0.075 |
| num_images=6, resolution="1K" | 0.24 |
| num_images=6, resolution="2K" | 0.45 |

Formula: `(params.num_images ?? 1) * ((params.resolution ?? "1K") == "2K" ? 0.075 : 0.04)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen-image-3/text-to-image", "prompt": "<prompt>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/qwen-image-3/text-to-image', {'prompt': '<prompt>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/qwen-image-3/text-to-image", {
  "prompt": "<prompt>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/qwen-image-3/text-to-image", sandbase.Params{
	"prompt": "<prompt>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-2147483647).  |
| `prompt` | string | yes | Text prompt describing the desired image. Supports Chinese and English. Max 5000 characters.  |
| `num_images` | integer |  |  default `1`; range 1–6 |
| `resolution` | string |  | Output resolution tier; the price depends on it. one of: `1K`, `2K`; default `"1K"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Qwen Image 3 (Pro) generates photorealistic images and dense layouts such as posters, infographics, and slides, with accurate Chinese and English text rendering. Up to 6 images per request at 1K or 2K.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `num_images` | integer 1–6 | 1 | Images to generate (1–6); each is billed. |
| `resolution` | `1K` / `2K` | `1K` | Sets the per-image rate. |

### Billing

$0.04 per image at 1K and $0.075 at 2K, Alibaba's list price for Qwen Image 3.0 Pro.

| Images | 1K | 2K |
|---|---|---|
| 1 | $0.04 | $0.075 |
| 2 | $0.08 | $0.15 |
| 4 | $0.16 | $0.30 |
| 6 | $0.24 | $0.45 |

Failed runs are not charged.

### Prompting

- Quote every piece of text that must appear and say where it goes.
- For infographics and slides, describe the layout region by region.
- Name the style explicitly: photo, flat illustration, 3D render.

### Limits

- Up to 6 images per request.

### Also on SandBase

Related: `alibaba/qwen-image-3/edit` (edit with Qwen Image 3), `alibaba/qwen-image-2`.

---
Machine-readable: [`catalog/models/alibaba/qwen-image-3/text-to-image.json`](../../../../catalog/models/alibaba/qwen-image-3/text-to-image.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen-image-3/text-to-image
