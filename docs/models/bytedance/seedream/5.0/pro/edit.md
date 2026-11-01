# Seedream 5.0 Pro Edit

`bytedance/seedream/5.0/pro/edit` · image · Bytedance

Seedream 5.0 Pro is Bytedance's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from background replacement to artistic style conversion.

## Pricing

- Depends on parameters (`params.images`, `params.num_images`).

| parameters | USD |
|---|---|
| num_images=1 | 0.096 |

Formula: `(params.num_images ?? 1) * (0.09 + Math.max(0.0, len(params.images ?? []) - 1.0) * 0.003)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedream/5.0/pro/edit", "images": ["https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/83baa511-b454-4c5e-b799-66cf7a0c47fb.png", "https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/e8207f7d-83ad-4d7d-a340-cd3c53a00319.png", "https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/9bf41b90-b1b3-4b70-98cc-5616f8c52af1.png"], "prompt": "Replace the product in Figure 1 with that in Figure 2. Seamlessly render the logo in Figure 3 into the product design, in a frosted glass texture."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedream/5.0/pro/edit', {'images': ['https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/83baa511-b454-4c5e-b799-66cf7a0c47fb.png', 'https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/e8207f7d-83ad-4d7d-a340-cd3c53a00319.png', 'https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/9bf41b90-b1b3-4b70-98cc-5616f8c52af1.png'], 'prompt': 'Replace the product in Figure 1 with that in Figure 2. Seamlessly render the logo in Figure 3 into the product design, in a frosted glass texture.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedream/5.0/pro/edit", {
  "images": [
    "https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/83baa511-b454-4c5e-b799-66cf7a0c47fb.png",
    "https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/e8207f7d-83ad-4d7d-a340-cd3c53a00319.png",
    "https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/9bf41b90-b1b3-4b70-98cc-5616f8c52af1.png"
  ],
  "prompt": "Replace the product in Figure 1 with that in Figure 2. Seamlessly render the logo in Figure 3 into the product design, in a frosted glass texture."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedream/5.0/pro/edit", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/83baa511-b454-4c5e-b799-66cf7a0c47fb.png", "https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/e8207f7d-83ad-4d7d-a340-cd3c53a00319.png", "https://static.sandbase.ai/examples/a41b72ba-8748-49c4-9eca-e1a1d1566e86/input/9bf41b90-b1b3-4b70-98cc-5616f8c52af1.png"},
	"prompt": "Replace the product in Figure 1 with that in Figure 2. Seamlessly render the logo in Figure 3 into the product design, in a frosted glass texture.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | List of URLs of input reference images. Up to 10 images are supported; if more are sent, only the last 10 are used.  |
| `prompt` | string | yes | The text prompt used to edit the image.  |
| `num_images` | integer |  | The number of edited images to generate. Currently limited to 1. default `1`; range 1–1 |
| `aspect_ratio` | string |  | The aspect ratio of the edited 2K image. Leave unset to follow the reference image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The file format of the generated image. one of: `jpeg`, `png`; default `"jpeg"` |

## Details

Seedream 5.0 Pro edit: change or fuse up to 10 images with an instruction while keeping identity, products, and text consistent.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] (≤10), required | — | Images to edit or combine, Image 1, Image 2, … |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Omit to follow the first input image. |
| `num_images` | integer 1–1 | 1 | Fixed at 1. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |

### Billing

$0.09 per output image plus $0.003 for each input image after the first.

| Inputs | Price |
|---|---|
| 1 input image | $0.09 |
| 3 input images | $0.096 |
| 10 input images | $0.117 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other Seedream endpoints: `bytedance/seedream/5.0/pro`, `bytedance/seedream/5.0/lite`, `bytedance/seedream/5.0/lite/edit`, `bytedance/seedream/5.0/flash`, `bytedance/seedream/5.0/flash/edit`, `bytedance/seedream/4.5`, `bytedance/seedream/4.5/edit`.

---
Machine-readable: [`catalog/models/bytedance/seedream/5.0/pro/edit.json`](../../../../../../catalog/models/bytedance/seedream/5.0/pro/edit.json) · Store page: https://www.sandbase.ai/model/bytedance/seedream/5.0/pro/edit
