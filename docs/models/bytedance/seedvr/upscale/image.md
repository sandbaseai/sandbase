# SeedVR2 Image Upscale API: pricing, parameters and code examples

`bytedance/seedvr/upscale/image` · image generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

Seedvr Upscale Image by Bytedance - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedvr/upscale/image", "image": "https://static.sandbase.ai/examples/e9063ae5-ae76-45df-ba78-5b81c56d1157/input/99a0d455-36a3-421d-a064-48062fa13691.jpg", "target_resolution": "4k"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedvr/upscale/image', {'image': 'https://static.sandbase.ai/examples/e9063ae5-ae76-45df-ba78-5b81c56d1157/input/99a0d455-36a3-421d-a064-48062fa13691.jpg', 'target_resolution': '4k'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedvr/upscale/image", {
  "image": "https://static.sandbase.ai/examples/e9063ae5-ae76-45df-ba78-5b81c56d1157/input/99a0d455-36a3-421d-a064-48062fa13691.jpg",
  "target_resolution": "4k"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedvr/upscale/image", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/e9063ae5-ae76-45df-ba78-5b81c56d1157/input/99a0d455-36a3-421d-a064-48062fa13691.jpg",
	"target_resolution": "4k",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | The input image to be processed  |
| `output_format` | string |  | The format of the output image. one of: `png`, `jpg`; default `"jpg"` |
| `target_resolution` | string |  | The target resolution to upscale to. one of: `2k`, `4k`; default `"4k"` |

## Details

SeedVR2 restores and upscales a single image to 2K or 4K, sharpening detail without changing content.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Image to upscale. JPEG, PNG, or WebP URL. |
| `target_resolution` | `2k` / `4k` | `4k` | Output long-side tier. |
| `output_format` | `png` / `jpg` | `jpg` | Output file format. |

### Billing

$0.01 per image.

| Request | Price |
|---|---|
| One image | $0.01 |

Failed runs are not charged.

### Limits

- One image per request.

### Also on SandBase

Related: `bytedance/seedvr/upscale/video`, `topaz/upscale/image` (Topaz).

---
Machine-readable: [`catalog/models/bytedance/seedvr/upscale/image.json`](../../../../../catalog/models/bytedance/seedvr/upscale/image.json) · Store page: https://www.sandbase.ai/model/bytedance/seedvr/upscale/image
