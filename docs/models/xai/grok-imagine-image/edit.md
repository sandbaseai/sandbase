# Grok Imagine Image Edit

`xai/grok-imagine-image/edit` · image · xAI

Grok Imagine Image Edit is xAI's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from background replacement to artistic style conversion.

## Pricing

- Depends on parameters (`params.images`).

| parameters | USD |
|---|---|
| defaults | 0.02 |

Formula: `0.02 + len(params.images ?? []) * 0.002`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-image/edit", "prompt": "Make this scene more realistic but still keep the game vibes"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-image/edit', {'prompt': 'Make this scene more realistic but still keep the game vibes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-image/edit", {
  "prompt": "Make this scene more realistic but still keep the game vibes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-image/edit", sandbase.Params{
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
| `resolution` | string |  | Resolution of the generated image. `1k` for standard resolution, `2k` for high resolution. one of: `1k`, `2k`; default `"1k"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"jpeg"` |

## Details

Grok Imagine Image edit (standard): fast, low-cost image edits.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 8,000 characters. |
| `images` | image URL[] | — | Images to edit or combine, Image 1, Image 2, … |
| `resolution` | `1k` / `2k` | `1k` | Sets the per-image rate. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |

### Billing

$0.02 per output image plus $0.002 per input image.

| Request | Price |
|---|---|
| 1 input image | $0.022 |
| 3 input images | $0.026 |

Failed runs are not charged.

### Prompting

- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other Grok Imagine Image endpoints: `xai/grok-imagine-image/quality`, `xai/grok-imagine-image/quality/edit`, `xai/grok-imagine-image/2.0/text-to-image`, `xai/grok-imagine-image/2.0/edit`.

---
Machine-readable: [`catalog/models/xai/grok-imagine-image/edit.json`](../../../../catalog/models/xai/grok-imagine-image/edit.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-image/edit
