# Meshy T2 Image to 3D API: pricing, parameters and code examples

`meshy/t2/image-to-3d` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $0.92 per run, depending on parameters · **Modes:** async

Meshy T2 turns a single image into a clean Smart Topology triangle mesh (up to 15,000 triangles), with optional textures, rigging and animation.

## Pricing

- Depends on parameters (`params.enable_animation`, `params.enable_rigging`, `params.should_texture`).

| parameters | USD |
|---|---|
| enable_animation=false, enable_rigging=false, should_texture=false | 0.2 |
| enable_animation=false, enable_rigging=false, should_texture=true | 0.6 |
| enable_animation=false, enable_rigging=true, should_texture=false | 0.4 |
| enable_animation=false, enable_rigging=true, should_texture=true | 0.8 |
| enable_animation=true, enable_rigging=false, should_texture=false | 0.52 |
| enable_animation=true, enable_rigging=false, should_texture=true | 0.92 |
| enable_animation=true, enable_rigging=true, should_texture=false | 0.52 |
| enable_animation=true, enable_rigging=true, should_texture=true | 0.92 |

Formula: `((params.should_texture ?? true) ? 0.6 : 0.2) + (((params.enable_rigging ?? false) || (params.enable_animation ?? false)) ? 0.2 : 0.0) + ((params.enable_animation ?? false) ? 0.12 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/t2/image-to-3d", "image": "<image>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/t2/image-to-3d', {'image': '<image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/t2/image-to-3d", {
  "image": "<image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/t2/image-to-3d", sandbase.Params{
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
| `image` | string | yes | Image URL or base64 data URI of the object. Supports .jpg, .jpeg and .png; AVIF and HEIF are converted automatically.  |
| `pose_mode` | string |  | Generate the character in an A-pose or T-pose; empty for no specific pose. one of: `a-pose`, `t-pose`, ``; default `""` |
| `enable_pbr` | boolean |  | Generate PBR maps (metallic, roughness, normal) in addition to base color. default `false` |
| `texture_image` | string |  | Image URL to guide texturing.  |
| `enable_rigging` | boolean |  | Rig the model as a humanoid character. The rigged GLB is returned as rigged_glb. default `false` |
| `should_texture` | boolean |  | Generate textures. Untextured meshes cost less. default `true` |
| `texture_prompt` | string |  | Text prompt to guide texturing. Maximum 800 characters.  |
| `enable_animation` | boolean |  | Apply an animation preset to the rigged character (billed together with rigging). The animated GLB is returned as animation_glb. default `false` |
| `target_polycount` | integer |  | Target polygon count (100–15,000). default `4000`; range 100–15000 |
| `animation_action_id` | integer |  | Animation preset ID from Meshy's animation library (0 is Idle). Only used when animation is enabled. default `92`; range 0–696 |

## Details

Meshy T2 turns a single image into a clean Smart Topology triangle mesh (up to 15,000 triangles), with optional textures, rigging and animation.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Image URL or base64 data URI of the object. Supports .jpg, .jpeg and .png; AVIF and HEIF are converted automatically. |
| `should_texture` | boolean | `true` | Generate textures. Untextured meshes cost less. |
| `target_polycount` | integer 100–15000 | `4000` | Target polygon count (100–15,000). |
| `pose_mode` | `a-pose` / `t-pose` / `` | `""` | Generate the character in an A-pose or T-pose; empty for no specific pose. |
| `enable_pbr` | boolean | `false` | Generate PBR maps (metallic, roughness, normal) in addition to base color. |
| `texture_prompt` | string | — | Text prompt to guide texturing. Maximum 800 characters. |
| `texture_image` | image URL | — | Image URL to guide texturing. |
| `enable_rigging` | boolean | `false` | Rig the model as a humanoid character. The rigged GLB is returned as rigged_glb. |
| `enable_animation` | boolean | `false` | Apply an animation preset to the rigged character (billed together with rigging). The animated GLB is returned as animation_glb. |
| `animation_action_id` | integer 0–696 | `92` | Animation preset ID from Meshy's animation library (0 is Idle). Only used when animation is enabled. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
- `rigged_glb`: Additional file returned by the provider.
- `animation_glb`: Additional file returned by the provider.
### Billing
$0.60 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| enable_animation on | $0.92 |
| enable_animation off | $0.60 |
| enable_rigging on | $0.80 |
| enable_rigging off | $0.60 |
| should_texture on | $0.60 |
| should_texture off | $0.20 |
Failed runs are not charged.
### Also on SandBase
Other Meshy 3D endpoints: `meshy/6.0-lite/retexture`, `meshy/6.0/retexture`, `meshy/7.0/image-to-3d`, `meshy/7.0/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/t2/image-to-3d.json`](../../../../catalog/models/meshy/t2/image-to-3d.json) · Store page: https://www.sandbase.ai/model/meshy/t2/image-to-3d
