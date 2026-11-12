# Meshy Rigging Multi-Animation API: pricing, parameters and code examples

`meshy/rigging/multi-animation` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.44 per run, depending on parameters · **Modes:** async

Meshy Rigging Multi-Animation rigs an existing humanoid character model and generates up to 10 animation clips on the same rig.

## Pricing

- Depends on parameters (`params.animation_action_ids`).

| parameters | USD |
|---|---|
| defaults | 0.44 |

Formula: `0.2 + len(params.animation_action_ids ?? []) * 0.12`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/rigging/multi-animation", "animation_action_ids": [92, 4], "model_url": "https://static.sandbase.ai/examples/b6ee151f-f759-4310-913a-3ef685bd1615/input/9d665214-a80d-47a1-b73e-b1c023a701e9.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/rigging/multi-animation', {'animation_action_ids': [92, 4], 'model_url': 'https://static.sandbase.ai/examples/b6ee151f-f759-4310-913a-3ef685bd1615/input/9d665214-a80d-47a1-b73e-b1c023a701e9.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/rigging/multi-animation", {
  "animation_action_ids": [
    92,
    4
  ],
  "model_url": "https://static.sandbase.ai/examples/b6ee151f-f759-4310-913a-3ef685bd1615/input/9d665214-a80d-47a1-b73e-b1c023a701e9.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/rigging/multi-animation", sandbase.Params{
	"animation_action_ids": []any{92, 4},
	"model_url": "https://static.sandbase.ai/examples/b6ee151f-f759-4310-913a-3ef685bd1615/input/9d665214-a80d-47a1-b73e-b1c023a701e9.glb",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `model_url` | string | yes | URL of a humanoid character model in GLB format with clearly defined limbs. Works with models from Meshy, Hunyuan, Trellis or any other 3D tool.  |
| `height_meters` | number |  | Approximate height of the character in meters. default `1.7` |
| `include_fingers` | boolean |  | Rig the character's fingers. default `false` |
| `skeleton_template` | string |  | Skeleton template for the rig (e.g. mixamo, ue5_mannequin, unity_humanoid). Some models can only be rigged on meshyrig without fingers. one of: `mixamo`, `ue5_mannequin`, `unity_humanoid`, `maya_human_ik`, `blender_rigify_basic_human`, `max_biped`, `cc5_hd_neutral_base`, `daz_genesis9`, `meshyrig`; default `"meshyrig"` |
| `animation_action_ids` | array | yes | 1 to 10 animation preset IDs from Meshy's animation library (0 is Idle). One clip is generated per ID, in request order; duplicates are merged.  |

## Details

Meshy Rigging Multi-Animation rigs an existing humanoid character model and generates up to 10 animation clips on the same rig.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of a humanoid character model in GLB format with clearly defined limbs. Works with models from Meshy, Hunyuan, Trellis or any other 3D tool. |
| `animation_action_ids` | array (1–10), required | — | 1 to 10 animation preset IDs from Meshy's animation library (0 is Idle). One clip is generated per ID, in request order; duplicates are merged. |
| `skeleton_template` | `mixamo` / `ue5_mannequin` / `unity_humanoid` / `maya_human_ik` / `blender_rigify_basic_human` / `max_biped` / `cc5_hd_neutral_base` / `daz_genesis9` / `meshyrig` | `meshyrig` | Skeleton template for the rig (e.g. mixamo, ue5_mannequin, unity_humanoid). Some models can only be rigged on meshyrig without fingers. |
| `include_fingers` | boolean | `false` | Rig the character's fingers. |
| `height_meters` | number | `1.7` | Approximate height of the character in meters. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `fbx`: Additional file returned by the provider.
- `animation_glb`: Additional file returned by the provider.
- `animation_fbx`: Additional file returned by the provider.
### Billing
$0.32 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| 1 animation action ids | $0.32 |
| 2 animation action ids | $0.44 |
| 4 animation action ids | $0.68 |
Failed runs are not charged.
### Also on SandBase
Other Meshy 3D endpoints: `meshy/6.0-lite/retexture`, `meshy/6.0/retexture`, `meshy/7.0/image-to-3d`, `meshy/7.0/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/rigging/multi-animation.json`](../../../../catalog/models/meshy/rigging/multi-animation.json) · Store page: https://www.sandbase.ai/model/meshy/rigging/multi-animation
