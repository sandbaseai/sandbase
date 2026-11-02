# PixVerse V6 Image to Video API: pricing, parameters and code examples

`pixverse/v6/image-to-video` · video generation model · PixVerse · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.025 to $1.725 per run, depending on parameters · **Modes:** async

V6 is PixVerse's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio_switch`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, generate_audio_switch=false, resolution="360p" | 0.025 |
| duration=1, generate_audio_switch=false, resolution="540p" | 0.035 |
| duration=1, generate_audio_switch=false, resolution="720p" | 0.045 |
| duration=1, generate_audio_switch=false, resolution="1080p" | 0.09 |
| duration=1, generate_audio_switch=true, resolution="360p" | 0.035 |
| duration=1, generate_audio_switch=true, resolution="540p" | 0.045 |
| duration=1, generate_audio_switch=true, resolution="720p" | 0.06 |
| duration=1, generate_audio_switch=true, resolution="1080p" | 0.115 |
| duration=5, generate_audio_switch=false, resolution="360p" | 0.125 |
| duration=5, generate_audio_switch=false, resolution="540p" | 0.175 |
| duration=5, generate_audio_switch=false, resolution="720p" | 0.225 |
| duration=5, generate_audio_switch=false, resolution="1080p" | 0.45 |
| duration=5, generate_audio_switch=true, resolution="360p" | 0.175 |
| duration=5, generate_audio_switch=true, resolution="540p" | 0.225 |
| duration=5, generate_audio_switch=true, resolution="720p" | 0.3 |
| duration=5, generate_audio_switch=true, resolution="1080p" | 0.575 |
| duration=15, generate_audio_switch=false, resolution="360p" | 0.375 |
| duration=15, generate_audio_switch=false, resolution="540p" | 0.525 |
| duration=15, generate_audio_switch=false, resolution="720p" | 0.675 |
| duration=15, generate_audio_switch=false, resolution="1080p" | 1.35 |
| duration=15, generate_audio_switch=true, resolution="360p" | 0.525 |
| duration=15, generate_audio_switch=true, resolution="540p" | 0.675 |
| duration=15, generate_audio_switch=true, resolution="720p" | 0.9 |
| duration=15, generate_audio_switch=true, resolution="1080p" | 1.725 |

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pixverse/v6/image-to-video", "image": "https://static.sandbase.ai/examples/d4f66263-064a-477b-9a97-bcc82efe6328/input/6813c620-675d-4c6b-ae6d-27616b6f440d.png", "prompt": "A woman warrior with her hammer walking with his glacier wolf."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pixverse/v6/image-to-video', {'image': 'https://static.sandbase.ai/examples/d4f66263-064a-477b-9a97-bcc82efe6328/input/6813c620-675d-4c6b-ae6d-27616b6f440d.png', 'prompt': 'A woman warrior with her hammer walking with his glacier wolf.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pixverse/v6/image-to-video", {
  "image": "https://static.sandbase.ai/examples/d4f66263-064a-477b-9a97-bcc82efe6328/input/6813c620-675d-4c6b-ae6d-27616b6f440d.png",
  "prompt": "A woman warrior with her hammer walking with his glacier wolf."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pixverse/v6/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/d4f66263-064a-477b-9a97-bcc82efe6328/input/6813c620-675d-4c6b-ae6d-27616b6f440d.png",
	"prompt": "A woman warrior with her hammer walking with his glacier wolf.",
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
| `style` | string |  | The style of the generated video one of: `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk` |
| `prompt` | string | yes | Prompt  |
| `duration` | integer |  | The duration of the generated video in seconds. v6 supports values from 1 to 15 seconds default `5`; range 1–15 |
| `resolution` | string |  | The resolution of the generated video one of: `360p`, `540p`, `720p`, `1080p`; default `"720p"` |
| `generate_audio_switch` | boolean |  | Enable audio generation (BGM, SFX, dialogue) default `false` |

## Details

PixVerse V6 image-to-video: animate a picture into a 1–15 second clip, with optional generated audio and style presets.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `resolution` | `360p` / `540p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–15 | 5 | Output length in seconds. |
| `style` | `anime` / `3d_animation` / `clay` / `comic` / `cyberpunk` | — | Optional style preset. |
| `generate_audio_switch` | boolean | false | Generate audio; raises the rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay per output second; the rate depends on resolution and whether audio is on:

| Output | 360p | 540p | 720p | 1080p |
|---|---|---|---|---|
| 5s (default) | $0.125 | $0.175 | $0.225 | $0.45 |
| 10s | $0.25 | $0.35 | $0.45 | $0.90 |
| 5s with audio | $0.175 | $0.225 | $0.30 | $0.575 |

Failed runs are not charged.

### Prompting

- Describe the motion and camera in one or two sentences.

### Also on SandBase

Related: `pixverse/c1/image-to-video`.

---
Machine-readable: [`catalog/models/pixverse/v6/image-to-video.json`](../../../../catalog/models/pixverse/v6/image-to-video.json) · Store page: https://www.sandbase.ai/model/pixverse/v6/image-to-video
