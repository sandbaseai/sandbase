# Meshy 7 Text to 3D API: pricing, parameters and code examples

`meshy/7.0/text-to-3d` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.8 to $1.72 per run, depending on parameters · **Modes:** async

Meshy 7 generates a 3D model from a text prompt, either as an untextured preview mesh or fully textured, with optional 2K geometry, rigging and animation.

## Pricing

- Depends on parameters (`params.enable_animation`, `params.enable_rigging`, `params.generation_mode`, `params.geometry_resolution`).

| parameters | USD |
|---|---|
| enable_animation=false, enable_rigging=false, generation_mode="preview", geometry_resolution="standard" | 0.8 |
| enable_animation=false, enable_rigging=false, generation_mode="preview", geometry_resolution="2k" | 1 |
| enable_animation=false, enable_rigging=false, generation_mode="full", geometry_resolution="standard" | 1.2 |
| enable_animation=false, enable_rigging=false, generation_mode="full", geometry_resolution="2k" | 1.4 |
| enable_animation=false, enable_rigging=true, generation_mode="preview", geometry_resolution="standard" | 1 |
| enable_animation=false, enable_rigging=true, generation_mode="preview", geometry_resolution="2k" | 1.2 |
| enable_animation=false, enable_rigging=true, generation_mode="full", geometry_resolution="standard" | 1.4 |
| enable_animation=false, enable_rigging=true, generation_mode="full", geometry_resolution="2k" | 1.6 |
| enable_animation=true, enable_rigging=false, generation_mode="preview", geometry_resolution="standard" | 1.12 |
| enable_animation=true, enable_rigging=false, generation_mode="preview", geometry_resolution="2k" | 1.32 |
| enable_animation=true, enable_rigging=false, generation_mode="full", geometry_resolution="standard" | 1.52 |
| enable_animation=true, enable_rigging=false, generation_mode="full", geometry_resolution="2k" | 1.72 |
| enable_animation=true, enable_rigging=true, generation_mode="preview", geometry_resolution="standard" | 1.12 |
| enable_animation=true, enable_rigging=true, generation_mode="preview", geometry_resolution="2k" | 1.32 |
| enable_animation=true, enable_rigging=true, generation_mode="full", geometry_resolution="standard" | 1.52 |
| enable_animation=true, enable_rigging=true, generation_mode="full", geometry_resolution="2k" | 1.72 |

