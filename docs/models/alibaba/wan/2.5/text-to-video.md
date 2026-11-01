# Wan 2.5 Text to Video

`alibaba/wan/2.5/text-to-video` · video · Alibaba

Wan 2.5 is Alibaba's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="480p" | 0.25 |
| duration=5, resolution="720p" | 0.5 |
| duration=5, resolution="1080p" | 0.75 |
| duration=10, resolution="480p" | 0.5 |
| duration=10, resolution="720p" | 1 |
| duration=10, resolution="1080p" | 1.5 |

Formula: `(params.resolution ?? "720p") == "1080p" ? (params.duration ?? 5) * 0.15 : (params.resolution ?? "720p") == "720p" ? (params.duration ?? 5) * 0.10 : (params.duration ?? 5) * 0.05`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.5/text-to-video", "prompt": "The white dragon warrior stands still, eyes full of determination and strength. The camera slowly moves closer or circles around the warrior, highlighting the powerful presence and heroic spirit of the character."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.5/text-to-video', {'prompt': 'The white dragon warrior stands still, eyes full of determination and strength. The camera slowly moves closer or circles around the warrior, highlighting the powerful presence and heroic spirit of the character.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.5/text-to-video", {
  "prompt": "The white dragon warrior stands still, eyes full of determination and strength. The camera slowly moves closer or circles around the warrior, highlighting the powerful presence and heroic spirit of the character."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.5/text-to-video", sandbase.Params{
	"prompt": "The white dragon warrior stands still, eyes full of determination and strength. The camera slowly moves closer or circles around the warrior, highlighting the powerful presence and heroic spirit of the character.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility. If None, a random seed is chosen.  |
| `audio` | string |  | URL of the audio to use as the background music. Must be publicly accessible. Limit handling: If the audio duration exceeds the duration value (5 or 10 seconds), the audio is truncated to the first 5 or 10 seconds, and…  |
| `prompt` | string | yes | The text prompt for video generation. Supports Chinese and English, max 800 characters.  |
| `duration` | integer |  | Duration of the generated video in seconds. Choose between 5 or 10 seconds. one of: `5`, `10`; default `5` |
| `resolution` | string |  | Video resolution tier one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default `"16:9"` |

## Details

Wan 2.5 text-to-video: a 5 or 10 second clip from a written scene, with optional driving audio. Newer Wan versions are listed below.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` | `16:9` | Output frame shape. |
| `audio` | audio URL | — | Optional WAV/MP3 URL that drives speech or rhythm. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.05 at 480p, $0.10 at 720p, and $0.15 at 1080p.

| Output | 480p | 720p | 1080p |
|---|---|---|---|
| 5s (default) | $0.25 | $0.50 | $0.75 |
| 10s | $0.50 | $1.00 | $1.50 |

Failed runs are not charged.

### Prompting

- Describe the shot in order: subject, action, setting, camera move, light, and sound.
- Give camera timing explicitly, e.g. “holds for two seconds, then pushes in slowly”.

### Limits

- Durations are 5 or 10 seconds only.

### Also on SandBase

Other Wan 2.5 endpoints: `alibaba/wan/2.5/image-to-video`, `alibaba/wan/2.5/text-to-image`, `alibaba/wan/2.5/image-to-image`, `alibaba/wan/2.7/text-to-video` (newer).

---
Machine-readable: [`catalog/models/alibaba/wan/2.5/text-to-video.json`](../../../../../catalog/models/alibaba/wan/2.5/text-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.5/text-to-video
