# Grok Imagine Video Text to Video

`xai/grok-imagine-video/text-to-video` · video · xAI

Grok Imagine Video by xAI - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural motion, camera control, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=1 | 0.05 |
| duration=6 | 0.3 |
| duration=15 | 0.75 |

Formula: `(params.duration ?? 6) * 0.05`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/text-to-video", "prompt": "Anime schoolgirl bursting out of house door, cherry blossoms blowing, morning light, speed lines indicating rush, chibi-ready expressions, classic shojo aesthetic, vibrant colors"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/text-to-video', {'prompt': 'Anime schoolgirl bursting out of house door, cherry blossoms blowing, morning light, speed lines indicating rush, chibi-ready expressions, classic shojo aesthetic, vibrant colors'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/text-to-video", {
  "prompt": "Anime schoolgirl bursting out of house door, cherry blossoms blowing, morning light, speed lines indicating rush, chibi-ready expressions, classic shojo aesthetic, vibrant colors"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/text-to-video", sandbase.Params{
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
| `resolution` | string |  | Resolution of the output video. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`; default `"16:9"` |

## Details

Grok Imagine Video turns a prompt into a 1–15 second clip with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–15 | 6 | Output length in seconds. |
| `aspect_ratio` | `16:9` / `4:3` / `3:2` / `1:1` / `2:3` / `3:4` / `9:16` | `16:9` | Output frame shape. |

### Billing

$0.05 per output second.

| Output | Price |
|---|---|
| 6s (default) | $0.30 |
| 10s | $0.50 |
| 15s | $0.75 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video endpoints: `xai/grok-imagine-video/image-to-video`, `xai/grok-imagine-video/reference-to-video`, `xai/grok-imagine-video/video-edit`, `xai/grok-imagine-video/video-extend`, `xai/grok-imagine-video/1.5/text-to-video` (1.5, newer).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/text-to-video.json`](../../../../catalog/models/xai/grok-imagine-video/text-to-video.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/text-to-video
