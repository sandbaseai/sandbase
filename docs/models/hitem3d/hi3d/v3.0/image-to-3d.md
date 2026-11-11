# Hitem3D Hi3D 3.0 Image to 3D API: pricing, parameters and code examples

`hitem3d/hi3d/v3.0/image-to-3d` · image generation model · Hitem3D · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $2.16 to $10.92 per run, depending on parameters · **Modes:** async

Hi3D 3.0 by Hitem3D reconstructs a detailed, watertight 3D model at 2048³ resolution from a single image, with optional texture and PBR materials.

## Pricing

- Depends on parameters (`params.enable_pbr`, `params.enable_texture`, `params.resolution`).

| parameters | USD |
|---|---|
| enable_pbr=false, enable_texture=false, resolution="2048quality" | 2.16 |
| enable_pbr=false, enable_texture=false, resolution="2048master" | 10.56 |
| enable_pbr=false, enable_texture=true, resolution="2048quality" | 2.4 |
| enable_pbr=false, enable_texture=true, resolution="2048master" | 10.8 |
| enable_pbr=true, enable_texture=false, resolution="2048quality" | 2.16 |
| enable_pbr=true, enable_texture=false, resolution="2048master" | 10.56 |
| enable_pbr=true, enable_texture=true, resolution="2048quality" | 2.52 |
| enable_pbr=true, enable_texture=true, resolution="2048master" | 10.92 |

Formula: `((params.resolution ?? "2048quality") == "2048master" ? 10.56 : 2.16) + ((params.enable_texture ?? true) ? ((params.enable_pbr ?? true) ? 0.36 : 0.24) : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hitem3d/hi3d/v3.0/image-to-3d", "image": "https://storage.googleapis.com/falserverless/example_inputs/dog.png"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hitem3d/hi3d/v3.0/image-to-3d', {'image': 'https://storage.googleapis.com/falserverless/example_inputs/dog.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hitem3d/hi3d/v3.0/image-to-3d", {
  "image": "https://storage.googleapis.com/falserverless/example_inputs/dog.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hitem3d/hi3d/v3.0/image-to-3d", sandbase.Params{
	"image": "https://storage.googleapis.com/falserverless/example_inputs/dog.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Input image URL. PNG, JPEG and WebP, up to 20MB.  |
| `shading` | number |  | De-shading strength. default `0.5`; range 0–1 |
| `enable_pbr` | boolean |  | Generate PBR material maps with the texture (billed add-on, ignored when texture is off). default `true` |
| `face_count` | integer |  | Target face count. Recommended 2,000,000 for 2048quality and 5,000,000 for 2048master. range 100000–5000000 |
| `resolution` | string |  | 2048quality is the faster default; 2048master gives the highest quality. one of: `2048quality`, `2048master`; default `"2048quality"` |
| `export_format` | string |  | File format of the generated model. one of: `glb`, `obj`, `stl`, `fbx`, `usdz`; default `"glb"` |
| `enable_texture` | boolean |  | Generate textures in addition to geometry. When false, only the geometry mesh is generated (cheaper). default `true` |

## Details

Hi3D 3.0 by Hitem3D reconstructs a detailed, watertight 3D model at 2048³ resolution from a single image, with optional texture and PBR materials.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Input image URL. PNG, JPEG and WebP, up to 20MB. |
| `resolution` | `2048quality` / `2048master` | `2048quality` | 2048quality is the faster default; 2048master gives the highest quality. |
| `enable_texture` | boolean | `true` | Generate textures in addition to geometry. When false, only the geometry mesh is generated (cheaper). |
| `enable_pbr` | boolean | `true` | Generate PBR material maps with the texture (billed add-on, ignored when texture is off). |
| `face_count` | integer 100000–5000000 | — | Target face count. Recommended 2,000,000 for 2048quality and 5,000,000 for 2048master. |
| `shading` | number 0–1 | `0.5` | De-shading strength. |
| `export_format` | `glb` / `obj` / `stl` / `fbx` / `usdz` | `glb` | File format of the generated model. |
### Output
- `url`: Main 3D file (GLB unless another export format is selected).
- `thumbnail`: Preview image rendered by the provider.
### Billing
$2.52 per request with default settings. Price by option (other settings at default):
| Option | Price |
|---|---|
| enable_pbr on | $2.52 |
| enable_pbr off | $2.40 |
| enable_texture on | $2.52 |
| enable_texture off | $2.16 |
| resolution = 2048quality | $2.52 |
| resolution = 2048master | $10.92 |
Failed runs are not charged.
### Also on SandBase
Other Hitem3D 3D endpoints: `hitem3d/hi3d/image-to-3d`, `hitem3d/hi3d/multi-view-to-3d`, `hitem3d/hi3d/multicolor`, `hitem3d/hi3d/split`.

---
Machine-readable: [`catalog/models/hitem3d/hi3d/v3.0/image-to-3d.json`](../../../../../catalog/models/hitem3d/hi3d/v3.0/image-to-3d.json) · Store page: https://www.sandbase.ai/model/hitem3d/hi3d/v3.0/image-to-3d
