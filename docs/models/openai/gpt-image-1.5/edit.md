# GPT Image 1.5 Edit

`openai/gpt-image-1.5/edit` · image · OpenAI

Gpt Image 1.5 Edit by OpenAI - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- Depends on parameters (`params.aspect_ratio`, `params.quality`).

| parameters | USD |
|---|---|
| aspect_ratio="1:1", quality="low" | 0.009 |
| aspect_ratio="1:1", quality="medium" | 0.034 |
| aspect_ratio="1:1", quality="high" | 0.133 |
| aspect_ratio="2:3", quality="low" | 0.013 |
| aspect_ratio="2:3", quality="medium" | 0.051 |
| aspect_ratio="2:3", quality="high" | 0.2 |
| aspect_ratio="3:2", quality="low" | 0.013 |
| aspect_ratio="3:2", quality="medium" | 0.051 |
| aspect_ratio="3:2", quality="high" | 0.2 |

Formula: `(params.quality ?? "high") == "low" ? ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.009 : 0.013) : (params.quality ?? "high") == "medium" ? ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.034 : 0.051) : ((params.aspect_ratio ?? "1:1") == "1:1" ? 0.133 : 0.200)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-image-1.5/edit", "prompt": "Same workers, same beam, same lunch boxes - but they'\''re all on their phones now. One is taking a selfie. One is on a call looking annoyed. Same danger, new priorities. A hard hat has AirPods."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('openai/gpt-image-1.5/edit', {'prompt': "Same workers, same beam, same lunch boxes - but they're all on their phones now. One is taking a selfie. One is on a call looking annoyed. Same danger, new priorities. A hard hat has AirPods."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("openai/gpt-image-1.5/edit", {
  "prompt": "Same workers, same beam, same lunch boxes - but they're all on their phones now. One is taking a selfie. One is on a call looking annoyed. Same danger, new priorities. A hard hat has AirPods."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "openai/gpt-image-1.5/edit", sandbase.Params{
	"prompt": "Same workers, same beam, same lunch boxes - but they're all on their phones now. One is taking a selfie. One is on a call looking annoyed. Same danger, new priorities. A hard hat has AirPods.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mask` | string |  | The URL of the mask image to use for the generation. This indicates what part of the image to edit.  |
| `images` | array |  | The URLs of the images to use as a reference for the generation.  |
| `prompt` | string | yes | The prompt for image generation  |
| `quality` | string |  | Quality for the generated image one of: `low`, `medium`, `high`; default `"high"` |
| `background` | string |  | Background for the generated image one of: `auto`, `transparent`, `opaque`; default `"auto"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `1:1`, `2:3`, `3:2` |
| `output_format` | string |  | Output format for the images one of: `jpeg`, `png`; default `"png"` |
| `input_fidelity` | string |  | Input fidelity for the generated image one of: `low`, `high`; default `"high"` |

## Details

GPT Image 1.5 edit: change images with an instruction, with an optional mask for local edits and `input_fidelity` to keep faces and logos close to the original.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 32,000 characters. |
| `images` | image URL[] | — | Images to edit, Image 1, Image 2, … |
| `mask` | image URL | — | Optional PNG mask; transparent areas are edited. |
| `aspect_ratio` | `1:1` / `2:3` / `3:2` | — | 1:1, 3:2, or 2:3; non-square sizes cost more. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `input_fidelity` | `low` / `high` | `high` | `high` preserves faces and logos more closely. |
| `quality` | `low` / `medium` / `high` | `high` | Higher quality costs more; `high` is the default. |
| `background` | `auto` / `transparent` / `opaque` | `auto` | `transparent` returns a PNG with alpha. |

### Billing

Price depends on quality and shape, per output image:

| Quality | 1:1 | 3:2 or 2:3 |
|---|---|---|
| low | $0.009 | $0.013 |
| medium | $0.034 | $0.051 |
| high | $0.133 | $0.20 |

Failed runs are not charged.

### Prompting

- Use a mask when only one region should change.

### Limits

- Three shapes only: 1:1, 3:2, 2:3.

### Also on SandBase

Related: `openai/gpt-image-1.5`, `openai/gpt-image-2/edit` (newer).

---
Machine-readable: [`catalog/models/openai/gpt-image-1.5/edit.json`](../../../../catalog/models/openai/gpt-image-1.5/edit.json) · Store page: https://www.sandbase.ai/model/openai/gpt-image-1.5/edit
