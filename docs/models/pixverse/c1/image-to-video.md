# PixVerse C1 Image to Video

`pixverse/c1/image-to-video` · video · PixVerse

C1 is PixVerse's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio_switch`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, generate_audio_switch=false, resolution="360p" | 0.03 |
| duration=1, generate_audio_switch=false, resolution="540p" | 0.04 |
| duration=1, generate_audio_switch=false, resolution="720p" | 0.05 |
| duration=1, generate_audio_switch=false, resolution="1080p" | 0.095 |
| duration=1, generate_audio_switch=true, resolution="360p" | 0.04 |
| duration=1, generate_audio_switch=true, resolution="540p" | 0.05 |
| duration=1, generate_audio_switch=true, resolution="720p" | 0.065 |
| duration=1, generate_audio_switch=true, resolution="1080p" | 0.12 |
| duration=5, generate_audio_switch=false, resolution="360p" | 0.15 |
| duration=5, generate_audio_switch=false, resolution="540p" | 0.2 |
| duration=5, generate_audio_switch=false, resolution="720p" | 0.25 |
| duration=5, generate_audio_switch=false, resolution="1080p" | 0.475 |
| duration=5, generate_audio_switch=true, resolution="360p" | 0.2 |
| duration=5, generate_audio_switch=true, resolution="540p" | 0.25 |
| duration=5, generate_audio_switch=true, resolution="720p" | 0.325 |
| duration=5, generate_audio_switch=true, resolution="1080p" | 0.6 |
| duration=15, generate_audio_switch=false, resolution="360p" | 0.45 |
| duration=15, generate_audio_switch=false, resolution="540p" | 0.6 |
| duration=15, generate_audio_switch=false, resolution="720p" | 0.75 |
| duration=15, generate_audio_switch=false, resolution="1080p" | 1.425 |
| duration=15, generate_audio_switch=true, resolution="360p" | 0.6 |
| duration=15, generate_audio_switch=true, resolution="540p" | 0.75 |
| duration=15, generate_audio_switch=true, resolution="720p" | 0.975 |
| duration=15, generate_audio_switch=true, resolution="1080p" | 1.8 |

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pixverse/c1/image-to-video", "prompt": "<prompt>", "image": "<image>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pixverse/c1/image-to-video', {'prompt': '<prompt>', 'image': '<image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pixverse/c1/image-to-video", {
  "prompt": "<prompt>",
  "image": "<image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pixverse/c1/image-to-video", sandbase.Params{
	"prompt": "<prompt>",
	"image": "<image>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | The same seed and the same prompt given to the same version of the model will output the same video every time.  |
| `image` | string | yes | URL of the image to use as the first frame  |
| `prompt` | string | yes | Prompt  |
| `duration` | integer |  | The duration of the generated video in seconds (1-15) default `5`; range 1–15 |
| `resolution` | string |  | The resolution of the generated video one of: `360p`, `540p`, `720p`, `1080p`; default `"720p"` |
| `generate_audio_switch` | boolean |  | Enable audio generation (BGM, SFX, dialogue) default `false` |

## Details

PixVerse C1 image-to-video: animate a picture into a 1–15 second clip, with optional generated audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `resolution` | `360p` / `540p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–15 | 5 | Output length in seconds. |
| `generate_audio_switch` | boolean | false | Generate audio; raises the rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay per output second; the rate depends on resolution and whether audio is on:

| Output | 360p | 540p | 720p | 1080p |
|---|---|---|---|---|
| 5s (default) | $0.15 | $0.20 | $0.25 | $0.475 |
| 10s | $0.30 | $0.40 | $0.50 | $0.95 |
| 5s with audio | $0.20 | $0.25 | $0.325 | $0.60 |

Failed runs are not charged.

### Prompting

- Describe the motion and camera in one or two sentences.

### Also on SandBase

Related: `pixverse/v6/image-to-video`.

---
Machine-readable: [`catalog/models/pixverse/c1/image-to-video.json`](../../../../catalog/models/pixverse/c1/image-to-video.json) · Store page: https://www.sandbase.ai/model/pixverse/c1/image-to-video
