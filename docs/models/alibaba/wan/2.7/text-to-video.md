# Wan 2.7 Text to Video API: pricing, parameters and code examples

`alibaba/wan/2.7/text-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $1.05 per run, depending on parameters · **Modes:** async

Alibaba Wan 2.7 text-to-video model with cinematic visuals, native audio generation, and configurable duration and resolution.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=2, resolution="720p" | 0.2 |
| duration=2, resolution="1080p" | 0.3 |
| duration=3, resolution="720p" | 0.3 |
| duration=3, resolution="1080p" | 0.45 |
| duration=4, resolution="720p" | 0.4 |
| duration=4, resolution="1080p" | 0.6 |
| duration=5, resolution="720p" | 0.5 |
| duration=5, resolution="1080p" | 0.75 |
| duration=6, resolution="720p" | 0.6 |
| duration=6, resolution="1080p" | 0.9 |
| duration=7, resolution="720p" | 0.7 |
| duration=7, resolution="1080p" | 1.05 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == '1080p' ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.7/text-to-video", "aspect_ratio": "9:16", "duration": 2, "prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.7/text-to-video', {'aspect_ratio': '9:16', 'duration': 2, 'prompt': 'A red paper lantern swaying gently in a quiet bamboo forest at dusk', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.7/text-to-video", {
  "aspect_ratio": "9:16",
  "duration": 2,
  "prompt": "A red paper lantern swaying gently in a quiet bamboo forest at dusk",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.7/text-to-video", sandbase.Params{
	"aspect_ratio": "9:16",
	"duration": 2,
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
| `prompt` | string | yes | The text prompt to generate a video from. default `"A young woman sitting by a rain-streaked window in a café, slowly turning to look at the camera with a gentle smile, warm interior lighting"` |
| `duration` | integer |  | The duration of the generated video in seconds. one of: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default `"16:9"` |

## Details

Write a scene and get back a 2–15 second clip with optional driving audio. Wan 2.7 improves motion smoothness and scene fidelity over 2.6 and keeps camera instructions more faithfully.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `duration` | 2–15 | 5 | Output length in seconds. |
| `audio` | audio URL | — | Optional WAV/MP3 URL that drives speech or rhythm in the clip. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` | `16:9` | Output frame shape. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.10 at 720p and $0.15 at 1080p, the same as Alibaba's list price.

| Output | 720p | 1080p |
|---|---|---|
| 2s | $0.20 | $0.30 |
| 5s (default) | $0.50 | $0.75 |
| 10s | $1.00 | $1.50 |
| 15s | $1.50 | $2.25 |

Failed runs are not charged.

### Prompting

- Describe the shot in order: subject, action, setting, camera move, light, and sound.
- Give camera timing explicitly, e.g. “holds for two seconds, then pushes in slowly”.
- Put spoken lines in quotes and say who speaks them.

> A young woman sits by a rain-streaked café window, slowly turns toward the camera and smiles; slow push-in, warm interior light, soft rain on the glass.

### Limits

- Text only; to start from your own picture use `alibaba/wan/2.7/image-to-video`.

### Also on SandBase

Other Wan 2.7 endpoints: `alibaba/wan/2.7/image-to-video`, `alibaba/wan/2.7/reference-to-video`, `alibaba/wan/2.7/video-edit`, `alibaba/wan/2.7/video-extend`, `alibaba/wan/3.0/video` (newer, up to 30s).

---
Machine-readable: [`catalog/models/alibaba/wan/2.7/text-to-video.json`](../../../../../catalog/models/alibaba/wan/2.7/text-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.7/text-to-video
