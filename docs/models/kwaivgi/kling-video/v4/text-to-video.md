# Kling V4 Text to Video

`kwaivgi/kling-video/v4/text-to-video` · video · KwaiVGI

Kling V4 Text to Video by Kuaishou turns a text prompt into a 3-30 second video at 720p or 1080p.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="720p" | 0.471 |
| duration=3, resolution="1080p" | 0.705 |
| duration=5, resolution="720p" | 0.785 |
| duration=5, resolution="1080p" | 1.175 |
| duration=30, resolution="720p" | 4.71 |
| duration=30, resolution="1080p" | 7.05 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "1080p") == "720p" ? 0.157 : 0.235)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v4/text-to-video", "aspect_ratio": "16:9", "prompt": "Close-up: a single drop of water falls from the tip of a leaf into a shallow dish, creating concentric ripples. Warm window light gives the ripples a golden glow. Macro cinematography, photorealistic."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v4/text-to-video', {'aspect_ratio': '16:9', 'prompt': 'Close-up: a single drop of water falls from the tip of a leaf into a shallow dish, creating concentric ripples. Warm window light gives the ripples a golden glow. Macro cinematography, photorealistic.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v4/text-to-video", {
  "aspect_ratio": "16:9",
  "prompt": "Close-up: a single drop of water falls from the tip of a leaf into a shallow dish, creating concentric ripples. Warm window light gives the ripples a golden glow. Macro cinematography, photorealistic."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v4/text-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "Close-up: a single drop of water falls from the tip of a leaf into a shallow dish, creating concentric ripples. Warm window light gives the ripples a golden glow. Macro cinematography, photorealistic.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Describe subject, action, camera and light.  |
| `duration` | integer |  | Output length in seconds (3-30). default `5`; range 3–30 |
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output frame shape. one of: `16:9`, `9:16`, `1:1`, `21:9`; default `"16:9"` |

## Details

Kling V4 text-to-video: write a scene and get back a 3–30 second clip at 720p or 1080p.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `21:9` | `16:9` | Output frame shape. |
| `resolution` | `720p` / `1080p` | `1080p` | Output resolution. |
| `duration` | 3–30 | 5 | Output length in seconds. |
### Billing
Billed per output second: $0.157 at 720p, $0.235 at 1080p.
| Output | Price |
|---|---|
| 5s, 1080p (default) | $1.175 |
| 5s, 720p | $0.785 |
| 10s, 1080p | $2.35 |
| 30s, 1080p | $7.05 |
Failed runs are not charged.
### Prompting
- Describe subject, action, camera move and light in order.
### Limits
- Clips are 3–30 seconds.
### Also on SandBase
Other Kling V4 endpoints: `kwaivgi/kling-video/v4/text-to-video`, `kwaivgi/kling-video/v4/image-to-video`, `kwaivgi/kling-video/v4/reference-to-video`, `kwaivgi/kling-video/v4/video-edit`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v4/text-to-video.json`](../../../../../catalog/models/kwaivgi/kling-video/v4/text-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v4/text-to-video
