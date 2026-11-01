# HeyGen Video Image to Video

`heygen/heygen-video/image-to-video` · video · HeyGen

HeyGen Video Image to Video animates a first-frame image into a 5-15 second video at up to 2K resolution.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="480p" | 0.1 |
| duration=5, resolution="768p" | 0.18 |
| duration=5, resolution="1080p" | 0.5 |
| duration=5, resolution="2k" | 0.5 |
| duration=15, resolution="480p" | 0.3 |
| duration=15, resolution="768p" | 0.54 |
| duration=15, resolution="1080p" | 1.5 |
| duration=15, resolution="2k" | 1.5 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "768p") == "480p" ? 0.02 : (params.resolution ?? "768p") == "768p" ? 0.036 : 0.1)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/heygen-video/image-to-video", "image": "https://static.sandbase.ai/examples/94899ae4-37d0-4620-ba7a-ef9556167062/input/4374abb0-8e3b-43b7-b3cf-44e962c720ad.png", "prompt": "The rabbit looks around curiously, its ears twitch, then it hops toward the camera. Soft breeze in the grass."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/heygen-video/image-to-video', {'image': 'https://static.sandbase.ai/examples/94899ae4-37d0-4620-ba7a-ef9556167062/input/4374abb0-8e3b-43b7-b3cf-44e962c720ad.png', 'prompt': 'The rabbit looks around curiously, its ears twitch, then it hops toward the camera. Soft breeze in the grass.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/heygen-video/image-to-video", {
  "image": "https://static.sandbase.ai/examples/94899ae4-37d0-4620-ba7a-ef9556167062/input/4374abb0-8e3b-43b7-b3cf-44e962c720ad.png",
  "prompt": "The rabbit looks around curiously, its ears twitch, then it hops toward the camera. Soft breeze in the grass."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/heygen-video/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/94899ae4-37d0-4620-ba7a-ef9556167062/input/4374abb0-8e3b-43b7-b3cf-44e962c720ad.png",
	"prompt": "The rabbit looks around curiously, its ears twitch, then it hops toward the camera. Soft breeze in the grass.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | First frame. JPEG, PNG or WebP URL.  |
| `prompt` | string | yes | Describe the scene, action, camera and sound.  |
| `duration` | integer |  | Output length in seconds (5-15). default `5`; range 5–15 |
| `resolution` | string |  | Output resolution. 1080p and 2k cost more. one of: `480p`, `768p`, `1080p`, `2k`; default `"768p"` |

## Details

HeyGen Video animates a first-frame image into a 5–15 second video at up to 2K resolution.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Motion, camera and sound. |
| `image` | image URL, required | — | First frame. JPEG, PNG or WebP URL. The output follows its aspect ratio. |
| `resolution` | `480p` / `768p` / `1080p` / `2k` | `768p` | Output resolution; 1080p and 2k cost more. |
| `duration` | 5–15 | 5 | Output length in seconds. |
### Billing
Billed per output second: $0.02 at 480p, $0.036 at 768p, $0.10 at 1080p and 2k.
| Output | Price |
|---|---|
| 5s, 768p (default) | $0.18 |
| 5s, 480p | $0.10 |
| 5s, 1080p | $0.50 |
| 15s, 2k | $1.50 |
Failed runs are not charged.
### Prompting
- Describe what moves and how the camera moves; the image sets the look.
### Limits
- Clips are 5–15 seconds.
### Also on SandBase
Other HeyGen Video endpoints: `heygen/heygen-video/text-to-video`, `heygen/heygen-video/reference-to-video`.

---
Machine-readable: [`catalog/models/heygen/heygen-video/image-to-video.json`](../../../../catalog/models/heygen/heygen-video/image-to-video.json) · Store page: https://www.sandbase.ai/model/heygen/heygen-video/image-to-video
