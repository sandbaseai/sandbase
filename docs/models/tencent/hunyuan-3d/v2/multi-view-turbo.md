# Hunyuan3D 2.0 Multi-View Turbo API: pricing, parameters and code examples

`tencent/hunyuan-3d/v2/multi-view-turbo` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.14 to $0.42 per run, depending on parameters · **Modes:** async

Hunyuan3D 2.0 Multi-View Turbo by Tencent, the fast multi-view variant, generates a 3D mesh from front, back, and left view images, as a white mesh or with textures.

## Pricing

- Depends on parameters (`params.textured_mesh`).

| parameters | USD |
|---|---|
| textured_mesh=false | 0.14 |
| textured_mesh=true | 0.42 |

Formula: `(params.textured_mesh ?? false) ? 0.42 : 0.14`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/v2/multi-view-turbo", "back_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/371dca8d-79f9-48e9-8d92-c1592ef15e51.png", "front_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/eeca101c-7a40-458c-88fe-ed8a6304bf73.png", "left_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/2dcabb82-db8a-4212-a32b-268932ec88d8.png", "textured_mesh": true}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/v2/multi-view-turbo', {'back_image': 'https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/371dca8d-79f9-48e9-8d92-c1592ef15e51.png', 'front_image': 'https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/eeca101c-7a40-458c-88fe-ed8a6304bf73.png', 'left_image': 'https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/2dcabb82-db8a-4212-a32b-268932ec88d8.png', 'textured_mesh': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/v2/multi-view-turbo", {
  "back_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/371dca8d-79f9-48e9-8d92-c1592ef15e51.png",
  "front_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/eeca101c-7a40-458c-88fe-ed8a6304bf73.png",
  "left_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/2dcabb82-db8a-4212-a32b-268932ec88d8.png",
  "textured_mesh": true
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/v2/multi-view-turbo", sandbase.Params{
	"back_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/371dca8d-79f9-48e9-8d92-c1592ef15e51.png",
	"front_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/eeca101c-7a40-458c-88fe-ed8a6304bf73.png",
	"left_image": "https://static.sandbase.ai/examples/c809e1ac-d46b-4fc2-b297-9e556c704dc9/input/2dcabb82-db8a-4212-a32b-268932ec88d8.png",
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
| `back_image` | string | yes | URL of the back view image of the object.  |
| `left_image` | string | yes | URL of the left view image of the object.  |
| `front_image` | string | yes | URL of the front view image of the object.  |
| `textured_mesh` | boolean |  | Generate a textured mesh instead of a white (untextured) mesh. Textured output costs 3x. default `false` |
| `octree_resolution` | integer |  | Octree resolution of the generated mesh. Higher values give finer geometry. default `256`; range 1–1024 |

## Details

Hunyuan3D 2.0 Multi-View Turbo by Tencent, the fast multi-view variant, generates a 3D mesh from front, back, and left view images, as a white mesh or with textures.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `front_image` | image URL, required | — | URL of the front view image of the object. |
| `back_image` | image URL, required | — | URL of the back view image of the object. |
| `left_image` | image URL, required | — | URL of the left view image of the object. |
| `textured_mesh` | boolean | `false` | Generate a textured mesh instead of a white (untextured) mesh. Textured output costs 3x. |
| `octree_resolution` | integer 1–1024 | `256` | Octree resolution of the generated mesh. Higher values give finer geometry. |
| `seed` | integer | — | Random seed. The same seed and input reproduce the same result. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
### Billing
$0.14 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| textured_mesh on | $0.42 |
| textured_mesh off | $0.14 |
Failed runs are not charged.
### Also on SandBase
Other Tencent 3D endpoints: `tencent/hunyuan-3d/3.0/image-to-3d`, `tencent/hunyuan-3d/3.1/part`, `tencent/hunyuan-3d/3.1/pro/image-to-3d`, `tencent/hunyuan-3d/3.1/pro/text-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/v2/multi-view-turbo.json`](../../../../../catalog/models/tencent/hunyuan-3d/v2/multi-view-turbo.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/v2/multi-view-turbo
