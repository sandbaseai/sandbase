# LTX 2.3 Fast Image to Video API: pricing, parameters and code examples

`lightricks/ltx-2.3-fast/image-to-video` · video generation model · Lightricks · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.36 to $3.84 per run, depending on parameters · **Modes:** async

Ltx 2.3 Fast is Lightricks's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=6, resolution="1080p" | 0.36 |
| duration=6, resolution="1440p" | 0.72 |
| duration=6, resolution="2160p" | 1.44 |
| duration=8, resolution="1080p" | 0.48 |
| duration=8, resolution="1440p" | 0.96 |
| duration=8, resolution="2160p" | 1.92 |
| duration=10, resolution="1080p" | 0.6 |
| duration=10, resolution="1440p" | 1.2 |
| duration=10, resolution="2160p" | 2.4 |
| duration=12, resolution="1080p" | 0.72 |
| duration=12, resolution="1440p" | 1.44 |
| duration=12, resolution="2160p" | 2.88 |
| duration=14, resolution="1080p" | 0.84 |
| duration=14, resolution="1440p" | 1.68 |
| duration=14, resolution="2160p" | 3.36 |
| duration=16, resolution="1080p" | 0.96 |
| duration=16, resolution="1440p" | 1.92 |
| duration=16, resolution="2160p" | 3.84 |

Formula: `(params.resolution ?? "1080p") == "2160p" ? (params.duration ?? 6) * 0.24 : (params.resolution ?? "1080p") == "1440p" ? (params.duration ?? 6) * 0.12 : (params.duration ?? 6) * 0.06`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lightricks/ltx-2.3-fast/image-to-video", "image": "https://static.sandbase.ai/examples/78072a01-7219-4993-a8f3-089836e6ad15/input/cc432447-c109-463d-a28b-0e4b21c66923.png", "prompt": "Snorkel lens ground-scraping tracking shot following a barefoot Ethiopian long-distance runner training on a dirt road at dawn, camera inches from the ground racing alongside, her feet kicking up red dust in slow motion at 240fps, Rift Valley landscape blurred in the background, the texture of earth and callused skin in hyper-detail, 40mm snorkel lens at ground height, Nike Running documentary meets Lubezki natural light, the poetry of human endurance"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lightricks/ltx-2.3-fast/image-to-video', {'image': 'https://static.sandbase.ai/examples/78072a01-7219-4993-a8f3-089836e6ad15/input/cc432447-c109-463d-a28b-0e4b21c66923.png', 'prompt': 'Snorkel lens ground-scraping tracking shot following a barefoot Ethiopian long-distance runner training on a dirt road at dawn, camera inches from the ground racing alongside, her feet kicking up red dust in slow motion at 240fps, Rift Valley landscape blurred in the background, the texture of earth and callused skin in hyper-detail, 40mm snorkel lens at ground height, Nike Running documentary meets Lubezki natural light, the poetry of human endurance'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lightricks/ltx-2.3-fast/image-to-video", {
  "image": "https://static.sandbase.ai/examples/78072a01-7219-4993-a8f3-089836e6ad15/input/cc432447-c109-463d-a28b-0e4b21c66923.png",
  "prompt": "Snorkel lens ground-scraping tracking shot following a barefoot Ethiopian long-distance runner training on a dirt road at dawn, camera inches from the ground racing alongside, her feet kicking up red dust in slow motion at 240fps, Rift Valley landscape blurred in the background, the texture of earth and callused skin in hyper-detail, 40mm snorkel lens at ground height, Nike Running documentary meets Lubezki natural light, the poetry of human endurance"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lightricks/ltx-2.3-fast/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/78072a01-7219-4993-a8f3-089836e6ad15/input/cc432447-c109-463d-a28b-0e4b21c66923.png",
	"prompt": "Snorkel lens ground-scraping tracking shot following a barefoot Ethiopian long-distance runner training on a dirt road at dawn, camera inches from the ground racing alongside, her feet kicking up red dust in slow motion at 240fps, Rift Valley landscape blurred in the background, the texture of earth and callused skin in hyper-detail, 40mm snorkel lens at ground height, Nike Running documentary meets Lubezki natural light, the poetry of human endurance",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the image to generate the video from. Must be publicly accessible or base64 data URI. Supports PNG, JPEG, WebP, AVIF, and HEIF formats.  |
| `prompt` | string | yes | The prompt to generate the video from  |
| `duration` | integer |  | The duration of the generated video in seconds. The fast model supports 6-20 seconds. Note: Durations longer than 10 seconds (12, 14, 16, 18, 20) are only supported with 25 FPS and 1080p resolution. one of: `6`, `8`, `10`, `12`, `14`, `16`, `18`, `20`; default `6` |
| `end_image` | string |  | The URL of the end image to use for the generated video. When provided, generates a transition video between start and end frames.  |
| `resolution` | string |  | The resolution of the generated video one of: `1080p`, `1440p`, `2160p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input image. one of: `16:9`, `9:16` |
| `generate_audio` | boolean |  | Whether to generate audio for the generated video default `true` |

## Details

LTX 2.3 Fast image to video: up to 20 second clips with native audio at 1080p, 1440p, or 4K (2160p). `image` is the first frame; `end_image` optionally the last.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `resolution` | `1080p` / `1440p` / `2160p` | `1080p` | Sets the per-second rate. |
| `duration` | 6 / 8 / 10 / 12 / 14 / 16 / 18 / 20 | 6 | Output length in seconds. |
| `generate_audio` | boolean | true | Native audio. |
| `aspect_ratio` | `16:9` / `9:16` | — | Output frame shape. |

### Billing

You pay for output seconds: $0.06 at 1080p, $0.12 at 1440p, $0.24 at 2160p.

| Output | 1080p | 1440p | 2160p |
|---|---|---|---|
| 6s (default) | $0.36 | $0.72 | $1.44 |
| 10s | $0.60 | $1.20 | $2.40 |
| 20s | $1.20 | $2.40 | $4.80 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other LTX 2.3 endpoints: `lightricks/ltx-2.3-pro/text-to-video`, `lightricks/ltx-2.3-pro/image-to-video`, `lightricks/ltx-2.3-pro/audio-to-video`, `lightricks/ltx-2.3-pro/retake`.

---
Machine-readable: [`catalog/models/lightricks/ltx-2.3-fast/image-to-video.json`](../../../../catalog/models/lightricks/ltx-2.3-fast/image-to-video.json) · Store page: https://www.sandbase.ai/model/lightricks/ltx-2.3-fast/image-to-video
