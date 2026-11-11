# TRELLIS.2 API: pricing, parameters and code examples

`trellis/trellis-2` · image generation model · trellis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.25 to $0.45 per run, depending on parameters · **Modes:** async

TRELLIS.2 by Microsoft generates a textured 3D model (GLB with PBR materials) from a single image.

## Pricing

- Depends on parameters (`params.resolution`, `params.texture_size`).

| parameters | USD |
|---|---|
| resolution=512, texture_size=1024 | 0.25 |
| resolution=512, texture_size=2048 | 0.25 |
| resolution=512, texture_size=4096 | 0.25 |
| resolution=1024, texture_size=1024 | 0.3 |
| resolution=1024, texture_size=2048 | 0.3 |
| resolution=1024, texture_size=4096 | 0.3 |
| resolution=1536, texture_size=1024 | 0.4 |
| resolution=1536, texture_size=2048 | 0.4 |
| resolution=1536, texture_size=4096 | 0.45 |

Formula: `(params.resolution ?? 1024) == 1536 ? ((params.texture_size ?? 2048) == 4096 ? 0.45 : 0.4) : ((params.resolution ?? 1024) == 512 ? 0.25 : 0.3)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trellis/trellis-2", "image": "https://static.sandbase.ai/examples/trellis/trellis-2/input_image_0.png"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trellis/trellis-2', {'image': 'https://static.sandbase.ai/examples/trellis/trellis-2/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trellis/trellis-2", {
  "image": "https://static.sandbase.ai/examples/trellis/trellis-2/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trellis/trellis-2", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/trellis/trellis-2/input_image_0.png",
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
| `remesh` | boolean |  | Rebuild the mesh topology for cleaner triangles. Slower, but usually better for animation or 3D printing. default `true` |
| `resolution` | integer |  | Generation resolution. Higher is slower and more detailed, and changes the price. one of: `512`, `1024`, `1536`; default `1024` |
| `texture_size` | integer |  | Resolution of the baked texture image. Higher values keep finer surface detail but produce larger files. one of: `1024`, `2048`, `4096`; default `2048` |
| `decimation_target` | integer |  | Target number of vertices in the final mesh. Lower values give smaller files; 20k-50k suits web and mobile. default `500000`; range 5000–2000000 |

## Details

TRELLIS.2 by Microsoft generates a textured 3D model (GLB with PBR materials) from a single image.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Image of the object to convert to 3D. |
| `resolution` | `512` / `1024` / `1536` | `1024` | Generation resolution. Higher is slower and more detailed, and changes the price. |
| `texture_size` | `1024` / `2048` / `4096` | `2048` | Resolution of the baked texture image. Higher values keep finer surface detail but produce larger files. |
| `decimation_target` | integer 5000–2000000 | `500000` | Target number of vertices in the final mesh. Lower values give smaller files; 20k-50k suits web and mobile. |
| `remesh` | boolean | `true` | Rebuild the mesh topology for cleaner triangles. Slower, but usually better for animation or 3D printing. |
| `seed` | integer | — | Random seed for reproducible results. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
### Billing
$0.30 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| resolution = 512 | $0.25 |
| resolution = 1024 | $0.30 |
| resolution = 1536 | $0.40 |
| texture_size = 1024 | $0.30 |
| texture_size = 2048 | $0.30 |
| texture_size = 4096 | $0.30 |
Failed runs are not charged.
### Also on SandBase
Other trellis 3D endpoints: `trellis/trellis`, `trellis/trellis-2/retexture`, `trellis/trellis/multi`.

---
Machine-readable: [`catalog/models/trellis/trellis-2.json`](../../../catalog/models/trellis/trellis-2.json) · Store page: https://www.sandbase.ai/model/trellis/trellis-2
