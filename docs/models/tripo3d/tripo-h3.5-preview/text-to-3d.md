# Tripo H3.5 Preview Text to 3D API: pricing, parameters and code examples

`tripo3d/tripo-h3.5-preview/text-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.3 to $0.75 per run, depending on parameters · **Modes:** async

Tripo H3.5 Preview is Tripo3D's newest high-fidelity text-to-3D model. Turn written descriptions into detailed, textured 3D models for 3D printing, games and product visuals.

## Pricing

- Depends on parameters (`params.geometry_quality`, `params.pbr`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| geometry_quality="standard", pbr=false, texture=false, texture_quality="fast" | 0.3 |
| geometry_quality="standard", pbr=false, texture=false, texture_quality="standard" | 0.3 |
| geometry_quality="standard", pbr=false, texture=false, texture_quality="detailed" | 0.3 |
| geometry_quality="standard", pbr=false, texture=false, texture_quality="extreme" | 0.3 |
| geometry_quality="standard", pbr=false, texture=true, texture_quality="fast" | 0.4 |
| geometry_quality="standard", pbr=false, texture=true, texture_quality="standard" | 0.4 |
| geometry_quality="standard", pbr=false, texture=true, texture_quality="detailed" | 0.5 |
| geometry_quality="standard", pbr=false, texture=true, texture_quality="extreme" | 0.6 |
| geometry_quality="standard", pbr=true, texture=false, texture_quality="fast" | 0.4 |
| geometry_quality="standard", pbr=true, texture=false, texture_quality="standard" | 0.4 |
| geometry_quality="standard", pbr=true, texture=false, texture_quality="detailed" | 0.5 |
| geometry_quality="standard", pbr=true, texture=false, texture_quality="extreme" | 0.6 |
| geometry_quality="standard", pbr=true, texture=true, texture_quality="fast" | 0.4 |
| geometry_quality="standard", pbr=true, texture=true, texture_quality="standard" | 0.4 |
| geometry_quality="standard", pbr=true, texture=true, texture_quality="detailed" | 0.5 |
| geometry_quality="standard", pbr=true, texture=true, texture_quality="extreme" | 0.6 |
| geometry_quality="detailed", pbr=false, texture=false, texture_quality="fast" | 0.45 |
| geometry_quality="detailed", pbr=false, texture=false, texture_quality="standard" | 0.45 |
| geometry_quality="detailed", pbr=false, texture=false, texture_quality="detailed" | 0.45 |
| geometry_quality="detailed", pbr=false, texture=false, texture_quality="extreme" | 0.45 |
| geometry_quality="detailed", pbr=false, texture=true, texture_quality="fast" | 0.55 |
| geometry_quality="detailed", pbr=false, texture=true, texture_quality="standard" | 0.55 |
| geometry_quality="detailed", pbr=false, texture=true, texture_quality="detailed" | 0.65 |
| geometry_quality="detailed", pbr=false, texture=true, texture_quality="extreme" | 0.75 |

Formula: `(((params.texture ?? true) || (params.pbr ?? true)) ? (0.40 + ((params.texture_quality ?? "standard") == "detailed" ? 0.10 : (params.texture_quality ?? "standard") == "extreme" ? 0.20 : 0.0)) : 0.30) + ((params.geometry_quality ?? "standard") == "detailed" ? 0.15 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-h3.5-preview/text-to-3d", "prompt": "An ornate knight helmet with engraved gold filigree, rows of rivets and a red horsehair plume"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-h3.5-preview/text-to-3d', {'prompt': 'An ornate knight helmet with engraved gold filigree, rows of rivets and a red horsehair plume'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-h3.5-preview/text-to-3d", {
  "prompt": "An ornate knight helmet with engraved gold filigree, rows of rivets and a red horsehair plume"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-h3.5-preview/text-to-3d", sandbase.Params{
	"prompt": "An ornate knight helmet with engraved gold filigree, rows of rivets and a red horsehair plume",
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
| `prompt` | string | yes | Text description of the 3D object to generate. Maximum 1024 characters.  |
| `delight` | boolean |  | Remove baked-in lighting from the reference image before texturing (texture v3.5). default `false` |
| `texture` | boolean |  | Generate textures. Set texture and pbr to false for bare geometry (cheaper). default `true` |
| `compress` | string |  | geometry applies meshopt compression to reduce file size. one of: `geometry` |
| `auto_size` | boolean |  | Scale the model to real-world size in meters. default `false` |
| `export_uv` | boolean |  | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. default `true` |
| `face_limit` | integer |  | Maximum face count, up to 5,000,000 (detailed geometry) or 2,000,000; 10,000-150,000 typical for quad. Adaptive when unset. range –5000000 |
| `image_seed` | integer |  | Seed for the internal text-to-image step.  |
| `texture_seed` | integer |  | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry.  |
| `generate_parts` | boolean |  | Editable segmented parts. Requires texture=false and pbr=false. default `false` |
| `smart_low_poly` | boolean |  | Hand-crafted style low-poly topology (500-20,000 faces). Best for simple objects. default `false` |
| `negative_prompt` | string |  | What to avoid, up to 255 characters.  |
| `texture_quality` | string |  | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |
| `texture_version` | string |  | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. one of: `v3.5-20260815`, `v3.0-20250812`, `v2.5-20250123` |
| `geometry_quality` | string |  | detailed (Ultra) adds mesh detail and is billed as an add-on. one of: `standard`, `detailed`; default `"standard"` |
| `export_orientation` | string |  | Forward axis of the exported model. Leave unset if you will post-process the model. one of: `+x`, `-x`, `+y`, `-y` |

## Details

Tripo H3.5 Preview (v3.5-20261108) is Tripo's newest H-series model. It keeps finer geometric detail from the reference than H3.1 and allows up to 5,000,000 faces with detailed geometry. It supports HD geometry, quad, smart low-poly and part generation. This is a preview release; Tripo may update the model.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text description of the 3D object to generate. Maximum 1024 characters. |
| `negative_prompt` | string | — | What to avoid, up to 255 characters. |
| `texture` | boolean | `true` | Generate textures. Set texture and pbr to false for bare geometry (cheaper). |
| `pbr` | boolean | `true` | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. |
| `geometry_quality` | `standard` / `detailed` | `standard` | detailed (Ultra) adds mesh detail and is billed as an add-on. |
| `quad` | boolean | `false` | Quad topology instead of triangles. Output becomes FBX; 10,000 faces when face_limit is unset. |
| `smart_low_poly` | boolean | `false` | Hand-crafted style low-poly topology (500-20,000 faces). Best for simple objects. |
| `generate_parts` | boolean | `false` | Editable segmented parts. Requires texture=false and pbr=false. |
| `face_limit` | integer | — | Maximum face count, up to 5,000,000 (detailed geometry) or 2,000,000; 10,000-150,000 typical for quad. Adaptive when unset. |
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
$0.40 textured (standard or fast texture), $0.30 untextured (texture and pbr false). Text, image and multiview input cost the same.
| Add-on | Price |
|---|---|
| texture_quality = detailed | +$0.10 |
| texture_quality = extreme | +$0.20 |
| geometry_quality = detailed | +$0.15 |
quad, smart_low_poly and generate_parts carry no extra charge on H3.5 Preview. Prices follow Tripo's preview pricing and may change when the model leaves preview.
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo-h3.5-preview/text-to-3d.json`](../../../../catalog/models/tripo3d/tripo-h3.5-preview/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-h3.5-preview/text-to-3d
