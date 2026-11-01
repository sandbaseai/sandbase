# Flux 2 Klein 4B Edit

`bfl/flux-2/klein/4b/edit` · image · BFL

Flux 2 Klein 4b by BFL - AI-powered image editing, style transfer, and transformation. Edit photos with natural language instructions, remove backgrounds, change styles, and enhance images effortlessly.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/klein/4b/edit", "prompt": "Turn this into a realistic image"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/klein/4b/edit', {'prompt': 'Turn this into a realistic image'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/klein/4b/edit", {
  "prompt": "Turn this into a realistic image"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/klein/4b/edit", sandbase.Params{
	"prompt": "Turn this into a realistic image",
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
| `images` | array |  | The URLs of the images for editing. A maximum of 4 images are allowed.  |
| `prompt` | string | yes | The prompt to edit the image.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |
| `num_inference_steps` | integer |  | The number of inference steps to perform. default `4`; range 4–8 |

## Details

FLUX.2 [klein] 4B, the smallest FLUX.2 model, built for speed. Edit or combine images with an instruction.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Images to edit or combine, Image 1, Image 2, … |
| `num_inference_steps` | integer 4–8 | 4 | More steps add detail and time. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.02 per image.

| Request | Price |
|---|---|
| One image | $0.02 |

Failed runs are not charged.

### Prompting

- Say which image is the base and what each other image contributes.
- List what must not change.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX.2 endpoints: `bfl/flux-2/max/edit`, `bfl/flux-2/pro/edit`, `bfl/flux-2/flex/edit`, `bfl/flux-2/dev/edit`, `bfl/flux-2/klein/4b`.

---
Machine-readable: [`catalog/models/bfl/flux-2/klein/4b/edit.json`](../../../../../../catalog/models/bfl/flux-2/klein/4b/edit.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/klein/4b/edit
