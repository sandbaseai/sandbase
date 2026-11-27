# HeyGen Avatar 6 Turbo Reference Video to Video API: pricing, parameters and code examples

`heygen/avatar6-turbo/ref-video-to-video` · video generation model · HeyGen · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.3 per call · **Modes:** async

HeyGen Avatar 6 Turbo by HeyGen animates an illustrated or animated character from a reference video, lip-synced to speech audio. Turbo is the faster, lower-cost tier.

## Pricing

- Depends on parameters (`params.audio`, `params.resolution`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.audio) ?? 5.0) * ((params.resolution ?? "1080p") == "2k" ? 0.0875 : 0.06)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/avatar6-turbo/ref-video-to-video", "audio": "https://static.sandbase.ai/examples/c0fcc21b-8d8c-4b08-9fa2-3eaec184e214/input/ffba4ee9-a398-41a0-b820-b2dc6d9f0a12.mp3", "video": "https://static.sandbase.ai/examples/c0fcc21b-8d8c-4b08-9fa2-3eaec184e214/input/9c450085-319b-4db7-aaef-ecabfb3ce51b.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/avatar6-turbo/ref-video-to-video', {'audio': 'https://static.sandbase.ai/examples/c0fcc21b-8d8c-4b08-9fa2-3eaec184e214/input/ffba4ee9-a398-41a0-b820-b2dc6d9f0a12.mp3', 'video': 'https://static.sandbase.ai/examples/c0fcc21b-8d8c-4b08-9fa2-3eaec184e214/input/9c450085-319b-4db7-aaef-ecabfb3ce51b.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/avatar6-turbo/ref-video-to-video", {
  "audio": "https://static.sandbase.ai/examples/c0fcc21b-8d8c-4b08-9fa2-3eaec184e214/input/ffba4ee9-a398-41a0-b820-b2dc6d9f0a12.mp3",
  "video": "https://static.sandbase.ai/examples/c0fcc21b-8d8c-4b08-9fa2-3eaec184e214/input/9c450085-319b-4db7-aaef-ecabfb3ce51b.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/avatar6-turbo/ref-video-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/c0fcc21b-8d8c-4b08-9fa2-3eaec184e214/input/ffba4ee9-a398-41a0-b820-b2dc6d9f0a12.mp3",
	"video": "https://static.sandbase.ai/examples/c0fcc21b-8d8c-4b08-9fa2-3eaec184e214/input/9c450085-319b-4db7-aaef-ecabfb3ce51b.mp4",
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
| `image` | string |  | Optional photo of the same character, file or URL.  |
| `video` | string | yes | Reference video of an animated or illustrated character, file or URL. Videos of real people are not supported.  |
| `resolution` | string |  | Output resolution; 2k is billed at a higher per-second rate. one of: `1080p`, `2k`; default `"1080p"` |
| `motion_prompt` | string |  | Optional direction for the avatar's motion and expression.  |
| `motion_expressiveness` | string |  | less gives fewer, smaller gestures and calmer expressions. one of: `default`, `less`; default `"default"` |

## Details

HeyGen Avatar 6 Turbo animates an illustrated or animated character from a reference video, lip-synced to a speech track. Turbo is the faster, lower-cost tier.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `video` | video file or URL, required | — | Animated or illustrated character only. |
| `audio` | audio file or URL, required | — | Sets the video length. |
| `image` | image file or URL | — | Optional extra reference. |
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
Related: `heygen/avatar6-turbo/image-to-video`, `heygen/avatar6-turbo/identity-to-video`, `heygen/avatar5/digital-twin`.

---
Machine-readable: [`catalog/models/heygen/avatar6-turbo/ref-video-to-video.json`](../../../../catalog/models/heygen/avatar6-turbo/ref-video-to-video.json) · Store page: https://www.sandbase.ai/model/heygen/avatar6-turbo/ref-video-to-video
