# MiniMax H3 Image Highspeed Text to Image API: pricing, parameters and code examples

`minimax/h3-image-highspeed` · image generation model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.05 to $0.18 per run, depending on parameters · **Modes:** async

MiniMax H3 Image Highspeed is the faster version of MiniMax's H3 image generation model, with the same prompt enhancement, aspect ratios from 1:3 to 3:1 and 1K, 2K or 4K output at lower latency.

## Pricing

- Depends on parameters (`params.resolution`).

| parameters | USD |
|---|---|
| resolution="1K" | 0.05 |
| resolution="2K" | 0.05 |
| resolution="4K" | 0.18 |

Formula: `((params.resolution ?? "1K") == "4K" ? 0.18 : 0.05)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3-image-highspeed", "aspect_ratio": "16:9", "prompt": "A rustic farm-to-table feast on a weathered wooden table, overhead food photograph, warm side light", "resolution": "1K"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3-image-highspeed', {'aspect_ratio': '16:9', 'prompt': 'A rustic farm-to-table feast on a weathered wooden table, overhead food photograph, warm side light', 'resolution': '1K'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3-image-highspeed", {
  "aspect_ratio": "16:9",
  "prompt": "A rustic farm-to-table feast on a weathered wooden table, overhead food photograph, warm side light",
  "resolution": "1K"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3-image-highspeed", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "A rustic farm-to-table feast on a weathered wooden table, overhead food photograph, warm side light",
	"resolution": "1K",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt to generate an image from. default `"A rustic farm-to-table feast on a weathered wooden table, overhead food photograph, warm side light"` |
| `resolution` | string |  | Output resolution tier: 1K (about 1 MP), 2K (about 4 MP) or 4K (about 16 MP). one of: `1K`, `2K`, `4K`; default `"1K"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `21:9`, `16:9`, `2:1`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `1:2`, `9:16` …; default `"1:1"` |
| `output_format` | string |  | The format of the generated image. one of: `jpeg`, `png`, `webp`; default `"png"` |

---
Machine-readable: [`catalog/models/minimax/h3-image-highspeed.json`](../../../catalog/models/minimax/h3-image-highspeed.json) · Store page: https://www.sandbase.ai/model/minimax/h3-image-highspeed
