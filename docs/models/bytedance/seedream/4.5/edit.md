# Seedream 4.5 Edit API: pricing, parameters and code examples

`bytedance/seedream/4.5/edit` · image generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.04 per call · **Modes:** async

A new-generation image creation model from ByteDance, Seedream 4.5 integrates text-to-image generation and image editing into a single unified architecture, delivering high-fidelity visuals, precise prompt control, and seamless creative workflows for professional AIGC applications.

## Pricing

- **$0.04 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedream/4.5/edit", "prompt": "Replace the clothing in image 1 with the outfit from image 2.", "images": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4b4464161cf3463db6f9463b10939178~tplv-goo7wpa0wc-image.image"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedream/4.5/edit', {'prompt': 'Replace the clothing in image 1 with the outfit from image 2.', 'images': 'https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4b4464161cf3463db6f9463b10939178~tplv-goo7wpa0wc-image.image'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedream/4.5/edit", {
  "prompt": "Replace the clothing in image 1 with the outfit from image 2.",
  "images": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4b4464161cf3463db6f9463b10939178~tplv-goo7wpa0wc-image.image"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedream/4.5/edit", sandbase.Params{
	"prompt": "Replace the clothing in image 1 with the outfit from image 2.",
	"images": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4b4464161cf3463db6f9463b10939178~tplv-goo7wpa0wc-image.image",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | The URLs of the images to use for image-to-image generation or image editing.  |
| `prompt` | string | yes | The text prompt to generate an image from. default `"Replace the clothing in image 1 with the outfit from image 2."` |
| `image_size` | object |  | Custom Size  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Seedream 4.5 edit: instruction-based edits and multi-image composition with consistent identity and typography.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URL[], required | — | Images to edit or combine, Image 1, Image 2, … |
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `1:1` / `3:4` / `2:3` / `9:16` | — | Omit to follow the first input image. |
| `image_size` | object | — | Optional explicit output size; overrides `aspect_ratio`. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |

### Billing

$0.04 per output image.

| Request | Price |
|---|---|
| One image | $0.04 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other Seedream endpoints: `bytedance/seedream/5.0/pro`, `bytedance/seedream/5.0/pro/edit`, `bytedance/seedream/5.0/lite`, `bytedance/seedream/5.0/lite/edit`, `bytedance/seedream/5.0/flash`, `bytedance/seedream/5.0/flash/edit`, `bytedance/seedream/4.5`.

---
Machine-readable: [`catalog/models/bytedance/seedream/4.5/edit.json`](../../../../../catalog/models/bytedance/seedream/4.5/edit.json) · Store page: https://www.sandbase.ai/model/bytedance/seedream/4.5/edit
