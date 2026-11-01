# MiniMax H3 Max Image to Video

`minimax/h3-max/image-to-video` · video · MiniMax

MiniMax H3 Max by MiniMax animates a first frame, optionally toward a last frame, into a 5-15 second video with native audio at 480P or 768P.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="480P" | 0.25 |
| duration=5, resolution="768P" | 0.4 |
| duration=15, resolution="480P" | 0.75 |
| duration=15, resolution="768P" | 1.2 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "768P") == "480P" ? 0.05 : 0.08)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3-max/image-to-video", "image": "https://static.sandbase.ai/examples/30966cf1-a803-4cf2-b849-e807d01a784f/input/f30537e1-2438-45da-a376-d327897489c7.jpg", "prompt": "A calm lake at sunrise, gentle ripples, birds flying overhead", "resolution": "480P"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3-max/image-to-video', {'image': 'https://static.sandbase.ai/examples/30966cf1-a803-4cf2-b849-e807d01a784f/input/f30537e1-2438-45da-a376-d327897489c7.jpg', 'prompt': 'A calm lake at sunrise, gentle ripples, birds flying overhead', 'resolution': '480P'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3-max/image-to-video", {
  "image": "https://static.sandbase.ai/examples/30966cf1-a803-4cf2-b849-e807d01a784f/input/f30537e1-2438-45da-a376-d327897489c7.jpg",
  "prompt": "A calm lake at sunrise, gentle ripples, birds flying overhead",
  "resolution": "480P"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3-max/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/30966cf1-a803-4cf2-b849-e807d01a784f/input/f30537e1-2438-45da-a376-d327897489c7.jpg",
	"prompt": "A calm lake at sunrise, gentle ripples, birds flying overhead",
	"resolution": "480P",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Optional URL of the image to use as the first frame. When provided, the output aspect ratio follows this image. When omitted, the request is handled as text-to-video (16:9 by default).  |
| `prompt` | string | yes | Text prompt for video generation  |
| `duration` | integer |  | The duration of the video in seconds. default `5`; range 5–15 |
| `end_image` | string |  | Optional URL of the image to use as the last frame, for first-to-last keyframe generation.  |
| `resolution` | string |  | The native generation resolution of the video. one of: `480P`, `768P`; default `"768P"` |
| `prompt_expansion_mode` | string |  | How much effort to spend rewriting the prompt before generation. `balanced` returns in about a second; `quality` spends up to ~30 seconds on a richer prompt. one of: `balanced`, `quality`; default `"balanced"` |

## Details

MiniMax H3 Max image-to-video: animate a first frame, optionally toward a last frame, into a 5–15 second clip with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `resolution` | `480P` / `768P` | `768P` | Sets the per-second rate. |
| `duration` | integer 5–15 | 5 | Output length in seconds. |
| `prompt_expansion_mode` | `balanced` / `quality` | `balanced` | `balanced` rewrites the prompt lightly; `quality` expands it more for richer detail. |

### Billing

You pay for output seconds: $0.08 at 768P and $0.05 at 480P.

| Output | 768P | 480P |
|---|---|---|
| 5s (default) | $0.40 | $0.25 |
| 10s | $0.80 | $0.50 |
| 15s | $1.20 | $0.75 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound in order.
- Quote dialogue and name the speaker.

### Limits

- Clips are 5–15 seconds.

### Also on SandBase

Other MiniMax H3 Max endpoints: `minimax/h3-max/text-to-video`, `minimax/h3-max/reference-to-video`, `minimax/h3/image-to-video` (2K).

---
Machine-readable: [`catalog/models/minimax/h3-max/image-to-video.json`](../../../../catalog/models/minimax/h3-max/image-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/h3-max/image-to-video
