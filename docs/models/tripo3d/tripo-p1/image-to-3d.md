# Tripo P1 Image to 3D API: pricing, parameters and code examples

`tripo3d/tripo-p1/image-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.4 to $0.7 per run, depending on parameters · **Modes:** async

Tripo P1 is Tripo3D's image-to-3D model. It reconstructs a 3D mesh with optional textures from a single image.

## Pricing

- Depends on parameters (`params.pbr`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| pbr=false, texture=false, texture_quality="fast" | 0.4 |
| pbr=false, texture=false, texture_quality="standard" | 0.4 |
| pbr=false, texture=false, texture_quality="detailed" | 0.4 |
| pbr=false, texture=false, texture_quality="extreme" | 0.4 |
| pbr=false, texture=true, texture_quality="fast" | 0.5 |
| pbr=false, texture=true, texture_quality="standard" | 0.5 |
| pbr=false, texture=true, texture_quality="detailed" | 0.6 |
| pbr=false, texture=true, texture_quality="extreme" | 0.7 |
| pbr=true, texture=false, texture_quality="fast" | 0.5 |
| pbr=true, texture=false, texture_quality="standard" | 0.5 |
| pbr=true, texture=false, texture_quality="detailed" | 0.6 |
| pbr=true, texture=false, texture_quality="extreme" | 0.7 |
| pbr=true, texture=true, texture_quality="fast" | 0.5 |
| pbr=true, texture=true, texture_quality="standard" | 0.5 |
| pbr=true, texture=true, texture_quality="detailed" | 0.6 |
| pbr=true, texture=true, texture_quality="extreme" | 0.7 |

Formula: `(((params.texture ?? true) || (params.pbr ?? false)) ? (0.50 + ((params.texture_quality ?? "standard") == "detailed" ? 0.10 : (params.texture_quality ?? "standard") == "extreme" ? 0.20 : 0.0)) : 0.40)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-p1/image-to-3d", "image": "https://static.sandbase.ai/examples/38efe400-c0cd-4761-bb18-b0595f824967/input/c721985f-24e4-405a-9265-ce3a9f6118ff.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-p1/image-to-3d', {'image': 'https://static.sandbase.ai/examples/38efe400-c0cd-4761-bb18-b0595f824967/input/c721985f-24e4-405a-9265-ce3a9f6118ff.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-p1/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/38efe400-c0cd-4761-bb18-b0595f824967/input/c721985f-24e4-405a-9265-ce3a9f6118ff.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-p1/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/38efe400-c0cd-4761-bb18-b0595f824967/input/c721985f-24e4-405a-9265-ce3a9f6118ff.png",
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
| `image` | string | yes | Input image URL for 3D model creation.  |
| `delight` | boolean |  | Remove baked-in lighting from the reference image before texturing (texture v3.5). default `false` |
| `texture` | boolean |  | Generate textures. Set texture and pbr to false for bare geometry (cheaper). default `true` |
| `auto_size` | boolean |  | Scale the model to real-world size in meters. default `false` |
| `export_uv` | boolean |  | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. default `true` |
| `face_limit` | integer |  | Maximum face count (50-20,000). Adaptive when unset. range 50–20000 |
| `orientation` | string |  | align_image rotates the model to match the input image (needs texture). one of: `default`, `align_image`; default `"default"` |
| `texture_seed` | integer |  | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry.  |
| `texture_quality` | string |  | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |
| `texture_version` | string |  | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. one of: `v3.5-20260815`, `v3.0-20250812`, `v2.5-20250123` |
| `texture_alignment` | string |  | original_image keeps textures close to the input image; geometry favors the mesh. one of: `original_image`, `geometry`; default `"original_image"` |
| `export_orientation` | string |  | Forward axis of the exported model. Leave unset if you will post-process the model. one of: `+x`, `-x`, `+y`, `-y` |
| `enable_image_autofix` | boolean |  | Enhance the input image before generation. default `false` |

## Details

Tripo P1 (P1-20260311) produces clean low-poly meshes (50–20,000 faces).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Input image URL for 3D model creation. |
| `texture` | boolean | `true` | Generate textures. Set texture and pbr to false for bare geometry (cheaper). |
| `pbr` | boolean | `false` | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. |
| `face_limit` | integer 50–20000 | — | Maximum face count (50-20,000). Adaptive when unset. |
| `texture_alignment` | `original_image` / `geometry` | `original_image` | original_image keeps textures close to the input image; geometry favors the mesh. |
| `orientation` | `default` / `align_image` | `default` | align_image rotates the model to match the input image (needs texture). |
| `enable_image_autofix` | boolean | `false` | Enhance the input image before generation. |
| `seed` | integer | — | Seed for geometry generation (Tripo model_seed). Same seed and input give the same mesh. |
| `texture_seed` | integer | — | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry. |
| `texture_version` | `v3.5-20260815` / `v3.0-20250812` / `v2.5-20250123` | — | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. |
| `delight` | boolean | `false` | Remove baked-in lighting from the reference image before texturing (texture v3.5). |
| `export_uv` | boolean | `true` | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. |
| `export_orientation` | `+x` / `-x` / `+y` / `-y` | — | Forward axis of the exported model. Leave unset if you will post-process the model. |
| `auto_size` | boolean | `false` | Scale the model to real-world size in meters. |
### Output
- `url`: 3D model (GLB; FBX when quad is on).
- `thumbnail`: Preview render.
### Billing
$0.50 textured (standard or fast texture), $0.40 untextured (texture and pbr false).
| Add-on | Price |
|---|---|
| texture_quality = detailed | +$0.10 |
| texture_quality = extreme | +$0.20 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo-p1/image-to-3d.json`](../../../../catalog/models/tripo3d/tripo-p1/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-p1/image-to-3d
