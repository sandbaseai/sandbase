# Flux 2 Flash Text to Image API: pricing, parameters and code examples

`bfl/flux-2/flash` · image generation model · BFL · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.025 per run, depending on parameters · **Modes:** async

Flux 2 Flash by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.025 |

Formula: `0.025`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/flash", "prompt": "An army of ants battles for a sugar cube in a giant sandbox, with tiny plastic soldier toys caught in the melee. Ant bodies shine against gritty beige sand and the glossy, crystalline cube. Fiery sunrise spills golden highlights, throwing dramatic shadows, amplifying the excitement. Shot macro (100mm), aperture f/2.8 for soft background, centered composition with ground-level POV, mixing organic and manufactured textures."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/flash', {'prompt': 'An army of ants battles for a sugar cube in a giant sandbox, with tiny plastic soldier toys caught in the melee. Ant bodies shine against gritty beige sand and the glossy, crystalline cube. Fiery sunrise spills golden highlights, throwing dramatic shadows, amplifying the excitement. Shot macro (100mm), aperture f/2.8 for soft background, centered composition with ground-level POV, mixing organic and manufactured textures.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/flash", {
  "prompt": "An army of ants battles for a sugar cube in a giant sandbox, with tiny plastic soldier toys caught in the melee. Ant bodies shine against gritty beige sand and the glossy, crystalline cube. Fiery sunrise spills golden highlights, throwing dramatic shadows, amplifying the excitement. Shot macro (100mm), aperture f/2.8 for soft background, centered composition with ground-level POV, mixing organic and manufactured textures."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/flash", sandbase.Params{
	"prompt": "An army of ants battles for a sugar cube in a giant sandbox, with tiny plastic soldier toys caught in the melee. Ant bodies shine against gritty beige sand and the glossy, crystalline cube. Fiery sunrise spills golden highlights, throwing dramatic shadows, amplifying the excitement. Shot macro (100mm), aperture f/2.8 for soft background, centered composition with ground-level POV, mixing organic and manufactured textures.",
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

FLUX.2 Flash, the fastest, lowest-cost FLUX.2 variant. Text to image.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `guidance_scale` | number 0–20 | 2.5 | How strictly to follow the prompt. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.025 per image.

| Request | Price |
|---|---|
| One image | $0.025 |

Failed runs are not charged.

### Prompting

- Write subject, setting, composition, style, then light.
- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX.2 endpoints: `bfl/flux-2/max`, `bfl/flux-2/pro`, `bfl/flux-2/flex`, `bfl/flux-2/dev`, `bfl/flux-2/flash/edit`.

---
Machine-readable: [`catalog/models/bfl/flux-2/flash.json`](../../../../catalog/models/bfl/flux-2/flash.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/flash
