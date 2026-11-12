# Meshy Rigging API: pricing, parameters and code examples

`meshy/rigging` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $0.32 per run, depending on parameters · **Modes:** async

Meshy Rigging adds a humanoid skeleton to an existing character model and can also apply one animation preset.

## Pricing

- Depends on parameters (`params.enable_animation`).

| parameters | USD |
|---|---|
| enable_animation=false | 0.2 |
| enable_animation=true | 0.32 |

Formula: `(params.enable_animation ?? false) ? 0.32 : 0.2`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/rigging", "enable_animation": true, "model_url": "https://static.sandbase.ai/examples/3d5a1315-3549-4c25-b133-5efbee7dbc0d/input/255717e2-2107-4e10-bfbe-4abaed9024ee.glb"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/rigging', {'enable_animation': True, 'model_url': 'https://static.sandbase.ai/examples/3d5a1315-3549-4c25-b133-5efbee7dbc0d/input/255717e2-2107-4e10-bfbe-4abaed9024ee.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/rigging", {
  "enable_animation": true,
  "model_url": "https://static.sandbase.ai/examples/3d5a1315-3549-4c25-b133-5efbee7dbc0d/input/255717e2-2107-4e10-bfbe-4abaed9024ee.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/rigging", sandbase.Params{
	"enable_animation": true,
	"model_url": "https://static.sandbase.ai/examples/3d5a1315-3549-4c25-b133-5efbee7dbc0d/input/255717e2-2107-4e10-bfbe-4abaed9024ee.glb",
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
| `enable_animation` | boolean |  | Also generate one animation clip on the rig. Returned as animation_glb / animation_fbx. default `false` |
| `skeleton_template` | string |  | Skeleton template for the rig (e.g. mixamo, ue5_mannequin, unity_humanoid). Some models can only be rigged on meshyrig without fingers. one of: `mixamo`, `ue5_mannequin`, `unity_humanoid`, `maya_human_ik`, `blender_rigify_basic_human`, `max_biped`, `cc5_hd_neutral_base`, `daz_genesis9`, `meshyrig`; default `"meshyrig"` |
| `animation_action_id` | integer |  | Animation preset ID from Meshy's animation library (0 is Idle). Only used when animation is enabled. default `92`; range 0–696 |

## Details

Meshy Rigging adds a humanoid skeleton to an existing character model and can also apply one animation preset.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of a humanoid character model in GLB format with clearly defined limbs. Works with models from Meshy, Hunyuan, Trellis or any other 3D tool. |
| `enable_animation` | boolean | `false` | Also generate one animation clip on the rig. Returned as animation_glb / animation_fbx. |
| `animation_action_id` | integer 0–696 | `92` | Animation preset ID from Meshy's animation library (0 is Idle). Only used when animation is enabled. |
| `skeleton_template` | `mixamo` / `ue5_mannequin` / `unity_humanoid` / `maya_human_ik` / `blender_rigify_basic_human` / `max_biped` / `cc5_hd_neutral_base` / `daz_genesis9` / `meshyrig` | `meshyrig` | Skeleton template for the rig (e.g. mixamo, ue5_mannequin, unity_humanoid). Some models can only be rigged on meshyrig without fingers. |
| `include_fingers` | boolean | `false` | Rig the character's fingers. |
| `height_meters` | number | `1.7` | Approximate height of the character in meters. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `fbx`: Additional file returned by the provider.
- `animation_glb`: Additional file returned by the provider.
- `animation_fbx`: Additional file returned by the provider.
### Billing
$0.20 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| enable_animation on | $0.32 |
| enable_animation off | $0.20 |
Failed runs are not charged.
### Also on SandBase
Other Meshy 3D endpoints: `meshy/6.0-lite/retexture`, `meshy/6.0/retexture`, `meshy/7.0/image-to-3d`, `meshy/7.0/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/rigging.json`](../../../catalog/models/meshy/rigging.json) · Store page: https://www.sandbase.ai/model/meshy/rigging
