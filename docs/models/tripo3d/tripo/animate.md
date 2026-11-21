# Tripo Animate API: pricing, parameters and code examples

`tripo3d/tripo/animate` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.35 per run, depending on parameters · **Modes:** async

Tripo Animate rigs a 3D character or creature and applies preset animations to it in one call (Tripo Rig + Animation Retarget).

## Pricing

- Depends on parameters (`params.animations`).

| parameters | USD |
|---|---|
| defaults | 0.35 |

Formula: `0.25 + 0.10 * Math.max(1.0, len(params.animations ?? []) * 1.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/animate", "model_url": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/animate', {'model_url': 'https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/animate", {
  "model_url": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/animate", sandbase.Params{
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
| `animation` | string |  | One preset, e.g. preset:walk. Rig v3.0 biped: preset:idle, walk, run, dive, climb, jump, slash, shoot, hurt, fall, turn. Non-biped: preset:quadruped:walk, preset:hexapod:walk, preset:octopod:walk,…  |
| `model_url` | string | yes | URL of the 3D model (GLB, FBX, OBJ or STL, up to 150 MB).  |
| `animations` | array |  | 1 to 5 presets in one file (same names as animation). Each animation is billed.  |
| `out_format` | string |  | Format of the rigged and the animated model. one of: `glb`, `fbx`; default `"glb"` |
| `model_version` | string |  | v3.0-20260909 is recommended for humanoids and supports others; v2.5-20260210 for non-humanoids; v1.0-20240301 biped only (90+ presets). one of: `v3.0-20260909`, `v2.5-20260210`, `v1.0-20240301`; default `"v3.0-20260909"` |
| `animate_in_place` | boolean |  | Remove root motion so the character stays in place. default `false` |
| `export_with_geometry` | boolean |  | Include the mesh in the animated file; false exports the skeleton animation only. default `true` |

## Details

Tripo Animate rigs a 3D character or creature and applies preset animations to it in one call (Tripo Rig + Animation Retarget).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the 3D model (GLB, FBX, OBJ or STL, up to 150 MB). |
| `animation` | string | — | One preset, e.g. preset:walk. Rig v3.0 biped: preset:idle, walk, run, dive, climb, jump, slash, shoot, hurt, fall, turn. Non-biped: preset:quadruped:walk, preset:hexapod:walk, preset:octopod:walk, preset:serpentine:march, preset:aquatic:march. Rig v1.0: preset:biped:<name>. Use animation or animations. |
| `animations` | array | — | 1 to 5 presets in one file (same names as animation). Each animation is billed. |
| `model_version` | `v3.0-20260909` / `v2.5-20260210` / `v1.0-20240301` | `v3.0-20260909` | v3.0-20260909 is recommended for humanoids and supports others; v2.5-20260210 for non-humanoids; v1.0-20240301 biped only (90+ presets). |
| `rig_type` | `biped` / `quadruped` / `hexapod` / `octopod` / `avian` / `serpentine` / `aquatic` / `others` | `biped` | Skeleton type. Use Tripo Rig Check to find it. |
| `spec` | `tripo` / `mixamo` / `actorcore` / `unity` / `unreal` / `vrm` | `tripo` | Bone naming for biped rigs. actorcore, unity, unreal and vrm need rig model v3.0-20260909. |
| `out_format` | `glb` / `fbx` | `glb` | Format of the rigged and the animated model. |
| `export_with_geometry` | boolean | `true` | Include the mesh in the animated file; false exports the skeleton animation only. |
| `animate_in_place` | boolean | `false` | Remove root motion so the character stays in place. |
### Output
- `url`: Animated model.
- `rigged`: Rigged model without animation.
- `thumbnail`: Preview render.
### Billing
$0.25 for rigging plus $0.10 per animation ($0.35 with one animation).
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/animate.json`](../../../../catalog/models/tripo3d/tripo/animate.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/animate
