# Gemini Omni Flash Image to Video

`google/gemini-omni-flash/image-to-video` · video · Google

Gemini Omni Flash by Google - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=3 | 0.39 |
| duration=8 | 1.04 |
| duration=10 | 1.3 |

Formula: `(params.duration ?? 8) * 0.13`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/image-to-video", "aspect_ratio": "9:16", "duration": 3, "image": "https://static.sandbase.ai/examples/cfbc9108-0728-4751-a18f-2e8eb3e6a9ea/input/4746f7db-31ca-43c2-a62c-cbc2ef82a1eb.jpg", "prompt": "The waves roll gently onto the shore, slow push-in, no dialogue"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/image-to-video', {'aspect_ratio': '9:16', 'duration': 3, 'image': 'https://static.sandbase.ai/examples/cfbc9108-0728-4751-a18f-2e8eb3e6a9ea/input/4746f7db-31ca-43c2-a62c-cbc2ef82a1eb.jpg', 'prompt': 'The waves roll gently onto the shore, slow push-in, no dialogue'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/image-to-video", {
  "aspect_ratio": "9:16",
  "duration": 3,
  "image": "https://static.sandbase.ai/examples/cfbc9108-0728-4751-a18f-2e8eb3e6a9ea/input/4746f7db-31ca-43c2-a62c-cbc2ef82a1eb.jpg",
  "prompt": "The waves roll gently onto the shore, slow push-in, no dialogue"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/image-to-video", sandbase.Params{
	"aspect_ratio": "9:16",
	"duration": 3,
	"image": "https://static.sandbase.ai/examples/cfbc9108-0728-4751-a18f-2e8eb3e6a9ea/input/4746f7db-31ca-43c2-a62c-cbc2ef82a1eb.jpg",
	"prompt": "The waves roll gently onto the shore, slow push-in, no dialogue",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the input image to animate.  |
| `prompt` | string | yes | The text prompt describing how the image should be animated.  |
| `duration` | integer |  | The duration of the generated video, in seconds. default `8`; range 3–10 |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Gemini Omni Flash image-to-video: animate a picture into a 3–10 second clip with synchronized audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `duration` | integer 3–10 | 8 | Output length in seconds (3–10). |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |

### Billing

You pay $0.13 per output second.

| Output | Price |
|---|---|
| 3s | $0.39 |
| 8s (default) | $1.04 |
| 10s | $1.30 |

Failed runs are not charged.

### Prompting

- Describe what moves and what it sounds like, not what is already visible.

### Limits

- 16:9 or 9:16 only.

### Also on SandBase

Other Gemini Omni Flash endpoints: `google/gemini-omni-flash/text-to-video`, `google/gemini-omni-flash/reference-to-video`, `google/gemini-omni-flash/edit`, `google/gemini-omni-flash/1.1/image-to-video` (newer).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/image-to-video.json`](../../../../catalog/models/google/gemini-omni-flash/image-to-video.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/image-to-video
