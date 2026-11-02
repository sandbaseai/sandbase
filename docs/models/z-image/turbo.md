# Z-Image Turbo Text to Image API: pricing, parameters and code examples

`z-image/turbo` · image generation model · Z-Image · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** async

Turbo is Z-Image's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural language descriptions with exceptional detail and prompt adherence.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-image/turbo", "aspect_ratio": "9:16", "prompt": "A red paper lantern in a quiet bamboo forest at dusk"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('z-image/turbo', {'aspect_ratio': '9:16', 'prompt': 'A red paper lantern in a quiet bamboo forest at dusk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("z-image/turbo", {
  "aspect_ratio": "9:16",
  "prompt": "A red paper lantern in a quiet bamboo forest at dusk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "z-image/turbo", sandbase.Params{
	"aspect_ratio": "9:16",
	"prompt": "A red paper lantern in a quiet bamboo forest at dusk",
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
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"png"` |

## Details

Z-Image Turbo, Alibaba's fast 6B model, generates photorealistic images with bilingual text in a few steps.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output shape. |
| `output_format` | `jpeg` / `png` | `png` | Output file format. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.015 per image.

| Request | Price |
|---|---|
| One image | $0.015 |

Failed runs are not charged.

### Prompting

- Write subject, setting, style, then light.

### Also on SandBase

Related: `alibaba/z-image/base`, `alibaba/z-image/turbo/edit`.

---
Machine-readable: [`catalog/models/z-image/turbo.json`](../../../catalog/models/z-image/turbo.json) · Store page: https://www.sandbase.ai/model/z-image/turbo
