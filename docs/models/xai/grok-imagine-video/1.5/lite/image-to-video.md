# Grok Imagine Video 1.5 Lite Image to Video API: pricing, parameters and code examples

`xai/grok-imagine-video/1.5/lite/image-to-video` · video generation model · xAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.03 to $2.11 per run, depending on parameters · **Modes:** async

Grok Imagine Video 1.5 Lite, the low-cost tier of xAI's video model, animates an image into a 1-15 second video with native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="480p" | 0.03 |
| duration=1, resolution="720p" | 0.04 |
| duration=1, resolution="1080p" | 0.15 |
| duration=6, resolution="480p" | 0.13 |
| duration=6, resolution="720p" | 0.19 |
| duration=6, resolution="1080p" | 0.85 |
| duration=15, resolution="480p" | 0.31 |
| duration=15, resolution="720p" | 0.46 |
| duration=15, resolution="1080p" | 2.11 |

Formula: `(params.duration ?? 6) * ((params.resolution ?? "720p") == "1080p" ? 0.14 : (params.resolution ?? "720p") == "480p" ? 0.02 : 0.03) + 0.01`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/1.5/lite/image-to-video", "duration": 1, "image": "https://static.sandbase.ai/examples/5d48e76d-5a0c-452b-8181-aa4ba0072b12/input/9ef1f22e-26ce-4d56-8500-03a900ca4b9c.png", "prompt": "the camera slowly zooms in", "resolution": "480p"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/1.5/lite/image-to-video', {'duration': 1, 'image': 'https://static.sandbase.ai/examples/5d48e76d-5a0c-452b-8181-aa4ba0072b12/input/9ef1f22e-26ce-4d56-8500-03a900ca4b9c.png', 'prompt': 'the camera slowly zooms in', 'resolution': '480p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/1.5/lite/image-to-video", {
  "duration": 1,
  "image": "https://static.sandbase.ai/examples/5d48e76d-5a0c-452b-8181-aa4ba0072b12/input/9ef1f22e-26ce-4d56-8500-03a900ca4b9c.png",
  "prompt": "the camera slowly zooms in",
  "resolution": "480p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/1.5/lite/image-to-video", sandbase.Params{
	"duration": 1,
	"image": "https://static.sandbase.ai/examples/5d48e76d-5a0c-452b-8181-aa4ba0072b12/input/9ef1f22e-26ce-4d56-8500-03a900ca4b9c.png",
	"prompt": "the camera slowly zooms in",
	"resolution": "480p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the input image for video generation.  |
| `prompt` | string | yes | Text description of desired changes or motion in the video.  |
| `duration` | integer |  | Video duration in seconds. default `6`; range 1–15 |
| `resolution` | string |  | Resolution of the output video. one of: `480p`, `720p`, `1080p`; default `"720p"` |

## Details

Grok Imagine Video 1.5 Lite image-to-video: low-cost animation of a picture into a 1–15 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–15 | 6 | Output length in seconds. |

### Billing

Per output second: $0.02 at 480p, $0.03 at 720p, $0.14 at 1080p, plus $0.01 per request.

| Output | 480p | 720p | 1080p |
|---|---|---|---|
| 6s (default) | $0.13 | $0.19 | $0.85 |
| 10s | $0.21 | $0.31 | $1.41 |
| 15s | $0.31 | $0.46 | $2.11 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video 1.5 endpoints: `xai/grok-imagine-video/1.5/text-to-video`, `xai/grok-imagine-video/1.5/image-to-video`, `xai/grok-imagine-video/1.5/reference-to-video`, `xai/grok-imagine-video/1.5/lite/text-to-video`, `xai/grok-imagine-video/text-to-video` (previous version).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/1.5/lite/image-to-video.json`](../../../../../../catalog/models/xai/grok-imagine-video/1.5/lite/image-to-video.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/1.5/lite/image-to-video
