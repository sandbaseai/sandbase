# Meshy Creative Lab Fidget Pixel API: pricing, parameters and code examples

`meshy/creative-lab/fidget-pixel` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.44 per call · **Modes:** async

Turns a photo into a multi-color pixel-art fidget board, returned as a 3MF.

## Pricing

- **$1.44 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/creative-lab/fidget-pixel", "image": "<image>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/creative-lab/fidget-pixel', {'image': '<image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/creative-lab/fidget-pixel", {
  "image": "<image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/creative-lab/fidget-pixel", sandbase.Params{
	"image": "<image>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | person: chibi sprite; other: bead-art icon. one of: `person`, `other`; default `"other"` |
| `image` | string | yes | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP).  |
| `shape` | string |  | Footprint of each piece. one of: `square`, `hex`; default `"square"` |
| `grid_size` | integer |  | Cells per side. one of: `16`, `32`; default `32` |
| `color_count` | integer |  | Number of colors. default `8`; range 2–16 |

## Details

Turns a photo into a multi-color pixel-art fidget board, returned as a 3MF.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Photo of the subject, as an image URL or base64 data URI (JPG, PNG or WebP). |
| `type` | `person` / `other` | `"other"` | person: chibi sprite; other: bead-art icon. |
| `shape` | `square` / `hex` | `"square"` | Footprint of each piece. |
| `grid_size` | `16` / `32` | `32` | Cells per side. |
| `color_count` | integer 2–16 | `8` | Number of colors. |
### Output
- `url`: Multi-color 3MF.
- `concept_image`: Pixel-art image.
### Billing
$1.44 per object (concept image + 3D build).

---
Machine-readable: [`catalog/models/meshy/creative-lab/fidget-pixel.json`](../../../../catalog/models/meshy/creative-lab/fidget-pixel.json) · Store page: https://www.sandbase.ai/model/meshy/creative-lab/fidget-pixel
