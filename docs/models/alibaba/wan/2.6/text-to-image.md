# Wan 2.6 Text to Image

`alibaba/wan/2.6/text-to-image` · image · Alibaba

Alibaba Wan 2.6 text-to-image model with high-quality generation and selectable aspect ratio.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.03 |

Formula: `0.03`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.6/text-to-image", "prompt": "A red bicycle leaning on a white wall, morning light"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.6/text-to-image', {'prompt': 'A red bicycle leaning on a white wall, morning light'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.6/text-to-image", {
  "prompt": "A red bicycle leaning on a white wall, morning light"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.6/text-to-image", sandbase.Params{
	"prompt": "A red bicycle leaning on a white wall, morning light",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible results.  |
| `prompt` | string | yes | The prompt to generate an image from. default `"Flowing liquid metal in iridescent blue and gold forming an impossible Möbius strip, floating in a void with soft caustic reflections, 3D render, octane, studio lighting"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21`; default `"16:9"` |

## Details

Wan 2.6 text-to-image: one image from a written brief in Chinese or English.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 10,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `9:21` | `16:9` | Output shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

$0.03 per image, Alibaba's list price.

| Request | Price |
|---|---|
| One image | $0.03 |

Failed runs are not charged.

### Prompting

- Write subject, setting, composition, style, then light and color.

### Limits

- One image per request. Wan 2.7 is the newer model at the same price.

### Also on SandBase

Other Wan 2.6 endpoints: `alibaba/wan/2.6/text-to-video`, `alibaba/wan/2.6/image-to-video`, `alibaba/wan/2.6/reference-to-video`, `alibaba/wan/2.6/flash/image-to-video`, `alibaba/wan/2.6/flash/reference-to-video`, `alibaba/wan/2.6/image-to-image`, `alibaba/wan/2.7/text-to-video` (newer), `alibaba/wan/2.7/text-to-image` (newer, same price).

---
Machine-readable: [`catalog/models/alibaba/wan/2.6/text-to-image.json`](../../../../../catalog/models/alibaba/wan/2.6/text-to-image.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.6/text-to-image
