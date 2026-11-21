# Tripo Convert API: pricing, parameters and code examples

`tripo3d/tripo/convert` · image generation model · Tripo3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.1 per run, depending on parameters · **Modes:** async

Tripo Convert exports a 3D model to GLTF, FBX, USDZ, OBJ, STL or 3MF, with optional quad remesh, scaling and texture settings.

## Pricing

- Depends on parameters (`params.face_limit`, `params.flatten_bottom`, `params.flatten_bottom_threshold`, `params.pivot_to_center_bottom`, `params.quad`, `params.scale_factor`, `params.texture_format`, `params.texture_size`).

| parameters | USD |
|---|---|
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=false, scale_factor=1, texture_format="JPEG", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=false, scale_factor=1, texture_format="PNG", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=false, scale_factor=1, texture_format="WEBP", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=false, scale_factor=1, texture_format="BMP", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=false, scale_factor=1, texture_format="DPX", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=false, scale_factor=1, texture_format="HDR", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=true, scale_factor=1, texture_format="JPEG", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=true, scale_factor=1, texture_format="PNG", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=true, scale_factor=1, texture_format="WEBP", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=true, scale_factor=1, texture_format="BMP", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=true, scale_factor=1, texture_format="DPX", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=false, quad=true, scale_factor=1, texture_format="HDR", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=false, scale_factor=1, texture_format="JPEG", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=false, scale_factor=1, texture_format="PNG", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=false, scale_factor=1, texture_format="WEBP", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=false, scale_factor=1, texture_format="BMP", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=false, scale_factor=1, texture_format="DPX", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=false, scale_factor=1, texture_format="HDR", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=true, scale_factor=1, texture_format="JPEG", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=true, scale_factor=1, texture_format="PNG", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=true, scale_factor=1, texture_format="WEBP", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=true, scale_factor=1, texture_format="BMP", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=true, scale_factor=1, texture_format="DPX", texture_size=4096 | 0.1 |
| face_limit=1, flatten_bottom=false, flatten_bottom_threshold=0.01, pivot_to_center_bottom=true, quad=true, scale_factor=1, texture_format="HDR", texture_size=4096 | 0.1 |

