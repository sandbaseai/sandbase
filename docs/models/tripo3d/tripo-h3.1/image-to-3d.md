# Tripo H3.1 Image to 3D API: pricing, parameters and code examples

`tripo3d/tripo-h3.1/image-to-3d` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.24 to $0.78 per run, depending on parameters · **Modes:** async

Tripo H3.1 by Tripo3D - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for games, AR/VR, e-commerce, and digital content creation.

## Pricing

- Depends on parameters (`params.geometry_quality`, `params.pbr`, `params.quad`, `params.texture`, `params.texture_quality`).

| parameters | USD |
|---|---|
| geometry_quality="standard", pbr=false, quad=false, texture=false, texture_quality="standard" | 0.24 |
| geometry_quality="standard", pbr=false, quad=false, texture=false, texture_quality="detailed" | 0.24 |
| geometry_quality="standard", pbr=false, quad=false, texture=true, texture_quality="standard" | 0.36 |
| geometry_quality="standard", pbr=false, quad=false, texture=true, texture_quality="detailed" | 0.48 |
| geometry_quality="standard", pbr=false, quad=true, texture=false, texture_quality="standard" | 0.3 |
| geometry_quality="standard", pbr=false, quad=true, texture=false, texture_quality="detailed" | 0.3 |
| geometry_quality="standard", pbr=false, quad=true, texture=true, texture_quality="standard" | 0.42 |
| geometry_quality="standard", pbr=false, quad=true, texture=true, texture_quality="detailed" | 0.54 |
| geometry_quality="standard", pbr=true, quad=false, texture=false, texture_quality="standard" | 0.36 |
| geometry_quality="standard", pbr=true, quad=false, texture=false, texture_quality="detailed" | 0.48 |
| geometry_quality="standard", pbr=true, quad=false, texture=true, texture_quality="standard" | 0.36 |
| geometry_quality="standard", pbr=true, quad=false, texture=true, texture_quality="detailed" | 0.48 |
| geometry_quality="standard", pbr=true, quad=true, texture=false, texture_quality="standard" | 0.42 |
| geometry_quality="standard", pbr=true, quad=true, texture=false, texture_quality="detailed" | 0.54 |
| geometry_quality="standard", pbr=true, quad=true, texture=true, texture_quality="standard" | 0.42 |
| geometry_quality="standard", pbr=true, quad=true, texture=true, texture_quality="detailed" | 0.54 |
| geometry_quality="detailed", pbr=false, quad=false, texture=false, texture_quality="standard" | 0.48 |
| geometry_quality="detailed", pbr=false, quad=false, texture=false, texture_quality="detailed" | 0.48 |
| geometry_quality="detailed", pbr=false, quad=false, texture=true, texture_quality="standard" | 0.6 |
| geometry_quality="detailed", pbr=false, quad=false, texture=true, texture_quality="detailed" | 0.72 |
| geometry_quality="detailed", pbr=false, quad=true, texture=false, texture_quality="standard" | 0.54 |
| geometry_quality="detailed", pbr=false, quad=true, texture=false, texture_quality="detailed" | 0.54 |
| geometry_quality="detailed", pbr=false, quad=true, texture=true, texture_quality="standard" | 0.66 |
| geometry_quality="detailed", pbr=false, quad=true, texture=true, texture_quality="detailed" | 0.78 |

Formula: `(((params.texture ?? true) || (params.pbr ?? true)) ? ((params.texture_quality ?? "standard") == "detailed" ? 0.48 : 0.36) : 0.24) + ((params.geometry_quality ?? "standard") == "detailed" ? 0.24 : 0.0) + ((params.quad ?? false) ? 0.06 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo-h3.1/image-to-3d", "image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo-h3.1/image-to-3d', {'image': 'https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo-h3.1/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo-h3.1/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/tripo3d/tripo-h3.1/image-to-3d/input_image_0.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pbr` | boolean |  | Generate PBR materials (also enables texture). default `true` |
| `quad` | boolean |  | Generate quad mesh topology instead of triangles. default `false` |
| `seed` | integer |  | Seed for reproducible geometry generation.  |
| `image` | string | yes | URL of the input image for 3D model creation.  |
| `texture` | boolean |  | Generate textures. Set both texture and pbr to false for an untextured model. default `true` |
| `face_limit` | integer |  | Target face count. Adaptive when unset. range 1000–2000000 |
| `texture_quality` | string |  | standard or detailed (HD) textures. one of: `standard`, `detailed`; default `"standard"` |
| `geometry_quality` | string |  | detailed geometry is billed as an add-on. one of: `standard`, `detailed`; default `"standard"` |

## Details

Tripo H3.1 turns a single image into a textured 3D model quickly and at low cost.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | URL of the input image for 3D model creation. |
| `pbr` | boolean | true | PBR materials. |
| `quad` | boolean | false | Quad mesh output. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `texture` | boolean | true | Generate textures. |
| `face_limit` | integer 1000–2000000 | — | Maximum face count. |
| `texture_quality` | `standard` / `detailed` | `standard` | Texture detail; higher costs more. |
| `geometry_quality` | `standard` / `detailed` | `standard` | `detailed` adds mesh detail and cost. |

### Billing

$0.36 per textured model at standard quality, $0.48 detailed, $0.24 untextured; detailed geometry adds $0.24 and quad output $0.06.

| Request | Price |
|---|---|
| Standard texture | $0.36 |
| Detailed texture | $0.48 |
| Untextured | $0.24 |
| Standard + detailed geometry | $0.60 |

Failed runs are not charged.

### Also on SandBase

Other Tripo endpoints: `tripo3d/tripo-p2/text-to-3d`, `tripo3d/tripo-p2/image-to-3d`, `tripo3d/tripo-h3.1/text-to-3d`.

---
Machine-readable: [`catalog/models/tripo3d/tripo-h3.1/image-to-3d.json`](../../../../catalog/models/tripo3d/tripo-h3.1/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo-h3.1/image-to-3d
