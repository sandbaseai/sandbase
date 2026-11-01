# Grok Imagine Video 1.5 Reference to Video

`xai/grok-imagine-video/1.5/reference-to-video` · video · xAI

Grok Imagine Video 1.5 is xAI's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.duration`, `params.images`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="480p" | 0.09 |
| duration=1, resolution="720p" | 0.15 |
| duration=8, resolution="480p" | 0.65 |
| duration=8, resolution="720p" | 1.13 |
| duration=15, resolution="480p" | 1.21 |
| duration=15, resolution="720p" | 2.11 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "720p" ? 0.14 : 0.08) + len(params.images ?? []) * 0.01`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/1.5/reference-to-video", "duration": 1, "images": ["https://static.sandbase.ai/examples/182071c8-4a68-49d6-8ddb-2e1ba5af7d4d/input/2e71e37f-fbf8-44ba-a7ad-c1a366f777bd.png"], "prompt": "the subject walks forward", "resolution": "480p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/1.5/reference-to-video', {'duration': 1, 'images': ['https://static.sandbase.ai/examples/182071c8-4a68-49d6-8ddb-2e1ba5af7d4d/input/2e71e37f-fbf8-44ba-a7ad-c1a366f777bd.png'], 'prompt': 'the subject walks forward', 'resolution': '480p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/1.5/reference-to-video", {
  "duration": 1,
  "images": [
    "https://static.sandbase.ai/examples/182071c8-4a68-49d6-8ddb-2e1ba5af7d4d/input/2e71e37f-fbf8-44ba-a7ad-c1a366f777bd.png"
  ],
  "prompt": "the subject walks forward",
  "resolution": "480p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/1.5/reference-to-video", sandbase.Params{
	"duration": 1,
	"images": []any{"https://static.sandbase.ai/examples/182071c8-4a68-49d6-8ddb-2e1ba5af7d4d/input/2e71e37f-fbf8-44ba-a7ad-c1a366f777bd.png"},
	"prompt": "the subject walks forward",
	"resolution": "480p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | One or more reference image URLs to guide the video generation as style and content references. Reference in prompt as <IMAGE_0>, <IMAGE_1>, etc. Maximum 7 images.  |
| `prompt` | string | yes | Text prompt describing the video. Tag references as <IMAGE_0>, <IMAGE_1>, etc.  |
| `duration` | integer |  | Video duration in seconds. default `8`; range 1–15 |
| `resolution` | string |  | Resolution of the output video. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |

## Details

Grok Imagine Video 1.5 reference-to-video: reference images keep characters and objects consistent in a 1–15 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output frame shape. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–15 | 8 | Output length in seconds. |
| `images` | image URL[], required | — | Reference images, Image 1, Image 2, … |

### Billing

Per output second: $0.08 at 480p and $0.14 at 720p, plus $0.01 per reference image.

| Output | 480p | 720p |
|---|---|---|
| 8s (default) | $0.65 | $1.13 |
| 15s | $1.21 | $2.11 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video 1.5 endpoints: `xai/grok-imagine-video/1.5/text-to-video`, `xai/grok-imagine-video/1.5/image-to-video`, `xai/grok-imagine-video/1.5/lite/text-to-video`, `xai/grok-imagine-video/1.5/lite/image-to-video`, `xai/grok-imagine-video/text-to-video` (previous version).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/1.5/reference-to-video.json`](../../../../../catalog/models/xai/grok-imagine-video/1.5/reference-to-video.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/1.5/reference-to-video
