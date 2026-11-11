# TRELLIS Multi-Image API: pricing, parameters and code examples

`trellis/trellis/multi` · image generation model · trellis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

TRELLIS by Microsoft generates a textured 3D mesh (GLB) from several views of the same object.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trellis/trellis/multi", "images": "https://static.sandbase.ai/examples/trellis/trellis/multi/input_images_0.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trellis/trellis/multi', {'images': 'https://static.sandbase.ai/examples/trellis/trellis/multi/input_images_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trellis/trellis/multi", {
  "images": "https://static.sandbase.ai/examples/trellis/trellis/multi/input_images_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trellis/trellis/multi", sandbase.Params{
	"images": "https://static.sandbase.ai/examples/trellis/trellis/multi/input_images_0.png",
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
| `images` | array | yes | 2 or more views of the same object.  |
| `texture_size` | integer |  | Resolution of the baked texture image. one of: `512`, `1024`, `2048`; default `1024` |

## Details

TRELLIS by Microsoft generates a textured 3D mesh (GLB) from several views of the same object.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URLs, required | — | 2 or more views of the same object. |
| `texture_size` | `512` / `1024` / `2048` | `1024` | Resolution of the baked texture image. |
| `seed` | integer | — | Random seed for reproducible results. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
### Billing
$0.02 per request.
Failed runs are not charged.
### Also on SandBase
Other trellis 3D endpoints: `trellis/trellis`, `trellis/trellis-2`, `trellis/trellis-2/retexture`.

---
Machine-readable: [`catalog/models/trellis/trellis/multi.json`](../../../../catalog/models/trellis/trellis/multi.json) · Store page: https://www.sandbase.ai/model/trellis/trellis/multi
