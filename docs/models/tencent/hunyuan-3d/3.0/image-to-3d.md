# Hunyuan 3D 3.0 Image to 3D API: pricing, parameters and code examples

`tencent/hunyuan-3d/3.0/image-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.45 to $0.9 per run, depending on parameters · **Modes:** async

Hunyuan 3d V3 is Tencent's image-to-3D AI model. Transform photographs into production-ready 3D meshes with accurate geometry and texture mapping.

## Pricing

- Depends on parameters (`params.back_image`, `params.enable_pbr`, `params.generate_type`, `params.left_image`, `params.right_image`).

| parameters | USD |
|---|---|
| enable_pbr=false, generate_type="Normal" | 0.63 |
| enable_pbr=false, generate_type="LowPoly" | 0.72 |
| enable_pbr=false, generate_type="Geometry" | 0.45 |
| enable_pbr=true, generate_type="Normal" | 0.81 |
| enable_pbr=true, generate_type="LowPoly" | 0.9 |
| enable_pbr=true, generate_type="Geometry" | 0.45 |

Formula: `((params.generate_type ?? "Normal") == "LowPoly" ? 0.72 : (params.generate_type ?? "Normal") == "Geometry" ? 0.45 : 0.63) + ((params.enable_pbr ?? false) && (params.generate_type ?? "Normal") != "Geometry" ? 0.18 : 0.0) + (((params.back_image ?? "") != "" || (params.left_image ?? "") != "" || (params.right_image ?? "") != "") ? 0.18 : 0.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/3.0/image-to-3d", "image": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/v3/input_image_0.png"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/3.0/image-to-3d', {'image': 'https://static.sandbase.ai/examples/tencent/hunyuan-3d/v3/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/3.0/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/v3/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/3.0/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/tencent/hunyuan-3d/v3/input_image_0.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of image to use while generating the 3D model.  |
| `back_image` | string |  | Optional back view image URL for multi-view reconstruction.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. default `false` |
| `face_count` | integer |  | Target polygon face count (custom face count is billed as an add-on). default `500000`; range 40000–1500000 |
| `left_image` | string |  | Optional left view image URL for multi-view reconstruction.  |
| `right_image` | string |  | Optional right view image URL for multi-view reconstruction.  |
| `polygon_type` | string |  | Polygon type. Only takes effect when generate_type is LowPoly. one of: `triangle`, `quadrilateral`; default `"triangle"` |
| `generate_type` | string |  | Normal: textured model. LowPoly: polygon reduction. Geometry: white model without texture. one of: `Normal`, `LowPoly`, `Geometry`; default `"Normal"` |

## Details

Hunyuan 3D 3.0 turns an image (plus optional side and back views) into a textured, low-poly, or geometry-only 3D model.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Front view. JPEG, PNG, or WebP URL. |
| `enable_pbr` | boolean | false | PBR materials. |
| `polygon_type` | `triangle` / `quadrilateral` | `triangle` | Triangle or quad mesh. |
| `generate_type` | `Normal` / `LowPoly` / `Geometry` | `Normal` | `Normal` textured, `LowPoly`, or `Geometry` (untextured). |
| `face_count` | integer 40000–1500000 | 500000 | Target face count. |
| `back_image` | image URL | — | Optional extra view. |
| `left_image` | image URL | — | Optional extra view. |
| `right_image` | image URL | — | Optional extra view. |

### Billing

$0.63 per textured model, $0.72 low-poly, $0.45 geometry-only; PBR adds $0.18 and extra views add $0.18.

| Request | Price |
|---|---|
| Normal | $0.63 |
| LowPoly | $0.72 |
| Geometry | $0.45 |
| Normal + PBR + extra views | $0.99 |

Failed runs are not charged.

### Also on SandBase

Other Hunyuan 3D endpoints: `tencent/hunyuan-3d/3.1/pro/text-to-3d`, `tencent/hunyuan-3d/3.1/pro/image-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/3.0/image-to-3d.json`](../../../../../catalog/models/tencent/hunyuan-3d/3.0/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/3.0/image-to-3d
