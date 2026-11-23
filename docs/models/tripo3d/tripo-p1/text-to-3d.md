# Tripo P1 Text to 3D API: pricing, parameters and code examples

`tripo3d/tripo-p1/text-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.3 to $0.6 per run, depending on parameters · **Modes:** async

Tripo P1 is Tripo3D's text-to-3D model. It generates a 3D mesh with optional textures from a text description.

## Pricing

- Depends on parameters (`params.pbr`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| pbr=false, texture=false, texture_quality="fast" | 0.3 |
| pbr=false, texture=false, texture_quality="standard" | 0.3 |
| pbr=false, texture=false, texture_quality="detailed" | 0.3 |
| pbr=false, texture=false, texture_quality="extreme" | 0.3 |
| pbr=false, texture=true, texture_quality="fast" | 0.4 |
| pbr=false, texture=true, texture_quality="standard" | 0.4 |
| pbr=false, texture=true, texture_quality="detailed" | 0.5 |
| pbr=false, texture=true, texture_quality="extreme" | 0.6 |
| pbr=true, texture=false, texture_quality="fast" | 0.4 |
| pbr=true, texture=false, texture_quality="standard" | 0.4 |
| pbr=true, texture=false, texture_quality="detailed" | 0.5 |
| pbr=true, texture=false, texture_quality="extreme" | 0.6 |
| pbr=true, texture=true, texture_quality="fast" | 0.4 |
| pbr=true, texture=true, texture_quality="standard" | 0.4 |
| pbr=true, texture=true, texture_quality="detailed" | 0.5 |
| pbr=true, texture=true, texture_quality="extreme" | 0.6 |

Formula: `(((params.texture ?? true) || (params.pbr ?? false)) ? (0.40 + ((params.texture_quality ?? "standard") == "detailed" ? 0.10 : (params.texture_quality ?? "standard") == "extreme" ? 0.20 : 0.0)) : 0.30)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-p1/text-to-3d", "prompt": "A potted bonsai tree with twisted trunk and lush green foliage in a glazed blue pot"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-p1/text-to-3d', {'prompt': 'A potted bonsai tree with twisted trunk and lush green foliage in a glazed blue pot'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-p1/text-to-3d", {
  "prompt": "A potted bonsai tree with twisted trunk and lush green foliage in a glazed blue pot"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-p1/text-to-3d", sandbase.Params{
	"prompt": "A potted bonsai tree with twisted trunk and lush green foliage in a glazed blue pot",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pbr` | boolean |  | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. default `false` |
| `seed` | integer |  | Seed for geometry generation (Tripo model_seed). Same seed and input give the same mesh.  |
| `prompt` | string | yes | Text description of the 3D object to generate. Maximum 1024 characters.  |
| `delight` | boolean |  | Remove baked-in lighting from the reference image before texturing (texture v3.5). default `false` |
| `texture` | boolean |  | Generate textures. Set texture and pbr to false for bare geometry (cheaper). default `true` |
| `auto_size` | boolean |  | Scale the model to real-world size in meters. default `false` |
| `export_uv` | boolean |  | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. default `true` |
| `face_limit` | integer |  | Maximum face count (50-20,000). Adaptive when unset. range 50–20000 |
| `image_seed` | integer |  | Seed for the internal text-to-image step.  |
| `texture_seed` | integer |  | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry.  |
| `negative_prompt` | string |  | What to avoid, up to 255 characters.  |
| `texture_quality` | string |  | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |
| `texture_version` | string |  | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. one of: `v3.5-20260815`, `v3.0-20250812`, `v2.5-20250123` |
| `export_orientation` | string |  | Forward axis of the exported model. Leave unset if you will post-process the model. one of: `+x`, `-x`, `+y`, `-y` |

## Details

Tripo P1 (P1-20260311) produces clean low-poly meshes (50–20,000 faces).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text description of the 3D object to generate. Maximum 1024 characters. |
| `negative_prompt` | string | — | What to avoid, up to 255 characters. |
| `texture` | boolean | `true` | Generate textures. Set texture and pbr to false for bare geometry (cheaper). |
| `pbr` | boolean | `false` | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. |
| `face_limit` | integer 50–20000 | — | Maximum face count (50-20,000). Adaptive when unset. |
| `seed` | integer | — | Seed for geometry generation (Tripo model_seed). Same seed and input give the same mesh. |
| `texture_seed` | integer | — | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry. |
| `image_seed` | integer | — | Seed for the internal text-to-image step. |
| `texture_version` | `v3.5-20260815` / `v3.0-20250812` / `v2.5-20250123` | — | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. |
| `delight` | boolean | `false` | Remove baked-in lighting from the reference image before texturing (texture v3.5). |
| `export_uv` | boolean | `true` | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. |
| `export_orientation` | `+x` / `-x` / `+y` / `-y` | — | Forward axis of the exported model. Leave unset if you will post-process the model. |
| `auto_size` | boolean | `false` | Scale the model to real-world size in meters. |
### Output
- `url`: 3D model (GLB; FBX when quad is on).
- `thumbnail`: Preview render.
- `generated_image`: Reference image Tripo generated from the prompt.
### Billing
$0.40 textured (standard or fast texture), $0.30 untextured (texture and pbr false).
| Add-on | Price |
|---|---|
| texture_quality = detailed | +$0.10 |
| texture_quality = extreme | +$0.20 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo-p1/text-to-3d.json`](../../../../catalog/models/tripo3d/tripo-p1/text-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-p1/text-to-3d
