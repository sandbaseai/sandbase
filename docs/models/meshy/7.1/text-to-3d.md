# Meshy 7.1 Text to 3D API: pricing, parameters and code examples

`meshy/7.1/text-to-3d` · image generation model · Meshy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $1.44 to $2.304 per run, depending on parameters · **Modes:** async

Meshy 7.1 generates a textured, optionally rigged and animated 3D model from a text prompt.

## Pricing

- Depends on parameters (`params.enable_animation`, `params.enable_rigging`, `params.geometry_resolution`).

| parameters | USD |
|---|---|
| enable_animation=false, enable_rigging=false, geometry_resolution="standard" | 1.44 |
| enable_animation=false, enable_rigging=false, geometry_resolution="2k" | 1.68 |
| enable_animation=false, enable_rigging=false, geometry_resolution="4k" | 1.92 |
| enable_animation=false, enable_rigging=true, geometry_resolution="standard" | 1.68 |
| enable_animation=false, enable_rigging=true, geometry_resolution="2k" | 1.92 |
| enable_animation=false, enable_rigging=true, geometry_resolution="4k" | 2.16 |
| enable_animation=true, enable_rigging=false, geometry_resolution="standard" | 1.44 |
| enable_animation=true, enable_rigging=false, geometry_resolution="2k" | 1.68 |
| enable_animation=true, enable_rigging=false, geometry_resolution="4k" | 1.92 |
| enable_animation=true, enable_rigging=true, geometry_resolution="standard" | 1.824 |
| enable_animation=true, enable_rigging=true, geometry_resolution="2k" | 2.064 |
| enable_animation=true, enable_rigging=true, geometry_resolution="4k" | 2.304 |

Formula: `1.44 + ((params.geometry_resolution ?? "standard") == "4k" ? 0.48 : (params.geometry_resolution ?? "standard") == "2k" ? 0.24 : 0.0) + ((params.enable_rigging ?? false) ? 0.24 : 0.0) + ((params.enable_rigging ?? false) && (params.enable_animation ?? false) ? 0.144 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meshy/7.1/text-to-3d", "prompt": "A sci-fi hover bike with glowing cyan thrusters and sleek white armor panels"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meshy/7.1/text-to-3d', {'prompt': 'A sci-fi hover bike with glowing cyan thrusters and sleek white armor panels'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meshy/7.1/text-to-3d", {
  "prompt": "A sci-fi hover bike with glowing cyan thrusters and sleek white armor panels"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meshy/7.1/text-to-3d", sandbase.Params{
	"prompt": "A sci-fi hover bike with glowing cyan thrusters and sleek white armor panels",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Seed for reproducible results.  |
| `prompt` | string | yes | Describe what kind of object the 3D model is. Maximum 600 characters.  |
| `topology` | string |  | quad for smooth surfaces, triangle for detail. one of: `quad`, `triangle`; default `"triangle"` |
| `pose_mode` | string |  | a-pose, t-pose or empty for none. one of: `a-pose`, `t-pose`, ``; default `""` |
| `enable_pbr` | boolean |  | Generate PBR maps (metallic, roughness, normal). default `false` |
| `model_type` | string |  | Model type. Only standard is supported by Meshy 7.1; use Meshy T2 / T2.5 for Smart Topology meshes. one of: `standard`; default `"standard"` |
| `symmetry_mode` | string |  | off / auto / on. one of: `off`, `auto`, `on`; default `"auto"` |
| `texture_image` | string |  | Image URL to guide texturing.  |
| `enable_rigging` | boolean |  | Rig the model as a humanoid character (+$0.20). default `false` |
| `texture_prompt` | string |  | Text prompt to guide texturing.  |
| `enable_animation` | boolean |  | Apply an animation preset; requires enable_rigging (+$0.12). default `false` |
| `target_polycount` | integer |  | Target polygon count (100–300,000). default `30000`; range 100–300000 |
| `geometry_resolution` | string |  | Geometry resolution. one of: `standard`, `2k`, `4k`; default `"standard"` |

## Details

Meshy 7.1 turns a text prompt into a textured 3D model, optionally rigged and animated.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 600 characters. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `texture_prompt` | string | — | Optional texture description. |
| `pose_mode` | `a-pose` / `t-pose` / `` | — | Force an A- or T-pose. |
| `symmetry_mode` | `off` / `auto` / `on` | `auto` | Enforce symmetry. |
| `enable_animation` | boolean | false | Add a walk/run animation (requires rigging). |
| `enable_pbr` | boolean | false | PBR texture maps. |
| `target_polycount` | integer 100–300000 | 30000 | Target polygon count. |
| `topology` | `quad` / `triangle` | `triangle` | Quad or triangle mesh. |
| `model_type` | `standard` | `standard` | Only `standard` is supported; use Meshy T2 / T2.5 for Smart Topology meshes. |
| `enable_rigging` | boolean | false | Add a humanoid rig. |
| `geometry_resolution` | `standard` / `2k` / `4k` | `standard` | Mesh detail; higher tiers cost more. |
| `texture_image` | image URL | — | Optional texture reference image. |

### Billing

$1.44 per textured model; 2K geometry adds $0.24 and 4K adds $0.48; rigging adds $0.24 and animation another $0.144.

| Request | Price |
|---|---|
| Textured | $1.44 |
| Textured, 2K geometry | $1.68 |
| Textured + rig + animation | $1.824 |

Failed runs are not charged.

### Prompting

- Describe or show one object; plain backgrounds work best.

### Also on SandBase

Other Meshy 7.1 endpoints: `meshy/7.1/image-to-3d`, `meshy/7.1/multi-image-to-3d`.

---
Machine-readable: [`catalog/models/meshy/7.1/text-to-3d.json`](../../../../catalog/models/meshy/7.1/text-to-3d.json) · Store page: https://www.sandbase.ai/model/meshy/7.1/text-to-3d
