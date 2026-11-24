# FlashVSR+ API: pricing, parameters and code examples

`openimaginglab/flashvsr-plus` · video generation model · openimaginglab · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.156 per call · **Modes:** async

Flashvsr Plus is openimaginglab's video-to-video AI model. Transform, enhance, and edit video content using text prompts - from style changes to object manipulation and scene modification.

## Pricing

- Depends on parameters (`params.temporal_compression`, `params.video`, `usage.duration`, `usage.height`, `usage.width`).

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openimaginglab/flashvsr-plus"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('openimaginglab/flashvsr-plus', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("openimaginglab/flashvsr-plus", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "openimaginglab/flashvsr-plus", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The random seed used for the generation process.  |
| `model` | string |  | turbo: fastest (hybrid sliding attention). base: highest quality. v1: FlashVSR v1.1 weights with the base configuration. one of: `turbo`, `base`, `v1`; default `"turbo"` |
| `video` | string |  | The input video to upscale.  |
| `color_fix` | boolean |  | Apply low-frequency wavelet color correction. default `false` |
| `video_quality` | string |  | Output encoding quality. one of: `low`, `medium`, `high`, `maximum`; default `"high"` |
| `preserve_audio` | boolean |  | Copy the input audio track into the output. default `true` |
| `upscale_factor` | number |  | Spatial upscaling factor. Output is capped at about 4K. default `2`; range 1–4 |
| `video_write_mode` | string |  | Output write mode. one of: `fast`, `balanced`, `small`; default `"balanced"` |
| `video_output_type` | string |  | Output container/codec. one of: `X264 (.mp4)`, `VP9 (.webm)`, `PRORES4444 (.mov)`, `GIF (.gif)`; default `"X264 (.mp4)"` |
| `temporal_compression` | integer |  | Input frames per latent frame. Use 2 or 1 for large motion; inference cost rises about 2x or 4x. one of: `1`, `2`, `4`; default `4` |

---
Machine-readable: [`catalog/models/openimaginglab/flashvsr-plus.json`](../../../catalog/models/openimaginglab/flashvsr-plus.json) · Store page: https://www.sandbase.ai/model/openimaginglab/flashvsr-plus
