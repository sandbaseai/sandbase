# Meshy 7.1 Image to 3D

`meshy/7.1/image-to-3d` · image · Meshy

Meshy 7.1 turns a single image into a textured, optionally rigged and animated 3D model.

## Pricing

- Depends on parameters (`params.enable_animation`, `params.enable_rigging`, `params.geometry_resolution`, `params.should_texture`).

| parameters | USD |
|---|---|
| enable_animation=false, enable_rigging=false, geometry_resolution="standard", should_texture=false | 0.96 |
| enable_animation=false, enable_rigging=false, geometry_resolution="standard", should_texture=true | 1.44 |
| enable_animation=false, enable_rigging=false, geometry_resolution="2k", should_texture=false | 1.2 |
| enable_animation=false, enable_rigging=false, geometry_resolution="2k", should_texture=true | 1.68 |
| enable_animation=false, enable_rigging=false, geometry_resolution="4k", should_texture=false | 1.44 |
| enable_animation=false, enable_rigging=false, geometry_resolution="4k", should_texture=true | 1.92 |
| enable_animation=false, enable_rigging=true, geometry_resolution="standard", should_texture=false | 1.2 |
| enable_animation=false, enable_rigging=true, geometry_resolution="standard", should_texture=true | 1.68 |
| enable_animation=false, enable_rigging=true, geometry_resolution="2k", should_texture=false | 1.44 |
| enable_animation=false, enable_rigging=true, geometry_resolution="2k", should_texture=true | 1.92 |
| enable_animation=false, enable_rigging=true, geometry_resolution="4k", should_texture=false | 1.68 |
| enable_animation=false, enable_rigging=true, geometry_resolution="4k", should_texture=true | 2.16 |
| enable_animation=true, enable_rigging=false, geometry_resolution="standard", should_texture=false | 0.96 |
| enable_animation=true, enable_rigging=false, geometry_resolution="standard", should_texture=true | 1.44 |
| enable_animation=true, enable_rigging=false, geometry_resolution="2k", should_texture=false | 1.2 |
| enable_animation=true, enable_rigging=false, geometry_resolution="2k", should_texture=true | 1.68 |
| enable_animation=true, enable_rigging=false, geometry_resolution="4k", should_texture=false | 1.44 |
| enable_animation=true, enable_rigging=false, geometry_resolution="4k", should_texture=true | 1.92 |
| enable_animation=true, enable_rigging=true, geometry_resolution="standard", should_texture=false | 1.344 |
| enable_animation=true, enable_rigging=true, geometry_resolution="standard", should_texture=true | 1.824 |
| enable_animation=true, enable_rigging=true, geometry_resolution="2k", should_texture=false | 1.584 |
| enable_animation=true, enable_rigging=true, geometry_resolution="2k", should_texture=true | 2.064 |
| enable_animation=true, enable_rigging=true, geometry_resolution="4k", should_texture=false | 1.824 |
| enable_animation=true, enable_rigging=true, geometry_resolution="4k", should_texture=true | 2.304 |

Formula: `((params.should_texture ?? true) ? 1.44 : 0.96) + ((params.geometry_resolution ?? "standard") == "4k" ? 0.48 : (params.geometry_resolution ?? "standard") == "2k" ? 0.24 : 0.0) + ((params.enable_rigging ?? false) ? 0.24 : 0.0) + ((params.enable_rigging ?? false) && (params.enable_animation ?? false) ? 0.144 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/7.1/image-to-3d", "image": "<image>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/7.1/image-to-3d', {'image': '<image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/7.1/image-to-3d", {
  "image": "<image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/7.1/image-to-3d", sandbase.Params{
	"image": "<image>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Image URL or base64 data URI for 3D model creation. Supports .jpg, .jpeg, and .png formats. Also supports AVIF and HEIF formats which will be automatically converted.  |
| `topology` | string |  | quad for smooth surfaces, triangle for detail. one of: `quad`, `triangle`; default `"triangle"` |
| `pose_mode` | string |  | a-pose, t-pose or empty for none. one of: `a-pose`, `t-pose`, ``; default `""` |
| `enable_pbr` | boolean |  | Generate PBR maps (metallic, roughness, normal). default `false` |
| `model_type` | string |  | standard, lowpoly or smart-topology. one of: `standard`, `lowpoly`, `smart-topology`; default `"standard"` |
| `symmetry_mode` | string |  | off / auto / on. one of: `off`, `auto`, `on`; default `"auto"` |
| `texture_image` | string |  | Image URL to guide texturing.  |
| `enable_rigging` | boolean |  | Rig the model as a humanoid character (+$0.20). default `false` |
| `should_texture` | boolean |  | Generate textures (untextured models are cheaper). default `true` |
| `texture_prompt` | string |  | Text prompt to guide texturing.  |
| `enable_animation` | boolean |  | Apply an animation preset; requires enable_rigging (+$0.12). default `false` |
| `target_polycount` | integer |  | Target polygon count (100–300,000). default `30000`; range 100–300000 |
| `geometry_resolution` | string |  | Geometry resolution. one of: `standard`, `2k`, `4k`; default `"standard"` |

## Details

Meshy 7.1 turns a single image into a textured 3D model, optionally rigged and animated.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Image URL or base64 data URI for 3D model creation. |
| `symmetry_mode` | `off` / `auto` / `on` | `auto` | Enforce symmetry. |
| `enable_rigging` | boolean | false | Add a humanoid rig. |
| `model_type` | `standard` / `lowpoly` / `smart-topology` | `standard` | Mesh style. |
| `enable_pbr` | boolean | false | PBR texture maps. |
| `pose_mode` | `a-pose` / `t-pose` / `` | — | Force an A- or T-pose. |
| `should_texture` | boolean | true | Generate textures; untextured costs less. |
| `enable_animation` | boolean | false | Add a walk/run animation (requires rigging). |
| `texture_prompt` | string | — | Optional texture description. |
| `geometry_resolution` | `standard` / `2k` / `4k` | `standard` | Mesh detail; higher tiers cost more. |
| `target_polycount` | integer 100–300000 | 30000 | Target polygon count. |
| `topology` | `quad` / `triangle` | `triangle` | Quad or triangle mesh. |
| `texture_image` | image URL | — | Optional texture reference image. |

### Billing

$1.44 per textured model ($0.96 untextured); 2K geometry adds $0.24 and 4K adds $0.48; rigging adds $0.24 and animation another $0.144.

| Request | Price |
|---|---|
| Textured | $1.44 |
| Untextured | $0.96 |
| Textured, 2K geometry | $1.68 |
| Textured + rig + animation | $1.824 |

Failed runs are not charged.

### Prompting

- Describe or show one object; plain backgrounds work best.

### Also on SandBase

Other Meshy 7.1 endpoints: `meshy/7.1/text-to-3d`, `meshy/7.1/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/7.1/image-to-3d.json`](../../../../catalog/models/meshy/7.1/image-to-3d.json) · Store page: https://www.sandbase.ai/model/meshy/7.1/image-to-3d
