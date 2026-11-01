# Grok Imagine Video 1.5 Text to Video

`xai/grok-imagine-video/1.5/text-to-video` · video · xAI

Grok Imagine Video 1.5 by xAI - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural motion, camera control, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="480p" | 0.08 |
| duration=1, resolution="720p" | 0.14 |
| duration=1, resolution="1080p" | 0.25 |
| duration=6, resolution="480p" | 0.48 |
| duration=6, resolution="720p" | 0.84 |
| duration=6, resolution="1080p" | 1.5 |
| duration=15, resolution="480p" | 1.2 |
| duration=15, resolution="720p" | 2.1 |
| duration=15, resolution="1080p" | 3.75 |

Formula: `(params.duration ?? 6) * ((params.resolution ?? "720p") == "1080p" ? 0.25 : (params.resolution ?? "720p") == "480p" ? 0.08 : 0.14)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/1.5/text-to-video", "prompt": "Anime schoolgirl bursting out of house door, cherry blossoms blowing, morning light, speed lines indicating rush, chibi-ready expressions, classic shojo aesthetic, vibrant colors"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/1.5/text-to-video', {'prompt': 'Anime schoolgirl bursting out of house door, cherry blossoms blowing, morning light, speed lines indicating rush, chibi-ready expressions, classic shojo aesthetic, vibrant colors'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/1.5/text-to-video", {
  "prompt": "Anime schoolgirl bursting out of house door, cherry blossoms blowing, morning light, speed lines indicating rush, chibi-ready expressions, classic shojo aesthetic, vibrant colors"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/1.5/text-to-video", sandbase.Params{
	"prompt": "Anime schoolgirl bursting out of house door, cherry blossoms blowing, morning light, speed lines indicating rush, chibi-ready expressions, classic shojo aesthetic, vibrant colors",
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
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |

## Details

Grok Imagine Video 1.5 turns a prompt into a 1–15 second clip with native audio, up to 1080p.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output frame shape. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–15 | 6 | Output length in seconds. |

### Billing

Per output second: $0.08 at 480p, $0.14 at 720p, $0.25 at 1080p.

| Output | 480p | 720p | 1080p |
|---|---|---|---|
| 6s (default) | $0.48 | $0.84 | $1.50 |
| 10s | $0.80 | $1.40 | $2.50 |
| 15s | $1.20 | $2.10 | $3.75 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video 1.5 endpoints: `xai/grok-imagine-video/1.5/image-to-video`, `xai/grok-imagine-video/1.5/reference-to-video`, `xai/grok-imagine-video/1.5/lite/text-to-video`, `xai/grok-imagine-video/1.5/lite/image-to-video`, `xai/grok-imagine-video/text-to-video` (previous version).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/1.5/text-to-video.json`](../../../../../catalog/models/xai/grok-imagine-video/1.5/text-to-video.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/1.5/text-to-video
