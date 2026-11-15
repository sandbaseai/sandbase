# Miora 3D Multi-View to 3D API: pricing, parameters and code examples

`tencent/miora-3d/multi-view-to-3d` · image generation model · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.6 to $0.857143 per run, depending on parameters · **Modes:** async

Miora 3D by Tencent Design reconstructs a textured or untextured 3D asset from a front image plus optional back, side, top, bottom and 45-degree views.

## Pricing

- Depends on parameters (`params.back_image`, `params.bottom_image`, `params.enable_pbr`, `params.face_count`, `params.generate_type`, `params.left_front_image`, `params.left_image`, `params.right_front_image`, `params.right_image`, `params.top_image`).

| parameters | USD |
|---|---|
| enable_pbr=false, face_count=3000, generate_type="Normal" | 0.685714 |
| enable_pbr=false, face_count=3000, generate_type="Geometry" | 0.6 |
| enable_pbr=false, face_count=1500000, generate_type="Normal" | 0.685714 |
| enable_pbr=false, face_count=1500000, generate_type="Geometry" | 0.6 |
| enable_pbr=true, face_count=3000, generate_type="Normal" | 0.857143 |
| enable_pbr=true, face_count=3000, generate_type="Geometry" | 0.6 |
| enable_pbr=true, face_count=1500000, generate_type="Normal" | 0.857143 |
| enable_pbr=true, face_count=1500000, generate_type="Geometry" | 0.6 |

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/miora-3d/multi-view-to-3d", "back_image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/a136f725-ff3d-46c9-8451-ca84dc72ca73.png", "image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/fe06a98d-0e79-4ffb-a08e-8401e2d2ba8d.png", "left_image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/d2780dc6-53fd-4e9e-8eca-4539d02187ce.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent/miora-3d/multi-view-to-3d', {'back_image': 'https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/a136f725-ff3d-46c9-8451-ca84dc72ca73.png', 'image': 'https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/fe06a98d-0e79-4ffb-a08e-8401e2d2ba8d.png', 'left_image': 'https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/d2780dc6-53fd-4e9e-8eca-4539d02187ce.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent/miora-3d/multi-view-to-3d", {
  "back_image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/a136f725-ff3d-46c9-8451-ca84dc72ca73.png",
  "image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/fe06a98d-0e79-4ffb-a08e-8401e2d2ba8d.png",
  "left_image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/d2780dc6-53fd-4e9e-8eca-4539d02187ce.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent/miora-3d/multi-view-to-3d", sandbase.Params{
	"back_image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/a136f725-ff3d-46c9-8451-ca84dc72ca73.png",
	"image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/fe06a98d-0e79-4ffb-a08e-8401e2d2ba8d.png",
	"left_image": "https://static.sandbase.ai/examples/ecfc21d3-eab9-4dea-9fd6-68dd64d229dc/input/d2780dc6-53fd-4e9e-8eca-4539d02187ce.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Front view image URL. 128-5000 px per side, up to 10 MB, JPG/PNG/WEBP. Works best with a single object on a simple background.  |
| `top_image` | string |  | Optional top view image URL for multi-view reconstruction.  |
| `back_image` | string |  | Optional back view image URL for multi-view reconstruction.  |
| `enable_pbr` | boolean |  | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. default `false` |
| `face_count` | integer |  | Target polygon face count. Uses the model default when unset. range 3000–1500000 |
| `left_image` | string |  | Optional left view image URL for multi-view reconstruction.  |
| `right_image` | string |  | Optional right view image URL for multi-view reconstruction.  |
| `bottom_image` | string |  | Optional bottom view image URL for multi-view reconstruction.  |
| `generate_type` | string |  | Normal: textured model. Geometry: untextured white model. one of: `Normal`, `Geometry`; default `"Normal"` |
| `left_front_image` | string |  | Optional left-front view image URL for multi-view reconstruction.  |
| `right_front_image` | string |  | Optional right-front view image URL for multi-view reconstruction.  |

## Details

Miora 3D by Tencent Design reconstructs a textured or untextured 3D asset from a front image plus optional back, side, top, bottom and 45-degree views.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Front view image URL. 128-5000 px per side, up to 10 MB, JPG/PNG/WEBP. Works best with a single object on a simple background. |
| `generate_type` | string | "Normal" | Normal: textured model. Geometry: untextured white model. |
| `enable_pbr` | boolean | false | Generate PBR materials (metallic, roughness, normal). Ignored for Geometry output. |
| `face_count` | integer | — | Target polygon face count. Uses the model default when unset. |
| `back_image` | image URL | — | Optional back view image URL for multi-view reconstruction. |
| `left_image` | image URL | — | Optional left view image URL for multi-view reconstruction. |
| `right_image` | image URL | — | Optional right view image URL for multi-view reconstruction. |
| `top_image` | image URL | — | Optional top view image URL for multi-view reconstruction. |
| `bottom_image` | image URL | — | Optional bottom view image URL for multi-view reconstruction. |
| `left_front_image` | image URL | — | Optional left-front view image URL for multi-view reconstruction. |
| `right_front_image` | image URL | — | Optional right-front view image URL for multi-view reconstruction. |

### Billing

| Request | Price |
|---|---|
| Default | $0.3429 |
| Geometry (untextured) | $0.2571 |
| With PBR | $0.5143 |
| With custom face count | $0.5143 |
| With extra views | $0.5143 |

PBR, a custom face count and extra views each add to the default price. Failed runs are not charged.

---
Machine-readable: [`catalog/models/tencent/miora-3d/multi-view-to-3d.json`](../../../../catalog/models/tencent/miora-3d/multi-view-to-3d.json) · Store page: https://www.sandbase.ai/model/tencent/miora-3d/multi-view-to-3d
