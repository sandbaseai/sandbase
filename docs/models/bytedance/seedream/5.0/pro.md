# Seedream 5.0 Pro Text to Image

`bytedance/seedream/5.0/pro` · image · Bytedance

Seedream 5.0 Pro by Bytedance - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- Depends on parameters (`params.num_images`).

| parameters | USD |
|---|---|
| num_images=1 | 0.09 |

Formula: `(params.num_images ?? 1) * 0.09`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedream/5.0/pro", "prompt": "Vibrant editorial of a model in contemporary fashion fused with West African textile patterns and beadwork, Campbell Addy bold aesthetic, saturated palette, dramatic studio lighting, celebratory cultural richness, striking contemporary portraiture"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedream/5.0/pro', {'prompt': 'Vibrant editorial of a model in contemporary fashion fused with West African textile patterns and beadwork, Campbell Addy bold aesthetic, saturated palette, dramatic studio lighting, celebratory cultural richness, striking contemporary portraiture'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedream/5.0/pro", {
  "prompt": "Vibrant editorial of a model in contemporary fashion fused with West African textile patterns and beadwork, Campbell Addy bold aesthetic, saturated palette, dramatic studio lighting, celebratory cultural richness, striking contemporary portraiture"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedream/5.0/pro", sandbase.Params{
	"prompt": "Vibrant editorial of a model in contemporary fashion fused with West African textile patterns and beadwork, Campbell Addy bold aesthetic, saturated palette, dramatic studio lighting, celebratory cultural richness, striking contemporary portraiture",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt used to generate the image.  |
| `num_images` | integer |  | The number of images to generate. Currently limited to 1. default `1`; range 1–1 |
| `aspect_ratio` | string |  | The aspect ratio of the generated 2K image. Defaults to 1:1. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The file format of the generated image. one of: `jpeg`, `png`; default `"jpeg"` |

## Details

Seedream 5.0 Pro is ByteDance's top image tier: photorealistic detail, dense layouts, and reliable Chinese and English text.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `num_images` | integer 1–1 | 1 | Fixed at 1. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |

### Billing

$0.09 per image.

| Request | Price |
|---|---|
| One image | $0.09 |

Failed runs are not charged.

### Prompting

- Write subject, layout, style, then light and color.
- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other Seedream endpoints: `bytedance/seedream/5.0/pro/edit`, `bytedance/seedream/5.0/lite`, `bytedance/seedream/5.0/lite/edit`, `bytedance/seedream/5.0/flash`, `bytedance/seedream/5.0/flash/edit`, `bytedance/seedream/4.5`, `bytedance/seedream/4.5/edit`.

---
Machine-readable: [`catalog/models/bytedance/seedream/5.0/pro.json`](../../../../../catalog/models/bytedance/seedream/5.0/pro.json) · Store page: https://www.sandbase.ai/model/bytedance/seedream/5.0/pro
