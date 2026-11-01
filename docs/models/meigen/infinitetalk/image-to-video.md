# InfiniteTalk Image to Video

`meigen/infinitetalk/image-to-video` · video · MeiGen-AI

InfiniteTalk turns a portrait image and speech audio into a long-form talking video with natural lip sync, head and body motion.

## Pricing

- Depends on parameters (`params.audio`, `params.num_frames`, `params.resolution`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.audio) ?? ((params.num_frames ?? 145) / 25.0)) * 0.2 * ((params.resolution ?? "720p") == "720p" ? 2.0 : 1.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meigen/infinitetalk/image-to-video", "audio": "https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/eb358b1f-cd6a-45d4-b926-27a4bdc68388.mp3", "image": "https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/cd175c0b-f141-4ec1-8f8b-9fcf5c063865.png", "num_frames": 41, "prompt": "A woman with colorful hair talking on a podcast.", "resolution": "480p"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meigen/infinitetalk/image-to-video', {'audio': 'https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/eb358b1f-cd6a-45d4-b926-27a4bdc68388.mp3', 'image': 'https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/cd175c0b-f141-4ec1-8f8b-9fcf5c063865.png', 'num_frames': 41, 'prompt': 'A woman with colorful hair talking on a podcast.', 'resolution': '480p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meigen/infinitetalk/image-to-video", {
  "audio": "https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/eb358b1f-cd6a-45d4-b926-27a4bdc68388.mp3",
  "image": "https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/cd175c0b-f141-4ec1-8f8b-9fcf5c063865.png",
  "num_frames": 41,
  "prompt": "A woman with colorful hair talking on a podcast.",
  "resolution": "480p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meigen/infinitetalk/image-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/eb358b1f-cd6a-45d4-b926-27a4bdc68388.mp3",
	"image": "https://static.sandbase.ai/examples/d33fa92a-e37d-4e1b-ae63-7dc37efcf42f/input/cd175c0b-f141-4ec1-8f8b-9fcf5c063865.png",
	"num_frames": 41,
	"prompt": "A woman with colorful hair talking on a podcast.",
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
| `seed` | integer |  | Random seed for reproducibility. range 0–2147483647 |
| `audio` | string | yes | Input audio URL.  |
| `image` | string | yes | Input image URL (face / character).  |
| `prompt` | string | yes | Text prompt guiding the generation.  |
| `num_frames` | integer |  | Maximum frames to generate (41–721, 25 fps); output also stops at the end of the audio. default `145`; range 41–721 |
| `resolution` | string |  | Output resolution (720p costs 2x). one of: `480p`, `720p`; default `"720p"` |

## Details

InfiniteTalk turns a portrait and speech audio into a long-form talking video with natural lip sync and head and body motion.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Scene and gesture direction. |
| `image` | image URL, required | — | Portrait. JPEG, PNG, or WebP URL. |
| `audio` | audio URL, required | — | Speech that drives the lips. |
| `num_frames` | integer 41–721 | 145 | Frames at 25fps when the length is not set by audio. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

Per output second: $0.20 at 480p and $0.40 at 720p. Length follows the audio; without it, `num_frames` at 25fps (default 145 frames, 5.8 seconds).

| Output | 480p | 720p |
|---|---|---|
| 6s | $1.20 | $2.40 |
| 30s | $6.00 | $12.00 |
| 60s | $12.00 | $24.00 |

Failed runs are not charged.

### Prompting

- Use a front-facing portrait with the mouth visible.

### Also on SandBase

Other InfiniteTalk endpoints: `meigen/infinitetalk/text-to-video`, `meigen/infinitetalk/video-to-video`.

---
Machine-readable: [`catalog/models/meigen/infinitetalk/image-to-video.json`](../../../../catalog/models/meigen/infinitetalk/image-to-video.json) · Store page: https://www.sandbase.ai/model/meigen/infinitetalk/image-to-video
