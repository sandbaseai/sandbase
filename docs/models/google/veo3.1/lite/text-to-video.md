# Veo 3.1 Lite Text to Video

`google/veo3.1/lite/text-to-video` · video · Google

Veo3.1 Lite is Google's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=4, generate_audio=false, resolution="720p" | 0.12 |
| duration=4, generate_audio=false, resolution="1080p" | 0.2 |
| duration=4, generate_audio=true, resolution="720p" | 0.2 |
| duration=4, generate_audio=true, resolution="1080p" | 0.32 |
| duration=6, generate_audio=false, resolution="720p" | 0.18 |
| duration=6, generate_audio=false, resolution="1080p" | 0.3 |
| duration=6, generate_audio=true, resolution="720p" | 0.3 |
| duration=6, generate_audio=true, resolution="1080p" | 0.48 |
| duration=8, generate_audio=false, resolution="720p" | 0.24 |
| duration=8, generate_audio=false, resolution="1080p" | 0.4 |
| duration=8, generate_audio=true, resolution="720p" | 0.4 |
| duration=8, generate_audio=true, resolution="1080p" | 0.64 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "720p" ? ((params.generate_audio ?? true) ? 0.05 : 0.03) : (params.resolution ?? "720p") == "1080p" ? ((params.generate_audio ?? true) ? 0.08 : 0.05) : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/veo3.1/lite/text-to-video", "aspect_ratio": "9:16", "duration": 4, "generate_audio": false, "prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/veo3.1/lite/text-to-video', {'aspect_ratio': '9:16', 'duration': 4, 'generate_audio': False, 'prompt': 'A red paper lantern swaying gently in a quiet bamboo forest at dusk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/veo3.1/lite/text-to-video", {
  "aspect_ratio": "9:16",
  "duration": 4,
  "generate_audio": false,
  "prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/veo3.1/lite/text-to-video", sandbase.Params{
	"aspect_ratio": "9:16",
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
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate synchronized audio. Videos without audio are cheaper. default `true` |
| `negative_prompt` | string |  | What to avoid in the video.  |

## Details

Veo 3.1 Lite text-to-video, the lowest-cost Veo 3.1 tier for high-volume drafts. Write a scene and get back a 4, 6, or 8 second clip with native audio: dialogue, music, and sound effects generated alongside the picture.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `duration` | 4 / 6 / 8 | 8 | Output length in seconds. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects; turning it off lowers the rate. |
| `negative_prompt` | string | — | What to avoid. |
| `seed` | integer 0–4294967295 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds, Google's list price. With audio: $0.05 at 720p, $0.08 at 1080p. Without audio: $0.03 / $0.05 respectively.

| Output | 720p | 1080p |
|---|---|---|
| 4s with audio | $0.20 | $0.32 |
| 6s with audio | $0.30 | $0.48 |
| 8s with audio (default) | $0.40 | $0.64 |
| 8s without audio | $0.24 | $0.40 |

Failed runs are not charged.

### Prompting

- Describe subject, action, setting, camera, and light, then the sound.
- Put dialogue in quotes and name the speaker.
- Use `negative_prompt` for things to keep out of frame.

### Limits

- Clips are 4, 6, or 8 seconds.
- No 4K on this tier.

### Also on SandBase

Other Veo 3.1 Lite endpoints: `google/veo3.1/lite/image-to-video`, `google/veo3.1/lite/first-last-frame-to-video`, `google/veo3.1/text-to-video`, `google/veo3.1/fast/text-to-video`.

---
Machine-readable: [`catalog/models/google/veo3.1/lite/text-to-video.json`](../../../../../catalog/models/google/veo3.1/lite/text-to-video.json) · Store page: https://www.sandbase.ai/model/google/veo3.1/lite/text-to-video
