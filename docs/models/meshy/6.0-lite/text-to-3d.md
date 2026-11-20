# Meshy 6 Lite Text to 3D API: pricing, parameters and code examples

`meshy/6.0-lite/text-to-3d` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $0.92 per run, depending on parameters · **Modes:** async

Meshy 6 Lite turns a text prompt into a 3D model at a lower price: a preview mesh, then textures, with optional humanoid rigging and animation.

## Pricing

- Depends on parameters (`params.enable_animation`, `params.enable_rigging`, `params.generation_mode`).

| parameters | USD |
|---|---|
| enable_animation=false, enable_rigging=false, generation_mode="preview" | 0.2 |
| enable_animation=false, enable_rigging=false, generation_mode="full" | 0.6 |
| enable_animation=false, enable_rigging=true, generation_mode="preview" | 0.4 |
| enable_animation=false, enable_rigging=true, generation_mode="full" | 0.8 |
| enable_animation=true, enable_rigging=false, generation_mode="preview" | 0.52 |
| enable_animation=true, enable_rigging=false, generation_mode="full" | 0.92 |
| enable_animation=true, enable_rigging=true, generation_mode="preview" | 0.52 |
| enable_animation=true, enable_rigging=true, generation_mode="full" | 0.92 |

Formula: `((params.generation_mode ?? "full") == "full" ? 0.6 : 0.2) + (((params.enable_rigging ?? false) || (params.enable_animation ?? false)) ? 0.2 : 0.0) + ((params.enable_animation ?? false) ? 0.12 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/6.0-lite/text-to-3d", "prompt": "A rustic, antique wooden treasure chest with a curved, domed lid, constructed from weathered, dark brown planks exhibiting prominent wood grain and subtle distress. It'\''s heavily reinforced with broad, dark grey, oxidized metal bands secured by numerous circular rivets. Ornate, dark iron decorative elements featuring swirling foliate patterns and dragon motifs adorn the corners and lid. A prominent, circular, intricately carved metal lock plate with a central keyhole dominates the front, flanked by two large, dark metallic pull rings."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/6.0-lite/text-to-3d', {'prompt': "A rustic, antique wooden treasure chest with a curved, domed lid, constructed from weathered, dark brown planks exhibiting prominent wood grain and subtle distress. It's heavily reinforced with broad, dark grey, oxidized metal bands secured by numerous circular rivets. Ornate, dark iron decorative elements featuring swirling foliate patterns and dragon motifs adorn the corners and lid. A prominent, circular, intricately carved metal lock plate with a central keyhole dominates the front, flanked by two large, dark metallic pull rings."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/6.0-lite/text-to-3d", {
  "prompt": "A rustic, antique wooden treasure chest with a curved, domed lid, constructed from weathered, dark brown planks exhibiting prominent wood grain and subtle distress. It's heavily reinforced with broad, dark grey, oxidized metal bands secured by numerous circular rivets. Ornate, dark iron decorative elements featuring swirling foliate patterns and dragon motifs adorn the corners and lid. A prominent, circular, intricately carved metal lock plate with a central keyhole dominates the front, flanked by two large, dark metallic pull rings."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/6.0-lite/text-to-3d", sandbase.Params{
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

## Details

Meshy 6 Lite turns a text prompt into a 3D model at a lower price: a preview mesh, then textures, with optional humanoid rigging and animation.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `seed` | integer | — | Seed for reproducible geometry. |
| `prompt` | string, required | — | Describe the object to generate. Maximum 600 characters. |
| `topology` | `quad` / `triangle` | `"triangle"` | quad for smooth surfaces, triangle for detail. |
| `pose_mode` | `a-pose` / `t-pose` / `` | `""` | Generate the character in an A-pose or T-pose; empty for no specific pose. |
| `enable_pbr` | boolean | `false` | Generate PBR maps (metallic, roughness, normal) in addition to base color. |
| `symmetry_mode` | `off` / `auto` / `on` | `"auto"` | Symmetry enforcement: off, auto or on. |
| `texture_image` | string | — | Image URL to guide texturing. |
| `enable_rigging` | boolean | `false` | Rig the model as a humanoid character. The rigged GLB is returned as rigged_glb. |
| `texture_prompt` | string | — | Text prompt to guide texturing. Maximum 800 characters. |
| `generation_mode` | `preview` / `full` | `"full"` | 'preview' returns the untextured mesh only; 'full' also textures it. |
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
Machine-readable: [`catalog/models/meshy/6.0-lite/text-to-3d.json`](../../../../catalog/models/meshy/6.0-lite/text-to-3d.json) · Store page: https://www.sandbase.ai/model/meshy/6.0-lite/text-to-3d
