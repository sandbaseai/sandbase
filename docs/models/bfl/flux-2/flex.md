# Flux 2 Flex Text to Image

`bfl/flux-2/flex` · image · BFL

Flux 2 Flex is BFL's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural language descriptions with exceptional detail and prompt adherence.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.06 |

Formula: `0.06`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/flex", "prompt": "A high-quality 3D render of a cute fluffy monster eating a giant donut; the fur simulation is incredibly detailed, the donut glaze is sticky and reflective, bright daylight lighting, shallow depth of field."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/flex', {'prompt': 'A high-quality 3D render of a cute fluffy monster eating a giant donut; the fur simulation is incredibly detailed, the donut glaze is sticky and reflective, bright daylight lighting, shallow depth of field.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/flex", {
  "prompt": "A high-quality 3D render of a cute fluffy monster eating a giant donut; the fur simulation is incredibly detailed, the donut glaze is sticky and reflective, bright daylight lighting, shallow depth of field."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/flex", sandbase.Params{
	"prompt": "A high-quality 3D render of a cute fluffy monster eating a giant donut; the fur simulation is incredibly detailed, the donut glaze is sticky and reflective, bright daylight lighting, shallow depth of field.",
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
| `prompt` | string | yes | The prompt to generate an image from.  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"16:9"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"jpeg"` |
| `guidance_scale` | number |  | The guidance scale to use for the generation. default `3.5`; range 1.5–10 |
| `num_inference_steps` | integer |  | The number of inference steps to perform. default `28`; range 2–50 |

## Details

FLUX.2 [flex], the tunable tier: adjust steps and guidance for typography-heavy or detailed work. Text to image.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `guidance_scale` | number 1.5–10 | 3.5 | How strictly to follow the prompt. |
| `num_inference_steps` | integer 2–50 | 28 | More steps add detail and time. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.06 per image.

| Request | Price |
|---|---|
| One image | $0.06 |

Failed runs are not charged.

### Prompting

- Write subject, setting, composition, style, then light.
- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX.2 endpoints: `bfl/flux-2/max`, `bfl/flux-2/pro`, `bfl/flux-2/dev`, `bfl/flux-2/turbo`, `bfl/flux-2/flex/edit`.

---
Machine-readable: [`catalog/models/bfl/flux-2/flex.json`](../../../../catalog/models/bfl/flux-2/flex.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/flex
