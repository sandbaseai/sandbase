# Tripo Remesh API: pricing, parameters and code examples

`tripo3d/tripo/remesh` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.42 to $0.48 per run, depending on parameters · **Modes:** async

Tripo Remesh rebuilds an existing 3D model with clean triangle or quad topology at a target face count. Accepts GLB, OBJ, FBX or STL input.

## Pricing

- Depends on parameters (`params.quad`).

| parameters | USD |
|---|---|
| quad=false | 0.42 |
| quad=true | 0.48 |

Formula: `(params.quad ?? false) ? 0.48 : 0.42`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/remesh", "model_url": "https://static.sandbase.ai/examples/d844350a-5fac-4a9d-a0c3-79ef0ea8e7e7/input/1a91c960-1c7f-4348-90e9-55eadc4a9b77.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/remesh', {'model_url': 'https://static.sandbase.ai/examples/d844350a-5fac-4a9d-a0c3-79ef0ea8e7e7/input/1a91c960-1c7f-4348-90e9-55eadc4a9b77.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/remesh", {
  "model_url": "https://static.sandbase.ai/examples/d844350a-5fac-4a9d-a0c3-79ef0ea8e7e7/input/1a91c960-1c7f-4348-90e9-55eadc4a9b77.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/remesh", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/d844350a-5fac-4a9d-a0c3-79ef0ea8e7e7/input/1a91c960-1c7f-4348-90e9-55eadc4a9b77.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bake` | boolean |  | Bake textures onto the remeshed model. default `true` |
| `quad` | boolean |  | Generate quad topology instead of triangles. Forces FBX output. default `false` |
| `model_url` | string | yes | URL of the input 3D model (GLB, OBJ, FBX or STL, max 150MB).  |
| `face_limit` | integer |  | Target face count, 500-20000 (500-10000 with quad). Adaptive when unset. range 500–20000 |

## Details

Tripo Remesh rebuilds an existing 3D model with clean triangle or quad topology at a target face count. Accepts GLB, OBJ, FBX or STL input.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input 3D model (GLB, OBJ, FBX or STL, max 150MB). |
| `quad` | boolean | `false` | Generate quad topology instead of triangles. Forces FBX output. |
| `face_limit` | integer 500–20000 | — | Target face count, 500-20000 (500-10000 with quad). Adaptive when unset. |
| `bake` | boolean | `true` | Bake textures onto the remeshed model. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$0.42 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| quad on | $0.48 |
| quad off | $0.42 |
Failed runs are not charged.
### Also on SandBase
Other Tripo3D 3D endpoints: `tripo3d/tripo-h3.1/image-to-3d`, `tripo3d/tripo-h3.1/multiview-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`, `tripo3d/tripo-p1/image-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo/remesh.json`](../../../../catalog/models/tripo3d/tripo/remesh.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/remesh
