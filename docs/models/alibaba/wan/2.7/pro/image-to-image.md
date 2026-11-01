# Wan 2.7 Pro Image to Image

`alibaba/wan/2.7/pro/image-to-image` · image · Alibaba

Alibaba Wan 2.7 Pro image-to-image model that edits images from a natural-language instruction, with multi-reference support and selectable aspect ratio.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.075 |

Formula: `0.075`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.7/pro/image-to-image", "images": ["https://static.sandbase.ai/examples/b6b5c008-4e2b-443b-a9ce-2fcf162ecdb1/input/53727e1f-7615-415c-b23b-2afcd51b167a.webp"], "prompt": "Edit based on image 1. Replace the raspberry selected in box 1 with a lemon, the raspberry in box 2 with a strawberry, and the raspberry in box 3 with a blueberry. The result should be harmoniously integrated with the original image, without the reference boxes and numbers, and keep the rest of the content unchanged."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.7/pro/image-to-image', {'images': ['https://static.sandbase.ai/examples/b6b5c008-4e2b-443b-a9ce-2fcf162ecdb1/input/53727e1f-7615-415c-b23b-2afcd51b167a.webp'], 'prompt': 'Edit based on image 1. Replace the raspberry selected in box 1 with a lemon, the raspberry in box 2 with a strawberry, and the raspberry in box 3 with a blueberry. The result should be harmoniously integrated with the original image, without the reference boxes and numbers, and keep the rest of the content unchanged.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.7/pro/image-to-image", {
  "images": [
    "https://static.sandbase.ai/examples/b6b5c008-4e2b-443b-a9ce-2fcf162ecdb1/input/53727e1f-7615-415c-b23b-2afcd51b167a.webp"
  ],
  "prompt": "Edit based on image 1. Replace the raspberry selected in box 1 with a lemon, the raspberry in box 2 with a strawberry, and the raspberry in box 3 with a blueberry. The result should be harmoniously integrated with the original image, without the reference boxes and numbers, and keep the rest of the content unchanged."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.7/pro/image-to-image", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/b6b5c008-4e2b-443b-a9ce-2fcf162ecdb1/input/53727e1f-7615-415c-b23b-2afcd51b167a.webp"},
	"prompt": "Edit based on image 1. Replace the raspberry selected in box 1 with a lemon, the raspberry in box 2 with a strawberry, and the raspberry in box 3 with a blueberry. The result should be harmoniously integrated with the original image, without the reference boxes and numbers, and keep the rest of the content unchanged.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | List of input image URLs for editing. Up to 4 images.  |
| `prompt` | string | yes | The editing instruction describing what changes to make. default `"Change the time to dramatic sunset with orange and purple sky, long shadows, warm golden light on the lighthouse"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21` |

## Details

The Pro tier of Wan 2.7 image editing: the same instruction-based edits as the standard tier, rendered with more detail and better preservation of faces, text, and fine texture.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 10,000 characters. |
| `images` | image URL[], required | — | Images to edit or combine, referred to as Image 1, Image 2, … |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `9:21` | — | Omit to follow the first input image. |

### Billing

$0.075 per output image, Alibaba's list price. Input images are not metered.

| Request | Price |
|---|---|
| One image | $0.075 |

Failed runs are not charged.

### Prompting

- Lead with the edit, then list what must not change.
- Describe light and color for relighting edits: “dramatic sunset, long shadows, warm light on the walls”.

### Limits

- One output image per request.

### Also on SandBase

Other Wan 2.7 image endpoints: `alibaba/wan/2.7/text-to-image`, `alibaba/wan/2.7/image-to-image`, `alibaba/wan/2.7/pro/text-to-image`.

---
Machine-readable: [`catalog/models/alibaba/wan/2.7/pro/image-to-image.json`](../../../../../../catalog/models/alibaba/wan/2.7/pro/image-to-image.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.7/pro/image-to-image
