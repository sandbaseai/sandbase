# Vidu Q4 Reference to Video API: pricing, parameters and code examples

`vidu/q4/reference-to-video` · video generation model · Vidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.135 to $6.24 per run, depending on parameters · **Modes:** async

Vidu Q4 Preview by Shengshu builds a 3 to 16 second video at up to 4K from up to 12 reference images and 3 voice clips, keeping characters, products, and voices consistent across the clip.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="540p" | 0.135 |
| duration=3, resolution="720p" | 0.285 |
| duration=3, resolution="1080p" | 0.36 |
| duration=3, resolution="2K" | 0.57 |
| duration=3, resolution="4K" | 1.17 |
| duration=5, resolution="540p" | 0.225 |
| duration=5, resolution="720p" | 0.475 |
| duration=5, resolution="1080p" | 0.6 |
| duration=5, resolution="2K" | 0.95 |
| duration=5, resolution="4K" | 1.95 |
| duration=16, resolution="540p" | 0.72 |
| duration=16, resolution="720p" | 1.52 |
| duration=16, resolution="1080p" | 1.92 |
| duration=16, resolution="2K" | 3.04 |
| duration=16, resolution="4K" | 6.24 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == "4K" ? 0.39 : (params.resolution ?? "720p") == "2K" ? 0.19 : (params.resolution ?? "720p") == "1080p" ? 0.12 : (params.resolution ?? "720p") == "540p" ? 0.045 : 0.095)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vidu/q4/reference-to-video", "aspect_ratio": "16:9", "prompt": "[@reference_image_1] waddles across the sunny sand of [@reference_image_2], stops at the shell, sniffs it curiously and flaps its small wings with a happy chirp as waves roll in.", "reference_image_urls": ["https://static.sandbase.ai/examples/ea55f5ce-2b72-4369-b2dd-7aae51f770e5/input/127f444c-b589-4225-9dd1-22597400ba65.png", "https://static.sandbase.ai/examples/ea55f5ce-2b72-4369-b2dd-7aae51f770e5/input/5958a2b3-3eeb-479a-b5c2-65eeabee22fe.png"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vidu/q4/reference-to-video', {'aspect_ratio': '16:9', 'prompt': '[@reference_image_1] waddles across the sunny sand of [@reference_image_2], stops at the shell, sniffs it curiously and flaps its small wings with a happy chirp as waves roll in.', 'reference_image_urls': ['https://static.sandbase.ai/examples/ea55f5ce-2b72-4369-b2dd-7aae51f770e5/input/127f444c-b589-4225-9dd1-22597400ba65.png', 'https://static.sandbase.ai/examples/ea55f5ce-2b72-4369-b2dd-7aae51f770e5/input/5958a2b3-3eeb-479a-b5c2-65eeabee22fe.png']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vidu/q4/reference-to-video", {
  "aspect_ratio": "16:9",
  "prompt": "[@reference_image_1] waddles across the sunny sand of [@reference_image_2], stops at the shell, sniffs it curiously and flaps its small wings with a happy chirp as waves roll in.",
  "reference_image_urls": [
    "https://static.sandbase.ai/examples/ea55f5ce-2b72-4369-b2dd-7aae51f770e5/input/127f444c-b589-4225-9dd1-22597400ba65.png",
    "https://static.sandbase.ai/examples/ea55f5ce-2b72-4369-b2dd-7aae51f770e5/input/5958a2b3-3eeb-479a-b5c2-65eeabee22fe.png"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vidu/q4/reference-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "[@reference_image_1] waddles across the sunny sand of [@reference_image_2], stops at the shell, sniffs it curiously and flaps its small wings with a happy chirp as waves roll in.",
	"reference_image_urls": []any{"https://static.sandbase.ai/examples/ea55f5ce-2b72-4369-b2dd-7aae51f770e5/input/127f444c-b589-4225-9dd1-22597400ba65.png", "https://static.sandbase.ai/examples/ea55f5ce-2b72-4369-b2dd-7aae51f770e5/input/5958a2b3-3eeb-479a-b5c2-65eeabee22fe.png"},
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
| `audio` | boolean |  | Whether to generate audio (dialogue and sound effects) with the video. When false, the output video is silent. default `true` |
| `prompt` | string | yes | Text prompt for video generation, max 5000 characters. Refer to references by position: [@reference_image_1], [@reference_image_2], ... for images and [reference_audio_1], [reference_audio_2], ... for audio clips.  |
| `duration` | integer |  | Duration of the video in seconds (3-16) default `5`; range 3–16 |
| `resolution` | string |  | Output video resolution. Sets the per-second rate. one of: `540p`, `720p`, `1080p`, `2K`, `4K`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the output video. one of: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`; default `"16:9"` |
| `reference_audio_urls` | array |  | URLs of up to 3 mp3 reference audio clips (3-12 seconds each, max 50 MB) used to keep voices consistent.  |
| `reference_image_urls` | array | yes | URLs of 1 to 12 reference images (png, jpeg, jpg, webp) used to keep characters, products, objects, or locations consistent.  |

## Details

Vidu Q4 Preview reference-to-video: build a 3–16 second clip at up to 4K from up to 12 reference images and 3 voice clips, keeping characters, products, and voices consistent.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. Tag references as `[@reference_image_1]` and `[reference_audio_1]`. |
| `reference_image_urls` | image URL[], required | — | 1–12 images of characters, products, objects, or locations. |
| `reference_audio_urls` | audio URL[] | — | Up to 3 mp3 clips, 3–12 seconds each, for voice consistency. |
| `aspect_ratio` | `16:9` / `9:16` / `4:3` / `3:4` / `1:1` | `16:9` | Output frame shape. |
| `audio` | boolean | true | Generate dialogue and sound effects. Same price on or off. |
| `resolution` | `540p` / `720p` / `1080p` / `2K` / `4K` | `720p` | Sets the per-second rate. |
| `duration` | integer 3–16 | 5 | Output length in seconds. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.045 at 540p, $0.095 at 720p, $0.12 at 1080p, $0.19 at 2K, $0.39 at 4K.

| Output | 540p | 720p | 1080p | 2K | 4K |
|---|---|---|---|---|---|
| 3s | $0.135 | $0.285 | $0.36 | $0.57 | $1.17 |
| 5s (default) | $0.225 | $0.475 | $0.60 | $0.95 | $1.95 |
| 8s | $0.36 | $0.76 | $0.96 | $1.52 | $3.12 |
| 16s | $0.72 | $1.52 | $1.92 | $3.04 | $6.24 |

Failed runs are not charged.

### Prompting

- Refer to each reference by its position in the list, for example `[@reference_image_2]` holds the product.
- Describe subject, action, camera, and sound. Put spoken lines in quotes.

### Also on SandBase

`vidu/q4/image-to-video` animates a single first frame. Vidu Q3 endpoints such as `vidu/q3/reference-to-video/mix` remain available.

---
Machine-readable: [`catalog/models/vidu/q4/reference-to-video.json`](../../../../catalog/models/vidu/q4/reference-to-video.json) · Store page: https://www.sandbase.ai/model/vidu/q4/reference-to-video
