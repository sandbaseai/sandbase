# SAM 3 Image API: pricing, parameters and code examples

`meta/sam-3/image` · image generation model · Meta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call · **Modes:** async

SAM 3 Image is Meta's segmentation model. It finds objects in an image from a text, point, or box prompt and returns masks and the masked image, with optional confidence scores.

## Pricing

- **$0.005 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meta/sam-3/image", "prompt": "wheel", "image": "<image>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meta/sam-3/image', {'prompt': 'wheel', 'image': '<image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meta/sam-3/image", {
  "prompt": "wheel",
  "image": "<image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meta/sam-3/image", sandbase.Params{
	"prompt": "wheel",
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
| `image` | string | yes | URL of the image to be segmented  |
| `prompt` | string | yes | Text prompt for segmentation default `"wheel"` |
| `max_masks` | integer |  | Maximum number of masks to return when `return_multiple_masks` is enabled. default `3`; range 1–32 |
| `apply_mask` | boolean |  | Apply the mask on the image. default `true` |
| `box_prompts` | array |  | Box prompt coordinates (x_min, y_min, x_max, y_max). Multiple boxes supported - use object_id to group boxes for the same object or leave empty for separate objects. default `[]` |
| `text_prompt` | string |  | [DEPRECATED] Use 'prompt' instead. Kept for backward compatibility.  |
| `include_boxes` | boolean |  | Whether to include bounding boxes for each mask (when available). default `false` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `point_prompts` | array |  | List of point prompts default `[]` |
| `include_scores` | boolean |  | Whether to include mask confidence scores. default `false` |
| `return_multiple_masks` | boolean |  | If True, upload and return multiple generated masks as defined by `max_masks`. default `false` |

## Details

SAM 3 segments objects in an image from a text, point, or box prompt and returns masks.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | `wheel` | What to segment, e.g. “the red car”. |
| `image` | image URL, required | — | Image to segment. JPEG, PNG, or WebP URL. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `box_prompts` | item[] | `[]` | Optional boxes. |
| `text_prompt` | string | — | [DEPRECATED] Use 'prompt' instead. |
| `include_scores` | boolean | false | Whether to include mask confidence scores. |
| `apply_mask` | boolean | true | Return the masked image. |
| `point_prompts` | item[] | `[]` | Optional points. |
| `return_multiple_masks` | boolean | false | If True, upload and return multiple generated masks as defined by `max_masks`. |
| `max_masks` | integer 1–32 | 3 | Maximum masks to return. |
| `include_boxes` | boolean | false | Whether to include bounding boxes for each mask (when available). |

### Billing

$0.005 per image.

| Request | Price |
|---|---|
| One image | $0.005 |

Failed runs are not charged.

### Also on SandBase

Related: `meta/sam-3/3d-objects`.

---
Machine-readable: [`catalog/models/meta/sam-3/image.json`](../../../../catalog/models/meta/sam-3/image.json) · Store page: https://www.sandbase.ai/model/meta/sam-3/image
