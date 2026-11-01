# Topaz Video Upscale

`topaz/upscale/video` · video · Topaz Labs

Upscale Video is Topaz Labs's video-to-video AI model. Transform, enhance, and edit video content using text prompts - from style changes to object manipulation and scene modification.

## Pricing

- Depends on parameters (`params.model`, `params.target_fps`, `params.video`, `usage.duration`, `usage.fps`, `usage.height`, `usage.width`).

Formula: `Math.max((usage.duration ?? media_duration(params.video) ?? 0.0), 5.0) * (((usage.width ?? 0.0) * (usage.height ?? 0.0)) <= 0.0 ? 0.02 : ((usage.width * usage.height) <= 921600.0 ? 0.01 : ((usage.width * usage.height) <= 2073600.0 ? 0.02 : 0.08))) * ((usage.fps ?? (params.target_fps ?? 30.0)) >= 60.0 ? 2.0 : 1.0) * ((params.model ?? "") == "Gaia 2" ? 0.5 : 1.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "topaz/upscale/video", "video": "https://static.sandbase.ai/examples/1e4dfe61-979e-46cb-b89b-febca05cad88/input/b80bd4f4-a0df-434c-98c9-e7f418ff0cb3.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('topaz/upscale/video', {'video': 'https://static.sandbase.ai/examples/1e4dfe61-979e-46cb-b89b-febca05cad88/input/b80bd4f4-a0df-434c-98c9-e7f418ff0cb3.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("topaz/upscale/video", {
  "video": "https://static.sandbase.ai/examples/1e4dfe61-979e-46cb-b89b-febca05cad88/input/b80bd4f4-a0df-434c-98c9-e7f418ff0cb3.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "topaz/upscale/video", sandbase.Params{
	"video": "https://static.sandbase.ai/examples/1e4dfe61-979e-46cb-b89b-febca05cad88/input/b80bd4f4-a0df-434c-98c9-e7f418ff0cb3.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `halo` | number |  | Halo reduction level (0.0-1.0). Default varies by model. range 0–1 |
| `grain` | number |  | Film grain amount (0.0-0.1). Default varies by model. range 0–0.1 |
| `noise` | number |  | Noise reduction level (0.0-1.0). Default varies by model. range 0–1 |
| `video` | string | yes | URL of the video to upscale  |
| `target_fps` | integer |  | Target FPS for frame interpolation. If set, frame interpolation will be enabled. range 16–60 |
| `H264_output` | boolean |  | Whether to use H264 codec for output video. Default is H265. default `false` |
| `compression` | number |  | Compression artifact removal level (0.0-1.0). Default varies by model. range 0–1 |
| `recover_detail` | number |  | Recover original detail level (0.0-1.0). Higher values preserve more original detail. range 0–1 |
| `upscale_factor` | number |  | Factor to upscale the video by (e.g. 2.0 doubles width and height) default `2`; range 1–4 |

## Details

Topaz upscales and enhances video, with optional frame interpolation to 60fps.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `video` | video URL, required | — | Video to upscale. |
| `noise` | number 0–1 | — | Noise reduction level (0.0-1.0). |
| `upscale_factor` | number 1–4 | 2 | 1–4×. |
| `halo` | number 0–1 | — | Halo reduction level (0.0-1.0). |
| `compression` | number 0–1 | — | Compression artifact removal level (0.0-1.0). |
| `grain` | number 0–0.1 | — | Film grain amount (0.0-0.1). |
| `recover_detail` | number 0–1 | — | Recover original detail level (0.0-1.0). |
| `target_fps` | integer 16–60 | — | Interpolate to this frame rate (16–60). |
| `H264_output` | boolean | false | Whether to use H264 codec for output video. |

### Billing

Per output second (minimum 5): $0.01 up to 720p, $0.02 up to 1080p, $0.08 above; 60fps doubles the rate.

| Output | 720p | 1080p | 4K |
|---|---|---|---|
| 10s | $0.10 | $0.20 | $0.80 |

Failed runs are not charged.

### Also on SandBase

Related: `bytedance/upscaler/video`.

---
Machine-readable: [`catalog/models/topaz/upscale/video.json`](../../../../catalog/models/topaz/upscale/video.json) · Store page: https://www.sandbase.ai/model/topaz/upscale/video
