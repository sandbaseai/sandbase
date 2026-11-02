# Ideogram 3.0 Edit API: pricing, parameters and code examples

`ideogram-ai/ideogram-v3/edit` · image generation model · Ideogram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.03 to $0.09 per run, depending on parameters · **Modes:** async

Ideogram V3 Edit by ideogram-ai - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- Depends on parameters (`params.rendering_speed`).

| parameters | USD |
|---|---|
| rendering_speed="TURBO" | 0.03 |
| rendering_speed="BALANCED" | 0.06 |
| rendering_speed="QUALITY" | 0.09 |

Formula: `(params.rendering_speed ?? "BALANCED") == "TURBO" ? 0.03 : (params.rendering_speed ?? "BALANCED") == "QUALITY" ? 0.09 : 0.06`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ideogram-ai/ideogram-v3/edit", "image": "https://static.sandbase.ai/examples/fef92fd9-0a39-4571-841d-06952aa5e9c6/input/e6ec02d2-e595-4933-8819-321bf1c82b1a.png", "prompt": "black bag"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ideogram-ai/ideogram-v3/edit', {'image': 'https://static.sandbase.ai/examples/fef92fd9-0a39-4571-841d-06952aa5e9c6/input/e6ec02d2-e595-4933-8819-321bf1c82b1a.png', 'prompt': 'black bag'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ideogram-ai/ideogram-v3/edit", {
  "image": "https://static.sandbase.ai/examples/fef92fd9-0a39-4571-841d-06952aa5e9c6/input/e6ec02d2-e595-4933-8819-321bf1c82b1a.png",
  "prompt": "black bag"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ideogram-ai/ideogram-v3/edit", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/fef92fd9-0a39-4571-841d-06952aa5e9c6/input/e6ec02d2-e595-4933-8819-321bf1c82b1a.png",
	"prompt": "black bag",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mask` | string |  | The mask URL to inpaint the image. MUST have the exact same dimensions (width and height) as the input image.  |
| `seed` | integer |  | Seed for the random number generator  |
| `image` | string | yes | The image URL to generate an image from. MUST have the exact same dimensions (width and height) as the mask image.  |
| `images` | array |  | A set of images to use as style references (maximum total size 10MB across all style references). The images should be in JPEG, PNG or WebP format  |
| `prompt` | string | yes | The prompt to fill the masked part of the image.  |
| `rendering_speed` | string |  | The rendering speed to use. one of: `TURBO`, `BALANCED`, `QUALITY`; default `"BALANCED"` |

## Details

Ideogram 3.0 edit: inpaint a masked region of an image from a prompt.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `image` | image URL, required | — | Image to edit. JPEG, PNG, or WebP URL. |
| `images` | image URL[] | — | Optional style references. |
| `mask` | image URL | — | Area to edit. |
| `rendering_speed` | `TURBO` / `BALANCED` / `QUALITY` | `BALANCED` | Sets the per-image rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

Per image: $0.03 Turbo, $0.06 Balanced, $0.09 Quality.

| Speed | Price |
|---|---|
| TURBO | $0.03 |
| BALANCED | $0.06 |
| QUALITY | $0.09 |

Failed runs are not charged.

### Prompting

- Quote all text that must appear.

### Also on SandBase

Related: `ideogram/4.5` (newer).

---
Machine-readable: [`catalog/models/ideogram-ai/ideogram-v3/edit.json`](../../../../catalog/models/ideogram-ai/ideogram-v3/edit.json) · Store page: https://www.sandbase.ai/model/ideogram-ai/ideogram-v3/edit
