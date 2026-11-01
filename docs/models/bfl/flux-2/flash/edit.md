# Flux 2 Flash Edit

`bfl/flux-2/flash/edit` · image · BFL

Flux 2 Flash Edit is BFL's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from background replacement to artistic style conversion.

## Pricing

- Depends on parameters (`params.images`).

| parameters | USD |
|---|---|
| defaults | 0.03 |

Formula: `0.03 + Math.max(0.0, len(params.images ?? []) - 1.0) * 0.005`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/flash/edit", "prompt": "Remove the meat from the hamburger"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/flash/edit', {'prompt': 'Remove the meat from the hamburger'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/flash/edit", {
  "prompt": "Remove the meat from the hamburger"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/flash/edit", sandbase.Params{
	"prompt": "Remove the meat from the hamburger",
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
| `images` | array |  | The URLs of the images for editing. A maximum of 4 images are allowed, if more are provided, only the first 4 will be used.  |
| `prompt` | string | yes | The prompt to edit the image.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `guidance_scale` | number |  | Guidance Scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you. default `2.5`; range 0–20 |

## Details

FLUX.2 Flash, the fastest, lowest-cost FLUX.2 variant. Edit or combine images with an instruction.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Images to edit or combine, Image 1, Image 2, … |
| `guidance_scale` | number 0–20 | 2.5 | How strictly to follow the prompt. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.03 per output image, plus $0.005 for each input image after the first.

| Inputs | Price |
|---|---|
| 1 input image | $0.03 |
| 2 input images | $0.035 |
| 4 input images | $0.045 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX.2 endpoints: `bfl/flux-2/max/edit`, `bfl/flux-2/pro/edit`, `bfl/flux-2/flex/edit`, `bfl/flux-2/dev/edit`, `bfl/flux-2/flash`.

---
Machine-readable: [`catalog/models/bfl/flux-2/flash/edit.json`](../../../../../catalog/models/bfl/flux-2/flash/edit.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/flash/edit