Formula: `((params.quad ?? false) || (params.face_limit ?? 0) > 0 || (params.flatten_bottom ?? false) || (params.flatten_bottom_threshold ?? 0.01) != 0.01 || (params.texture_size ?? 4096) != 4096 || (params.texture_format ?? "JPEG") != "JPEG" || (params.pivot_to_center_bottom ?? false) || (params.scale_factor ?? 1) != 1) ? 0.10 : 0.05`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tripo3d/tripo/convert", "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb", "format": "FBX"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tripo3d/tripo/convert', {'model_url': 'https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb', 'format': 'FBX'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tripo3d/tripo/convert", {
  "model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb",
  "format": "FBX"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tripo3d/tripo/convert", sandbase.Params{
	"model_url": "https://static.sandbase.ai/examples/tripo3d/tripo/shared/object.glb",
	"format": "FBX",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bake` | boolean |  | Bake advanced materials into the textures. default `true` |
| `quad` | boolean |  | Quad remesh (10,000 faces when face_limit is unset). Forces FBX. default `false` |
| `format` | string | yes | Output format. one of: `GLTF`, `FBX`, `USDZ`, `OBJ`, `STL`, `3MF`; default `"FBX"` |
| `pack_uv` | boolean |  | Pack all UV islands into one texture. default `false` |
| `model_url` | string | yes | URL of the input 3D model (GLB, GLTF, FBX, OBJ or STL, up to 150 MB).  |
| `face_limit` | integer |  | Target face count. Original when unset. range 1– |
| `fbx_preset` | string |  | FBX target application. one of: `blender`, `3dsmax`, `mixamo`, `bake_scale`; default `"blender"` |
| `part_names` | array |  | Only process these parts (node names from a segmentation, e.g. tripo_part_0). All parts when unset.  |
| `scale_factor` | number |  | Uniform scale. default `1` |
| `texture_size` | integer |  | Texture size in pixels. default `4096` |
| `flatten_bottom` | boolean |  | Flatten the bottom of the model. default `false` |
| `force_symmetry` | boolean |  | Symmetric quad mesh. Only with quad. default `false` |
| `texture_format` | string |  | Texture image format. one of: `JPEG`, `PNG`, `WEBP`, `BMP`, `DPX`, `HDR`, `OPEN_EXR`, `TARGA`, `TIFF`; default `"JPEG"` |
| `with_animation` | boolean |  | Keep animations. default `true` |
| `animate_in_place` | boolean |  | Remove root motion from animations. default `false` |
| `texture_packaging` | string |  | FBX only: embedded textures, or a zip with the FBX and a .fbm folder. one of: `embedded`, `zip`; default `"embedded"` |
| `export_orientation` | string |  | Forward axis of the exported model. one of: `+x`, `-x`, `+y`, `-y` |
| `export_vertex_colors` | boolean |  | Vertex colors (OBJ and GLTF only). default `false` |
| `pivot_to_center_bottom` | boolean |  | Move the pivot to the bottom center. default `false` |
| `flatten_bottom_threshold` | number |  | Depth flattened when flatten_bottom is on. default `0.01` |

## Details

Tripo Convert exports a 3D model to GLTF, FBX, USDZ, OBJ, STL or 3MF, with optional quad remesh, scaling and texture settings.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `model_url` | string, required | — | URL of the input 3D model (GLB, GLTF, FBX, OBJ or STL, up to 150 MB). |
| `format` | `GLTF` / `FBX` / `USDZ` / `OBJ` / `STL` / `3MF`, required | `FBX` | Output format. |
| `quad` | boolean | `false` | Quad remesh (10,000 faces when face_limit is unset). Forces FBX. |
| `force_symmetry` | boolean | `false` | Symmetric quad mesh. Only with quad. |
| `face_limit` | integer | — | Target face count. Original when unset. |
| `texture_size` | integer | `4096` | Texture size in pixels. |
| `texture_format` | `JPEG` / `PNG` / `WEBP` / `BMP` / `DPX` / `HDR` / `OPEN_EXR` / `TARGA` / `TIFF` | `JPEG` | Texture image format. |
| `bake` | boolean | `true` | Bake advanced materials into the textures. |
| `pack_uv` | boolean | `false` | Pack all UV islands into one texture. |
| `export_vertex_colors` | boolean | `false` | Vertex colors (OBJ and GLTF only). |
| `flatten_bottom` | boolean | `false` | Flatten the bottom of the model. |
| `flatten_bottom_threshold` | number | `0.01` | Depth flattened when flatten_bottom is on. |
| `pivot_to_center_bottom` | boolean | `false` | Move the pivot to the bottom center. |
| `scale_factor` | number | `1` | Uniform scale. |
| `with_animation` | boolean | `true` | Keep animations. |
| `animate_in_place` | boolean | `false` | Remove root motion from animations. |
| `part_names` | array | — | Only process these parts (node names from a segmentation, e.g. tripo_part_0). All parts when unset. |
| `export_orientation` | `+x` / `-x` / `+y` / `-y` | — | Forward axis of the exported model. |
| `fbx_preset` | `blender` / `3dsmax` / `mixamo` / `bake_scale` | `blender` | FBX target application. |
| `texture_packaging` | `embedded` / `zip` | `embedded` | FBX only: embedded textures, or a zip with the FBX and a .fbm folder. |
### Output
- `url`: Converted model file (a .zip when texture_packaging is zip).
### Billing
$0.05 per conversion; $0.10 when any of quad, face_limit, flatten_bottom, flatten_bottom_threshold, texture_size, texture_format, pivot_to_center_bottom or scale_factor is not the default.
Failed runs are not charged.

---
Machine-readable: [`catalog/models/tripo3d/tripo/convert.json`](../../../../catalog/models/tripo3d/tripo/convert.json) · Store page: https://www.sandbase.ai/model/tripo3d/tripo/convert
