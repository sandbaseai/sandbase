# Vidu Q4 Image to Video API: pricing, parameters and code examples

`vidu/q4/image-to-video` · video generation model · Vidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.135 to $6.24 per run, depending on parameters · **Modes:** async

Vidu Q4 Preview by Shengshu animates a first-frame image into a 3 to 16 second video at up to 4K. Prompts can direct motion, camera cuts, and spoken dialogue, with native speech and sound effects.

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
  -d '{"model": "vidu/q4/image-to-video", "image": "https://static.sandbase.ai/examples/da3da75f-2e08-46a9-95f1-398e0499bed9/input/99da89c9-98be-4974-8eed-5e8b4965db43.webp", "prompt": "The woman turns toward the camera and smiles, then the shot cuts to a close-up as she says: \"Let'\''s go.\""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vidu/q4/image-to-video', {'image': 'https://static.sandbase.ai/examples/da3da75f-2e08-46a9-95f1-398e0499bed9/input/99da89c9-98be-4974-8eed-5e8b4965db43.webp', 'prompt': 'The woman turns toward the camera and smiles, then the shot cuts to a close-up as she says: "Let\'s go."'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vidu/q4/image-to-video", {
  "image": "https://static.sandbase.ai/examples/da3da75f-2e08-46a9-95f1-398e0499bed9/input/99da89c9-98be-4974-8eed-5e8b4965db43.webp",
  "prompt": "The woman turns toward the camera and smiles, then the shot cuts to a close-up as she says: \"Let's go.\""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vidu/q4/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/da3da75f-2e08-46a9-95f1-398e0499bed9/input/99da89c9-98be-4974-8eed-5e8b4965db43.webp",
	"prompt": "The woman turns toward the camera and smiles, then the shot cuts to a close-up as she says: \"Let's go.\"",
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
| `image` | string | yes | URL or base64 data URI of the image to use as the first frame. Supports png, jpeg, jpg and webp up to 50 MB.  |
| `prompt` | string |  | Text prompt for video generation, max 5000 characters. Can direct motion, camera cuts, and spoken dialogue. default `""` |
| `duration` | integer |  | Duration of the video in seconds (3-16) default `5`; range 3–16 |
| `resolution` | string |  | Output video resolution. Sets the per-second rate. one of: `540p`, `720p`, `1080p`, `2K`, `4K`; default `"720p"` |

## Details

Vidu Q4 Preview image-to-video: animate a first frame into a 3–16 second clip at up to 4K, with native audio such as speech and sound effects directed by the prompt.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | empty | Up to 5,000 characters. Describe motion, camera cuts, and dialogue. |
| `image` | image URL, required | — | First frame. PNG, JPEG, or WebP up to 50 MB. |
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

- Describe subject, action, camera, and sound. Put spoken lines in quotes.
- This endpoint has no audio switch.

### Also on SandBase

`vidu/q4/reference-to-video` keeps characters, products, and voices consistent from reference images and audio. Vidu Q3 endpoints such as `vidu/q3/image-to-video` remain available.

---
Machine-readable: [`catalog/models/vidu/q4/image-to-video.json`](../../../../catalog/models/vidu/q4/image-to-video.json) · Store page: https://www.sandbase.ai/model/vidu/q4/image-to-video
