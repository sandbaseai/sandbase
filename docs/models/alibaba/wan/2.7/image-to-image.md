# Wan 2.7 Image to Image API: pricing, parameters and code examples

`alibaba/wan/2.7/image-to-image` · image generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.03 per run, depending on parameters · **Modes:** async

Alibaba Wan 2.7 image-to-image model that edits images from a natural-language instruction, with multi-reference support and selectable aspect ratio.

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
  -d '{"model": "alibaba/wan/2.7/image-to-image", "aspect_ratio": "9:16", "images": ["https://static.sandbase.ai/examples/0eeefa8f-0c4d-4a75-ad7e-6ead1df9e998/input/2a3945fe-b5cb-4a5c-bc95-e9b14b69d6ed.png"], "prompt": "Turn the scene into a snowy winter night"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.7/image-to-image', {'aspect_ratio': '9:16', 'images': ['https://static.sandbase.ai/examples/0eeefa8f-0c4d-4a75-ad7e-6ead1df9e998/input/2a3945fe-b5cb-4a5c-bc95-e9b14b69d6ed.png'], 'prompt': 'Turn the scene into a snowy winter night'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.7/image-to-image", {
  "aspect_ratio": "9:16",
  "images": [
    "https://static.sandbase.ai/examples/0eeefa8f-0c4d-4a75-ad7e-6ead1df9e998/input/2a3945fe-b5cb-4a5c-bc95-e9b14b69d6ed.png"
  ],
  "prompt": "Turn the scene into a snowy winter night"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.7/image-to-image", sandbase.Params{
	"aspect_ratio": "9:16",
	"images": []any{"https://static.sandbase.ai/examples/0eeefa8f-0c4d-4a75-ad7e-6ead1df9e998/input/2a3945fe-b5cb-4a5c-bc95-e9b14b69d6ed.png"},
	"prompt": "Turn the scene into a snowy winter night",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | List of input image URLs for editing. Up to 4 images.  |
| `prompt` | string | yes | The editing instruction describing what changes to make. default `"Convert this photograph into a delicate watercolor painting style with visible brush strokes and soft color bleeding"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21` |

## Details

Edit or restyle pictures with an instruction. Send one or more images and describe the change; Wan 2.7 keeps what you do not mention.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 10,000 characters. |
| `images` | image URL[], required | — | Images to edit or combine, referred to as Image 1, Image 2, … |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `9:21` | — | Omit to follow the first input image. |

### Billing

$0.03 per output image, Alibaba's list price. Input images are not metered.

| Request | Price |
|---|---|
| One image | $0.03 |

Failed runs are not charged.

### Prompting

- State the change and what must stay: “change the sky to sunset; keep the lighthouse and the rocks”.
- With several inputs, say which image supplies which element.

### Limits

- One output image per request.

### Also on SandBase

Other Wan 2.7 image endpoints: `alibaba/wan/2.7/text-to-image`, `alibaba/wan/2.7/pro/text-to-image`, `alibaba/wan/2.7/pro/image-to-image`.

---
Machine-readable: [`catalog/models/alibaba/wan/2.7/image-to-image.json`](../../../../../catalog/models/alibaba/wan/2.7/image-to-image.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.7/image-to-image
