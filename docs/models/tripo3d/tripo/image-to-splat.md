# Tripo Image to Splat API: pricing, parameters and code examples

`tripo3d/tripo/image-to-splat` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.3 per call · **Modes:** async

Tripo Image to Splat turns one image into a 3D Gaussian splat scene (.splat).

## Pricing

- **$0.3 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/image-to-splat", "image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/image-to-splat', {'image': 'https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/image-to-splat", {
  "image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/image-to-splat", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for geometry generation (Tripo model_seed). Same seed and input give the same mesh.  |
| `image` | string | yes | Input image URL (PNG, JPEG or WebP, up to 20 MB).  |

## Details

Tripo Image to Splat turns one image into a 3D Gaussian splat scene (.splat).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Input image URL (PNG, JPEG or WebP, up to 20 MB). |
| `seed` | integer | — | Seed for geometry generation (Tripo model_seed). Same seed and input give the same mesh. |
### Output
- `url`: Gaussian splat file (.splat).
### Billing
$0.30 per scene.
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/image-to-splat.json`](../../../../catalog/models/tripo3d/tripo/image-to-splat.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/image-to-splat
