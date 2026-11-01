# Wan 2.6 Text to Video

`alibaba/wan/2.6/text-to-video` · video · Alibaba

Alibaba Wan 2.6 text-to-video model with cinematic visuals, configurable duration (5 or 10 seconds) and resolution.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="720p" | 0.5 |
| duration=5, resolution="1080p" | 0.75 |
| duration=10, resolution="720p" | 1 |
| duration=10, resolution="1080p" | 1.5 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == '1080p' ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.6/text-to-video", "aspect_ratio": "9:16", "duration": 5, "prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.6/text-to-video', {'aspect_ratio': '9:16', 'duration': 5, 'prompt': 'A red paper lantern swaying gently in a quiet bamboo forest at dusk', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.6/text-to-video", {
  "aspect_ratio": "9:16",
  "duration": 5,
  "prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.6/text-to-video", sandbase.Params{
	"aspect_ratio": "9:16",
	"duration": 5,
	"prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk",
	"resolution": "720p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed (0-2147483647) for reproducible results. Omit for a random seed.  |
| `audio` | string |  | The URL of an audio file to guide video generation.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"Rim light, low contrast, medium close-up, daylight, left-weighted composition, clean single-person shot, warm tones, soft light, sunny day, side light, daytime. A young girl sits in a field of tall grass, with two fluffy little donkeys standing behind her. The girl is about eleven or twelve, wearing a simple floral dress, hair in two braids, with an innocent smile. She sits cross-legged, gently playing with wildflowers beside her. The donkeys are sturdy with perked ears, curiously looking toward the camera. Sunlight bathes the field, creating a warm and natural atmosphere."` |
| `duration` | integer |  | The duration of the generated video in seconds. Valid values are 5 and 10. one of: `5`, `10`; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `1:1`, `4:3`, `3:4`, `16:9`, `9:16`; default `"16:9"` |

## Details

Generate a 5 or 10 second clip from a written scene, with optional driving audio. For longer clips and better motion, Wan 2.7 is the newer option.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `audio` | audio URL | — | Optional WAV/MP3 URL that drives speech or rhythm. |
| `aspect_ratio` | `1:1` / `4:3` / `3:4` / `16:9` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.10 at 720p and $0.15 at 1080p, Alibaba's list price.

| Output | 720p | 1080p |
|---|---|---|
| 5s (default) | $0.50 | $0.75 |
| 10s | $1.00 | $1.50 |

Failed runs are not charged.

### Prompting

- Describe the shot in order: subject, action, setting, camera move, light, and sound.
- Give camera timing explicitly, e.g. “holds for two seconds, then pushes in slowly”.
- Put spoken lines in quotes and say who speaks them.

### Limits

- Durations are 5 or 10 seconds only.

### Also on SandBase

Other Wan 2.6 endpoints: `alibaba/wan/2.6/image-to-video`, `alibaba/wan/2.6/reference-to-video`, `alibaba/wan/2.6/flash/image-to-video`, `alibaba/wan/2.6/flash/reference-to-video`, `alibaba/wan/2.6/text-to-image`, `alibaba/wan/2.6/image-to-image`, `alibaba/wan/2.7/text-to-video` (newer).

---
Machine-readable: [`catalog/models/alibaba/wan/2.6/text-to-video.json`](../../../../../catalog/models/alibaba/wan/2.6/text-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.6/text-to-video
