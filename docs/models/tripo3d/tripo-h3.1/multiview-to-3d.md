# Tripo H3.1 Multiview to 3D API: pricing, parameters and code examples

`tripo3d/tripo-h3.1/multiview-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.3 to $0.5 per run, depending on parameters · **Modes:** async

Tripo H3.1 Multiview To 3d by Tripo3D - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for games, AR/VR, e-commerce, and digital content creation.

## Pricing

- Depends on parameters (`params.generate_parts`, `params.geometry_quality`, `params.pbr`, `params.quad`, `params.smart_low_poly`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| defaults | 0.3 |
| generate_parts=false | 0.3 |
| generate_parts=true | 0.5 |
| geometry_quality="standard" | 0.3 |
| geometry_quality="detailed" | 0.5 |
| pbr=false | 0.3 |
| pbr=true | 0.3 |
| quad=false | 0.3 |
| quad=true | 0.35 |
| smart_low_poly=false | 0.3 |
| smart_low_poly=true | 0.4 |
| texture=false | 0.3 |
| texture=true | 0.3 |
| texture_quality="fast" | 0.3 |
| texture_quality="standard" | 0.3 |
| texture_quality="detailed" | 0.4 |
| texture_quality="extreme" | 0.5 |

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-h3.1/multiview-to-3d", "images": ["https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/6fd3f606-1213-4602-81cb-f946c0825293.png", "https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/37c3b222-10ce-4689-80d1-4a7d369fa503.png", "https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/9a7324a5-25e8-4c9b-983a-a629bcdabf86.png"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-h3.1/multiview-to-3d', {'images': ['https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/6fd3f606-1213-4602-81cb-f946c0825293.png', 'https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/37c3b222-10ce-4689-80d1-4a7d369fa503.png', 'https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/9a7324a5-25e8-4c9b-983a-a629bcdabf86.png']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-h3.1/multiview-to-3d", {
  "images": [
    "https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/6fd3f606-1213-4602-81cb-f946c0825293.png",
    "https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/37c3b222-10ce-4689-80d1-4a7d369fa503.png",
    "https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/9a7324a5-25e8-4c9b-983a-a629bcdabf86.png"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-h3.1/multiview-to-3d", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/6fd3f606-1213-4602-81cb-f946c0825293.png", "https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/37c3b222-10ce-4689-80d1-4a7d369fa503.png", "https://static.sandbase.ai/examples/ea2bcfa8-a03d-4dda-a811-9c0fc84dd6ae/input/9a7324a5-25e8-4c9b-983a-a629bcdabf86.png"},
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
| `images` | array | yes | 2 to 4 images of the same object. Order: front, left, back, right.  |
| `delight` | boolean |  | Remove baked-in lighting from the reference image before texturing (texture v3.5). default `false` |
| `texture` | boolean |  | Generate textures. Set texture and pbr to false for bare geometry (cheaper). default `true` |
| `compress` | string |  | geometry applies meshopt compression to reduce file size. one of: `geometry` |
| `auto_size` | boolean |  | Scale the model to real-world size in meters. default `false` |
| `export_uv` | boolean |  | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. default `true` |
| `face_limit` | integer |  | Maximum face count, up to 2,000,000 (detailed geometry) or 1,500,000; 10,000-150,000 typical for quad. Adaptive when unset. range –2000000 |
| `orientation` | string |  | align_image rotates the model to match the input image (needs texture). one of: `default`, `align_image`; default `"default"` |
| `texture_seed` | integer |  | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry.  |
| `generate_parts` | boolean |  | Editable segmented parts. Requires texture=false and pbr=false; billed as an add-on. default `false` |
| `smart_low_poly` | boolean |  | Hand-crafted style low-poly topology (500-20,000 faces). Best for simple objects; billed as an add-on. default `false` |
| `texture_quality` | string |  | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |
| `texture_version` | string |  | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. one of: `v3.5-20260815`, `v3.0-20250812`, `v2.5-20250123` |
| `geometry_quality` | string |  | detailed (Ultra) adds mesh detail and is billed as an add-on. one of: `standard`, `detailed`; default `"standard"` |
| `texture_alignment` | string |  | original_image keeps textures close to the input image; geometry favors the mesh. one of: `original_image`, `geometry`; default `"original_image"` |
| `export_orientation` | string |  | Forward axis of the exported model. Leave unset if you will post-process the model. one of: `+x`, `-x`, `+y`, `-y` |

## Details

Tripo H3.1 (v3.1-20260211) is Tripo's recommended high-detail model, with HD geometry, quad, smart low-poly and part generation.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | array, required | — | 2 to 4 images of the same object. Order: front, left, back, right. |
| `texture` | boolean | `true` | Generate textures. Set texture and pbr to false for bare geometry (cheaper). |
| `pbr` | boolean | `true` | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. |
| `geometry_quality` | `standard` / `detailed` | `standard` | detailed (Ultra) adds mesh detail and is billed as an add-on. |
| `quad` | boolean | `false` | Quad topology instead of triangles. Output becomes FBX; 10,000 faces when face_limit is unset. |
| `smart_low_poly` | boolean | `false` | Hand-crafted style low-poly topology (500-20,000 faces). Best for simple objects; billed as an add-on. |
| `generate_parts` | boolean | `false` | Editable segmented parts. Requires texture=false and pbr=false; billed as an add-on. |
| `face_limit` | integer | — | Maximum face count, up to 2,000,000 (detailed geometry) or 1,500,000; 10,000-150,000 typical for quad. Adaptive when unset. |
| `texture_alignment` | `original_image` / `geometry` | `original_image` | original_image keeps textures close to the input image; geometry favors the mesh. |
| `orientation` | `default` / `align_image` | `default` | align_image rotates the model to match the input image (needs texture). |
| `seed` | integer | — | Seed for geometry generation (Tripo model_seed). Same seed and input give the same mesh. |
| `texture_seed` | integer | — | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry. |
| `texture_version` | `v3.5-20260815` / `v3.0-20250812` / `v2.5-20250123` | — | Texture model. v3.5-20260815 is current (v3.0-20250812 runs as v3.5); v2.5-20250123 is the legacy texture model and the default for v2.5 geometry. |
| `delight` | boolean | `false` | Remove baked-in lighting from the reference image before texturing (texture v3.5). |
| `export_uv` | boolean | `true` | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. |
| `export_orientation` | `+x` / `-x` / `+y` / `-y` | — | Forward axis of the exported model. Leave unset if you will post-process the model. |
| `compress` | `geometry` | — | geometry applies meshopt compression to reduce file size. |
| `auto_size` | boolean | `false` | Scale the model to real-world size in meters. |
### Output
- `url`: 3D model (GLB; FBX when quad is on).
- `thumbnail`: Preview render.
### Billing
$0.30 textured (standard or fast texture), $0.20 untextured (texture and pbr false).
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
Machine-readable: [`catalog/models/tripo3d/tripo-h3.1/multiview-to-3d.json`](../../../../catalog/models/tripo3d/tripo-h3.1/multiview-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-h3.1/multiview-to-3d
