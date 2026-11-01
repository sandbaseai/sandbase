# LTX 2.3 Pro Audio to Video

`lightricks/ltx-2.3-pro/audio-to-video` · video · Lightricks

Ltx 2.3 Pro Audio To Video by Lightricks - advanced AI model for audio-to-video. Delivers high-quality results with fast inference, suitable for both creative and production workflows.

## Pricing

- Depends on parameters (`params.audio`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.audio) ?? 5.0) * 0.10`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lightricks/ltx-2.3-pro/audio-to-video", "audio": "https://static.sandbase.ai/examples/d329ed93-dcc3-4816-a380-9ef3c56b9ed8/input/033e9797-2daf-4d8b-aae3-74eee1a9b8d6.mp3", "image": "https://static.sandbase.ai/examples/d329ed93-dcc3-4816-a380-9ef3c56b9ed8/input/c790a0f6-daad-468d-ad20-666837bc95ba.png", "prompt": "A woman whispering to the microphone"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lightricks/ltx-2.3-pro/audio-to-video', {'audio': 'https://static.sandbase.ai/examples/d329ed93-dcc3-4816-a380-9ef3c56b9ed8/input/033e9797-2daf-4d8b-aae3-74eee1a9b8d6.mp3', 'image': 'https://static.sandbase.ai/examples/d329ed93-dcc3-4816-a380-9ef3c56b9ed8/input/c790a0f6-daad-468d-ad20-666837bc95ba.png', 'prompt': 'A woman whispering to the microphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lightricks/ltx-2.3-pro/audio-to-video", {
  "audio": "https://static.sandbase.ai/examples/d329ed93-dcc3-4816-a380-9ef3c56b9ed8/input/033e9797-2daf-4d8b-aae3-74eee1a9b8d6.mp3",
  "image": "https://static.sandbase.ai/examples/d329ed93-dcc3-4816-a380-9ef3c56b9ed8/input/c790a0f6-daad-468d-ad20-666837bc95ba.png",
  "prompt": "A woman whispering to the microphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lightricks/ltx-2.3-pro/audio-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/d329ed93-dcc3-4816-a380-9ef3c56b9ed8/input/033e9797-2daf-4d8b-aae3-74eee1a9b8d6.mp3",
	"image": "https://static.sandbase.ai/examples/d329ed93-dcc3-4816-a380-9ef3c56b9ed8/input/c790a0f6-daad-468d-ad20-666837bc95ba.png",
	"prompt": "A woman whispering to the microphone",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audio` | string | yes | URL of the audio file to generate a video from. Duration must be between 2 and 20 seconds. Must be publicly accessible or base64 data URI.  |
| `image` | string | yes | URL of an image to use as the first frame of the video. If not provided, prompt is required.  |
| `prompt` | string | yes | Text description of how the video should be generated. Required if image_url is not provided. When image_url is provided, this describes how the image should be animated.  |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input media. one of: `16:9`, `9:16` |

## Details

LTX 2.3 Pro audio-to-video: animate an image into a video that follows an audio track, such as a voice or song.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `image` | image URL, required | — | Image to animate. JPEG, PNG, or WebP URL. |
| `audio` | audio URL, required | — | Audio that drives the video. |
| `aspect_ratio` | `16:9` / `9:16` | — | Output frame shape. |

### Billing

$0.10 per output second; the output is as long as the audio. The quote before submission assumes 5 seconds.

| Audio | Price |
|---|---|
| 5s audio | $0.50 |
| 10s audio | $1.00 |
| 20s audio | $2.00 |

Failed runs are not charged.

### Prompting

- Describe the scene and motion; timing follows the audio.

### Also on SandBase

Other LTX 2.3 endpoints: `lightricks/ltx-2.3-pro/text-to-video`, `lightricks/ltx-2.3-pro/image-to-video`, `lightricks/ltx-2.3-pro/retake`, `lightricks/ltx-2.3-pro/video-extend`.

---
Machine-readable: [`catalog/models/lightricks/ltx-2.3-pro/audio-to-video.json`](../../../../catalog/models/lightricks/ltx-2.3-pro/audio-to-video.json) · Store page: https://www.sandbase.ai/model/lightricks/ltx-2.3-pro/audio-to-video
