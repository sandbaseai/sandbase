# Hunyuan 3D 3.1 Pro Image to 3D API: pricing, parameters and code examples

`tencent/hunyuan-3d/3.1/pro/image-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.525 to $0.675 per run, depending on parameters · **Modes:** async

Hunyuan 3d 3.1 Pro by Tencent - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for games, AR/VR, e-commerce, and digital content creation.

## Pricing

- Depends on parameters (`params.back_image`, `params.bottom_image`, `params.enable_pbr`, `params.face_count`, `params.generate_type`, `params.left_front_image`, `params.left_image`, `params.right_front_image`, `params.right_image`, `params.top_image`).

| parameters | USD |
|---|---|
| enable_pbr=false, face_count=40000, generate_type="Normal" | 0.525 |
| enable_pbr=false, face_count=40000, generate_type="Geometry" | 0.525 |
| enable_pbr=false, face_count=1500000, generate_type="Normal" | 0.525 |
| enable_pbr=false, face_count=1500000, generate_type="Geometry" | 0.525 |
| enable_pbr=true, face_count=40000, generate_type="Normal" | 0.675 |
| enable_pbr=true, face_count=40000, generate_type="Geometry" | 0.525 |
| enable_pbr=true, face_count=1500000, generate_type="Normal" | 0.675 |
| enable_pbr=true, face_count=1500000, generate_type="Geometry" | 0.525 |

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hunyuan-3d/3.1/pro/image-to-3d", "image": "https://static.sandbase.ai/examples/94e37e73-ddad-454e-99f6-6362fce34d94/input/64c93e7c-ae98-4ead-975e-c35b5e237d72.png"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/hunyuan-3d/3.1/pro/image-to-3d', {'image': 'https://static.sandbase.ai/examples/94e37e73-ddad-454e-99f6-6362fce34d94/input/64c93e7c-ae98-4ead-975e-c35b5e237d72.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/hunyuan-3d/3.1/pro/image-to-3d", {
  "image": "https://static.sandbase.ai/examples/94e37e73-ddad-454e-99f6-6362fce34d94/input/64c93e7c-ae98-4ead-975e-c35b5e237d72.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/hunyuan-3d/3.1/pro/image-to-3d", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/94e37e73-ddad-454e-99f6-6362fce34d94/input/64c93e7c-ae98-4ead-975e-c35b5e237d72.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Front view image URL. Resolution: 128-5000px, max 8MB, formats: JPG/PNG/WEBP. Tips: simple background, single object, object >50% of frame.  |
| `top_image` | string |  | Optional top view image URL for multi-view reconstruction.  |
| `back_image` | string |  | Optional back view image URL for multi-view reconstruction.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. default `false` |
| `face_count` | integer |  | Target polygon face count (custom face count is billed as an add-on). range 40000–1500000 |
| `left_image` | string |  | Optional left view image URL for multi-view reconstruction.  |
| `right_image` | string |  | Optional right view image URL for multi-view reconstruction.  |
| `bottom_image` | string |  | Optional bottom view image URL for multi-view reconstruction.  |
| `generate_type` | string |  | Normal: textured model. Geometry: geometry-only white model. one of: `Normal`, `Geometry`; default `"Normal"` |
| `left_front_image` | string |  | Optional left-front view image URL for multi-view reconstruction.  |
| `right_front_image` | string |  | Optional right-front view image URL for multi-view reconstruction.  |

## Details

Hunyuan 3D 3.1 Pro turns an image (plus up to six extra views) into a high-detail textured or geometry-only 3D model.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Front view. JPEG, PNG, or WebP URL. |
| `top_image` | image URL | — | Optional extra view. |
| `back_image` | image URL | — | Optional extra view. |
| `enable_pbr` | boolean | false | PBR materials. |
| `face_count` | integer 40000–1500000 | — | Target face count. |
| `left_image` | image URL | — | Optional extra view. |
| `right_image` | image URL | — | Optional extra view. |
| `bottom_image` | image URL | — | Optional extra view. |
| `generate_type` | `Normal` / `Geometry` | `Normal` | `Normal` textured, `LowPoly`, or `Geometry` (untextured). |
| `left_front_image` | image URL | — | Optional extra view. |
| `right_front_image` | image URL | — | Optional extra view. |

### Billing

$0.375 per model; PBR, a custom face count, and extra views each add $0.15.

| Request | Price |
|---|---|
| Default | $0.375 |
| With PBR | $0.525 |
| With custom face count | $0.525 |

Failed runs are not charged.

### Also on SandBase

Other Hunyuan 3D endpoints: `tencent/hunyuan-3d/3.1/pro/text-to-3d`, `tencent/hunyuan-3d/3.0/image-to-3d`.

---
Machine-readable: [`catalog/models/tencent/hunyuan-3d/3.1/pro/image-to-3d.json`](../../../../../../catalog/models/tencent/hunyuan-3d/3.1/pro/image-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/hunyuan-3d/3.1/pro/image-to-3d
