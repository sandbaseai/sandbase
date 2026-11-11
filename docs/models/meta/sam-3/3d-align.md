# SAM 3 3D Align API: pricing, parameters and code examples

`meta/sam-3/3d-align` · image generation model · Meta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.024 per call · **Modes:** async

SAM 3D Align by Meta places a SAM 3D Body mesh into the scene of its source image, optionally combining it with a SAM 3D Objects mesh into one GLB scene.

## Pricing

- **$0.024 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meta/sam-3/3d-align", "image": "https://static.sandbase.ai/examples/meta/sam-3/3d-body/input_image_0.jpeg", "model_url": "<model_url>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meta/sam-3/3d-align', {'image': 'https://static.sandbase.ai/examples/meta/sam-3/3d-body/input_image_0.jpeg', 'model_url': '<model_url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meta/sam-3/3d-align", {
  "image": "https://static.sandbase.ai/examples/meta/sam-3/3d-body/input_image_0.jpeg",
  "model_url": "<model_url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meta/sam-3/3d-align", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/meta/sam-3/3d-body/input_image_0.jpeg",
	"model_url": "<model_url>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mask` | string |  | Optional human mask image. The full image is used when omitted.  |
| `image` | string | yes | Original image the body mesh was reconstructed from.  |
| `model_url` | string | yes | URL of the SAM 3D Body mesh (.ply or .glb) to align.  |
| `focal_length` | number |  | Focal length from SAM 3D Body metadata. Estimated from the image when omitted.  |
| `object_model_url` | string |  | Optional URL of a SAM 3D Objects mesh (.glb). When set, the output is a combined body + object scene.  |

## Details

SAM 3D Align by Meta places a SAM 3D Body mesh into the scene of its source image, optionally combining it with a SAM 3D Objects mesh into one GLB scene.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Original image the body mesh was reconstructed from. |
| `model_url` | string, required | — | URL of the SAM 3D Body mesh (.ply or .glb) to align. |
| `mask` | image URL | — | Optional human mask image. The full image is used when omitted. |
| `object_model_url` | string | — | Optional URL of a SAM 3D Objects mesh (.glb). When set, the output is a combined body + object scene. |
| `focal_length` | number | — | Focal length from SAM 3D Body metadata. Estimated from the image when omitted. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.024 per request.
Failed runs are not charged.
### Also on SandBase
Other Meta 3D endpoints: `meta/sam-3/3d-body`, `meta/sam-3/3d-objects`.

---
Machine-readable: [`catalog/models/meta/sam-3/3d-align.json`](../../../../catalog/models/meta/sam-3/3d-align.json) · Store page: https://www.sandbase.ai/model/meta/sam-3/3d-align
