# Tripo P1 Image to 3D API: pricing, parameters and code examples

`tripo3d/tripo-p1/image-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.48 to $0.6 per run, depending on parameters · **Modes:** async

Tripo P1 is Tripo3D's image-to-3D model. It reconstructs a 3D mesh with optional textures from a single image.

## Pricing

- Depends on parameters (`params.texture`).

| parameters | USD |
|---|---|
| texture=false | 0.48 |
| texture=true | 0.6 |

Formula: `(params.texture ?? true) ? 0.60 : 0.48`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-p1/image-to-3d", "image": "https://static.sandbase.ai/examples/tripo3d/tripo-p1/image-to-3d/input_image_0.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-p1/image-to-3d', {'image': 'https://static.sandbase.ai/examples/tripo3d/tripo-p1/image-to-3d/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-p1/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/tripo3d/tripo-p1/image-to-3d/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-p1/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/tripo3d/tripo-p1/image-to-3d/input_image_0.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for reproducible geometry generation.  |
| `image` | string | yes | Input image URL for 3D model creation.  |
| `texture` | boolean |  | Generate textures. Set to false for an untextured mesh (cheaper). default `true` |
| `face_limit` | integer |  | Target face count of the mesh. Adaptive when unset. range 48–20000 |

## Details

Tripo P1 is Tripo3D's image-to-3D model. It reconstructs a 3D mesh with optional textures from a single image.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Input image URL for 3D model creation. |
| `texture` | boolean | `true` | Generate textures. Set to false for an untextured mesh (cheaper). |
| `face_limit` | integer 48–20000 | — | Target face count of the mesh. Adaptive when unset. |
| `seed` | integer | — | Seed for reproducible geometry generation. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.60 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| texture on | $0.60 |
| texture off | $0.48 |
Failed runs are not charged.
### Also on SandBase
Other Tripo3D 3D endpoints: `tripo3d/tripo-h3.1/image-to-3d`, `tripo3d/tripo-h3.1/multiview-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`, `tripo3d/tripo-p1/text-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo-p1/image-to-3d.json`](../../../../catalog/models/tripo3d/tripo-p1/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-p1/image-to-3d
