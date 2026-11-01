# Wan 2.2 Speech to Video

`alibaba/wan/2.2/speech-to-video` · video · Alibaba

Wan 2.2 Speech to Video turns a portrait image and a speech audio into a talking video guided by a prompt.

## Pricing

- Depends on parameters (`params.num_frames`, `params.resolution`, `usage.duration`, `usage.fps`).

Formula: `((usage.duration ?? ((params.num_frames ?? 80) / 16.0)) * (usage.fps ?? 16.0) / 16.0) * ((params.resolution ?? "720p") == "720p" ? 0.20 : (params.resolution ?? "720p") == "580p" ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.2/speech-to-video", "audio": "https://static.sandbase.ai/examples/1e330d15-cead-4a6f-95c7-573cdf0002b4/input/a299cae5-adf2-4f2e-a69b-110e1cf5d1a1.wav", "image": "https://static.sandbase.ai/examples/1e330d15-cead-4a6f-95c7-573cdf0002b4/input/2e0cf355-04f3-49ac-9998-f9d7a51e8f19.png", "prompt": "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.2/speech-to-video', {'audio': 'https://static.sandbase.ai/examples/1e330d15-cead-4a6f-95c7-573cdf0002b4/input/a299cae5-adf2-4f2e-a69b-110e1cf5d1a1.wav', 'image': 'https://static.sandbase.ai/examples/1e330d15-cead-4a6f-95c7-573cdf0002b4/input/2e0cf355-04f3-49ac-9998-f9d7a51e8f19.png', 'prompt': 'Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.2/speech-to-video", {
  "audio": "https://static.sandbase.ai/examples/1e330d15-cead-4a6f-95c7-573cdf0002b4/input/a299cae5-adf2-4f2e-a69b-110e1cf5d1a1.wav",
  "image": "https://static.sandbase.ai/examples/1e330d15-cead-4a6f-95c7-573cdf0002b4/input/2e0cf355-04f3-49ac-9998-f9d7a51e8f19.png",
  "prompt": "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.2/speech-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/1e330d15-cead-4a6f-95c7-573cdf0002b4/input/a299cae5-adf2-4f2e-a69b-110e1cf5d1a1.wav",
	"image": "https://static.sandbase.ai/examples/1e330d15-cead-4a6f-95c7-573cdf0002b4/input/2e0cf355-04f3-49ac-9998-f9d7a51e8f19.png",
	"prompt": "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard.",
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
| `num_frames` | integer |  | Frames to generate (40–120, multiple of 4) at 16 fps. default `80`; range 40–120 |
| `resolution` | string |  | Output resolution. one of: `480p`, `580p`, `720p`; default `"720p"` |
| `negative_prompt` | string |  | Content to avoid. default `""` |

## Details

Turn a portrait and a speech track into a talking video. Wan 2.2 lip-syncs the face in `image` to `audio` and animates head and body movement; the prompt sets the scene and gestures.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `image` | image URL, required | — | Portrait to animate. JPEG, PNG, or WebP URL. |
| `audio` | audio URL, required | — | Speech track (WAV/MP3) that drives the lips. |
| `num_frames` | integer 40–120 | 80 | Frames to generate (40–120, 16 frames per second of video). |
| `resolution` | `480p` / `580p` / `720p` | `720p` | Sets the rate. |
| `negative_prompt` | string | — | What to avoid. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

Billed per output second at the upstream rate: $0.10 at 480p, $0.15 at 580p, $0.20 at 720p. The default 80 frames is 5 seconds.

| Output | 480p | 580p | 720p |
|---|---|---|---|
| 80 frames (5s, default) | $0.50 | $0.75 | $1.00 |
| 120 frames (7.5s) | $0.75 | $1.125 | $1.50 |

Failed runs are not charged.

### Prompting

- Describe gestures and setting; the lips follow the audio automatically.
- Use a front-facing portrait with the mouth clearly visible.

### Limits

- Up to 120 frames (7.5 seconds) per request.

### Also on SandBase

Other Wan 2.2 endpoints: `alibaba/wan/2.2/animate/move`, `alibaba/wan/2.2/animate/replace`.

---
Machine-readable: [`catalog/models/alibaba/wan/2.2/speech-to-video.json`](../../../../../catalog/models/alibaba/wan/2.2/speech-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.2/speech-to-video
