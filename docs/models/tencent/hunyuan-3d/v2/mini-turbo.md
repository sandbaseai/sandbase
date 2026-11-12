# Hunyuan3D 2.0 Mini Turbo API: pricing, parameters and code examples

`tencent/hunyuan-3d/v2/mini-turbo` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.08 to $0.24 per run, depending on parameters · **Modes:** async

Hunyuan3D 2.0 Mini Turbo by Tencent, the fast variant of Hunyuan3D 2.0 Mini, generates a 3D mesh from a single image, as a white mesh or with textures.

## Pricing

- Depends on parameters (`params.textured_mesh`).

| parameters | USD |
|---|---|
| textured_mesh=false | 0.08 |
| textured_mesh=true | 0.24 |

Formula: `(params.textured_mesh ?? false) ? 0.24 : 0.08`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/v2/mini-turbo", "image": "https://static.sandbase.ai/examples/6fe37f3c-0b82-4e4e-970b-ba6badab06de/input/38f2f71d-813d-48cf-99a8-6a8221d09797.png", "textured_mesh": true}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/v2/mini-turbo', {'image': 'https://static.sandbase.ai/examples/6fe37f3c-0b82-4e4e-970b-ba6badab06de/input/38f2f71d-813d-48cf-99a8-6a8221d09797.png', 'textured_mesh': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/v2/mini-turbo", {
  "image": "https://static.sandbase.ai/examples/6fe37f3c-0b82-4e4e-970b-ba6badab06de/input/38f2f71d-813d-48cf-99a8-6a8221d09797.png",
  "textured_mesh": true
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/v2/mini-turbo", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/6fe37f3c-0b82-4e4e-970b-ba6badab06de/input/38f2f71d-813d-48cf-99a8-6a8221d09797.png",
	"textured_mesh": true,
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed. The same seed and input reproduce the same result.  |
| `image` | string | yes | URL of the image to turn into a 3D model.  |
| `textured_mesh` | boolean |  | Generate a textured mesh instead of a white (untextured) mesh. Textured output costs 3x. default `false` |
| `octree_resolution` | integer |  | Octree resolution of the generated mesh. Higher values give finer geometry. default `256`; range 1–1024 |

## Details

Hunyuan3D 2.0 Mini Turbo by Tencent, the fast variant of Hunyuan3D 2.0 Mini, generates a 3D mesh from a single image, as a white mesh or with textures.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | URL of the image to turn into a 3D model. |
| `textured_mesh` | boolean | `false` | Generate a textured mesh instead of a white (untextured) mesh. Textured output costs 3x. |
| `octree_resolution` | integer 1–1024 | `256` | Octree resolution of the generated mesh. Higher values give finer geometry. |
| `seed` | integer | — | Random seed. The same seed and input reproduce the same result. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
### Billing
$0.08 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| textured_mesh on | $0.24 |
| textured_mesh off | $0.08 |
Failed runs are not charged.
### Also on SandBase
Other Tencent 3D endpoints: `tencent/hunyuan-3d/3.0/image-to-3d`, `tencent/hunyuan-3d/3.1/part`, `tencent/hunyuan-3d/3.1/pro/image-to-3d`, `tencent/hunyuan-3d/3.1/pro/text-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/v2/mini-turbo.json`](../../../../../catalog/models/tencent/hunyuan-3d/v2/mini-turbo.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/v2/mini-turbo
