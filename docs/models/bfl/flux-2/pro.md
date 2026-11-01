# Flux 2 Pro Text to Image

`bfl/flux-2/pro` · image · BFL

Flux 2 Pro by BFL - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-2/pro", "prompt": "An intense close-up of knight'\''s visor reflecting battle, sword raised, flames in background, chiaroscuro helmet shadows, hyper-detailed armor, square medieval, cinematic lighting"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-2/pro', {'prompt': "An intense close-up of knight's visor reflecting battle, sword raised, flames in background, chiaroscuro helmet shadows, hyper-detailed armor, square medieval, cinematic lighting"})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-2/pro", {
  "prompt": "An intense close-up of knight's visor reflecting battle, sword raised, flames in background, chiaroscuro helmet shadows, hyper-detailed armor, square medieval, cinematic lighting"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-2/pro", sandbase.Params{
	"prompt": "An intense close-up of knight's visor reflecting battle, sword raised, flames in background, chiaroscuro helmet shadows, hyper-detailed armor, square medieval, cinematic lighting",
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

## Details

FLUX.2 [pro], BFL's production tier: high quality at a predictable per-image price. Text to image.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.03 per image.

| Request | Price |
|---|---|
| One image | $0.03 |

Failed runs are not charged.

### Prompting

- Write subject, setting, composition, style, then light.
- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX.2 endpoints: `bfl/flux-2/max`, `bfl/flux-2/flex`, `bfl/flux-2/dev`, `bfl/flux-2/turbo`, `bfl/flux-2/pro/edit`.

---
Machine-readable: [`catalog/models/bfl/flux-2/pro.json`](../../../../catalog/models/bfl/flux-2/pro.json) · Store page: https://www.sandbase.ai/model/bfl/flux-2/pro
