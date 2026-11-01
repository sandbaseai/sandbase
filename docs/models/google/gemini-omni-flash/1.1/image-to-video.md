# Gemini Omni Flash 1.1 Image to Video

`google/gemini-omni-flash/1.1/image-to-video` · video · Google

Gemini Omni Flash 1.1 by Google - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="360p" | 0.09 |
| duration=3, resolution="720p" | 0.3 |
| duration=3, resolution="1080p" | 0.45 |
| duration=3, resolution="4k" | 0.9 |
| duration=8, resolution="360p" | 0.24 |
| duration=8, resolution="720p" | 0.8 |
| duration=8, resolution="1080p" | 1.2 |
| duration=8, resolution="4k" | 2.4 |
| duration=10, resolution="360p" | 0.3 |
| duration=10, resolution="720p" | 1 |
| duration=10, resolution="1080p" | 1.5 |
| duration=10, resolution="4k" | 3 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "360p" ? 0.03 : (params.resolution ?? "720p") == "1080p" ? 0.15 : (params.resolution ?? "720p") == "4k" ? 0.30 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/1.1/image-to-video", "duration": 3, "image": "https://static.sandbase.ai/examples/fc598f89-5a31-4128-9ff2-27c7f832b32c/input/57599f04-ed55-4178-8f81-6a3ea09fdddb.jpg", "prompt": "The waves roll gently onto the shore, slow camera push-in, no dialogue", "resolution": "360p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/1.1/image-to-video', {'duration': 3, 'image': 'https://static.sandbase.ai/examples/fc598f89-5a31-4128-9ff2-27c7f832b32c/input/57599f04-ed55-4178-8f81-6a3ea09fdddb.jpg', 'prompt': 'The waves roll gently onto the shore, slow camera push-in, no dialogue', 'resolution': '360p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/1.1/image-to-video", {
  "duration": 3,
  "image": "https://static.sandbase.ai/examples/fc598f89-5a31-4128-9ff2-27c7f832b32c/input/57599f04-ed55-4178-8f81-6a3ea09fdddb.jpg",
  "prompt": "The waves roll gently onto the shore, slow camera push-in, no dialogue",
  "resolution": "360p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/1.1/image-to-video", sandbase.Params{
	"duration": 3,
	"image": "https://static.sandbase.ai/examples/fc598f89-5a31-4128-9ff2-27c7f832b32c/input/57599f04-ed55-4178-8f81-6a3ea09fdddb.jpg",
	"prompt": "The waves roll gently onto the shore, slow camera push-in, no dialogue",
	"resolution": "360p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the first frame to animate.  |
| `prompt` | string | yes | The text prompt describing how the first image should be animated or interpolated into the optional end image.  |
| `duration` | integer |  | The duration of the generated video, in seconds. default `8`; range 3–10 |
| `end_image` | string |  | Optional URL of the end frame. When provided, the model interpolates between the two images in their listed order.  |
| `resolution` | string |  | The resolution of the generated video. one of: `360p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Gemini Omni Flash 1.1 image-to-video: animate a picture into a 3–10 second clip with synchronized audio. Add `end_image` to set the final frame.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `resolution` | `360p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `duration` | integer 3–10 | 8 | Output length in seconds (3–10). |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |

### Billing

You pay for output seconds: $0.03 at 360p, $0.10 at 720p, $0.15 at 1080p, and $0.30 at 4K.

| Output | 360p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 3s | $0.09 | $0.30 | $0.45 | $0.90 |
| 8s (default) | $0.24 | $0.80 | $1.20 | $2.40 |
| 10s | $0.30 | $1.00 | $1.50 | $3.00 |

Failed runs are not charged.

### Prompting

- Describe what moves and what it sounds like, not what is already visible.

### Limits

- 16:9 or 9:16 only.

### Also on SandBase

Other Gemini Omni Flash 1.1 endpoints: `google/gemini-omni-flash/1.1/text-to-video`, `google/gemini-omni-flash/1.1/reference-to-video`, `google/gemini-omni-flash/1.1/edit`, `google/gemini-omni-flash/image-to-video` (previous version).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/1.1/image-to-video.json`](../../../../../catalog/models/google/gemini-omni-flash/1.1/image-to-video.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/1.1/image-to-video
