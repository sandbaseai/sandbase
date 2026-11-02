# SeedVR2 Video Upscale API: pricing, parameters and code examples

`bytedance/seedvr/upscale/video` · video generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.31104 per call · **Modes:** async

Seedvr Upscale Video by Bytedance - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual effects to existing videos with natural language instructions.

## Pricing

- Depends on parameters (`usage.duration`, `usage.fps`, `usage.height`, `usage.width`).

Formula: `(usage.width ?? 1920.0) * (usage.height ?? 1080.0) * (usage.fps ?? 30.0) * (usage.duration ?? 5.0) / 1000000.0 * 0.001`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedvr/upscale/video", "video": "https://static.sandbase.ai/examples/7de0d710-8d33-4b43-b1f2-b9b69e54f046/input/f7174bd6-9315-4ac6-865b-eaeaa4c562bf.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedvr/upscale/video', {'video': 'https://static.sandbase.ai/examples/7de0d710-8d33-4b43-b1f2-b9b69e54f046/input/f7174bd6-9315-4ac6-865b-eaeaa4c562bf.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedvr/upscale/video", {
  "video": "https://static.sandbase.ai/examples/7de0d710-8d33-4b43-b1f2-b9b69e54f046/input/f7174bd6-9315-4ac6-865b-eaeaa4c562bf.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedvr/upscale/video", sandbase.Params{
	"video": "https://static.sandbase.ai/examples/7de0d710-8d33-4b43-b1f2-b9b69e54f046/input/f7174bd6-9315-4ac6-865b-eaeaa4c562bf.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The random seed used for the generation process.  |
| `video` | string | yes | The input video to be processed  |
| `noise_scale` | number |  | The noise scale to use for the generation process. default `0.1`; range 0–1 |
| `upscale_mode` | string |  | The mode to use for the upscale. If 'target', the upscale factor will be calculated based on the target resolution. If 'factor', the upscale factor will be used directly. one of: `target`, `factor`; default `"factor"` |
| `output_format` | string |  | The format of the output video. one of: `X264 (.mp4)`, `VP9 (.webm)`, `PRORES4444 (.mov)`, `GIF (.gif)`; default `"X264 (.mp4)"` |
| `output_quality` | string |  | The quality of the output video. one of: `low`, `medium`, `high`, `maximum`; default `"high"` |
| `upscale_factor` | number |  | Upscaling factor to be used. Will multiply the dimensions with this factor when `upscale_mode` is `factor`. default `2`; range 1–10 |
| `output_write_mode` | string |  | The write mode of the output video. one of: `fast`, `balanced`, `small`; default `"balanced"` |
| `target_resolution` | string |  | The target resolution to upscale to when `upscale_mode` is `target`. one of: `720p`, `1080p`, `1440p`, `2160p`; default `"1080p"` |

## Details

SeedVR2 video upscale restores and enlarges a video by a factor (default 2×) or to a target resolution, with temporal consistency across frames.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `video` | video URL, required | — | Video to upscale. |
| `output_format` | `X264 (.mp4)` / `VP9 (.webm)` / `PRORES4444 (.mov)` / `GIF (.gif)` | `X264 (.mp4)` | Output file format. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `output_quality` | `low` / `medium` / `high` / `maximum` | `high` | Encoder quality. |
| `noise_scale` | number 0–1 | 0.1 | Higher values add more restored detail. |
| `target_resolution` | `720p` / `1080p` / `1440p` / `2160p` | `1080p` | Used in `target` mode. |
| `upscale_factor` | number 1–10 | 2 | Used in `factor` mode. |
| `output_write_mode` | `fast` / `balanced` / `small` | `balanced` | Encoder speed/size trade-off. |
| `upscale_mode` | `target` / `factor` | `factor` | `factor` multiplies the input size; `target` upscales to `target_resolution`. |

### Billing

Billed on output video data at $0.001 per megapixel (width × height × frames). For 30fps output that is about $0.028 per second at 720p, $0.062 at 1080p, and $0.25 at 4K. The quote before submission assumes 5 seconds of 1080p at 30fps.

| Output at 30fps | 720p | 1080p | 4K |
|---|---|---|---|
| 5s | $0.1382 | $0.311 | $1.2442 |
| 10s | $0.2765 | $0.6221 | $2.4883 |
| 30s | $0.8294 | $1.8662 | $7.465 |

Failed runs are not charged.

### Limits

- Higher factors on long clips can be expensive; check the output size first.

### Also on SandBase

Related: `bytedance/upscaler/video` (per-second pricing), `bytedance/seedvr/upscale/image`.

---
Machine-readable: [`catalog/models/bytedance/seedvr/upscale/video.json`](../../../../../catalog/models/bytedance/seedvr/upscale/video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedvr/upscale/video
