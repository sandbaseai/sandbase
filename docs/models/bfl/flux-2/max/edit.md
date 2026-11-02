# Flux 2 Max Edit API: pricing, parameters and code examples

`bfl/flux-2/max/edit` · image generation model · BFL · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.1 per call · **Modes:** async

Flux 2 Max Edit is BFL's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts - from background replacement to artistic style conversion.

## Pricing

- **$0.1 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/max/edit", "prompt": "A red fox in a snowy forest at sunrise, photorealistic"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/max/edit', {'prompt': 'A red fox in a snowy forest at sunrise, photorealistic'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/max/edit", {
  "prompt": "A red fox in a snowy forest at sunrise, photorealistic"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/max/edit", sandbase.Params{
	"prompt": "A red fox in a snowy forest at sunrise, photorealistic",
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

## Details

FLUX.2 [max], BFL's highest-quality FLUX.2 tier, with the best prompt following and detail. Edit or combine images with an instruction.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Images to edit or combine, Image 1, Image 2, … |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.10 per image.

| Request | Price |
|---|---|
| One image | $0.10 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX.2 endpoints: `bfl/flux-2/pro/edit`, `bfl/flux-2/flex/edit`, `bfl/flux-2/dev/edit`, `bfl/flux-2/turbo/edit`, `bfl/flux-2/max`.

---
Machine-readable: [`catalog/models/bfl/flux-2/max/edit.json`](../../../../../catalog/models/bfl/flux-2/max/edit.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/max/edit
