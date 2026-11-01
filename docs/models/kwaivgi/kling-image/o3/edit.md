# Kling Image O3 Edit

`kwaivgi/kling-image/o3/edit` · image · KwaiVGI

Kling Image O3 Edit by Kuaishou edits or recomposes images from a text instruction using up to 10 reference images, with 1K, 2K, or 4K output.

## Pricing

- Depends on parameters (`params.resolution`).

| parameters | USD |
|---|---|
| resolution="1K" | 0.028 |
| resolution="2K" | 0.028 |
| resolution="4K" | 0.056 |

Formula: `(params.resolution ?? "1K") == "4K" ? 0.056 : 0.028`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-image/o3/edit", "images": ["https://static.sandbase.ai/examples/1a588da4-8a64-49ca-ad13-6a2efe9bf164/input/e4cacf41-40f9-4c26-b397-7862af7bd5d9.png"], "prompt": "Transform into photorealistic 3D render, add proper lighting and shadows, realistic materials and textures, maintain exact proportions and design from sketch, product visualization quality"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-image/o3/edit', {'images': ['https://static.sandbase.ai/examples/1a588da4-8a64-49ca-ad13-6a2efe9bf164/input/e4cacf41-40f9-4c26-b397-7862af7bd5d9.png'], 'prompt': 'Transform into photorealistic 3D render, add proper lighting and shadows, realistic materials and textures, maintain exact proportions and design from sketch, product visualization quality'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-image/o3/edit", {
  "images": [
    "https://static.sandbase.ai/examples/1a588da4-8a64-49ca-ad13-6a2efe9bf164/input/e4cacf41-40f9-4c26-b397-7862af7bd5d9.png"
  ],
  "prompt": "Transform into photorealistic 3D render, add proper lighting and shadows, realistic materials and textures, maintain exact proportions and design from sketch, product visualization quality"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-image/o3/edit", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/1a588da4-8a64-49ca-ad13-6a2efe9bf164/input/e4cacf41-40f9-4c26-b397-7862af7bd5d9.png"},
	"prompt": "Transform into photorealistic 3D render, add proper lighting and shadows, realistic materials and textures, maintain exact proportions and design from sketch, product visualization quality",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | List of reference images. Reference images in prompt using @Image1, @Image2, etc. (1-indexed). Max 10 images.  |
| `prompt` | string | yes | Text prompt for image generation. Reference images using @Image1, @Image2, etc. (or @Image if only one image). Max 2500 characters.  |
| `resolution` | string |  | Image generation resolution. 1K: standard, 2K: high-res, 4K: ultra high-res. one of: `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"16:9"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Kling Image O3 edit: change or combine images with an instruction, up to 4K.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `images` | image URL[], required | — | Images to edit or combine, @Image1, @Image2, … |
| `resolution` | `1K` / `2K` / `4K` | `1K` | Sets the per-image rate. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output shape. |

### Billing

$0.028 per image at 1K or 2K and $0.056 at 4K.

| Request | 1K | 2K | 4K |
|---|---|---|---|
| One image | $0.028 | $0.028 | $0.056 |

Failed runs are not charged.

### Prompting

- Quote any text that must appear.

### Limits

- One image per request.

### Also on SandBase

Related: `kwaivgi/kling-image/o3`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-image/o3/edit.json`](../../../../../catalog/models/kwaivgi/kling-image/o3/edit.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-image/o3/edit
