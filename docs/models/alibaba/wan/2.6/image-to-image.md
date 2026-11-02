# Wan 2.6 Image to Image API: pricing, parameters and code examples

`alibaba/wan/2.6/image-to-image` · image generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.03 per run, depending on parameters · **Modes:** async

Alibaba Wan 2.6 image-to-image model that edits images from a natural-language instruction, with multi-reference support and selectable aspect ratio.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.03 |

Formula: `0.03`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.6/image-to-image", "aspect_ratio": "9:16", "images": ["https://static.sandbase.ai/examples/6bc956c9-0728-4ee7-aa97-d02ad81fa8fb/input/24863bca-7df6-4e54-b38c-b93467a50f16.png"], "prompt": "Turn the scene into a snowy winter night", "seed": 7}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.6/image-to-image', {'aspect_ratio': '9:16', 'images': ['https://static.sandbase.ai/examples/6bc956c9-0728-4ee7-aa97-d02ad81fa8fb/input/24863bca-7df6-4e54-b38c-b93467a50f16.png'], 'prompt': 'Turn the scene into a snowy winter night', 'seed': 7})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.6/image-to-image", {
  "aspect_ratio": "9:16",
  "images": [
    "https://static.sandbase.ai/examples/6bc956c9-0728-4ee7-aa97-d02ad81fa8fb/input/24863bca-7df6-4e54-b38c-b93467a50f16.png"
  ],
  "prompt": "Turn the scene into a snowy winter night",
  "seed": 7
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.6/image-to-image", sandbase.Params{
	"aspect_ratio": "9:16",
	"images": []any{"https://static.sandbase.ai/examples/6bc956c9-0728-4ee7-aa97-d02ad81fa8fb/input/24863bca-7df6-4e54-b38c-b93467a50f16.png"},
	"prompt": "Turn the scene into a snowy winter night",
	"seed": 7,
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible results.  |
| `images` | array | yes | List of input image URLs for editing. Up to 4 images.  |
| `prompt` | string | yes | The editing instruction describing what changes to make. default `"Convert this photograph into a delicate watercolor painting style with visible brush strokes and soft color bleeding"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21` |

## Details

Wan 2.6 image editing: send one or more pictures and describe the change, such as a restyle, object swap, or new background.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 10,000 characters. |
| `images` | image URL[], required | — | Images to edit or combine, Image 1, Image 2, … |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `9:21` | — | Omit to follow the first input image. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.03 per output image, Alibaba's list price. Input images are not metered.

| Request | Price |
|---|---|
| One image | $0.03 |

Failed runs are not charged.

### Prompting

- State the change and what must stay the same.

### Limits

- One output image per request. Wan 2.7 image-to-image is the newer model at the same price.

### Also on SandBase

Other Wan 2.6 endpoints: `alibaba/wan/2.6/text-to-video`, `alibaba/wan/2.6/image-to-video`, `alibaba/wan/2.6/reference-to-video`, `alibaba/wan/2.6/flash/image-to-video`, `alibaba/wan/2.6/flash/reference-to-video`, `alibaba/wan/2.6/text-to-image`, `alibaba/wan/2.7/text-to-video` (newer), `alibaba/wan/2.7/image-to-image` (newer, same price).

---
Machine-readable: [`catalog/models/alibaba/wan/2.6/image-to-image.json`](../../../../../catalog/models/alibaba/wan/2.6/image-to-image.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.6/image-to-image
