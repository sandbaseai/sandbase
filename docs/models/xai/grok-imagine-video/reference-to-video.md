# Grok Imagine Video Reference to Video

`xai/grok-imagine-video/reference-to-video` · video · xAI

Grok Imagine Video is xAI's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="480p" | 0.052 |
| duration=1, resolution="720p" | 0.072 |
| duration=8, resolution="480p" | 0.402 |
| duration=8, resolution="720p" | 0.562 |
| duration=10, resolution="480p" | 0.502 |
| duration=10, resolution="720p" | 0.702 |

Formula: `(params.resolution ?? "720p") == "720p" ? (params.duration ?? 8) * 0.07 + 0.002 : (params.duration ?? 8) * 0.05 + 0.002`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/reference-to-video", "prompt": "A @Image1 running through a sunlit meadow, cinematic slow motion", "reference_image_urls": ["https://static.sandbase.ai/examples/1d487450-78ff-4d5a-87b2-0abdacea87d7/input/1bb4adf0-cb56-4abf-8133-5b627a7fd3ef.png"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/reference-to-video', {'prompt': 'A @Image1 running through a sunlit meadow, cinematic slow motion', 'reference_image_urls': ['https://static.sandbase.ai/examples/1d487450-78ff-4d5a-87b2-0abdacea87d7/input/1bb4adf0-cb56-4abf-8133-5b627a7fd3ef.png']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/reference-to-video", {
  "prompt": "A @Image1 running through a sunlit meadow, cinematic slow motion",
  "reference_image_urls": [
    "https://static.sandbase.ai/examples/1d487450-78ff-4d5a-87b2-0abdacea87d7/input/1bb4adf0-cb56-4abf-8133-5b627a7fd3ef.png"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/reference-to-video", sandbase.Params{
	"prompt": "A @Image1 running through a sunlit meadow, cinematic slow motion",
	"reference_image_urls": []any{"https://static.sandbase.ai/examples/1d487450-78ff-4d5a-87b2-0abdacea87d7/input/1bb4adf0-cb56-4abf-8133-5b627a7fd3ef.png"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text prompt describing the video to generate. Use @Image1, @Image2, etc. to reference specific images from reference_image_urls in order.  |
| `duration` | integer |  | Video duration in seconds. default `8`; range 1–10 |
| `resolution` | string |  | Resolution of the output video. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`; default `"16:9"` |
| `reference_image_urls` | array | yes | One or more reference image URLs to guide the video generation as style and content references. Reference in prompt as @Image1, @Image2, etc. Maximum 7 images.  |

## Details

Grok Imagine Video reference-to-video: up to 7 reference images keep characters and objects consistent in a 1–10 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `aspect_ratio` | `16:9` / `4:3` / `3:2` / `1:1` / `2:3` / `3:4` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–10 | 8 | Output length in seconds. |
| `reference_image_urls` | image URL[] (≤7), required | — | Reference images, up to 7. |

### Billing

$0.07 per output second at 720p and $0.05 at 480p, plus $0.002 per request.

| Output | 480p | 720p |
|---|---|---|
| 6s | $0.302 | $0.422 |
| 8s (default) | $0.402 | $0.562 |
| 10s | $0.502 | $0.702 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video endpoints: `xai/grok-imagine-video/text-to-video`, `xai/grok-imagine-video/image-to-video`, `xai/grok-imagine-video/video-edit`, `xai/grok-imagine-video/video-extend`, `xai/grok-imagine-video/1.5/text-to-video` (1.5, newer).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/reference-to-video.json`](../../../../catalog/models/xai/grok-imagine-video/reference-to-video.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/reference-to-video
