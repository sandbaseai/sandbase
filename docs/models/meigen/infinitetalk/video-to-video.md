# InfiniteTalk Video to Video

`meigen/infinitetalk/video-to-video` · video · MeiGen-AI

InfiniteTalk dubs an existing video: it re-animates lips, face and body to match new speech audio.

## Pricing

- Depends on parameters (`params.audio`, `params.num_frames`, `params.resolution`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.audio) ?? ((params.num_frames ?? 145) / 25.0)) * 0.3 * ((params.resolution ?? "720p") == "720p" ? 2.0 : 1.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meigen/infinitetalk/video-to-video", "audio": "https://static.sandbase.ai/examples/b4b962b1-cb06-48d0-a0a4-6c0feb67c13b/input/1a1b7894-fdb9-4a3e-a8d7-67471c91d020.mp3", "num_frames": 41, "prompt": "A woman with colorful hair talking on a podcast.", "resolution": "480p", "video": "https://static.sandbase.ai/examples/b4b962b1-cb06-48d0-a0a4-6c0feb67c13b/input/07b54b85-765a-4454-ab0b-14620a533e1d.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meigen/infinitetalk/video-to-video', {'audio': 'https://static.sandbase.ai/examples/b4b962b1-cb06-48d0-a0a4-6c0feb67c13b/input/1a1b7894-fdb9-4a3e-a8d7-67471c91d020.mp3', 'num_frames': 41, 'prompt': 'A woman with colorful hair talking on a podcast.', 'resolution': '480p', 'video': 'https://static.sandbase.ai/examples/b4b962b1-cb06-48d0-a0a4-6c0feb67c13b/input/07b54b85-765a-4454-ab0b-14620a533e1d.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meigen/infinitetalk/video-to-video", {
  "audio": "https://static.sandbase.ai/examples/b4b962b1-cb06-48d0-a0a4-6c0feb67c13b/input/1a1b7894-fdb9-4a3e-a8d7-67471c91d020.mp3",
  "num_frames": 41,
  "prompt": "A woman with colorful hair talking on a podcast.",
  "resolution": "480p",
  "video": "https://static.sandbase.ai/examples/b4b962b1-cb06-48d0-a0a4-6c0feb67c13b/input/07b54b85-765a-4454-ab0b-14620a533e1d.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meigen/infinitetalk/video-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/b4b962b1-cb06-48d0-a0a4-6c0feb67c13b/input/1a1b7894-fdb9-4a3e-a8d7-67471c91d020.mp3",
	"num_frames": 41,
	"prompt": "A woman with colorful hair talking on a podcast.",
	"resolution": "480p",
	"video": "https://static.sandbase.ai/examples/b4b962b1-cb06-48d0-a0a4-6c0feb67c13b/input/07b54b85-765a-4454-ab0b-14620a533e1d.mp4",
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
| `video` | string | yes | Input video URL.  |
| `prompt` | string | yes | Text prompt guiding the generation.  |
| `num_frames` | integer |  | Maximum frames to generate (41–241, 25 fps); output also stops at the end of the audio. default `145`; range 41–241 |
| `resolution` | string |  | Output resolution (720p costs 2x). one of: `480p`, `720p`; default `"720p"` |

## Details

InfiniteTalk video-to-video dubs an existing clip, re-animating lips, face, and body to new speech.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Scene and gesture direction. |
| `video` | video URL, required | — | Clip to re-animate. |
| `audio` | audio URL, required | — | Speech that drives the lips. |
| `num_frames` | integer 41–241 | 145 | Frames at 25fps when the length is not set by audio. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

Per output second: $0.30 at 480p and $0.60 at 720p. Length follows the audio; without it, `num_frames` at 25fps (default 145 frames, 5.8 seconds).

| Output | 480p | 720p |
|---|---|---|
| 6s | $1.80 | $3.60 |
| 30s | $9.00 | $18.00 |
| 60s | $18.00 | $36.00 |

Failed runs are not charged.

### Prompting

- Use a front-facing portrait with the mouth visible.

### Also on SandBase

Other InfiniteTalk endpoints: `meigen/infinitetalk/image-to-video`, `meigen/infinitetalk/text-to-video`.

---
Machine-readable: [`catalog/models/meigen/infinitetalk/video-to-video.json`](../../../../catalog/models/meigen/infinitetalk/video-to-video.json) · Store page: https://www.sandbase.ai/model/meigen/infinitetalk/video-to-video