Formula: `((params.generation_mode ?? "full") == "full" ? 1.2 : 0.8) + ((params.geometry_resolution ?? "standard") == "2k" ? 0.2 : 0.0) + (((params.enable_rigging ?? false) || (params.enable_animation ?? false)) ? 0.2 : 0.0) + ((params.enable_animation ?? false) ? 0.12 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/7.0/text-to-3d", "prompt": "A rustic, antique wooden treasure chest with a curved, domed lid, constructed from weathered, dark brown planks exhibiting prominent wood grain and subtle distress. It'\''s heavily reinforced with broad, dark grey, oxidized metal bands secured by numerous circular rivets. Ornate, dark iron decorative elements featuring swirling foliate patterns and dragon motifs adorn the corners and lid. A prominent, circular, intricately carved metal lock plate with a central keyhole dominates the front, flanked by two large, dark metallic pull rings."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/7.0/text-to-3d', {'prompt': "A rustic, antique wooden treasure chest with a curved, domed lid, constructed from weathered, dark brown planks exhibiting prominent wood grain and subtle distress. It's heavily reinforced with broad, dark grey, oxidized metal bands secured by numerous circular rivets. Ornate, dark iron decorative elements featuring swirling foliate patterns and dragon motifs adorn the corners and lid. A prominent, circular, intricately carved metal lock plate with a central keyhole dominates the front, flanked by two large, dark metallic pull rings."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/7.0/text-to-3d", {
  "prompt": "A rustic, antique wooden treasure chest with a curved, domed lid, constructed from weathered, dark brown planks exhibiting prominent wood grain and subtle distress. It's heavily reinforced with broad, dark grey, oxidized metal bands secured by numerous circular rivets. Ornate, dark iron decorative elements featuring swirling foliate patterns and dragon motifs adorn the corners and lid. A prominent, circular, intricately carved metal lock plate with a central keyhole dominates the front, flanked by two large, dark metallic pull rings."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/7.0/text-to-3d", sandbase.Params{
	"prompt": "A rustic, antique wooden treasure chest with a curved, domed lid, constructed from weathered, dark brown planks exhibiting prominent wood grain and subtle distress. It's heavily reinforced with broad, dark grey, oxidized metal bands secured by numerous circular rivets. Ornate, dark iron decorative elements featuring swirling foliate patterns and dragon motifs adorn the corners and lid. A prominent, circular, intricately carved metal lock plate with a central keyhole dominates the front, flanked by two large, dark metallic pull rings.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for reproducible geometry.  |
| `prompt` | string | yes | Describe the object to generate. Maximum 600 characters.  |
| `topology` | string |  | quad for smooth surfaces, triangle for detail. one of: `quad`, `triangle`; default `"triangle"` |
| `pose_mode` | string |  | Generate the character in an A-pose or T-pose; empty for no specific pose. one of: `a-pose`, `t-pose`, ``; default `""` |
| `enable_pbr` | boolean |  | Generate PBR maps (metallic, roughness, normal) in addition to base color. default `false` |
| `symmetry_mode` | string |  | Symmetry enforcement: off, auto or on. one of: `off`, `auto`, `on`; default `"auto"` |
| `texture_image` | string |  | Image URL to guide texturing.  |
| `enable_rigging` | boolean |  | Rig the model as a humanoid character. The rigged GLB is returned as rigged_glb. default `false` |
| `texture_prompt` | string |  | Text prompt to guide texturing. Maximum 800 characters.  |
| `generation_mode` | string |  | 'preview' returns the untextured mesh only; 'full' also textures it. one of: `preview`, `full`; default `"full"` |
| `enable_animation` | boolean |  | Apply an animation preset to the rigged character (billed together with rigging). The animated GLB is returned as animation_glb. default `false` |
| `target_polycount` | integer |  | Target polygon count (100–300,000). default `30000`; range 100–300000 |
| `animation_action_id` | integer |  | Animation preset ID from Meshy's animation library (0 is Idle). Only used when animation is enabled. default `92`; range 0–696 |
| `geometry_resolution` | string |  | Geometry resolution. 2k gives finer geometry at a higher price. one of: `standard`, `2k`; default `"standard"` |

## Details

Meshy 7 generates a 3D model from a text prompt, either as an untextured preview mesh or fully textured, with optional 2K geometry, rigging and animation.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Describe the object to generate. Maximum 600 characters. |
| `generation_mode` | `preview` / `full` | `full` | 'preview' returns the untextured mesh only; 'full' also textures it. |
| `seed` | integer | — | Seed for reproducible geometry. |
| `symmetry_mode` | `off` / `auto` / `on` | `auto` | Symmetry enforcement: off, auto or on. |
| `topology` | `quad` / `triangle` | `triangle` | quad for smooth surfaces, triangle for detail. |
| `geometry_resolution` | `standard` / `2k` | `standard` | Geometry resolution. 2k gives finer geometry at a higher price. |
| `target_polycount` | integer 100–300000 | `30000` | Target polygon count (100–300,000). |
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
$1.20 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| enable_animation on | $1.52 |
| enable_animation off | $1.20 |
| enable_rigging on | $1.40 |
| enable_rigging off | $1.20 |
| generation_mode = preview | $0.80 |
| generation_mode = full | $1.20 |
| geometry_resolution = standard | $1.20 |
| geometry_resolution = 2k | $1.40 |
Failed runs are not charged.
### Also on SandBase
Other Meshy 3D endpoints: `meshy/6.0-lite/retexture`, `meshy/6.0/retexture`, `meshy/7.0/image-to-3d`, `meshy/7.0/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/7.0/text-to-3d.json`](../../../../catalog/models/meshy/7.0/text-to-3d.json) · Store page: https://www.sandbase.ai/model/meshy/7.0/text-to-3d
