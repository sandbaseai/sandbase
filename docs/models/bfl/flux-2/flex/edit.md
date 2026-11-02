# Flux 2 Flex Edit API: pricing, parameters and code examples

`bfl/flux-2/flex/edit` · image generation model · BFL · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.12 per call · **Modes:** async

Flux 2 Flex Edit by BFL - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- **$0.12 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/flex/edit", "prompt": "Change colors of the vase. In a cozy living room setting, visualize a gradient vase placed on a table, flowing from rich #6a0dad to soft #ff69b4. Add an artistic carving text with a big font on vase says \"FLEX\" in the middle."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/flex/edit', {'prompt': 'Change colors of the vase. In a cozy living room setting, visualize a gradient vase placed on a table, flowing from rich #6a0dad to soft #ff69b4. Add an artistic carving text with a big font on vase says "FLEX" in the middle.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/flex/edit", {
  "prompt": "Change colors of the vase. In a cozy living room setting, visualize a gradient vase placed on a table, flowing from rich #6a0dad to soft #ff69b4. Add an artistic carving text with a big font on vase says \"FLEX\" in the middle."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/flex/edit", sandbase.Params{
	"prompt": "Change colors of the vase. In a cozy living room setting, visualize a gradient vase placed on a table, flowing from rich #6a0dad to soft #ff69b4. Add an artistic carving text with a big font on vase says \"FLEX\" in the middle.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The seed to use for the generation.  |
| `images` | array |  | List of URLs of input images for editing  |
| `prompt` | string | yes | The prompt to generate an image from.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"jpeg"` |
| `guidance_scale` | number |  | The guidance scale to use for the generation. default `3.5`; range 1.5–10 |
| `num_inference_steps` | integer |  | The number of inference steps to perform. default `28`; range 2–50 |

## Details

FLUX.2 [flex], the tunable tier: adjust steps and guidance for typography-heavy or detailed work. Edit or combine images with an instruction.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Images to edit or combine, Image 1, Image 2, … |
| `guidance_scale` | number 1.5–10 | 3.5 | How strictly to follow the prompt. |
| `num_inference_steps` | integer 2–50 | 28 | More steps add detail and time. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.12 per image.

| Request | Price |
|---|---|
| One image | $0.12 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX.2 endpoints: `bfl/flux-2/max/edit`, `bfl/flux-2/pro/edit`, `bfl/flux-2/dev/edit`, `bfl/flux-2/turbo/edit`, `bfl/flux-2/flex`.

---
Machine-readable: [`catalog/models/bfl/flux-2/flex/edit.json`](../../../../../catalog/models/bfl/flux-2/flex/edit.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/flex/edit
