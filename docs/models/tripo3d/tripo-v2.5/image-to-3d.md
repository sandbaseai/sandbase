# Tripo v2.5 Image to 3D API: pricing, parameters and code examples

`tripo3d/tripo-v2.5/image-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $0.45 per run, depending on parameters · **Modes:** async

Tripo v2.5 by Tripo3D generates a textured 3D mesh from a single image, with optional HD textures, PBR materials and quad topology.

## Pricing

- Depends on parameters (`params.pbr`, `params.quad`, `params.texture`).

| parameters | USD |
|---|---|
| pbr=false, quad=false, texture="no" | 0.2 |
| pbr=false, quad=false, texture="standard" | 0.3 |
| pbr=false, quad=false, texture="HD" | 0.4 |
| pbr=false, quad=true, texture="no" | 0.25 |
| pbr=false, quad=true, texture="standard" | 0.35 |
| pbr=false, quad=true, texture="HD" | 0.45 |
| pbr=true, quad=false, texture="no" | 0.3 |
| pbr=true, quad=false, texture="standard" | 0.3 |
| pbr=true, quad=false, texture="HD" | 0.4 |
| pbr=true, quad=true, texture="no" | 0.35 |
| pbr=true, quad=true, texture="standard" | 0.35 |
| pbr=true, quad=true, texture="HD" | 0.45 |

Formula: `((params.texture ?? "standard") == "HD" ? 0.40 : ((params.texture ?? "standard") == "no" && !(params.pbr ?? false)) ? 0.20 : 0.30) + ((params.quad ?? false) ? 0.05 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-v2.5/image-to-3d", "image": "https://static.sandbase.ai/examples/20dc0941-0d15-4467-9387-f1c3018cabba/input/73d6d211-722b-4b2c-9616-4f48332d7c75.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-v2.5/image-to-3d', {'image': 'https://static.sandbase.ai/examples/20dc0941-0d15-4467-9387-f1c3018cabba/input/73d6d211-722b-4b2c-9616-4f48332d7c75.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-v2.5/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/20dc0941-0d15-4467-9387-f1c3018cabba/input/73d6d211-722b-4b2c-9616-4f48332d7c75.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-v2.5/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/20dc0941-0d15-4467-9387-f1c3018cabba/input/73d6d211-722b-4b2c-9616-4f48332d7c75.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pbr` | boolean |  | Generate PBR materials. default `false` |
| `quad` | boolean |  | Generate quad mesh topology (billed as an add-on). default `false` |
| `seed` | integer |  | Seed for reproducible geometry generation.  |
| `image` | string | yes | Input image URL for 3D model creation.  |
| `delight` | boolean |  | Accepted for compatibility with Tripo; only the v3.5 texture model reads it, so it has no effect on v2.5. default `false` |
| `texture` | string |  | Texture quality: no (untextured), standard, or HD. one of: `no`, `standard`, `HD`; default `"standard"` |
| `export_uv` | boolean |  | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. default `true` |
| `face_limit` | integer |  | Maximum face count (1,000-500,000). Adaptive when unset. range 1000–500000 |
| `orientation` | string |  | Set to align_image to rotate the model to match the input image. one of: `default`, `align_image`; default `"default"` |
| `texture_seed` | integer |  | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry.  |
| `texture_version` | string |  | Accepted for compatibility with Tripo: v2.5 geometry is always textured with v2.5-20250123, whatever this field says. one of: `v3.5-20260815`, `v3.0-20250812`, `v2.5-20250123` |
| `texture_alignment` | string |  | original_image keeps textures close to the input image; geometry favors the mesh. one of: `original_image`, `geometry`; default `"original_image"` |
| `export_orientation` | string |  | Forward axis of the exported model. Leave unset if you will post-process the model. one of: `+x`, `-x`, `+y`, `-y` |
| `enable_image_autofix` | boolean |  | Enhance the input image before generation. default `false` |

## Details

Tripo v2.5 by Tripo3D generates a textured 3D mesh from a single image, with optional HD textures, PBR materials and quad topology.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | string, required | — | Input image URL for 3D model creation. |
| `texture` | `no` / `standard` / `HD` | `standard` | Texture quality: no (untextured), standard, or HD. |
| `pbr` | boolean | `false` | Generate PBR materials. |
| `quad` | boolean | `false` | Generate quad mesh topology (billed as an add-on). |
| `face_limit` | integer 1000–500000 | — | Maximum face count (1,000-500,000). Adaptive when unset. |
| `orientation` | `default` / `align_image` | `default` | Set to align_image to rotate the model to match the input image. |
| `seed` | integer | — | Seed for reproducible geometry generation. |
| `texture_seed` | integer | — | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry. |
| `texture_version` | `v3.5-20260815` / `v3.0-20250812` / `v2.5-20250123` | — | Accepted for compatibility with Tripo: v2.5 geometry is always textured with v2.5-20250123, whatever this field says. |
| `delight` | boolean | `false` | Accepted for compatibility with Tripo; only the v3.5 texture model reads it, so it has no effect on v2.5. |
| `export_orientation` | `+x` / `-x` / `+y` / `-y` | — | Forward axis of the exported model. Leave unset if you will post-process the model. |
| `export_uv` | boolean | `true` | UV-unwrap during generation. false is faster and smaller; UVs are then made during texturing. |
| `texture_alignment` | `original_image` / `geometry` | `original_image` | original_image keeps textures close to the input image; geometry favors the mesh. |
| `enable_image_autofix` | boolean | `false` | Enhance the input image before generation. |
### Output
- `url`: 3D model (GLB; FBX when quad is on).
- `thumbnail`: Preview render.
### Billing
$0.30 textured, $0.20 untextured (texture = no and pbr off).
| Add-on | Price |
|---|---|
| texture = HD | +$0.10 |
| quad | +$0.05 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo-v2.5/image-to-3d.json`](../../../../catalog/models/tripo3d/tripo-v2.5/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-v2.5/image-to-3d
