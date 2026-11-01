# Grok Imagine Video 1.5 Lite Text to Video

`xai/grok-imagine-video/1.5/lite/text-to-video` · video · xAI

Grok Imagine Video 1.5 Lite, the low-cost tier of xAI's video model, turns a text prompt into a 1-15 second video with native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="480p" | 0.02 |
| duration=1, resolution="720p" | 0.03 |
| duration=1, resolution="1080p" | 0.14 |
| duration=6, resolution="480p" | 0.12 |
| duration=6, resolution="720p" | 0.18 |
| duration=6, resolution="1080p" | 0.84 |
| duration=15, resolution="480p" | 0.3 |
| duration=15, resolution="720p" | 0.45 |
| duration=15, resolution="1080p" | 2.1 |

Formula: `(params.duration ?? 6) * ((params.resolution ?? "720p") == "1080p" ? 0.14 : (params.resolution ?? "720p") == "480p" ? 0.02 : 0.03)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/1.5/lite/text-to-video", "duration": 1, "prompt": "a paper boat drifting on a pond", "resolution": "480p"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/1.5/lite/text-to-video', {'duration': 1, 'prompt': 'a paper boat drifting on a pond', 'resolution': '480p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/1.5/lite/text-to-video", {
  "duration": 1,
  "prompt": "a paper boat drifting on a pond",
  "resolution": "480p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/1.5/lite/text-to-video", sandbase.Params{
	"duration": 1,
	"prompt": "a paper boat drifting on a pond",
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
| `prompt` | string | yes | Text description of the desired video.  |
| `duration` | integer |  | Video duration in seconds. default `6`; range 1–15 |
| `resolution` | string |  | Resolution of the output video. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`; default `"16:9"` |

## Details

Grok Imagine Video 1.5 Lite, the low-cost tier, turns a prompt into a 1–15 second clip with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `aspect_ratio` | `16:9` / `4:3` / `3:2` / `1:1` / `2:3` / `3:4` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–15 | 6 | Output length in seconds. |

### Billing

Per output second: $0.02 at 480p, $0.03 at 720p, $0.14 at 1080p.

| Output | 480p | 720p | 1080p |
|---|---|---|---|
| 6s (default) | $0.12 | $0.18 | $0.84 |
| 10s | $0.20 | $0.30 | $1.40 |
| 15s | $0.30 | $0.45 | $2.10 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video 1.5 endpoints: `xai/grok-imagine-video/1.5/text-to-video`, `xai/grok-imagine-video/1.5/image-to-video`, `xai/grok-imagine-video/1.5/reference-to-video`, `xai/grok-imagine-video/1.5/lite/image-to-video`, `xai/grok-imagine-video/text-to-video` (previous version).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/1.5/lite/text-to-video.json`](../../../../../../catalog/models/xai/grok-imagine-video/1.5/lite/text-to-video.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/1.5/lite/text-to-video
