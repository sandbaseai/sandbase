# Veo 3.1 Text to Video

`google/veo3.1/text-to-video` · video · Google

Veo3.1 by Google - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural motion, camera control, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=4, generate_audio=false, resolution="720p" | 0.8 |
| duration=4, generate_audio=false, resolution="1080p" | 0.8 |
| duration=4, generate_audio=false, resolution="4k" | 1.6 |
| duration=4, generate_audio=true, resolution="720p" | 1.6 |
| duration=4, generate_audio=true, resolution="1080p" | 1.6 |
| duration=4, generate_audio=true, resolution="4k" | 2.4 |
| duration=6, generate_audio=false, resolution="720p" | 1.2 |
| duration=6, generate_audio=false, resolution="1080p" | 1.2 |
| duration=6, generate_audio=false, resolution="4k" | 2.4 |
| duration=6, generate_audio=true, resolution="720p" | 2.4 |
| duration=6, generate_audio=true, resolution="1080p" | 2.4 |
| duration=6, generate_audio=true, resolution="4k" | 3.6 |
| duration=8, generate_audio=false, resolution="720p" | 1.6 |
| duration=8, generate_audio=false, resolution="1080p" | 1.6 |
| duration=8, generate_audio=false, resolution="4k" | 3.2 |
| duration=8, generate_audio=true, resolution="720p" | 3.2 |
| duration=8, generate_audio=true, resolution="1080p" | 3.2 |
| duration=8, generate_audio=true, resolution="4k" | 4.8 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "720p" ? ((params.generate_audio ?? true) ? 0.40 : 0.20) : (params.resolution ?? "720p") == "1080p" ? ((params.generate_audio ?? true) ? 0.40 : 0.20) : (params.resolution ?? "720p") == "4k" ? ((params.generate_audio ?? true) ? 0.60 : 0.40) : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/veo3.1/text-to-video", "duration": 4, "generate_audio": false, "prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/veo3.1/text-to-video', {'duration': 4, 'generate_audio': False, 'prompt': 'A red paper lantern swaying gently in a quiet bamboo forest at dusk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/veo3.1/text-to-video", {
  "duration": 4,
  "generate_audio": false,
  "prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/veo3.1/text-to-video", sandbase.Params{
	"duration": 4,
	"generate_audio": false,
	"prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for more reproducible results. range 0–4294967295 |
| `prompt` | string | yes | The text prompt describing the video you want to generate  |
| `duration` | integer |  | Duration of the generated video in seconds. one of: `4`, `6`, `8`; default `8` |
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate synchronized audio. Videos without audio are cheaper. default `true` |
| `negative_prompt` | string |  | What to avoid in the video.  |

## Details

Veo 3.1 text-to-video, Google's highest-quality video model. Write a scene and get back a 4, 6, or 8 second clip with native audio: dialogue, music, and sound effects generated alongside the picture.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `duration` | 4 / 6 / 8 | 8 | Output length in seconds. |
| `resolution` | `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects; turning it off lowers the rate. |
| `negative_prompt` | string | — | What to avoid. |
| `seed` | integer 0–4294967295 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds, Google's list price. With audio: $0.40 at 720p, $0.40 at 1080p, $0.60 at 4k. Without audio: $0.20 / $0.20 / $0.40 respectively.

| Output | 720p | 1080p | 4k |
|---|---|---|---|
| 4s with audio | $1.60 | $1.60 | $2.40 |
| 6s with audio | $2.40 | $2.40 | $3.60 |
| 8s with audio (default) | $3.20 | $3.20 | $4.80 |
| 8s without audio | $1.60 | $1.60 | $3.20 |

Failed runs are not charged.

### Prompting

- Describe subject, action, setting, camera, and light, then the sound.
- Put dialogue in quotes and name the speaker.
- Use `negative_prompt` for things to keep out of frame.

### Limits

- Clips are 4, 6, or 8 seconds; chain `video-extend` calls for longer shots.
- Use Veo 3.1 Fast for cheaper drafts.

### Also on SandBase

Other Veo 3.1 endpoints: `google/veo3.1/image-to-video`, `google/veo3.1/first-last-frame-to-video`, `google/veo3.1/reference-to-video`, `google/veo3.1/video-extend`, `google/veo3.1/fast/text-to-video`, `google/veo3.1/lite/text-to-video`.

---
Machine-readable: [`catalog/models/google/veo3.1/text-to-video.json`](../../../../catalog/models/google/veo3.1/text-to-video.json) · Store page: https://www.sandbase.ai/model/google/veo3.1/text-to-video
