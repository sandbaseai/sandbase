# Gemini Omni Flash 1.2 Image to Video API: pricing, parameters and code examples

`google/gemini-omni-flash/1.2/image-to-video` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.069 to $3.15 per run, depending on parameters · **Modes:** async

Gemini Omni Flash 1.2 Image to Video by Google animates a still image into a 3–15 second clip with synchronized audio, with an optional end frame for interpolation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="360p" | 0.069 |
| duration=3, resolution="720p" | 0.21 |
| duration=3, resolution="1080p" | 0.315 |
| duration=3, resolution="4k" | 0.63 |
| duration=8, resolution="360p" | 0.184 |
| duration=8, resolution="720p" | 0.56 |
| duration=8, resolution="1080p" | 0.84 |
| duration=8, resolution="4k" | 1.68 |
| duration=15, resolution="360p" | 0.345 |
| duration=15, resolution="720p" | 1.05 |
| duration=15, resolution="1080p" | 1.575 |
| duration=15, resolution="4k" | 3.15 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "360p" ? 0.023 : (params.resolution ?? "720p") == "1080p" ? 0.105 : (params.resolution ?? "720p") == "4k" ? 0.21 : 0.07)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/1.2/image-to-video", "prompt": "The dog turns its head and wags its tail in warm sunlight.", "image": "https://static.sandbase.ai/examples/google/gemini-omni-flash/image-to-video/input_image_0.png"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/1.2/image-to-video', {'prompt': 'The dog turns its head and wags its tail in warm sunlight.', 'image': 'https://static.sandbase.ai/examples/google/gemini-omni-flash/image-to-video/input_image_0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/1.2/image-to-video", {
  "prompt": "The dog turns its head and wags its tail in warm sunlight.",
  "image": "https://static.sandbase.ai/examples/google/gemini-omni-flash/image-to-video/input_image_0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/1.2/image-to-video", sandbase.Params{
	"prompt": "The dog turns its head and wags its tail in warm sunlight.",
	"image": "https://static.sandbase.ai/examples/google/gemini-omni-flash/image-to-video/input_image_0.png",
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
| `duration` | integer |  | The duration of the generated video, in seconds. At most 10 seconds when an end image is provided. default `8`; range 3–15 |
| `end_image` | string |  | Optional URL of the end frame. When provided, the model interpolates between the two images in their listed order and the duration is capped at 10 seconds.  |
| `resolution` | string |  | The resolution of the generated video. one of: `360p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Gemini Omni Flash 1.2 image-to-video: animate a picture into a 3–15 second clip with synchronized audio. Add `end_image` to interpolate between two frames (up to 10 seconds).

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. Caps `duration` at 10 seconds. |
| `resolution` | `360p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `duration` | integer 3–15 | 8 | Output length in seconds. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |

### Billing

You pay for output seconds: $0.023 at 360p, $0.07 at 720p, $0.105 at 1080p, and $0.21 at 4K.

| Output | 360p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 3s | $0.07 | $0.21 | $0.32 | $0.63 |
| 8s (default) | $0.18 | $0.56 | $0.84 | $1.68 |
| 10s | $0.23 | $0.70 | $1.05 | $2.10 |
| 15s | $0.34 | $1.05 | $1.57 | $3.15 |

Failed runs are not charged.

### Prompting

- Describe what moves and what it sounds like, not what is already visible.

### Limits

- 16:9 or 9:16 only.
- With `end_image`, duration is capped at 10 seconds.

### Also on SandBase

Other Gemini Omni Flash 1.2 endpoints: `google/gemini-omni-flash/1.2/text-to-video`, `google/gemini-omni-flash/1.2/reference-to-video`, `google/gemini-omni-flash/1.2/edit`, `google/gemini-omni-flash/1.1/image-to-video` (previous version).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/1.2/image-to-video.json`](../../../../../catalog/models/google/gemini-omni-flash/1.2/image-to-video.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/1.2/image-to-video
