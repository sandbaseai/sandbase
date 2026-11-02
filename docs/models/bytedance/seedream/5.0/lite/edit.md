# Seedream 5.0 Lite Edit API: pricing, parameters and code examples

`bytedance/seedream/5.0/lite/edit` · image generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.035 per call · **Modes:** async

Seedream 5.0 Lite — Fast Text-to-Image API The lightweight version of Seedream 5.0, delivering high-quality, low-latency AI image generation from text prompts. Ideal for real-time creative tools, e-commerce visuals, and high-volume AIGC pipelines.

## Pricing

- **$0.035 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedream/5.0/lite/edit", "prompt": "Generate 3 images of a girl and a cow plushie happily riding a roller coaster in an amusement park, depicting morning, noon, and night.", "images": "<images>"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedream/5.0/lite/edit', {'prompt': 'Generate 3 images of a girl and a cow plushie happily riding a roller coaster in an amusement park, depicting morning, noon, and night.', 'images': '<images>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedream/5.0/lite/edit", {
  "prompt": "Generate 3 images of a girl and a cow plushie happily riding a roller coaster in an amusement park, depicting morning, noon, and night.",
  "images": "<images>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedream/5.0/lite/edit", sandbase.Params{
	"prompt": "Generate 3 images of a girl and a cow plushie happily riding a roller coaster in an amusement park, depicting morning, noon, and night.",
	"images": "<images>",
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
| `prompt` | string | yes | The text prompt to generate an image from. default `"Generate 3 images of a girl and a cow plushie happily riding a roller coaster in an amusement park, depicting morning, noon, and night."` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Seedream 5.0 Lite edit: fast, low-cost edits and multi-image composition.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URL[], required | — | Images to edit or combine, Image 1, Image 2, … |
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `1:1` / `3:4` / `2:3` / `9:16` | — | Omit to follow the first input image. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |

### Billing

$0.035 per output image.

| Request | Price |
|---|---|
| One image | $0.035 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other Seedream endpoints: `bytedance/seedream/5.0/pro`, `bytedance/seedream/5.0/pro/edit`, `bytedance/seedream/5.0/lite`, `bytedance/seedream/5.0/flash`, `bytedance/seedream/5.0/flash/edit`, `bytedance/seedream/4.5`, `bytedance/seedream/4.5/edit`.

---
Machine-readable: [`catalog/models/bytedance/seedream/5.0/lite/edit.json`](../../../../../../catalog/models/bytedance/seedream/5.0/lite/edit.json) · Store page: https://www.sandbase.ai/model/bytedance/seedream/5.0/lite/edit
