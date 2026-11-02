# Z Image Base API: pricing, parameters and code examples

`alibaba/z-image/base` · image generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

Z Image Base by Alibaba - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/z-image/base", "prompt": "Grandmother knitting by a window, an empty chair by her"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/z-image/base', {'prompt': 'Grandmother knitting by a window, an empty chair by her'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/z-image/base", {
  "prompt": "Grandmother knitting by a window, an empty chair by her"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/z-image/base", sandbase.Params{
	"prompt": "Grandmother knitting by a window, an empty chair by her",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The same seed and the same prompt given to the same version of the model will output the same image every time.  |
| `prompt` | string | yes | The prompt to generate an image from.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Z-Image Base is Alibaba's 6B open text-to-image model: photorealistic results and bilingual text rendering at a low per-image cost.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.01 per image.

| Request | Price |
|---|---|
| One image | $0.01 |

Failed runs are not charged.

### Prompting

- Write subject, setting, style, then light and color.
- Quote text that must appear.

### Limits

- One image per request.

### Also on SandBase

Related: `alibaba/z-image/turbo/edit`, `z-image/turbo`.

---
Machine-readable: [`catalog/models/alibaba/z-image/base.json`](../../../../catalog/models/alibaba/z-image/base.json) · Store page: https://www.sandbase.ai/model/alibaba/z-image/base
