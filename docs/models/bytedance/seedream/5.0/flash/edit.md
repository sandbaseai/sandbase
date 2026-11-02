# Seedream 5.0 Flash Edit API: pricing, parameters and code examples

`bytedance/seedream/5.0/flash/edit` · image generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.018 per call · **Modes:** async

Seedream 5.0 Flash Editing edits and fuses up to 10 reference images from a text instruction at one flat price per image, with fast 15–20 second turnaround.

## Pricing

- **$0.018 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedream/5.0/flash/edit", "images": ["https://static.sandbase.ai/examples/d6b09b83-f5b3-4888-9f09-e2c0ac866bba/input/5fa58d60-3a2e-4707-83a2-b4e0d5437e80.jpg"], "prompt": "Put the woman from image 1 on a sunny beach"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedream/5.0/flash/edit', {'images': ['https://static.sandbase.ai/examples/d6b09b83-f5b3-4888-9f09-e2c0ac866bba/input/5fa58d60-3a2e-4707-83a2-b4e0d5437e80.jpg'], 'prompt': 'Put the woman from image 1 on a sunny beach'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedream/5.0/flash/edit", {
  "images": [
    "https://static.sandbase.ai/examples/d6b09b83-f5b3-4888-9f09-e2c0ac866bba/input/5fa58d60-3a2e-4707-83a2-b4e0d5437e80.jpg"
  ],
  "prompt": "Put the woman from image 1 on a sunny beach"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedream/5.0/flash/edit", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/d6b09b83-f5b3-4888-9f09-e2c0ac866bba/input/5fa58d60-3a2e-4707-83a2-b4e0d5437e80.jpg"},
	"prompt": "Put the woman from image 1 on a sunny beach",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | Reference images to edit or fuse (1–10). Refer to them in the prompt as image 1, image 2, ...  |
| `prompt` | string | yes | The text prompt to generate an image from. default `"Generate 3 images of a girl and a cow plushie happily riding a roller coaster in an amusement park, depicting morning, noon, and night."` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Seedream 5.0 Flash edit: edit or fuse up to 10 reference images at a flat per-image price with fast turnaround.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URL[] (≤10), required | — | Images to edit or combine, Image 1, Image 2, … |
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `1:1` / `3:4` / `2:3` / `9:16` | — | Omit to follow the first input image. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |

### Billing

$0.018 per output image.

| Request | Price |
|---|---|
| One image | $0.018 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other Seedream endpoints: `bytedance/seedream/5.0/pro`, `bytedance/seedream/5.0/pro/edit`, `bytedance/seedream/5.0/lite`, `bytedance/seedream/5.0/lite/edit`, `bytedance/seedream/5.0/flash`, `bytedance/seedream/4.5`, `bytedance/seedream/4.5/edit`.

---
Machine-readable: [`catalog/models/bytedance/seedream/5.0/flash/edit.json`](../../../../../../catalog/models/bytedance/seedream/5.0/flash/edit.json) · Store page: https://www.sandbase.ai/model/bytedance/seedream/5.0/flash/edit
