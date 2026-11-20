# Meshy 6 Lite Multi-Image to 3D API: pricing, parameters and code examples

`meshy/6.0-lite/multi-image-to-3d` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $0.92 per run, depending on parameters · **Modes:** async

Meshy 6 Lite turns 1–4 views of the same object into a 3D model at a lower price, with optional textures, PBR maps, humanoid rigging and animation.

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
  -d '{"model": "meshy/6.0-lite/multi-image-to-3d", "images": ["https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/8cd745f8-1eac-46bb-acfe-6fb7e7821578.png", "https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/bb330eb5-86bc-452c-bafc-b22f6a1ee4a0.png", "https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/c161bf92-9b5c-4043-89ce-b1e997af1f2d.png"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/6.0-lite/multi-image-to-3d', {'images': ['https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/8cd745f8-1eac-46bb-acfe-6fb7e7821578.png', 'https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/bb330eb5-86bc-452c-bafc-b22f6a1ee4a0.png', 'https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/c161bf92-9b5c-4043-89ce-b1e997af1f2d.png']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/6.0-lite/multi-image-to-3d", {
  "images": [
    "https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/8cd745f8-1eac-46bb-acfe-6fb7e7821578.png",
    "https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/bb330eb5-86bc-452c-bafc-b22f6a1ee4a0.png",
    "https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/c161bf92-9b5c-4043-89ce-b1e997af1f2d.png"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/6.0-lite/multi-image-to-3d", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/8cd745f8-1eac-46bb-acfe-6fb7e7821578.png", "https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/bb330eb5-86bc-452c-bafc-b22f6a1ee4a0.png", "https://static.sandbase.ai/examples/258db007-95dd-4ccd-9f96-c94239151a1c/input/c161bf92-9b5c-4043-89ce-b1e997af1f2d.png"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | 1 to 4 images of the same object from different angles. Supports .jpg, .jpeg and .png; AVIF and HEIF are converted automatically.  |
| `topology` | string |  | quad for smooth surfaces, triangle for detail. one of: `quad`, `triangle`; default `"triangle"` |
| `pose_mode` | string |  | Generate the character in an A-pose or T-pose; empty for no specific pose. one of: `a-pose`, `t-pose`, ``; default `""` |
| `enable_pbr` | boolean |  | Generate PBR maps (metallic, roughness, normal) in addition to base color. default `false` |
| `symmetry_mode` | string |  | Symmetry enforcement: off, auto or on. one of: `off`, `auto`, `on`; default `"auto"` |
| `texture_image` | string |  | Image URL to guide texturing.  |
| `enable_rigging` | boolean |  | Rig the model as a humanoid character. The rigged GLB is returned as rigged_glb. default `false` |
| `should_texture` | boolean |  | Generate textures. Untextured meshes cost less. default `true` |
| `texture_prompt` | string |  | Text prompt to guide texturing. Maximum 800 characters.  |
| `enable_animation` | boolean |  | Apply an animation preset to the rigged character (billed together with rigging). The animated GLB is returned as animation_glb. default `false` |
| `target_polycount` | integer |  | Target polygon count (100–300,000). default `30000`; range 100–300000 |
| `animation_action_id` | integer |  | Animation preset ID from Meshy's animation library (0 is Idle). Only used when animation is enabled. default `92`; range 0–696 |

## Details

Meshy 6 Lite turns 1–4 views of the same object into a 3D model at a lower price, with optional textures, PBR maps, humanoid rigging and animation.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | array, required | — | 1 to 4 images of the same object from different angles. Supports .jpg, .jpeg and .png; AVIF and HEIF are converted automatically. |
| `topology` | `quad` / `triangle` | `"triangle"` | quad for smooth surfaces, triangle for detail. |
| `pose_mode` | `a-pose` / `t-pose` / `` | `""` | Generate the character in an A-pose or T-pose; empty for no specific pose. |
| `enable_pbr` | boolean | `false` | Generate PBR maps (metallic, roughness, normal) in addition to base color. |
| `symmetry_mode` | `off` / `auto` / `on` | `"auto"` | Symmetry enforcement: off, auto or on. |
| `texture_image` | string | — | Image URL to guide texturing. |
| `enable_rigging` | boolean | `false` | Rig the model as a humanoid character. The rigged GLB is returned as rigged_glb. |
| `should_texture` | boolean | `true` | Generate textures. Untextured meshes cost less. |
| `texture_prompt` | string | — | Text prompt to guide texturing. Maximum 800 characters. |
| `enable_animation` | boolean | `false` | Apply an animation preset to the rigged character (billed together with rigging). The animated GLB is returned as animation_glb. |
| `target_polycount` | integer 100–300000 | `30000` | Target polygon count (100–300,000). |
| `animation_action_id` | integer 0–696 | `92` | Animation preset ID from Meshy's animation library (0 is Idle). Only used when animation is enabled. |
### Output
- `url`: GLB model.
- `thumbnail`: Preview image.
- `rigged_glb`: Rigged character (when rigging is enabled).
- `animation_glb`: Animated character (when animation is enabled).
### Billing
$0.60 per textured model, $0.20 untextured (text-to-3d: `generation_mode=preview`). Rigging adds $0.20; animation adds $0.12 on top of rigging.

---
Machine-readable: [`catalog/models/meshy/6.0-lite/multi-image-to-3d.json`](../../../../catalog/models/meshy/6.0-lite/multi-image-to-3d.json) · Store page: https://www.sandbase.ai/model/meshy/6.0-lite/multi-image-to-3d
