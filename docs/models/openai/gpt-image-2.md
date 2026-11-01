# GPT Image 2 Text to Image

`openai/gpt-image-2` · image · OpenAI

GPT Image 2, OpenAI's latest image model, is capable of making fine-grained, detailed edits to images.

## Pricing

- Depends on parameters (`params.quality`, `params.resolution`).

| parameters | USD |
|---|---|
| quality="low", resolution="1k" | 0.01 |
| quality="low", resolution="2k" | 0.02 |
| quality="low", resolution="4k" | 0.03 |
| quality="medium", resolution="1k" | 0.06 |
| quality="medium", resolution="2k" | 0.1 |
| quality="medium", resolution="4k" | 0.18 |
| quality="high", resolution="1k" | 0.22 |
| quality="high", resolution="2k" | 0.4 |
| quality="high", resolution="4k" | 0.72 |

Formula: `((params.quality ?? "high") == "low" ? ((params.resolution ?? "1k") == "4k" ? 0.03 : (params.resolution ?? "1k") == "2k" ? 0.02 : 0.01) : ((params.quality ?? "high") == "medium" ? ((params.resolution ?? "1k") == "4k" ? 0.18 : (params.resolution ?? "1k") == "2k" ? 0.1 : 0.06) : ((params.resolution ?? "1k") == "4k" ? 0.72 : (params.resolution ?? "1k") == "2k" ? 0.4 : 0.22)))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-image-2", "aspect_ratio": "16:9", "prompt": "Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.\nHe has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.\nHe is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.\nSoft coastal daylight, shallow depth of field, subtle film grain, natural color balance.\nThe image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching."}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('openai/gpt-image-2', {'aspect_ratio': '16:9', 'prompt': 'Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.\nHe has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.\nHe is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.\nSoft coastal daylight, shallow depth of field, subtle film grain, natural color balance.\nThe image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("openai/gpt-image-2", {
  "aspect_ratio": "16:9",
  "prompt": "Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.\nHe has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.\nHe is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.\nSoft coastal daylight, shallow depth of field, subtle film grain, natural color balance.\nThe image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "openai/gpt-image-2", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.\nHe has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.\nHe is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.\nSoft coastal daylight, shallow depth of field, subtle film grain, natural color balance.\nThe image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt to generate an image from. default `"Generate an image of gray tabby cat hugging an otter with an orange scarf"` |
| `quality` | string |  | Quality for the generated image one of: `low`, `medium`, `high`; default `"high"` |
| `resolution` | string |  | The resolution of the generated image. Leave unset to preserve the provider's standard dimensions. one of: `1k`, `2k`, `4k` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `1:1`, `1:2`, `2:1`, `1:3`, `3:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16` …; default `"1:1"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`, `webp`; default `"png"` |

## Details

GPT Image 2 generates detailed images with strong instruction following and accurate in-image text, at three quality levels and 1K to 4K.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `quality` | `low` / `medium` / `high` | `high` | Higher quality costs more; `high` is the default. |
| `resolution` | `1k` / `2k` / `4k` | — | Output size tier; omit for 1K. |
| `aspect_ratio` | `1:1` / `1:2` / `2:1` / `1:3` / `3:1` / `2:3` / `3:2` / `3:4` / `4:3` / `4:5` / `5:4` / `9:16` / `16:9` / `9:21` / `21:9` | `1:1` | Output frame shape. |
| `output_format` | `jpeg` / `png` / `webp` | `png` | Output file format. |

### Billing

Price depends on quality and resolution, per image:

| Quality | 1k | 2k | 4k |
|---|---|---|---|
| low | $0.01 | $0.02 | $0.03 |
| medium | $0.06 | $0.10 | $0.18 |
| high (default) | $0.22 | $0.40 | $0.72 |

Failed runs are not charged.

### Prompting

- Quote any text that must appear.
- Draft at `low`, finish at `high`.

### Limits

- One image per request.

### Also on SandBase

Other GPT Image endpoints: `openai/gpt-image-2.5-sunburst`, `openai/gpt-image-2.5-sunburst/edit`, `openai/gpt-image-2.5-flare`, `openai/gpt-image-2.5-flare/edit`, `openai/gpt-image-2/edit`.

---
Machine-readable: [`catalog/models/openai/gpt-image-2.json`](../../../catalog/models/openai/gpt-image-2.json) · Store page: https://www.sandbase.ai/model/openai/gpt-image-2
