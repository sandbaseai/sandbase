# Tripo Texture API: pricing, parameters and code examples

`tripo3d/tripo/texture` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.1 to $0.3 per run, depending on parameters · **Modes:** async

Tripo Texture paints new textures on an existing 3D model from a text prompt, one image or multiple views.

## Pricing

- Depends on parameters (`params.texture_quality`).

| parameters | USD |
|---|---|
| texture_quality="fast" | 0.1 |
| texture_quality="standard" | 0.1 |
| texture_quality="detailed" | 0.2 |
| texture_quality="extreme" | 0.3 |

Formula: `(params.texture_quality ?? "standard") == "extreme" ? 0.30 : (params.texture_quality ?? "standard") == "detailed" ? 0.20 : 0.10`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/texture", "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/texture', {'model_url': 'https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/texture", {
  "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/texture", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb",
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
| `bake` | boolean |  | Bake advanced materials into the textures. default `true` |
| `image` | string |  | Reference image for the texture (texture_prompt.image). Use prompt, image or images, not several.  |
| `images` | array |  | 2 to 4 reference views in the order front, left, back, right (texture_prompt.images).  |
| `prompt` | string |  | Text describing the texture (Tripo texture_prompt.text).  |
| `delight` | boolean |  | Remove baked-in lighting from the reference image before texturing (texture v3.5). default `false` |
| `compress` | string |  | geometry applies meshopt compression to reduce file size. one of: `geometry` |
| `model_url` | string | yes | URL of the input 3D model (GLB, GLTF, FBX, OBJ or STL, up to 150 MB).  |
| `part_names` | array |  | Only process these parts (node names from a segmentation, e.g. tripo_part_0). All parts when unset.  |
| `style_image` | string |  | Style reference used together with prompt (texture_prompt.style_image).  |
| `texture_seed` | integer |  | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry.  |
| `model_version` | string |  | v3.5-20260815 is current; v3.0-20250812 runs as v3.5; v2.5-20250123 for models made with Tripo v2.5. one of: `v3.5-20260815`, `v3.0-20250812`, `v2.5-20250123`; default `"v3.5-20260815"` |
| `texture_quality` | string |  | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. one of: `fast`, `standard`, `detailed`, `extreme`; default `"standard"` |
| `texture_alignment` | string |  | original_image keeps textures close to the input image; geometry favors the mesh. one of: `original_image`, `geometry`; default `"original_image"` |

## Details

Tripo Texture paints new textures on an existing 3D model from a text prompt, one image or multiple views.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input 3D model (GLB, GLTF, FBX, OBJ or STL, up to 150 MB). |
| `prompt` | string | — | Text describing the texture (Tripo texture_prompt.text). |
| `image` | string | — | Reference image for the texture (texture_prompt.image). Use prompt, image or images, not several. |
| `images` | array | — | 2 to 4 reference views in the order front, left, back, right (texture_prompt.images). |
| `style_image` | string | — | Style reference used together with prompt (texture_prompt.style_image). |
| `model_version` | `v3.5-20260815` / `v3.0-20250812` / `v2.5-20250123` | `v3.5-20260815` | v3.5-20260815 is current; v3.0-20250812 runs as v3.5; v2.5-20250123 for models made with Tripo v2.5. |
| `texture_quality` | `fast` / `standard` / `detailed` / `extreme` | `standard` | fast and standard cost the same; detailed (HD) and extreme (8K) are add-ons. |
| `pbr` | boolean | `true` | PBR material maps (base color, metallic, roughness, normal). true also turns texture on. |
| `texture_alignment` | `original_image` / `geometry` | `original_image` | original_image keeps textures close to the input image; geometry favors the mesh. |
| `delight` | boolean | `false` | Remove baked-in lighting from the reference image before texturing (texture v3.5). |
| `bake` | boolean | `true` | Bake advanced materials into the textures. |
| `part_names` | array | — | Only process these parts (node names from a segmentation, e.g. tripo_part_0). All parts when unset. |
| `texture_seed` | integer | — | Seed for texture generation. Keep seed and change texture_seed for new textures on the same geometry. |
| `compress` | `geometry` | — | geometry applies meshopt compression to reduce file size. |
### Output
- `url`: Textured GLB.
- `thumbnail`: Preview render.
### Billing
| texture_quality | Price |
|---|---|
| fast / standard | $0.10 |
| detailed | $0.20 |
| extreme (8K) | $0.30 |
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/texture.json`](../../../../catalog/models/tripo3d/tripo/texture.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/texture
