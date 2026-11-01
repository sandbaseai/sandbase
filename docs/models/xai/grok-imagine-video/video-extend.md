# Grok Imagine Video Extend

`xai/grok-imagine-video/video-extend` · video · xAI

Grok Imagine Video Extend is xAI's video-to-video AI model. Transform, enhance, and edit video content using text prompts - from style changes to object manipulation and scene modification.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=2 | 0.12 |
| duration=6 | 0.36 |
| duration=10 | 0.6 |

Formula: `(params.duration ?? 6) * 0.06`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/video-extend", "prompt": "The camera slowly zooms out to reveal the city skyline at sunset", "video": "https://static.sandbase.ai/examples/79b3c8a1-2494-4e33-a23c-0538c9b1e3b0/input/04b0e73a-3edd-452f-ba14-e335fd7c1c88.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/video-extend', {'prompt': 'The camera slowly zooms out to reveal the city skyline at sunset', 'video': 'https://static.sandbase.ai/examples/79b3c8a1-2494-4e33-a23c-0538c9b1e3b0/input/04b0e73a-3edd-452f-ba14-e335fd7c1c88.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/video-extend", {
  "prompt": "The camera slowly zooms out to reveal the city skyline at sunset",
  "video": "https://static.sandbase.ai/examples/79b3c8a1-2494-4e33-a23c-0538c9b1e3b0/input/04b0e73a-3edd-452f-ba14-e335fd7c1c88.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/video-extend", sandbase.Params{
	"prompt": "The camera slowly zooms out to reveal the city skyline at sunset",
	"video": "https://static.sandbase.ai/examples/79b3c8a1-2494-4e33-a23c-0538c9b1e3b0/input/04b0e73a-3edd-452f-ba14-e335fd7c1c88.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | URL of the source video to extend. Must be MP4 format (H.264, H.265, or AV1 codec), 2-15 seconds long.  |
| `prompt` | string | yes | Text description of what should happen next in the video.  |
| `duration` | integer |  | Length of the extension in seconds. default `6`; range 2–10 |

## Details

Grok Imagine Video extend: continue a clip with 2–10 seconds of new footage.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `video` | video URL, required | — | Source clip. |
| `duration` | integer 2–10 | 6 | Output length in seconds. |

### Billing

$0.06 per new second.

| Output | Price |
|---|---|
| 2s | $0.12 |
| 6s (default) | $0.36 |
| 10s | $0.60 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video endpoints: `xai/grok-imagine-video/text-to-video`, `xai/grok-imagine-video/image-to-video`, `xai/grok-imagine-video/reference-to-video`, `xai/grok-imagine-video/video-edit`, `xai/grok-imagine-video/1.5/text-to-video` (1.5, newer).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/video-extend.json`](../../../../catalog/models/xai/grok-imagine-video/video-extend.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/video-extend
