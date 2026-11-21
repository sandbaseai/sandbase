# Tripo Rig API: pricing, parameters and code examples

`tripo3d/tripo/rig` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.25 per call · **Modes:** async

Tripo Rig adds a skeleton to a 3D character or creature, for humanoids, quadrupeds, birds, snakes, sea creatures and more.

## Pricing

- **$0.25 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/rig", "model_url": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/rig', {'model_url': 'https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/rig", {
  "model_url": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/rig", sandbase.Params{
	"model_url": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `spec` | string |  | Bone naming for biped rigs. actorcore, unity, unreal and vrm need rig model v3.0-20260909. one of: `tripo`, `mixamo`, `actorcore`, `unity`, `unreal`, `vrm`; default `"tripo"` |
| `rig_type` | string |  | Skeleton type. Use Tripo Rig Check to find it. one of: `biped`, `quadruped`, `hexapod`, `octopod`, `avian`, `serpentine`, `aquatic`, `others`; default `"biped"` |
| `model_url` | string | yes | URL of the 3D model (GLB, FBX, OBJ or STL, up to 150 MB).  |
| `out_format` | string |  | Rigged model format. one of: `glb`, `fbx`; default `"glb"` |
| `model_version` | string |  | v3.0-20260909 is recommended for humanoids and supports others; v2.5-20260210 for non-humanoids; v1.0-20240301 biped only. one of: `v3.0-20260909`, `v2.5-20260210`, `v1.0-20240301`; default `"v3.0-20260909"` |

## Details

Tripo Rig adds a skeleton to a 3D character or creature, for humanoids, quadrupeds, birds, snakes, sea creatures and more.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, FBX, OBJ or STL, up to 150 MB). |
| `model_version` | `v3.0-20260909` / `v2.5-20260210` / `v1.0-20240301` | `v3.0-20260909` | v3.0-20260909 is recommended for humanoids and supports others; v2.5-20260210 for non-humanoids; v1.0-20240301 biped only. |
| `rig_type` | `biped` / `quadruped` / `hexapod` / `octopod` / `avian` / `serpentine` / `aquatic` / `others` | `biped` | Skeleton type. Use Tripo Rig Check to find it. |
| `spec` | `tripo` / `mixamo` / `actorcore` / `unity` / `unreal` / `vrm` | `tripo` | Bone naming for biped rigs. actorcore, unity, unreal and vrm need rig model v3.0-20260909. |
| `out_format` | `glb` / `fbx` | `glb` | Rigged model format. |
### Output
- `url`: Rigged model.
- `thumbnail`: Preview render.
### Billing
$0.25 per model.
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/rig.json`](../../../../catalog/models/tripo3d/tripo/rig.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/rig
