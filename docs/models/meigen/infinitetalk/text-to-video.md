# InfiniteTalk Text to Video API: pricing, parameters and code examples

`meigen/infinitetalk/text-to-video` · video generation model · MeiGen-AI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $2.32 per call · **Modes:** async

InfiniteTalk speaks the given text with a chosen voice and animates the portrait into a talking video.

## Pricing

- Depends on parameters (`params.num_frames`, `params.resolution`, `usage.duration`).

Formula: `(usage.duration ?? ((params.num_frames ?? 145) / 25.0)) * 0.2 * ((params.resolution ?? "720p") == "720p" ? 2.0 : 1.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meigen/infinitetalk/text-to-video", "image": "https://static.sandbase.ai/examples/dacdca53-ccb5-4504-9a89-85b592384fbf/input/b243da19-087f-47f1-9f0c-926f1c59fc20.png", "num_frames": 41, "prompt": "A woman with colorful hair talking on a podcast.", "resolution": "480p", "text": "Hello everyone, welcome to our product demo today.", "voice": "Aria"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('meigen/infinitetalk/text-to-video', {'image': 'https://static.sandbase.ai/examples/dacdca53-ccb5-4504-9a89-85b592384fbf/input/b243da19-087f-47f1-9f0c-926f1c59fc20.png', 'num_frames': 41, 'prompt': 'A woman with colorful hair talking on a podcast.', 'resolution': '480p', 'text': 'Hello everyone, welcome to our product demo today.', 'voice': 'Aria'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("meigen/infinitetalk/text-to-video", {
  "image": "https://static.sandbase.ai/examples/dacdca53-ccb5-4504-9a89-85b592384fbf/input/b243da19-087f-47f1-9f0c-926f1c59fc20.png",
  "num_frames": 41,
  "prompt": "A woman with colorful hair talking on a podcast.",
  "resolution": "480p",
  "text": "Hello everyone, welcome to our product demo today.",
  "voice": "Aria"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "meigen/infinitetalk/text-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/dacdca53-ccb5-4504-9a89-85b592384fbf/input/b243da19-087f-47f1-9f0c-926f1c59fc20.png",
	"num_frames": 41,
	"prompt": "A woman with colorful hair talking on a podcast.",
	"resolution": "480p",
	"text": "Hello everyone, welcome to our product demo today.",
	"voice": "Aria",
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
| `text` | string | yes | Text the person speaks.  |
| `image` | string | yes | Input image URL (face / character).  |
| `voice` | string | yes | Voice used to speak the text. one of: `Aria`, `Roger`, `Sarah`, `Laura`, `Charlie`, `George`, `Callum`, `River`, `Liam`, `Charlotte`, `Alice`, `Matilda` … |
| `prompt` | string | yes | Text prompt guiding the generation.  |
| `num_frames` | integer |  | Maximum frames to generate (41–721, 25 fps); output also stops at the end of the audio. default `145`; range 41–721 |
| `resolution` | string |  | Output resolution (720p costs 2x). one of: `480p`, `720p`; default `"720p"` |

## Details

InfiniteTalk text-to-video speaks your text with a chosen voice and animates the portrait to match.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Scene and gesture direction. |
| `text` | string, required | — | Text to speak. |
| `image` | image URL, required | — | Portrait. JPEG, PNG, or WebP URL. |
| `voice` | `Aria` / `Roger` / `Sarah` / `Laura` / `Charlie` / `George` / `Callum` / `River` / `Liam` / `Charlotte` / `Alice` / `Matilda` / `Will` / `Jessica` / `Eric` / `Chris` / `Brian` / `Daniel` / `Lily` / `Bill`, required | — | Voice for the text. |
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

Other InfiniteTalk endpoints: `meigen/infinitetalk/image-to-video`, `meigen/infinitetalk/video-to-video`.

---
Machine-readable: [`catalog/models/meigen/infinitetalk/text-to-video.json`](../../../../catalog/models/meigen/infinitetalk/text-to-video.json) · Store page: https://www.sandbase.ai/model/meigen/infinitetalk/text-to-video
