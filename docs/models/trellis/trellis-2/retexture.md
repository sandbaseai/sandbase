# TRELLIS.2 Retexture API: pricing, parameters and code examples

`trellis/trellis-2/retexture` · image generation model · trellis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $0.24 per run, depending on parameters · **Modes:** async

TRELLIS.2 Retexture by Microsoft paints new textures onto an existing 3D mesh (GLB, OBJ, PLY or STL) from a reference image.

## Pricing

- Depends on parameters (`params.resolution`).

| parameters | USD |
|---|---|
| resolution=512 | 0.2 |
| resolution=1024 | 0.24 |

Formula: `(params.resolution ?? 1024) == 512 ? 0.2 : 0.24`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trellis/trellis-2/retexture", "image": "https://static.sandbase.ai/examples/58df2e9a-50f3-4876-9093-7370da282318/input/a3464a2f-4f92-4afd-9f94-8cdf0059b338.png", "model_url": "https://static.sandbase.ai/examples/58df2e9a-50f3-4876-9093-7370da282318/input/caff59c3-5264-4305-bc2b-63d1b53bb3ad.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trellis/trellis-2/retexture', {'image': 'https://static.sandbase.ai/examples/58df2e9a-50f3-4876-9093-7370da282318/input/a3464a2f-4f92-4afd-9f94-8cdf0059b338.png', 'model_url': 'https://static.sandbase.ai/examples/58df2e9a-50f3-4876-9093-7370da282318/input/caff59c3-5264-4305-bc2b-63d1b53bb3ad.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trellis/trellis-2/retexture", {
  "image": "https://static.sandbase.ai/examples/58df2e9a-50f3-4876-9093-7370da282318/input/a3464a2f-4f92-4afd-9f94-8cdf0059b338.png",
  "model_url": "https://static.sandbase.ai/examples/58df2e9a-50f3-4876-9093-7370da282318/input/caff59c3-5264-4305-bc2b-63d1b53bb3ad.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trellis/trellis-2/retexture", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/58df2e9a-50f3-4876-9093-7370da282318/input/a3464a2f-4f92-4afd-9f94-8cdf0059b338.png",
	"model_url": "https://static.sandbase.ai/examples/58df2e9a-50f3-4876-9093-7370da282318/input/caff59c3-5264-4305-bc2b-63d1b53bb3ad.glb",
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
| `image` | string | yes | Reference image for the new texture.  |
| `model_url` | string | yes | URL of the untextured 3D mesh to retexture. Supports GLB, OBJ, PLY and STL.  |
| `resolution` | integer |  | Internal texture generation resolution. Higher gives finer texture detail, and changes the price. one of: `512`, `1024`; default `1024` |
| `texture_size` | integer |  | Resolution of the baked texture image. Higher values keep finer surface detail but produce larger files. one of: `1024`, `2048`, `4096`; default `2048` |

## Details

TRELLIS.2 Retexture by Microsoft paints new textures onto an existing 3D mesh (GLB, OBJ, PLY or STL) from a reference image.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the untextured 3D mesh to retexture. Supports GLB, OBJ, PLY and STL. |
| `image` | image URL, required | — | Reference image for the new texture. |
| `resolution` | `512` / `1024` | `1024` | Internal texture generation resolution. Higher gives finer texture detail, and changes the price. |
| `texture_size` | `1024` / `2048` / `4096` | `2048` | Resolution of the baked texture image. Higher values keep finer surface detail but produce larger files. |
| `seed` | integer | — | Random seed for reproducible results. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
### Billing
$0.24 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| resolution = 512 | $0.20 |
| resolution = 1024 | $0.24 |
Failed runs are not charged.
### Also on SandBase
Other trellis 3D endpoints: `trellis/trellis`, `trellis/trellis-2`, `trellis/trellis/multi`.

---
Machine-readable: [`catalog/models/trellis/trellis-2/retexture.json`](../../../../catalog/models/trellis/trellis-2/retexture.json) · Store page: https://www.sandbase.ai/model/trellis/trellis-2/retexture
