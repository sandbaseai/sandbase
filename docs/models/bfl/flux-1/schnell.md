# Flux 1 Schnell API: pricing, parameters and code examples

`bfl/flux-1/schnell` · image generation model · BFL · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call · **Modes:** async

Flux 1 Schnell by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- **$0.003 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-1/schnell", "aspect_ratio": "1:1", "num_inference_steps": 1, "output_format": "jpeg", "prompt": "A simple blue circle centered on a white background. QA test.", "seed": 20261006}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-1/schnell', {'aspect_ratio': '1:1', 'num_inference_steps': 1, 'output_format': 'jpeg', 'prompt': 'A simple blue circle centered on a white background. QA test.', 'seed': 20261006})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-1/schnell", {
  "aspect_ratio": "1:1",
  "num_inference_steps": 1,
  "output_format": "jpeg",
  "prompt": "A simple blue circle centered on a white background. QA test.",
  "seed": 20261006
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-1/schnell", sandbase.Params{
	"aspect_ratio": "1:1",
	"num_inference_steps": 1,
	"output_format": "jpeg",
	"prompt": "A simple blue circle centered on a white background. QA test.",
	"seed": 20261006,
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
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"16:9"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"jpeg"` |
| `guidance_scale` | number |  | The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you. default `3.5`; range 1–20 |
| `num_inference_steps` | integer |  | The number of inference steps to perform. default `4`; range 1–12 |

## Details

FLUX.1 [schnell] generates an image in 1–4 steps, the cheapest FLUX option for quick drafts.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output shape. |
| `guidance_scale` | number 1–20 | 3.5 | How strictly to follow the prompt. |
| `num_inference_steps` | integer 1–12 | 4 | More steps add detail and time. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.003 per image.

| Request | Price |
|---|---|
| One image | $0.003 |

Failed runs are not charged.

### Prompting

- Keep prompts short and concrete.

### Limits

- One image per request.

### Also on SandBase

Related: `bfl/flux-2/klein/4b` (newer, fast).

---
Machine-readable: [`catalog/models/bfl/flux-1/schnell.json`](../../../../catalog/models/bfl/flux-1/schnell.json) · Store page: https://www.sandbase.ai/model/bfl/flux-1/schnell
