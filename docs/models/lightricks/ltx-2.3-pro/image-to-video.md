# LTX 2.3 Pro Image to Video

`lightricks/ltx-2.3-pro/image-to-video` · video · Lightricks

Ltx 2.3 Pro by Lightricks - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=6, resolution="1080p" | 0.48 |
| duration=6, resolution="1440p" | 0.96 |
| duration=6, resolution="2160p" | 1.92 |
| duration=8, resolution="1080p" | 0.64 |
| duration=8, resolution="1440p" | 1.28 |
| duration=8, resolution="2160p" | 2.56 |
| duration=10, resolution="1080p" | 0.8 |
| duration=10, resolution="1440p" | 1.6 |
| duration=10, resolution="2160p" | 3.2 |

Formula: `(params.resolution ?? "1080p") == "2160p" ? (params.duration ?? 6) * 0.32 : (params.resolution ?? "1080p") == "1440p" ? (params.duration ?? 6) * 0.16 : (params.duration ?? 6) * 0.08`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lightricks/ltx-2.3-pro/image-to-video", "image": "https://static.sandbase.ai/examples/c7d8f59e-6180-41d0-88b2-298746c79af5/input/823e934f-9302-48ed-8c09-73ade1f07336.png", "prompt": "Periscope-level shot from behind tall grass of two Maasai warriors mid-leap during an adumu jumping dance, bodies fully airborne against a golden savanna sunset, red shuka robes frozen in motion, dust kicked up from the earth catching backlight, 85mm f/1.4 isolating the pair from a blurred circle of onlookers, Steve McCurry meets Emmanuel Lubezki"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lightricks/ltx-2.3-pro/image-to-video', {'image': 'https://static.sandbase.ai/examples/c7d8f59e-6180-41d0-88b2-298746c79af5/input/823e934f-9302-48ed-8c09-73ade1f07336.png', 'prompt': 'Periscope-level shot from behind tall grass of two Maasai warriors mid-leap during an adumu jumping dance, bodies fully airborne against a golden savanna sunset, red shuka robes frozen in motion, dust kicked up from the earth catching backlight, 85mm f/1.4 isolating the pair from a blurred circle of onlookers, Steve McCurry meets Emmanuel Lubezki'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lightricks/ltx-2.3-pro/image-to-video", {
  "image": "https://static.sandbase.ai/examples/c7d8f59e-6180-41d0-88b2-298746c79af5/input/823e934f-9302-48ed-8c09-73ade1f07336.png",
  "prompt": "Periscope-level shot from behind tall grass of two Maasai warriors mid-leap during an adumu jumping dance, bodies fully airborne against a golden savanna sunset, red shuka robes frozen in motion, dust kicked up from the earth catching backlight, 85mm f/1.4 isolating the pair from a blurred circle of onlookers, Steve McCurry meets Emmanuel Lubezki"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lightricks/ltx-2.3-pro/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/c7d8f59e-6180-41d0-88b2-298746c79af5/input/823e934f-9302-48ed-8c09-73ade1f07336.png",
	"prompt": "Periscope-level shot from behind tall grass of two Maasai warriors mid-leap during an adumu jumping dance, bodies fully airborne against a golden savanna sunset, red shuka robes frozen in motion, dust kicked up from the earth catching backlight, 85mm f/1.4 isolating the pair from a blurred circle of onlookers, Steve McCurry meets Emmanuel Lubezki",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | The URL of the start image to use for the generated video.  |
| `prompt` | string | yes | The prompt to use for the generated video  |
| `duration` | integer |  | The duration of the generated video in seconds one of: `6`, `8`, `10`; default `6` |
| `end_image` | string |  | The URL of the end image to use for the generated video. When provided, generates a transition video between start and end frames.  |
| `resolution` | string |  | The resolution of the generated video one of: `1080p`, `1440p`, `2160p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input image. one of: `16:9`, `9:16` |
| `generate_audio` | boolean |  | Whether to generate audio for the generated video default `true` |

## Details

LTX 2.3 Pro image to video: 6–10 second clips with native audio at 1080p, 1440p, or 4K (2160p). `image` is the first frame; `end_image` optionally the last.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `resolution` | `1080p` / `1440p` / `2160p` | `1080p` | Sets the per-second rate. |
| `duration` | 6 / 8 / 10 | 6 | Output length in seconds. |
| `generate_audio` | boolean | true | Native audio. |
| `aspect_ratio` | `16:9` / `9:16` | — | Output frame shape. |

### Billing

You pay for output seconds: $0.08 at 1080p, $0.16 at 1440p, $0.32 at 2160p.

| Output | 1080p | 1440p | 2160p |
|---|---|---|---|
| 6s (default) | $0.48 | $0.96 | $1.92 |
| 8s | $0.64 | $1.28 | $2.56 |
| 10s | $0.80 | $1.60 | $3.20 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other LTX 2.3 endpoints: `lightricks/ltx-2.3-pro/text-to-video`, `lightricks/ltx-2.3-pro/audio-to-video`, `lightricks/ltx-2.3-pro/retake`, `lightricks/ltx-2.3-pro/video-extend`.

---
Machine-readable: [`catalog/models/lightricks/ltx-2.3-pro/image-to-video.json`](../../../../catalog/models/lightricks/ltx-2.3-pro/image-to-video.json) · Store page: https://www.sandbase.ai/model/lightricks/ltx-2.3-pro/image-to-video
