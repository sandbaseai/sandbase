# Tripo P2 Multiview to 3D API: pricing, parameters and code examples

`tripo3d/tripo-p2/multiview-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $1 to $1.3 per run, depending on parameters · **Modes:** async

Tripo P2 Multiview to 3D by Tripo3D: build a textured 3D model from 2 to 4 views of the same object.

## Pricing

- Depends on parameters (`params.pbr`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| pbr=false, texture=false, texture_quality="fast" | 1 |
| pbr=false, texture=false, texture_quality="standard" | 1 |
| pbr=false, texture=false, texture_quality="detailed" | 1 |
| pbr=false, texture=false, texture_quality="extreme" | 1 |
| pbr=false, texture=true, texture_quality="fast" | 1.1 |
| pbr=false, texture=true, texture_quality="standard" | 1.1 |
| pbr=false, texture=true, texture_quality="detailed" | 1.2 |
| pbr=false, texture=true, texture_quality="extreme" | 1.3 |
| pbr=true, texture=false, texture_quality="fast" | 1.1 |
| pbr=true, texture=false, texture_quality="standard" | 1.1 |
| pbr=true, texture=false, texture_quality="detailed" | 1.2 |
| pbr=true, texture=false, texture_quality="extreme" | 1.3 |
| pbr=true, texture=true, texture_quality="fast" | 1.1 |
| pbr=true, texture=true, texture_quality="standard" | 1.1 |
| pbr=true, texture=true, texture_quality="detailed" | 1.2 |
| pbr=true, texture=true, texture_quality="extreme" | 1.3 |

Formula: `(((params.texture ?? true) || (params.pbr ?? true)) ? (1.10 + ((params.texture_quality ?? "standard") == "detailed" ? 0.10 : (params.texture_quality ?? "standard") == "extreme" ? 0.20 : 0.0)) : 1.00)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-p2/multiview-to-3d", "images": ["https://static.sandbase.ai/examples/tripo3d/tripo/shared/front.jpg", "https://static.sandbase.ai/examples/tripo3d/tripo/shared/left.jpg", "https://static.sandbase.ai/examples/tripo3d/tripo/shared/back.jpg", "https://static.sandbase.ai/examples/tripo3d/tripo/shared/right.jpg"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-p2/multiview-to-3d', {'images': ['https://static.sandbase.ai/examples/tripo3d/tripo/shared/front.jpg', 'https://static.sandbase.ai/examples/tripo3d/tripo/shared/left.jpg', 'https://static.sandbase.ai/examples/tripo3d/tripo/shared/back.jpg', 'https://static.sandbase.ai/examples/tripo3d/tripo/shared/right.jpg']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-p2/multiview-to-3d", {
  "images": [
    "https://static.sandbase.ai/examples/tripo3d/tripo/shared/front.jpg",
    "https://static.sandbase.ai/examples/tripo3d/tripo/shared/left.jpg",
    "https://static.sandbase.ai/examples/tripo3d/tripo/shared/back.jpg",
    "https://static.sandbase.ai/examples/tripo3d/tripo/shared/right.jpg"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-p2/multiview-to-3d", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/tripo3d/tripo/shared/front.jpg", "https://static.sandbase.ai/examples/tripo3d/tripo/shared/left.jpg", "https://static.sandbase.ai/examples/tripo3d/tripo/shared/back.jpg", "https://static.sandbase.ai/examples/tripo3d/tripo/shared/right.jpg"},
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
| `images` | array | yes | 2 to 4 images of the same object, in the order front, left, back, right. Front is required.  |
| `delight` | boolean |  | Remove baked-in lighting from the reference image before texturing (texture v3.5). default `false` |
| `texture` | boolean |  | Generate textures. Set texture and pbr to false for bare geometry (cheaper). default `true` |
| `auto_size` | boolean |  | Scale the model to real-world size in meters. default `false` |
| `export_uv` | boolean |  | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. default `true` |
| `face_limit` | integer |  | Maximum face count (48-50,000). Adaptive when unset. range 48–50000 |
| `orientation` | string |  | align_image rotates the model to match the input image (needs texture). one of: `default`, `align_image`; default `"default"` |
| `texture_seed` | integer |  | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry.  |
| `texture_quality` | string |  | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |
| `texture_version` | string |  | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. one of: `v3.5-20260815`, `v3.0-20250812`, `v2.5-20250123` |
| `texture_alignment` | string |  | original_image keeps textures close to the input image; geometry favors the mesh. one of: `original_image`, `geometry`; default `"original_image"` |
| `export_orientation` | string |  | Forward axis of the exported model. Leave unset if you will post-process the model. one of: `+x`, `-x`, `+y`, `-y` |

## Details

Tripo P2 (P2-20260801) produces production-ready low-poly meshes with native quad topology (48–50,000 faces).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | array, required | — | 2 to 4 images of the same object, in the order front, left, back, right. Front is required. |
| `texture` | boolean | `true` | Generate textures. Set texture and pbr to false for bare geometry (cheaper). |
| `pbr` | boolean | `true` | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. |
| `quad` | boolean | `false` | Quad topology instead of triangles. Output becomes FBX; 10,000 faces when face_limit is unset. |
| `face_limit` | integer 48–50000 | — | Maximum face count (48-50,000). Adaptive when unset. |
| `texture_alignment` | `original_image` / `geometry` | `original_image` | original_image keeps textures close to the input image; geometry favors the mesh. |
| `orientation` | `default` / `align_image` | `default` | align_image rotates the model to match the input image (needs texture). |
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
$1.10 textured (standard or fast texture), $1.00 untextured (texture and pbr false).
| Add-on | Price |
|---|---|
| texture_quality = detailed | +$0.10 |
| texture_quality = extreme | +$0.20 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo-p2/multiview-to-3d.json`](../../../../catalog/models/tripo3d/tripo-p2/multiview-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-p2/multiview-to-3d
