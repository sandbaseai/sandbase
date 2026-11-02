# Flux 3 Text to Image API: pricing, parameters and code examples

`bfl/flux-3/text-to-image` · image generation model · BFL · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.041 to $0.607 per run, depending on parameters · **Modes:** async

FLUX 3 by Black Forest Labs generates images from a text prompt, with strong prompt adherence and typography at 512px to 4K resolution tiers.

## Pricing

- Depends on parameters (`params.resolution`).

| parameters | USD |
|---|---|
| resolution="512sq" | 0.041 |
| resolution="768sq" | 0.041 |
| resolution="1k" | 0.048 |
| resolution="2k" | 0.1 |
| resolution="4k" | 0.607 |

Formula: `(params.resolution ?? "1k") == "4k" ? 0.607 : (params.resolution ?? "1k") == "2k" ? 0.1 : ((params.resolution ?? "1k") == "512sq" || (params.resolution ?? "1k") == "768sq") ? 0.041 : 0.048`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-3/text-to-image", "prompt": "a red bicycle leaning on a brick wall", "resolution": "1k"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-3/text-to-image', {'prompt': 'a red bicycle leaning on a brick wall', 'resolution': '1k'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-3/text-to-image", {
  "prompt": "a red bicycle leaning on a brick wall",
  "resolution": "1k"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-3/text-to-image", sandbase.Params{
	"prompt": "a red bicycle leaning on a brick wall",
	"resolution": "1k",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The prompt to generate an image from.  |
| `resolution` | string |  | Output resolution tier. 4k can take several minutes. one of: `512sq`, `768sq`, `1k`, `2k`, `4k`; default `"1k"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`; default `"jpeg"` |

## Details

FLUX 3 by Black Forest Labs generates images from a prompt, with strong prompt adherence and typography at resolution tiers from 512px to 4K.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `resolution` | `512sq` / `768sq` / `1k` / `2k` / `4k` | `1k` | Size tier; sets the per-image rate. |
| `output_format` | `jpeg` / `png` | `jpeg` | Output file format. |

### Billing

BFL's official per-image tiers: $0.041 for the 512 and 768 square tiers, $0.048 at 1K, $0.10 at 2K, $0.607 at 4K.

| Request | 512sq | 1k | 2k | 4k |
|---|---|---|---|---|
| One image | $0.041 | $0.048 | $0.10 | $0.607 |

Failed runs are not charged.

### Prompting

- Quote any text that must appear and say where it goes.

### Limits

- One output image per request.

### Also on SandBase

Other FLUX 3 endpoints: `bfl/flux-3/edit`, `bfl/flux-3/text-to-video`, `bfl/flux-3/image-to-video`.

---
Machine-readable: [`catalog/models/bfl/flux-3/text-to-image.json`](../../../../catalog/models/bfl/flux-3/text-to-image.json) · Store page: https://www.sandbase.ai/model/bfl/flux-3/text-to-image
