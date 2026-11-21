# Tripo Smart Segment API: pricing, parameters and code examples

`tripo3d/tripo/smart-segment` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.55 to $0.85 per run, depending on parameters · **Modes:** async

Tripo Smart Segment splits an image or a 3D model into named semantic parts, returning a segmented 3D model and a part mask.

## Pricing

- Depends on parameters (`params.seg_type`).

| parameters | USD |
|---|---|
| seg_type="image" | 0.85 |
| seg_type="model" | 0.55 |

Formula: `(params.seg_type ?? "image") == "model" ? 0.55 : 0.85`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/smart-segment", "seg_type": "image"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/smart-segment', {'seg_type': 'image'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/smart-segment", {
  "seg_type": "image"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/smart-segment", sandbase.Params{
	"seg_type": "image",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hint` | string |  | Optional text naming the parts you want.  |
| `image` | string |  | Input image when seg_type is image.  |
| `seg_type` | string | yes | image segments an image and builds a segmented 3D model; model segments an existing GLB. one of: `image`, `model`; default `"image"` |
| `model_url` | string |  | Input GLB when seg_type is model.  |
| `transform` | array |  | Model transform as a column-major 4x4 matrix (16 numbers). Used when seg_type is model; identity when unset.  |
| `granularity` | string |  | How finely to split. one of: `coarse`, `medium`, `fine`; default `"medium"` |

## Details

Tripo Smart Segment splits an image or a 3D model into named semantic parts, returning a segmented 3D model and a part mask.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `seg_type` | `image` / `model`, required | `image` | image segments an image and builds a segmented 3D model; model segments an existing GLB. |
| `image` | string | — | Input image when seg_type is image. |
| `model_url` | string | — | Input GLB when seg_type is model. |
| `granularity` | `coarse` / `medium` / `fine` | `medium` | How finely to split. |
| `hint` | string | — | Optional text naming the parts you want. |
| `transform` | array | — | Model transform as a column-major 4x4 matrix (16 numbers). Used when seg_type is model; identity when unset. |
### Output
- `url`: Segmented GLB, one node per part.
- `mask`: Part mask image.
- `parts`: Comma-separated part names.
### Billing
| seg_type | Price |
|---|---|
| image | $0.85 |
| model | $0.55 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/smart-segment.json`](../../../../catalog/models/tripo3d/tripo/smart-segment.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/smart-segment
