# Hunyuan 3D 3.6 Image to 3D API: pricing, parameters and code examples

`tencent/hunyuan-3d/3.6/image-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.6 to $1.4 per run, depending on parameters · **Modes:** async

Hunyuan 3D 3.6 (Hy3D 3.6) is Tencent's newest native 3D generation model. Turn a reference image, with optional extra views, into a detailed high-poly 3D model with PBR materials, up to 2,000,000 faces.

## Pricing

- Depends on parameters (`params.back_image`, `params.bottom_image`, `params.generate_type`, `params.left_front_image`, `params.left_image`, `params.right_front_image`, `params.right_image`, `params.top_image`).

| parameters | USD |
|---|---|
| generate_type="Normal" | 1.4 |
| generate_type="Geometry" | 0.6 |

Formula: `(((params.back_image ?? "") != "" || (params.left_image ?? "") != "" || (params.right_image ?? "") != "" || (params.top_image ?? "") != "" || (params.bottom_image ?? "") != "" || (params.left_front_image ?? "") != "" || (params.right_front_image ?? "") != "") ? ((params.generate_type ?? "Normal") == "Geometry" ? 0.80 : 2.00) : ((params.generate_type ?? "Normal") == "Geometry" ? 0.60 : 1.40))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/3.6/image-to-3d", "image": "https://static.sandbase.ai/examples/bc53910c-b5b6-4d6a-9ad9-bda31001c29d/input/8d834435-c74e-4336-b85b-a5541823c030.png"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/3.6/image-to-3d', {'image': 'https://static.sandbase.ai/examples/bc53910c-b5b6-4d6a-9ad9-bda31001c29d/input/8d834435-c74e-4336-b85b-a5541823c030.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/3.6/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/bc53910c-b5b6-4d6a-9ad9-bda31001c29d/input/8d834435-c74e-4336-b85b-a5541823c030.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/3.6/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/bc53910c-b5b6-4d6a-9ad9-bda31001c29d/input/8d834435-c74e-4336-b85b-a5541823c030.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Front view image, file or URL. Resolution 128-5000px, max 8MB, JPG/PNG/WEBP. Tips: simple background, single object, object >50% of frame.  |
| `top_image` | string |  | Optional top view image file or URL for multi-view reconstruction.  |
| `back_image` | string |  | Optional back view image file or URL for multi-view reconstruction.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. default `false` |
| `face_count` | integer |  | Target polygon face count, 40,000 to 2,000,000. range 40000–2000000 |
| `left_image` | string |  | Optional left view image file or URL for multi-view reconstruction.  |
| `right_image` | string |  | Optional right view image file or URL for multi-view reconstruction.  |
| `bottom_image` | string |  | Optional bottom view image file or URL for multi-view reconstruction.  |
| `generate_type` | string |  | Normal: textured model. Geometry: geometry-only white model. one of: `Normal`, `Geometry`; default `"Normal"` |
| `left_front_image` | string |  | Optional left-front view image file or URL for multi-view reconstruction.  |
| `right_front_image` | string |  | Optional right-front view image file or URL for multi-view reconstruction.  |

## Details

Hunyuan 3D 3.6 (Hy3D 3.6) is Tencent's newest native 3D model, released 2026-11-27. It learns geometry, textures and materials directly from 3D assets, with cleaner surfaces, sharper hard-surface structure and higher-quality PBR textures than 3.1. It turns an image (plus up to six extra views) into a textured or geometry-only model of up to 2,000,000 faces.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image file or URL, required | — | Front view. JPEG, PNG, or WebP. |
| `top_image` | image file or URL | — | Optional extra view. |
| `back_image` | image file or URL | — | Optional extra view. |
| `enable_pbr` | boolean | false | PBR materials. |
| `face_count` | integer 40000–2000000 | — | Target face count. |
| `left_image` | image file or URL | — | Optional extra view. |
| `right_image` | image file or URL | — | Optional extra view. |
| `bottom_image` | image file or URL | — | Optional extra view. |
| `generate_type` | `Normal` / `Geometry` | `Normal` | `Normal` textured or `Geometry` (untextured). |
| `left_front_image` | image file or URL | — | Optional extra view. |
| `right_front_image` | image file or URL | — | Optional extra view. |

### Billing
| Request | Price |
|---|---|
| Single image, textured | $1.40 |
| Single image, geometry only | $0.60 |
| With extra views, textured | $2.00 |
| With extra views, geometry only | $0.80 |
PBR materials and a custom face count do not change the price. Failed runs are not charged.
### Also on SandBase
Other Hunyuan 3D endpoints: `tencent/hunyuan-3d/3.6/text-to-3d`, `tencent/hunyuan-3d/3.1/pro/image-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/3.6/image-to-3d.json`](../../../../../catalog/models/tencent/hunyuan-3d/3.6/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/3.6/image-to-3d
