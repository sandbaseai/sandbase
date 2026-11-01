# Flux 2 Turbo Text to Image

`bfl/flux-2/turbo` · image · BFL

Flux 2 Turbo by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- **$0.04 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/turbo", "prompt": "A realistic photograph of a vintage typewriter with a sheet of paper inserted that says '\''Chapter One: The Journey Begins,'\'' sunlight falling across the desk."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/turbo', {'prompt': "A realistic photograph of a vintage typewriter with a sheet of paper inserted that says 'Chapter One: The Journey Begins,' sunlight falling across the desk."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/turbo", {
  "prompt": "A realistic photograph of a vintage typewriter with a sheet of paper inserted that says 'Chapter One: The Journey Begins,' sunlight falling across the desk."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/turbo", sandbase.Params{
	"prompt": "A realistic photograph of a vintage typewriter with a sheet of paper inserted that says 'Chapter One: The Journey Begins,' sunlight falling across the desk.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The seed to use for the generation. If not provided, a random seed will be used.  |
| `prompt` | string | yes | The prompt to generate an image from.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"16:9"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `guidance_scale` | number |  | Guidance Scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you. default `2.5`; range 0–20 |

## Details

FLUX.2 Turbo, a distilled FLUX.2 for fast generation. Text to image.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `guidance_scale` | number 0–20 | 2.5 | How strictly to follow the prompt. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.04 per image.

| Request | Price |
|---|---|
| One image | $0.04 |

Failed runs are not charged.

### Prompting

- Write subject, setting, composition, style, then light.
- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX.2 endpoints: `bfl/flux-2/max`, `bfl/flux-2/pro`, `bfl/flux-2/flex`, `bfl/flux-2/dev`, `bfl/flux-2/turbo/edit`.

---
Machine-readable: [`catalog/models/bfl/flux-2/turbo.json`](../../../../catalog/models/bfl/flux-2/turbo.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/turbo
