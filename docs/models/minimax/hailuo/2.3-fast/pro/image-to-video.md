# MiniMax Hailuo 2.3 Fast Pro Image to Video API: pricing, parameters and code examples

`minimax/hailuo/2.3-fast/pro/image-to-video` · video generation model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.33 per call · **Modes:** async

MiniMax Hailuo 2.3 Fast Pro by MiniMax animates a still image into a 6-second 1080P video at lower cost and latency than Hailuo 2.3 Pro.

## Pricing

- **$0.33 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/hailuo/2.3-fast/pro/image-to-video", "image": "https://static.sandbase.ai/examples/9d21c225-e58e-485c-af0d-dd330cb89b0b/input/3134eda0-a0fb-4c79-8c24-6dc43ccfd98e.jpg", "prompt": "Subject-tracking orbit: camera glides parallel to astronaut, Earth rotates beneath, sun crest reveals lens flare, astronaut tethers and spins slowly, 8K 60 fps slow-motion, ends with spacecraft blackout on sun disk"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/hailuo/2.3-fast/pro/image-to-video', {'image': 'https://static.sandbase.ai/examples/9d21c225-e58e-485c-af0d-dd330cb89b0b/input/3134eda0-a0fb-4c79-8c24-6dc43ccfd98e.jpg', 'prompt': 'Subject-tracking orbit: camera glides parallel to astronaut, Earth rotates beneath, sun crest reveals lens flare, astronaut tethers and spins slowly, 8K 60 fps slow-motion, ends with spacecraft blackout on sun disk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/hailuo/2.3-fast/pro/image-to-video", {
  "image": "https://static.sandbase.ai/examples/9d21c225-e58e-485c-af0d-dd330cb89b0b/input/3134eda0-a0fb-4c79-8c24-6dc43ccfd98e.jpg",
  "prompt": "Subject-tracking orbit: camera glides parallel to astronaut, Earth rotates beneath, sun crest reveals lens flare, astronaut tethers and spins slowly, 8K 60 fps slow-motion, ends with spacecraft blackout on sun disk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/hailuo/2.3-fast/pro/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/9d21c225-e58e-485c-af0d-dd330cb89b0b/input/3134eda0-a0fb-4c79-8c24-6dc43ccfd98e.jpg",
	"prompt": "Subject-tracking orbit: camera glides parallel to astronaut, Earth rotates beneath, sun crest reveals lens flare, astronaut tethers and spins slowly, 8K 60 fps slow-motion, ends with spacecraft blackout on sun disk",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the image to use as the first frame  |
| `prompt` | string | yes | Text prompt for video generation  |
| `prompt_optimizer` | boolean |  | Whether to use the model's prompt optimizer default `true` |

## Details

Hailuo 2.3 Fast Pro animates an image into a 6-second 1080P video at lower cost and latency than Hailuo 2.3 Pro.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `prompt_optimizer` | boolean | true | Let MiniMax rewrite the prompt for better results. |

### Billing

$0.33 per 6-second video.

| Request | Price |
|---|---|
| One video | $0.33 |

Failed runs are not charged.

### Prompting

- Describe the motion and camera in one or two sentences.

### Limits

- No audio track.

### Also on SandBase

Other Hailuo 2.3 endpoints: `minimax/hailuo/2.3/pro/text-to-video`, `minimax/hailuo/2.3/pro/image-to-video`, `minimax/hailuo/2.3/standard/text-to-video`, `minimax/hailuo/2.3/standard/image-to-video`, `minimax/hailuo/2.3-fast/standard/image-to-video`, `minimax/h3/text-to-video` (newer, with audio).

---
Machine-readable: [`catalog/models/minimax/hailuo/2.3-fast/pro/image-to-video.json`](../../../../../../catalog/models/minimax/hailuo/2.3-fast/pro/image-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/hailuo/2.3-fast/pro/image-to-video
