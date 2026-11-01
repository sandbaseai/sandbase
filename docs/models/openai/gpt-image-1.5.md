# GPT Image 1.5 Text to Image

`openai/gpt-image-1.5` · image · OpenAI

Gpt Image 1.5 is OpenAI's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural language descriptions with exceptional detail and prompt adherence.

## Pricing

- Depends on parameters (`params.aspect_ratio`, `params.prompt`, `params.quality`).

| parameters | USD |
|---|---|
| aspect_ratio="1:1", quality="low" | 0.014 |
| aspect_ratio="1:1", quality="medium" | 0.039 |
| aspect_ratio="1:1", quality="high" | 0.138 |
| aspect_ratio="3:2", quality="low" | 0.018 |
| aspect_ratio="3:2", quality="medium" | 0.056 |
| aspect_ratio="3:2", quality="high" | 0.205 |
| aspect_ratio="2:3", quality="low" | 0.018 |
| aspect_ratio="2:3", quality="medium" | 0.056 |
| aspect_ratio="2:3", quality="high" | 0.205 |

Formula: `Math.ceil(len(params.prompt ?? "") / 1000) * 0.005 + ((params.quality ?? "high") == "low" ? ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.009 : 0.013) : (params.quality ?? "high") == "medium" ? ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.034 : 0.051) : ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.133 : 0.200))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-image-1.5", "aspect_ratio": "1:1", "prompt": "a red apple on a white table, studio light", "quality": "low"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('openai/gpt-image-1.5', {'aspect_ratio': '1:1', 'prompt': 'a red apple on a white table, studio light', 'quality': 'low'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("openai/gpt-image-1.5", {
  "aspect_ratio": "1:1",
  "prompt": "a red apple on a white table, studio light",
  "quality": "low"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "openai/gpt-image-1.5", sandbase.Params{
	"aspect_ratio": "1:1",
	"prompt": "a red apple on a white table, studio light",
	"quality": "low",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The prompt for image generation  |
| `quality` | string |  | Quality for the generated image one of: `low`, `medium`, `high`; default `"high"` |
| `background` | string |  | Background for the generated image one of: `auto`, `transparent`, `opaque`; default `"auto"` |
| `aspect_ratio` | string |  | Output aspect ratio: 1:1 (1024x1024), 3:2 (1536x1024) or 2:3 (1024x1536). one of: `1:1`, `3:2`, `2:3`; default `"1:1"` |
| `output_format` | string |  | Output format for the images one of: `jpeg`, `png`; default `"png"` |

## Details

GPT Image 1.5 text-to-image, with transparent-background output for logos and stickers.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 32,000 characters. |
| `aspect_ratio` | `1:1` / `3:2` / `2:3` | `1:1` | 1:1, 3:2, or 2:3; non-square sizes cost more. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `background` | `auto` / `transparent` / `opaque` | `auto` | `transparent` returns a PNG with alpha. |
| `quality` | `low` / `medium` / `high` | `high` | Higher quality costs more; `high` is the default. |

### Billing

Price depends on quality and shape, plus $0.005 per started 1,000 prompt characters:

| Quality, short prompt | 1:1 | 3:2 or 2:3 |
|---|---|---|
| low | $0.014 | $0.018 |
| medium | $0.039 | $0.056 |
| high | $0.138 | $0.205 |

Failed runs are not charged.

### Prompting

- Use `background: transparent` with PNG output for cut-out assets.

### Limits

- Three shapes only: 1:1, 3:2, 2:3.

### Also on SandBase

Related: `openai/gpt-image-1.5/edit`, `openai/gpt-image-2` (newer).

---
Machine-readable: [`catalog/models/openai/gpt-image-1.5.json`](../../../catalog/models/openai/gpt-image-1.5.json) · Store page: https://www.sandbase.ai/model/openai/gpt-image-1.5
