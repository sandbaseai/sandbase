# TRELLIS API: pricing, parameters and code examples

`trellis/trellis` · image generation model · trellis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

TRELLIS by Microsoft generates a textured 3D mesh (GLB) from a single image using structured 3D latents.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trellis/trellis", "image": "https://static.sandbase.ai/examples/fe2420f6-f986-41b0-8ba0-a396d9df8b9b/input/9976ef54-909a-45aa-b4ce-c4fa20a068ad.png"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trellis/trellis', {'image': 'https://static.sandbase.ai/examples/fe2420f6-f986-41b0-8ba0-a396d9df8b9b/input/9976ef54-909a-45aa-b4ce-c4fa20a068ad.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trellis/trellis", {
  "image": "https://static.sandbase.ai/examples/fe2420f6-f986-41b0-8ba0-a396d9df8b9b/input/9976ef54-909a-45aa-b4ce-c4fa20a068ad.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trellis/trellis", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/fe2420f6-f986-41b0-8ba0-a396d9df8b9b/input/9976ef54-909a-45aa-b4ce-c4fa20a068ad.png",
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
| `image` | string | yes | Image of the object to convert to 3D.  |
| `texture_size` | integer |  | Resolution of the baked texture image. one of: `512`, `1024`, `2048`; default `1024` |

## Details

TRELLIS by Microsoft generates a textured 3D mesh (GLB) from a single image using structured 3D latents.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Image of the object to convert to 3D. |
| `texture_size` | `512` / `1024` / `2048` | `1024` | Resolution of the baked texture image. |
| `seed` | integer | — | Random seed for reproducible results. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
### Billing
$0.02 per request.
Failed runs are not charged.
### Also on SandBase
Other trellis 3D endpoints: `trellis/trellis-2`, `trellis/trellis-2/retexture`, `trellis/trellis/multi`.

---
Machine-readable: [`catalog/models/trellis/trellis.json`](../../../catalog/models/trellis/trellis.json) · Store page: https://www.sandbase.ai/model/trellis/trellis
