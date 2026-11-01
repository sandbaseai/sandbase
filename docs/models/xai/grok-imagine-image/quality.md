# Grok Imagine Image Quality Text to Image

`xai/grok-imagine-image/quality` · image · xAI

Grok Imagine Image Quality by xAI - generate stunning images from text prompts with state-of-the-art AI. Supports multiple aspect ratios, styles, and high-resolution output for creative and commercial use.

## Pricing

- Depends on parameters (`params.resolution`).

| parameters | USD |
|---|---|
| resolution="1k" | 0.05 |
| resolution="2k" | 0.07 |

Formula: `((params.resolution ?? "1k") == "2k" ? 0.07 : 0.05)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-image/quality", "prompt": "Abstract human silhouette, golden particles ready to burst outward representing joy, data visualization style, emotional expression through particles, artistic scientific"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-image/quality', {'prompt': 'Abstract human silhouette, golden particles ready to burst outward representing joy, data visualization style, emotional expression through particles, artistic scientific'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-image/quality", {
  "prompt": "Abstract human silhouette, golden particles ready to burst outward representing joy, data visualization style, emotional expression through particles, artistic scientific"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-image/quality", sandbase.Params{
	"prompt": "Abstract human silhouette, golden particles ready to burst outward representing joy, data visualization style, emotional expression through particles, artistic scientific",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text description of the desired image.  |
| `resolution` | string |  | Resolution of the generated image. `1k` for standard resolution, `2k` for high resolution. one of: `1k`, `2k`; default `"1k"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |

## Details

Grok Imagine Image (Quality) generates detailed images at 1K or 2K.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 8,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output shape. |
| `resolution` | `1k` / `2k` | `1k` | Sets the per-image rate. |

### Billing

$0.05 per image at 1K and $0.07 at 2K.

| Request | 1k | 2k |
|---|---|---|
| One image | $0.05 | $0.07 |

Failed runs are not charged.

### Prompting

- Quote any text that must appear.

### Limits

- One output image per request.

### Also on SandBase

Other Grok Imagine Image endpoints: `xai/grok-imagine-image/quality/edit`, `xai/grok-imagine-image/edit`, `xai/grok-imagine-image/2.0/text-to-image`, `xai/grok-imagine-image/2.0/edit`.

---
Machine-readable: [`catalog/models/xai/grok-imagine-image/quality.json`](../../../../catalog/models/xai/grok-imagine-image/quality.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-image/quality
