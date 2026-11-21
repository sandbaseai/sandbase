# Meshy 7.1 Image to 3D API: pricing, parameters and code examples

`meshy/7.1/image-to-3d` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.8 to $1.52 per run, depending on parameters · **Modes:** async

Meshy 7.1 turns a single image into a textured, optionally rigged and animated 3D model.

## Pricing

- Depends on parameters (`params.enable_animation`, `params.enable_rigging`, `params.geometry_resolution`, `params.should_texture`, `params.texture_resolution`).

| parameters | USD |
|---|---|
| defaults | 1.2 |
| enable_animation=false | 1.2 |
| enable_animation=true | 1.52 |
| enable_rigging=false | 1.2 |
| enable_rigging=true | 1.4 |
| geometry_resolution="standard" | 1.2 |
| geometry_resolution="2k" | 1.4 |
| geometry_resolution="4k" | 1.4 |
| should_texture=false | 0.8 |
| should_texture=true | 1.2 |
| texture_resolution="2k" | 1.2 |
| texture_resolution="4k" | 1.2 |
| texture_resolution="8k" | 1.4 |

Formula: `((params.should_texture ?? true) ? 1.2 : 0.8) + ((params.geometry_resolution ?? "standard") != "standard" ? 0.2 : 0.0) + (((params.enable_rigging ?? false) || (params.enable_animation ?? false)) ? 0.2 : 0.0) + ((params.enable_animation ?? false) ? 0.12 : 0.0) + ((params.should_texture ?? true) ? ((params.texture_resolution ?? "2k") == "8k" ? 0.2 : 0.0) : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/7.1/image-to-3d", "image": "https://static.sandbase.ai/examples/98a63072-1f8d-44bb-9613-1f62a41a7762/input/a144ab78-53c0-4a78-a9b1-8178c43bd71c.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/7.1/image-to-3d', {'image': 'https://static.sandbase.ai/examples/98a63072-1f8d-44bb-9613-1f62a41a7762/input/a144ab78-53c0-4a78-a9b1-8178c43bd71c.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/7.1/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/98a63072-1f8d-44bb-9613-1f62a41a7762/input/a144ab78-53c0-4a78-a9b1-8178c43bd71c.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/7.1/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/98a63072-1f8d-44bb-9613-1f62a41a7762/input/a144ab78-53c0-4a78-a9b1-8178c43bd71c.png",
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
| `auto_size` | boolean |  | Estimate the object's real-world height and scale the model to it. The origin goes to the bottom unless origin_at is set. default `false` |
| `origin_at` | string |  | Where to place the model origin. one of: `bottom`, `center` |
| `pose_mode` | string |  | a-pose, t-pose or empty for none. one of: `a-pose`, `t-pose`, ``; default `""` |
| `enable_pbr` | boolean |  | Generate PBR maps (metallic, roughness, normal). default `false` |
| `model_type` | string |  | Model type. Only standard is supported by Meshy 7.1; use Meshy T2 / T2.5 for Smart Topology meshes. one of: `standard`; default `"standard"` |
| `symmetry_mode` | string |  | off / auto / on. one of: `off`, `auto`, `on`; default `"auto"` |
| `texture_image` | string |  | Image URL to guide texturing.  |
| `texture_model` | string |  | Texture model that paints the mesh; leave empty for the geometry model's default. meshy-n1 textures from the image only (no text prompt, no PBR, 2k only). one of: `meshy-7`, `meshy-n1`, `meshy-6-lite` |
| `enable_rigging` | boolean |  | Rig the model as a humanoid character (+$0.20). default `false` |
| `should_texture` | boolean |  | Generate textures (untextured models are cheaper). default `true` |
| `texture_prompt` | string |  | Text prompt to guide texturing.  |
| `remove_lighting` | boolean |  | Remove baked highlights and shadows from the base color texture. Takes effect with the Meshy 6 texture model.  |
| `enable_animation` | boolean |  | Apply an animation preset; requires enable_rigging (+$0.12). default `false` |
| `target_polycount` | integer |  | Target polygon count (100–300,000). default `30000`; range 100–300000 |
| `image_enhancement` | boolean |  | Optimize the input image before generating; false keeps its exact look. Not supported by Meshy 6 Lite or Smart Topology.  |
| `texture_resolution` | string |  | Base color texture resolution. 8k costs $0.20 more. one of: `2k`, `4k`, `8k`; default `"2k"` |
| `geometry_resolution` | string |  | Geometry resolution. one of: `standard`, `2k`, `4k`; default `"standard"` |

## Details

Meshy 7.1 turns a single image into a textured 3D model, optionally rigged and animated.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Image URL or base64 data URI for 3D model creation. |
| `symmetry_mode` | `off` / `auto` / `on` | `auto` | Enforce symmetry. |
| `enable_rigging` | boolean | false | Add a humanoid rig. |
| `model_type` | `standard` | `standard` | Only `standard` is supported; use Meshy T2 / T2.5 for Smart Topology meshes. |
| `enable_pbr` | boolean | false | PBR texture maps. |
| `pose_mode` | `a-pose` / `t-pose` / `` | — | Force an A- or T-pose. |
| `should_texture` | boolean | true | Generate textures; untextured costs less. |
| `enable_animation` | boolean | false | Add a walk/run animation (requires rigging). |
| `texture_prompt` | string | — | Optional texture description. |
| `geometry_resolution` | `standard` / `2k` / `4k` | `standard` | Mesh detail; higher tiers cost more. |
| `target_polycount` | integer 100–300000 | 30000 | Target polygon count. |
| `topology` | `quad` / `triangle` | `triangle` | Quad or triangle mesh. |
| `texture_image` | image URL | — | Optional texture reference image. |

| `texture_resolution` | `2k` / `4k` / `8k` | `"2k"` | Base color texture resolution. 8k costs $0.20 more. |
| `texture_model` | `meshy-7` / `meshy-n1` / `meshy-6-lite` | — | Texture model that paints the mesh; leave empty for the geometry model's default. meshy-n1 textures from the image only (no text prompt, no PBR, 2k only). |
| `auto_size` | boolean | `false` | Estimate the object's real-world height and scale the model to it. The origin goes to the bottom unless origin_at is set. |
| `origin_at` | `bottom` / `center` | — | Where to place the model origin. |
| `image_enhancement` | boolean | — | Optimize the input image before generating; false keeps its exact look. Not supported by Meshy 6 Lite or Smart Topology. |
| `remove_lighting` | boolean | — | Remove baked highlights and shadows from the base color texture. Takes effect with the Meshy 6 texture model. |
### Billing
$1.20 per textured model ($0.80 untextured); 2K or 4K geometry adds $0.20; rigging adds $0.20 and animation (includes rigging) another $0.12.
| Request | Price |
|---|---|
| Textured | $1.20 |
| Untextured | $0.80 |
| Textured, 2K or 4K geometry | $1.40 |
| Textured + rig + animation | $1.52 |
8k textures add $0.20 (textured requests only).
Failed runs are not charged.
### Prompting

- Describe or show one object; plain backgrounds work best.

### Also on SandBase

Other Meshy 7.1 endpoints: `meshy/7.1/text-to-3d`, `meshy/7.1/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/7.1/image-to-3d.json`](../../../../catalog/models/meshy/7.1/image-to-3d.json) · Store page: https://www.sandbase.ai/model/meshy/7.1/image-to-3d
