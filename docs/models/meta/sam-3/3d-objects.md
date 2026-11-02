# SAM 3 3D Objects API: pricing, parameters and code examples

`meta/sam-3/3d-objects` · image generation model · Meta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.024 per run, depending on parameters · **Modes:** async

Sam 3 3d Objects by Meta - convert 2D images into 3D models with AI. Generate textured 3D assets from single photos for games, AR/VR, e-commerce, and digital content creation.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.024 |

Formula: `0.024`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meta/sam-3/3d-objects", "prompt": "car", "image": "<image>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meta/sam-3/3d-objects', {'prompt': 'car', 'image': '<image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meta/sam-3/3d-objects", {
  "prompt": "car",
  "image": "<image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meta/sam-3/3d-objects", sandbase.Params{
	"prompt": "car",
	"image": "<image>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility  |
| `image` | string | yes | URL of the image to reconstruct in 3D  |
| `prompt` | string | yes | Text prompt for auto-segmentation when no masks provided (e.g., 'chair', 'lamp') default `"car"` |
| `mask_urls` | array |  | Optional list of mask URLs (one per object). If not provided, use prompt/point_prompts/box_prompts to auto-segment, or entire image will be used.  |
| `box_prompts` | array |  | Box prompts for auto-segmentation when no masks provided. Multiple boxes supported - each produces a separate object mask for 3D reconstruction. default `[]` |
| `pointmap_url` | string |  | Optional URL to external pointmap/depth data (NPY or NPZ format) for improved 3D reconstruction depth estimation  |
| `point_prompts` | array |  | Point prompts for auto-segmentation when no masks provided default `[]` |
| `detection_threshold` | number |  | Detection confidence threshold (0.1-1.0). Lower = more detections but less precise. If not set, uses the model's default. range 0.1–1 |
| `export_textured_glb` | boolean |  | If True, exports GLB with baked texture and UVs instead of vertex colors. default `false` |

## Details

SAM 3D Objects reconstructs a segmented object from a single image as a 3D model.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | `car` | What to reconstruct. |
| `image` | image URL, required | — | Image containing the object. JPEG, PNG, or WebP URL. |
| `point_prompts` | object[] | `[]` | Point prompts for auto-segmentation when no masks provided |
| `detection_threshold` | number 0.1–1 | — | Detection confidence threshold (0.1-1.0). |
| `box_prompts` | object[] | `[]` | Box prompts for auto-segmentation when no masks provided. |
| `pointmap_url` | string | — | Optional URL to external pointmap/depth data (NPY or NPZ format) for improved 3D reconstruction depth estimation |
| `export_textured_glb` | boolean | false | Export a textured GLB. |
| `mask_urls` | image URL[] | — | Optional list of mask URLs (one per object). |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.024 per object.

| Request | Price |
|---|---|
| One object | $0.024 |

Failed runs are not charged.

### Also on SandBase

Related: `meta/sam-3/image`.

---
Machine-readable: [`catalog/models/meta/sam-3/3d-objects.json`](../../../../catalog/models/meta/sam-3/3d-objects.json) · Store page: https://www.sandbase.ai/model/meta/sam-3/3d-objects
