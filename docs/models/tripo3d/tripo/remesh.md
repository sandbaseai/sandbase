# Tripo Remesh API: pricing, parameters and code examples

`tripo3d/tripo/remesh` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.1 to $0.4 per run, depending on parameters · **Modes:** async

Tripo Remesh rebuilds an existing 3D model with clean triangle or quad topology at a target face count. Accepts GLB, OBJ, FBX or STL input.

## Pricing

- Depends on parameters (`params.model_version`, `params.quad`).

| parameters | USD |
|---|---|
| model_version="v3.0", quad=false | 0.35 |
| model_version="v3.0", quad=true | 0.4 |
| model_version="v2.0", quad=false | 0.3 |
| model_version="v2.0", quad=true | 0.3 |
| model_version="v1.0", quad=false | 0.1 |
| model_version="v1.0", quad=true | 0.1 |

Formula: `(params.model_version ?? "v3.0") == "v1.0" ? 0.10 : (params.model_version ?? "v3.0") == "v2.0" ? 0.30 : ((params.quad ?? false) ? 0.40 : 0.35)`

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
| `bake` | boolean |  | Bake textures onto the new mesh (not v1.0). default `true` |
| `quad` | boolean |  | Quad topology instead of triangles. default `false` |
| `smart_uv` | boolean |  | Also unwrap UVs (v3.0 only). default `false` |
| `model_url` | string | yes | URL of the input 3D model (GLB, GLTF, FBX, OBJ or STL, up to 150 MB).  |
| `face_limit` | integer |  | Target face count. v3.0: 500-20,000 (500-10,000 with quad). Adaptive when unset. range 500–20000 |
| `part_names` | array |  | Only process these parts (node names from a segmentation, e.g. tripo_part_0). All parts when unset.  |
| `model_version` | string |  | v3.0 is the newest; v2.0 smart; v1.0 basic (no bake or part_names). one of: `v3.0`, `v2.0`, `v1.0`; default `"v3.0"` |

## Details

Tripo Remesh rebuilds an existing 3D model with clean triangle or quad topology at a target face count. Accepts GLB, OBJ, FBX or STL input.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input 3D model (GLB, GLTF, FBX, OBJ or STL, up to 150 MB). |
| `model_version` | `v3.0` / `v2.0` / `v1.0` | `v3.0` | v3.0 is the newest; v2.0 smart; v1.0 basic (no bake or part_names). |
| `quad` | boolean | `false` | Quad topology instead of triangles. |
| `face_limit` | integer 500–20000 | — | Target face count. v3.0: 500-20,000 (500-10,000 with quad). Adaptive when unset. |
| `smart_uv` | boolean | `false` | Also unwrap UVs (v3.0 only). |
| `bake` | boolean | `true` | Bake textures onto the new mesh (not v1.0). |
| `part_names` | array | — | Only process these parts (node names from a segmentation, e.g. tripo_part_0). All parts when unset. |
### Output
- `url`: Remeshed model (FBX with quad).
- `thumbnail`: Preview render.
### Billing
| model | Price |
|---|---|
| v3.0 triangle | $0.35 |
| v3.0 quad | $0.40 |
| v2.0 | $0.30 |
| v1.0 | $0.10 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/remesh.json`](../../../../catalog/models/tripo3d/tripo/remesh.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/remesh
