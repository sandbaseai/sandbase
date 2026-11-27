# HeyGen Avatar 6 Turbo Image to Video API: pricing, parameters and code examples

`heygen/avatar6-turbo/image-to-video` · video generation model · HeyGen · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.3 per call · **Modes:** async

HeyGen Avatar 6 Turbo by HeyGen turns a photo of a person and a speech track into a lifelike talking video. Turbo is the faster, lower-cost tier.

## Pricing

- Depends on parameters (`params.audio`, `params.resolution`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.audio) ?? 5.0) * ((params.resolution ?? "1080p") == "2k" ? 0.0875 : 0.06)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/avatar6-turbo/image-to-video", "audio": "https://static.sandbase.ai/examples/d5971b7a-1eb9-423e-b169-66fc98d4bf87/input/ece18167-f8ab-49d2-b162-eeda05bde2f8.mp3", "image": "https://static.sandbase.ai/examples/d5971b7a-1eb9-423e-b169-66fc98d4bf87/input/9f3fd320-f150-4261-ad2a-f16e4c22ff3b.png"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/avatar6-turbo/image-to-video', {'audio': 'https://static.sandbase.ai/examples/d5971b7a-1eb9-423e-b169-66fc98d4bf87/input/ece18167-f8ab-49d2-b162-eeda05bde2f8.mp3', 'image': 'https://static.sandbase.ai/examples/d5971b7a-1eb9-423e-b169-66fc98d4bf87/input/9f3fd320-f150-4261-ad2a-f16e4c22ff3b.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/avatar6-turbo/image-to-video", {
  "audio": "https://static.sandbase.ai/examples/d5971b7a-1eb9-423e-b169-66fc98d4bf87/input/ece18167-f8ab-49d2-b162-eeda05bde2f8.mp3",
  "image": "https://static.sandbase.ai/examples/d5971b7a-1eb9-423e-b169-66fc98d4bf87/input/9f3fd320-f150-4261-ad2a-f16e4c22ff3b.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/avatar6-turbo/image-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/d5971b7a-1eb9-423e-b169-66fc98d4bf87/input/ece18167-f8ab-49d2-b162-eeda05bde2f8.mp3",
	"image": "https://static.sandbase.ai/examples/d5971b7a-1eb9-423e-b169-66fc98d4bf87/input/9f3fd320-f150-4261-ad2a-f16e4c22ff3b.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audio` | string | yes | Speech audio, file or URL. It sets the video length.  |
| `image` | string | yes | Photo of the person to animate, file or URL. The face should be clearly visible.  |
| `resolution` | string |  | Output resolution; 2k is billed at a higher per-second rate. one of: `1080p`, `2k`; default `"1080p"` |
| `motion_prompt` | string |  | Optional direction for the avatar's motion and expression.  |
| `motion_expressiveness` | string |  | less gives fewer, smaller gestures and calmer expressions. one of: `default`, `less`; default `"default"` |

## Details

HeyGen Avatar 6 Turbo turns one photo of a person and a speech track into a talking video with natural motion and lip-sync. Turbo is the faster, lower-cost tier.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image file or URL, required | — | Front-facing photo. |
| `audio` | audio file or URL, required | — | Sets the video length. |
| `motion_prompt` | string | — | Direction for motion and expression. |
| `motion_expressiveness` | `default` / `less` | `default` | `less` for calmer motion. |
| `resolution` | `1080p` / `2k` | `1080p` | Sets the per-second rate. |
### Billing
$0.06 per output second at 1080p, $0.0875 at 2k. Length follows the speech audio; the quote before submission assumes 5 seconds.
| Output | 1080p | 2k |
|---|---|---|
| 10s | $0.60 | $0.875 |
| 60s | $3.60 | $5.25 |
Failed runs are not charged.
### Also on SandBase
Related: `heygen/avatar6-turbo/ref-video-to-video`, `heygen/avatar6-turbo/identity-to-video`, `heygen/avatar5/digital-twin`.

---
Machine-readable: [`catalog/models/heygen/avatar6-turbo/image-to-video.json`](../../../../catalog/models/heygen/avatar6-turbo/image-to-video.json) · Store page: https://www.sandbase.ai/model/heygen/avatar6-turbo/image-to-video
