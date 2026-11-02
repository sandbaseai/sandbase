# Happy Horse 1.1 Image to Video API: pricing, parameters and code examples

`alibaba/happy-horse/1.1/image-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.21 to $1.44 per run, depending on parameters · **Modes:** async

Happy Horse 1.1 by Alibaba - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="480p" | 0.21 |
| duration=3, resolution="720p" | 0.42 |
| duration=3, resolution="1080p" | 0.54 |
| duration=4, resolution="480p" | 0.28 |
| duration=4, resolution="720p" | 0.56 |
| duration=4, resolution="1080p" | 0.72 |
| duration=5, resolution="480p" | 0.35 |
| duration=5, resolution="720p" | 0.7 |
| duration=5, resolution="1080p" | 0.9 |
| duration=6, resolution="480p" | 0.42 |
| duration=6, resolution="720p" | 0.84 |
| duration=6, resolution="1080p" | 1.08 |
| duration=7, resolution="480p" | 0.49 |
| duration=7, resolution="720p" | 0.98 |
| duration=7, resolution="1080p" | 1.26 |
| duration=8, resolution="480p" | 0.56 |
| duration=8, resolution="720p" | 1.12 |
| duration=8, resolution="1080p" | 1.44 |

Formula: `(params.resolution ?? "720p") == "1080p" ? (params.duration ?? 5) * 0.18 : (params.resolution ?? "720p") == "480p" ? (params.duration ?? 5) * 0.07 : (params.duration ?? 5) * 0.14`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/happy-horse/1.1/image-to-video", "duration": 3, "image": "https://static.sandbase.ai/examples/a73ed7f8-ca7d-4049-9722-d0434d557702/input/4b94aaa6-51ab-4e29-9068-274920cea45e.png", "prompt": "The black cat slowly looks up", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/happy-horse/1.1/image-to-video', {'duration': 3, 'image': 'https://static.sandbase.ai/examples/a73ed7f8-ca7d-4049-9722-d0434d557702/input/4b94aaa6-51ab-4e29-9068-274920cea45e.png', 'prompt': 'The black cat slowly looks up', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/happy-horse/1.1/image-to-video", {
  "duration": 3,
  "image": "https://static.sandbase.ai/examples/a73ed7f8-ca7d-4049-9722-d0434d557702/input/4b94aaa6-51ab-4e29-9068-274920cea45e.png",
  "prompt": "The black cat slowly looks up",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/happy-horse/1.1/image-to-video", sandbase.Params{
	"duration": 3,
	"image": "https://static.sandbase.ai/examples/a73ed7f8-ca7d-4049-9722-d0434d557702/input/4b94aaa6-51ab-4e29-9068-274920cea45e.png",
	"prompt": "The black cat slowly looks up",
	"resolution": "720p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-2147483647).  |
| `image` | string | yes | URL of the first frame image. Formats: JPEG, JPG, PNG, BMP, WEBP. Dimensions must be at least 300px. Aspect ratio must be between 1:2.5 and 2.5:1. Max 20 MB.  |
| `prompt` | string | yes | Optional text prompt guiding the animation. Max 2500 characters.  |
| `duration` | integer |  | Output video duration in seconds (3-15). one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | Output video resolution tier. one of: `480p`, `720p`, `1080p`; default `"720p"` |

## Details

Animate a picture with Happy Horse 1.1. `image` becomes the first frame and the prompt directs the action and camera over 3–15 seconds.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.07 at 480p, $0.14 at 720p, and $0.18 at 1080p, Alibaba's list price.

| Output | 480p | 720p | 1080p |
|---|---|---|---|
| 3s | $0.21 | $0.42 | $0.54 |
| 5s (default) | $0.35 | $0.70 | $0.90 |
| 10s | $0.70 | $1.40 | $1.80 |
| 15s | $1.05 | $2.10 | $2.70 |

Failed runs are not charged.

### Prompting

- Describe what moves and how the camera behaves, not what is already visible.
- Draft at 480p, then rerun the chosen take at 1080p.

### Limits

- The output follows the input image's aspect ratio.

### Also on SandBase

Other Happy Horse endpoints: `alibaba/happy-horse/1.1/text-to-video`, `alibaba/happy-horse/1.1/reference-to-video`, `alibaba/happy-horse/video-edit` (edit an existing clip).

---
Machine-readable: [`catalog/models/alibaba/happy-horse/1.1/image-to-video.json`](../../../../../catalog/models/alibaba/happy-horse/1.1/image-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/happy-horse/1.1/image-to-video
