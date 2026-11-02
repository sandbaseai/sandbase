# Grok Imagine Image 2.0 Edit API: pricing, parameters and code examples

`xai/grok-imagine-image/2.0/edit` · image generation model · xAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.04 to $0.08 per run, depending on parameters · **Modes:** async

Grok Imagine Image 2.0 Edit is xAI's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from background replacement to artistic style conversion.

## Pricing

- Depends on parameters (`params.images`, `params.quality`, `params.resolution`).

| parameters | USD |
|---|---|
| quality="low", resolution="1k" | 0.04 |
| quality="low", resolution="2k" | 0.06 |
| quality="medium", resolution="1k" | 0.06 |
| quality="medium", resolution="2k" | 0.08 |

Formula: `((params.resolution ?? "1k") == "2k" ? ((params.quality ?? "medium") == "low" ? 0.06 : 0.08) : ((params.quality ?? "medium") == "low" ? 0.04 : 0.06)) + len(params.images ?? []) * 0.01`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-image/2.0/edit", "prompt": "Make this scene more realistic but still keep the game vibes"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-image/2.0/edit', {'prompt': 'Make this scene more realistic but still keep the game vibes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-image/2.0/edit", {
  "prompt": "Make this scene more realistic but still keep the game vibes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-image/2.0/edit", sandbase.Params{
	"prompt": "Make this scene more realistic but still keep the game vibes",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array |  | List of URLs of the images to edit. A maximum of 3 images are supported.  |
| `prompt` | string | yes | Text description of the desired image.  |
| `quality` | string |  | Quality level of the edited image. one of: `low`, `medium`; default `"medium"` |
| `resolution` | string |  | Resolution of the generated image. `1k` for standard resolution, `2k` for high resolution. one of: `1k`, `2k`; default `"1k"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"jpeg"` |

## Details

Grok Imagine Image 2.0 edit: change or combine images at two quality levels.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 8,000 characters. |
| `images` | image URL[] | — | Images to edit or combine, Image 1, Image 2, … |
| `resolution` | `1k` / `2k` | `1k` | Sets the per-image rate. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |
| `quality` | `low` / `medium` | `medium` | Sets the per-image rate. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |

### Billing

Per output image: $0.04 (low) or $0.06 (medium) at 1K; $0.06 or $0.08 at 2K; plus $0.01 per input image.

| Request | 1k | 2k |
|---|---|---|
| low, 1 input | $0.05 | $0.07 |
| medium, 1 input | $0.07 | $0.09 |

Failed runs are not charged.

### Prompting

- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other Grok Imagine Image endpoints: `xai/grok-imagine-image/quality`, `xai/grok-imagine-image/quality/edit`, `xai/grok-imagine-image/edit`, `xai/grok-imagine-image/2.0/text-to-image`.

---
Machine-readable: [`catalog/models/xai/grok-imagine-image/2.0/edit.json`](../../../../../catalog/models/xai/grok-imagine-image/2.0/edit.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-image/2.0/edit
