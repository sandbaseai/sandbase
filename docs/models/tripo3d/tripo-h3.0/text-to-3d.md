# Tripo H3.0 Text to 3D API: pricing, parameters and code examples

`tripo3d/tripo-h3.0/text-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $0.4 per run, depending on parameters · **Modes:** async

Tripo H3.0 Text to 3D by Tripo3D: turn a text prompt into a textured 3D model.

## Pricing

- Depends on parameters (`params.generate_parts`, `params.geometry_quality`, `params.pbr`, `params.quad`, `params.smart_low_poly`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| defaults | 0.2 |
| generate_parts=false | 0.2 |
| generate_parts=true | 0.4 |
| geometry_quality="standard" | 0.2 |
| geometry_quality="detailed" | 0.4 |
| pbr=false | 0.2 |
| pbr=true | 0.2 |
| quad=false | 0.2 |
| quad=true | 0.25 |
| smart_low_poly=false | 0.2 |
| smart_low_poly=true | 0.3 |
| texture=false | 0.2 |
| texture=true | 0.2 |
| texture_quality="fast" | 0.2 |
| texture_quality="standard" | 0.2 |
| texture_quality="detailed" | 0.3 |
| texture_quality="extreme" | 0.4 |

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-h3.0/text-to-3d", "prompt": "A low-poly medieval wooden treasure chest with iron hinges and a rusty lock."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-h3.0/text-to-3d', {'prompt': 'A low-poly medieval wooden treasure chest with iron hinges and a rusty lock.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-h3.0/text-to-3d", {
  "prompt": "A low-poly medieval wooden treasure chest with iron hinges and a rusty lock."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-h3.0/text-to-3d", sandbase.Params{
	"prompt": "A low-poly medieval wooden treasure chest with iron hinges and a rusty lock.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pbr` | boolean |  | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. default `true` |
| `quad` | boolean |  | Quad topology instead of triangles. Output becomes FBX; 10,000 faces when face_limit is unset. default `false` |
| `seed` | integer |  | Seed for geometry generation (Tripo model_seed). Same seed and input give the same mesh.  |
| `prompt` | string | yes | Describe shape, material, style and scale. Up to 1,024 characters.  |
| `delight` | boolean |  | Remove baked-in lighting from the reference image before texturing (texture v3.5). default `false` |
| `texture` | boolean |  | Generate textures. Set texture and pbr to false for bare geometry (cheaper). default `true` |
| `compress` | string |  | geometry applies meshopt compression to reduce file size. one of: `geometry` |
| `auto_size` | boolean |  | Scale the model to real-world size in meters. default `false` |
| `export_uv` | boolean |  | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. default `true` |
| `face_limit` | integer |  | Maximum face count, up to 2,000,000 (detailed geometry) or 1,000,000; up to 150,000 with quad. Adaptive when unset. range –2000000 |
| `image_seed` | integer |  | Seed for the internal text-to-image step.  |
| `texture_seed` | integer |  | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry.  |
| `generate_parts` | boolean |  | Editable segmented parts. Requires texture=false and pbr=false; billed as an add-on. default `false` |
| `smart_low_poly` | boolean |  | Hand-crafted style low-poly topology (500-20,000 faces). Best for simple objects; billed as an add-on. default `false` |
| `negative_prompt` | string |  | What to avoid, up to 255 characters.  |
| `texture_quality` | string |  | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |
| `texture_version` | string |  | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. one of: `v3.5-20260815`, `v3.0-20250812`, `v2.5-20250123` |
| `geometry_quality` | string |  | detailed (Ultra) adds mesh detail and is billed as an add-on. one of: `standard`, `detailed`; default `"standard"` |
| `export_orientation` | string |  | Forward axis of the exported model. Leave unset if you will post-process the model. one of: `+x`, `-x`, `+y`, `-y` |

## Details

Tripo H3.0 (v3.0-20250812) is Tripo's previous-generation stable model, kept for backward compatibility, with HD geometry, quad, smart low-poly and part generation.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Describe shape, material, style and scale. Up to 1,024 characters. |
| `negative_prompt` | string | — | What to avoid, up to 255 characters. |
| `texture` | boolean | `true` | Generate textures. Set texture and pbr to false for bare geometry (cheaper). |
| `pbr` | boolean | `true` | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. |
| `geometry_quality` | `standard` / `detailed` | `standard` | detailed (Ultra) adds mesh detail and is billed as an add-on. |
| `quad` | boolean | `false` | Quad topology instead of triangles. Output becomes FBX; 10,000 faces when face_limit is unset. |
| `smart_low_poly` | boolean | `false` | Hand-crafted style low-poly topology (500-20,000 faces). Best for simple objects; billed as an add-on. |
| `generate_parts` | boolean | `false` | Editable segmented parts. Requires texture=false and pbr=false; billed as an add-on. |
| `face_limit` | integer | — | Maximum face count, up to 2,000,000 (detailed geometry) or 1,000,000; up to 150,000 with quad. Adaptive when unset. |
| `seed` | integer | — | Seed for geometry generation (Tripo model_seed). Same seed and input give the same mesh. |
| `texture_seed` | integer | — | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry. |
| `image_seed` | integer | — | Seed for the internal text-to-image step. |
| `texture_version` | `v3.5-20260815` / `v3.0-20250812` / `v2.5-20250123` | — | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. |
| `delight` | boolean | `false` | Remove baked-in lighting from the reference image before texturing (texture v3.5). |
| `export_uv` | boolean | `true` | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. |
| `export_orientation` | `+x` / `-x` / `+y` / `-y` | — | Forward axis of the exported model. Leave unset if you will post-process the model. |
| `compress` | `geometry` | — | geometry applies meshopt compression to reduce file size. |
| `auto_size` | boolean | `false` | Scale the model to real-world size in meters. |
### Output
- `url`: 3D model (GLB; FBX when quad is on).
- `thumbnail`: Preview render.
- `generated_image`: Reference image Tripo generated from the prompt.
### Billing
$0.20 textured (standard or fast texture), $0.10 untextured (texture and pbr false).
| Add-on | Price |
|---|---|
| texture_quality = detailed | +$0.10 |
| texture_quality = extreme | +$0.20 |
| geometry_quality = detailed | +$0.20 |
| quad | +$0.05 |
| smart_low_poly | +$0.10 |
| generate_parts | +$0.20 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo-h3.0/text-to-3d.json`](../../../../catalog/models/tripo3d/tripo-h3.0/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-h3.0/text-to-3d
