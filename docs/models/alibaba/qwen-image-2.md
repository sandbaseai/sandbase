# Qwen Image 2 API: pricing, parameters and code examples

`alibaba/qwen-image-2` · image generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.035 per run, depending on parameters · **Modes:** async

Alibaba Qwen Image 2 text-to-image model with high-quality generation and configurable output format.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.035 |

Formula: `0.035`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen-image-2", "prompt": "A red fox in a snowy forest at sunrise, photorealistic"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/qwen-image-2', {'prompt': 'A red fox in a snowy forest at sunrise, photorealistic'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/qwen-image-2", {
  "prompt": "A red fox in a snowy forest at sunrise, photorealistic"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/qwen-image-2", sandbase.Params{
	"prompt": "A red fox in a snowy forest at sunrise, photorealistic",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible results.  |
| `prompt` | string | yes | The prompt to generate an image from.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21`; default `"16:9"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Qwen Image 2 text-to-image, with strong Chinese and English text rendering for posters and graphics. Qwen Image 3 is the newer model.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 10,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `9:21` | `16:9` | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |

### Billing

$0.035 per image, Alibaba's list price.

| Request | Price |
|---|---|
| One image | $0.035 |

Failed runs are not charged.

### Prompting

- Quote any text that must appear in the image.

### Limits

- One image per request.

### Also on SandBase

Related: `alibaba/qwen-image-3/text-to-image` (newer).

---
Machine-readable: [`catalog/models/alibaba/qwen-image-2.json`](../../../catalog/models/alibaba/qwen-image-2.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen-image-2
