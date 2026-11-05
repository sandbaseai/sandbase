# GPT Image 2.6 Flare Edit API: pricing, parameters and code examples

`openai/gpt-image-2.6-flare/edit` · image generation model · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.025 to $0.285 per run, depending on parameters · **Modes:** sync, async

GPT Image 2.6 Flare Edit is optimized for fast, high-quality image editing and multi-image composition.

## Pricing

- Depends on parameters (`params.images`, `params.quality`, `params.resolution`).

| parameters | USD |
|---|---|
| quality="low", resolution="1k" | 0.025 |
| quality="low", resolution="2k" | 0.035 |
| quality="low", resolution="4k" | 0.045 |
| quality="medium", resolution="1k" | 0.039 |
| quality="medium", resolution="2k" | 0.055 |
| quality="medium", resolution="4k" | 0.085 |
| quality="high", resolution="1k" | 0.105 |
| quality="high", resolution="2k" | 0.165 |
| quality="high", resolution="4k" | 0.285 |

Formula: see the JSON record.

## Call it

Modes: sync, async (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-image-2.6-flare/edit", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/0de9d081-6109-4bf2-908c-fce8cad00373/input/4da5ba0b-d3ae-435c-846b-690644bf60b7.png"], "prompt": "Create a realistic billboard mockup of the shampoo on a highway scene during sunset.\nBillboard text (EXACT, verbatim, no extra characters):\n\"Fresh and clean\"\nTypography: bold sans-serif, high contrast, centered, clean kerning.\nEnsure text appears once and is perfectly legible.\nNo watermarks, no logos."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('openai/gpt-image-2.6-flare/edit', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/0de9d081-6109-4bf2-908c-fce8cad00373/input/4da5ba0b-d3ae-435c-846b-690644bf60b7.png'], 'prompt': 'Create a realistic billboard mockup of the shampoo on a highway scene during sunset.\nBillboard text (EXACT, verbatim, no extra characters):\n"Fresh and clean"\nTypography: bold sans-serif, high contrast, centered, clean kerning.\nEnsure text appears once and is perfectly legible.\nNo watermarks, no logos.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("openai/gpt-image-2.6-flare/edit", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/0de9d081-6109-4bf2-908c-fce8cad00373/input/4da5ba0b-d3ae-435c-846b-690644bf60b7.png"
  ],
  "prompt": "Create a realistic billboard mockup of the shampoo on a highway scene during sunset.\nBillboard text (EXACT, verbatim, no extra characters):\n\"Fresh and clean\"\nTypography: bold sans-serif, high contrast, centered, clean kerning.\nEnsure text appears once and is perfectly legible.\nNo watermarks, no logos."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "openai/gpt-image-2.6-flare/edit", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/0de9d081-6109-4bf2-908c-fce8cad00373/input/4da5ba0b-d3ae-435c-846b-690644bf60b7.png"},
	"prompt": "Create a realistic billboard mockup of the shampoo on a highway scene during sunset.\nBillboard text (EXACT, verbatim, no extra characters):\n\"Fresh and clean\"\nTypography: bold sans-serif, high contrast, centered, clean kerning.\nEnsure text appears once and is perfectly legible.\nNo watermarks, no logos.",
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
| `prompt` | string | yes | The text prompt to generate an image from. default `"Generate a photorealistic image of a gift basket on a white background labeled 'Relax & Unwind' with a ribbon and handwriting-like font, containing all the items in the reference pictures."` |
| `quality` | string |  | Rendering quality. Higher quality adds detail at higher latency and cost. one of: `low`, `medium`, `high`; default `"high"` |
| `resolution` | string |  | The resolution of the generated image. Leave unset to preserve the provider's standard dimensions. one of: `1k`, `2k`, `4k` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `1:1`, `1:2`, `2:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `9:21` … |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`, `webp`; default `"png"` |

## Details

GPT Image 2.6 Flare edit: fast edits and multi-image composition with GPT Image 2.6.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URL[], required | — | Images to edit or combine, Image 1, Image 2, … |
| `prompt` | string, required | — | Up to 32,000 characters. |
| `quality` | `low` / `medium` / `high` | `high` | Higher quality costs more; `high` is the default. |
| `resolution` | `1k` / `2k` / `4k` | — | Output size tier; omit for 1K. |
| `aspect_ratio` | `1:1` / `1:2` / `2:1` / `2:3` / `3:2` / `3:4` / `4:3` / `4:5` / `5:4` / `9:16` / `16:9` / `9:21` / `21:9` | — | Omit to follow the first input image. |
| `output_format` | `jpeg` / `png` / `webp` | `png` | Output file format. |

### Billing

Price depends on quality and resolution, per output image, plus $0.015 for each input image after the first:

| Quality, 1 input | 1k | 2k | 4k |
|---|---|---|---|
| low | $0.025 | $0.035 | $0.045 |
| medium | $0.039 | $0.055 | $0.085 |
| high (default) | $0.105 | $0.165 | $0.285 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image adds.
- List what must not change.

### Limits

- One output image per request.
- Up to 16 input images.

### Also on SandBase

Other GPT Image endpoints: `openai/gpt-image-2.6-flare`, `openai/gpt-image-2.6-sunburst`, `openai/gpt-image-2.6-sunburst/edit`, `openai/gpt-image-2.5-flare`, `openai/gpt-image-2.5-sunburst`.

---
Machine-readable: [`catalog/models/openai/gpt-image-2.6-flare/edit.json`](../../../../catalog/models/openai/gpt-image-2.6-flare/edit.json) · Store page: https://www.sandbase.ai/model/openai/gpt-image-2.6-flare/edit
