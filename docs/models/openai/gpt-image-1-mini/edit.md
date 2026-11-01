# GPT Image 1 Mini Edit

`openai/gpt-image-1-mini/edit` · image · OpenAI

Gpt Image 1 Mini Edit is OpenAI's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from background replacement to artistic style conversion.

## Pricing

- Depends on parameters (`params.aspect_ratio`, `params.prompt`, `params.quality`).

| parameters | USD |
|---|---|
| aspect_ratio="1:1", quality="auto" | 0.038 |
| aspect_ratio="1:1", quality="low" | 0.007 |
| aspect_ratio="1:1", quality="medium" | 0.013 |
| aspect_ratio="1:1", quality="high" | 0.038 |
| aspect_ratio="3:2", quality="auto" | 0.054 |
| aspect_ratio="3:2", quality="low" | 0.008 |
| aspect_ratio="3:2", quality="medium" | 0.017 |
| aspect_ratio="3:2", quality="high" | 0.054 |
| aspect_ratio="2:3", quality="auto" | 0.054 |
| aspect_ratio="2:3", quality="low" | 0.008 |
| aspect_ratio="2:3", quality="medium" | 0.017 |
| aspect_ratio="2:3", quality="high" | 0.054 |

Formula: `Math.ceil(len(params.prompt ?? "") / 1000) * 0.002 + ((params.quality ?? "auto") == "low" ? ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.005 : 0.006) : (params.quality ?? "auto") == "medium" ? ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.011 : 0.015) : ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.036 : 0.052))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-image-1-mini/edit", "aspect_ratio": "1:1", "images": ["https://static.sandbase.ai/examples/e4b5996b-021e-4360-bd2f-959dbdf45f4b/input/5c513255-9c78-4e10-a29a-358eb27f85e4.jpg"], "prompt": "make it watercolor", "quality": "low"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('openai/gpt-image-1-mini/edit', {'aspect_ratio': '1:1', 'images': ['https://static.sandbase.ai/examples/e4b5996b-021e-4360-bd2f-959dbdf45f4b/input/5c513255-9c78-4e10-a29a-358eb27f85e4.jpg'], 'prompt': 'make it watercolor', 'quality': 'low'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("openai/gpt-image-1-mini/edit", {
  "aspect_ratio": "1:1",
  "images": [
    "https://static.sandbase.ai/examples/e4b5996b-021e-4360-bd2f-959dbdf45f4b/input/5c513255-9c78-4e10-a29a-358eb27f85e4.jpg"
  ],
  "prompt": "make it watercolor",
  "quality": "low"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "openai/gpt-image-1-mini/edit", sandbase.Params{
	"aspect_ratio": "1:1",
	"images": []any{"https://static.sandbase.ai/examples/e4b5996b-021e-4360-bd2f-959dbdf45f4b/input/5c513255-9c78-4e10-a29a-358eb27f85e4.jpg"},
	"prompt": "make it watercolor",
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
| `images` | array |  | The URLs of the images to use as a reference for the generation.  |
| `prompt` | string | yes | The prompt for image generation  |
| `quality` | string |  | Quality for the generated image one of: `auto`, `low`, `medium`, `high`; default `"auto"` |
| `background` | string |  | Background for the generated image one of: `auto`, `transparent`, `opaque`; default `"auto"` |
| `aspect_ratio` | string |  | Output aspect ratio: 1:1 (1024x1024), 3:2 (1536x1024) or 2:3 (1024x1536). one of: `1:1`, `3:2`, `2:3`; default `"1:1"` |
| `output_format` | string |  | Output format for the images one of: `jpeg`, `png`; default `"png"` |

## Details

GPT Image 1 Mini edit: the low-cost GPT Image tier for quick edits and background swaps.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Images to edit, Image 1, Image 2, … |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `background` | `auto` / `transparent` / `opaque` | `auto` | `transparent` returns a PNG with alpha. |
| `quality` | `auto` / `low` / `medium` / `high` | `auto` | `auto` lets the model pick; billed as high. |
| `aspect_ratio` | `1:1` / `3:2` / `2:3` | `1:1` | 1:1, 3:2, or 2:3; non-square sizes cost more. |

### Billing

Price depends on quality and shape, plus $0.002 per started 1,000 prompt characters:

| Quality, short prompt | 1:1 | 3:2 or 2:3 |
|---|---|---|
| low | $0.007 | $0.008 |
| medium | $0.013 | $0.017 |
| high | $0.038 | $0.054 |

Failed runs are not charged.

### Prompting

- State the change and what must stay the same.

### Limits

- Three shapes only: 1:1, 3:2, 2:3.

### Also on SandBase

Related: `openai/gpt-image-2/edit` (higher quality).

---
Machine-readable: [`catalog/models/openai/gpt-image-1-mini/edit.json`](../../../../catalog/models/openai/gpt-image-1-mini/edit.json) · Store page: https://www.sandbase.ai/model/openai/gpt-image-1-mini/edit
