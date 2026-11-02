# ByteDance Video Upscaler API: pricing, parameters and code examples

`bytedance/upscaler/video` · video generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.036 per call · **Modes:** async

Bytedance Video Upscaler upscales videos to 4K resolution with AI-powered enhancement. Supports multiple quality tiers (fast, standard, pro), frame rate interpolation to 60fps, and presets optimized for UGC, short series, AIGC, and old film restoration.

## Pricing

- Depends on parameters (`params.enhancement_tier`, `params.target_fps`, `params.target_resolution`, `params.video`, `usage.duration`).

Formula: `Math.ceil(usage.duration ?? media_duration(params.video) ?? 5.0) * 0.0072 * ((params.target_resolution ?? "1080p") == "4k" ? 4 : (params.target_resolution ?? "1080p") == "2k" ? 2 : 1) * ((params.enhancement_tier ?? "standard") == "pro" ? 10 : 1) * ((params.target_fps ?? "30fps") == "60fps" ? 2 : 1)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/upscaler/video", "video": "https://static.sandbase.ai/examples/519bb19f-f235-4c5c-bff2-ba45eaaa714d/input/a36e41d0-65b7-4499-810b-1e7d2f89b885.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/upscaler/video', {'video': 'https://static.sandbase.ai/examples/519bb19f-f235-4c5c-bff2-ba45eaaa714d/input/a36e41d0-65b7-4499-810b-1e7d2f89b885.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/upscaler/video", {
  "video": "https://static.sandbase.ai/examples/519bb19f-f235-4c5c-bff2-ba45eaaa714d/input/a36e41d0-65b7-4499-810b-1e7d2f89b885.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/upscaler/video", sandbase.Params{
	"video": "https://static.sandbase.ai/examples/519bb19f-f235-4c5c-bff2-ba45eaaa714d/input/a36e41d0-65b7-4499-810b-1e7d2f89b885.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | The URL of the video to upscale.  |
| `fidelity` | string |  | The enhancement intensity. 'high' applies mild enhancement while keeping visual texture close to the source video. 'medium' provides a balanced image quality enhancement. one of: `high`, `medium`; default `"high"` |
| `target_fps` | string |  | The target FPS of the video to upscale. one of: `30fps`, `60fps`; default `"30fps"` |
| `scale_ratio` | number |  | The scaling ratio for the output video resolution. When set, overrides target_resolution and scales the input resolution by this factor (e.g., 2.0 doubles the resolution). Range: 1.1 to 10.0. Please note that this is… range 1.1–10 |
| `enhancement_tier` | string |  | The enhancement quality tier. 'fast' provides essential upscaling with good speed, 'standard' uses adaptive algorithms for better visual texture, 'pro' uses large-model restoration for cinematic quality (longer… one of: `fast`, `standard`, `pro`; default `"standard"` |
| `target_resolution` | string |  | The target resolution of the video to upscale. one of: `1080p`, `2k`, `4k`; default `"1080p"` |
| `enhancement_preset` | string |  | The enhancement preset optimized for specific video scenarios. 'general' is a general-purpose template, 'ugc' targets user-generated short videos, 'short_series' is for short dramas, 'aigc' is for AI-generated content,… one of: `general`, `ugc`, `short_series`, `aigc`, `old_film`; default `"general"` |

## Details

ByteDance Video Upscaler enlarges videos to 1080p, 2K, or 4K with three enhancement tiers, optional 60fps interpolation, and presets for UGC, short drama, AI-generated, and old-film footage.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `video` | video URL, required | — | Video to upscale. |
| `enhancement_preset` | `general` / `ugc` / `short_series` / `aigc` / `old_film` | `general` | Tune restoration to the footage type. |
| `scale_ratio` | number 1.1–10 | — | Optional explicit scale factor. |
| `target_resolution` | `1080p` / `2k` / `4k` | `1080p` | Output tier; sets the rate. |
| `target_fps` | `30fps` / `60fps` | `30fps` | `60fps` interpolates frames and doubles the rate. |
| `enhancement_tier` | `fast` / `standard` / `pro` | `standard` | `fast`, `standard`, or `pro` (10× the standard rate). |
| `fidelity` | `high` / `medium` | `high` | `high` stays closer to the source. |

### Billing

$0.0072 per second at 1080p, standard tier, 30fps. 2K is 2× and 4K is 4×; `pro` is 10×; `60fps` is 2×. Seconds are rounded up.

| Video | 1080p | 2k | 4k |
|---|---|---|---|
| 10s, standard, 30fps | $0.072 | $0.144 | $0.288 |
| 10s, standard, 60fps | $0.144 | $0.288 | $0.576 |
| 10s, pro, 30fps | $0.72 | $1.44 | $2.88 |

Failed runs are not charged.

### Also on SandBase

Related: `bytedance/seedvr/upscale/video`, `alibaba/flashvsr`.

---
Machine-readable: [`catalog/models/bytedance/upscaler/video.json`](../../../../catalog/models/bytedance/upscaler/video.json) · Store page: https://www.sandbase.ai/model/bytedance/upscaler/video
