# MiniMax Hailuo 2.3 Fast Standard Image to Video API: pricing, parameters and code examples

`minimax/hailuo/2.3-fast/standard/image-to-video` · video generation model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.19 to $0.32 per run, depending on parameters · **Modes:** async

MiniMax Hailuo 2.3 Fast Standard by MiniMax animates a still image into a 6 or 10 second 768P video at lower cost and latency than Hailuo 2.3 Standard.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=6 | 0.19 |
| duration=10 | 0.32 |

Formula: `(params.duration ?? 6) == 10 ? 0.32 : 0.19`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/hailuo/2.3-fast/standard/image-to-video", "image": "https://static.sandbase.ai/examples/756eec19-405a-400d-9422-cf21af40de58/input/5050463e-efe5-4f06-ae44-d63099f19f7f.jpg", "prompt": "Athlete running powerfully on beach, dynamic camera movement tracking the runner, waves and sunset in motion, Hollywood movie cinematography, professional sports filming, inspiring atmosphere"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/hailuo/2.3-fast/standard/image-to-video', {'image': 'https://static.sandbase.ai/examples/756eec19-405a-400d-9422-cf21af40de58/input/5050463e-efe5-4f06-ae44-d63099f19f7f.jpg', 'prompt': 'Athlete running powerfully on beach, dynamic camera movement tracking the runner, waves and sunset in motion, Hollywood movie cinematography, professional sports filming, inspiring atmosphere'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/hailuo/2.3-fast/standard/image-to-video", {
  "image": "https://static.sandbase.ai/examples/756eec19-405a-400d-9422-cf21af40de58/input/5050463e-efe5-4f06-ae44-d63099f19f7f.jpg",
  "prompt": "Athlete running powerfully on beach, dynamic camera movement tracking the runner, waves and sunset in motion, Hollywood movie cinematography, professional sports filming, inspiring atmosphere"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/hailuo/2.3-fast/standard/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/756eec19-405a-400d-9422-cf21af40de58/input/5050463e-efe5-4f06-ae44-d63099f19f7f.jpg",
	"prompt": "Athlete running powerfully on beach, dynamic camera movement tracking the runner, waves and sunset in motion, Hollywood movie cinematography, professional sports filming, inspiring atmosphere",
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
| `duration` | integer |  | The duration of the video in seconds. one of: `6`, `10`; default `6` |
| `prompt_optimizer` | boolean |  | Whether to use the model's prompt optimizer default `true` |

## Details

Hailuo 2.3 Fast Standard animates an image into a 6 or 10 second 768P video at lower cost than Hailuo 2.3 Standard.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `duration` | 6 / 10 | 6 | Output length in seconds. |
| `prompt_optimizer` | boolean | true | Let MiniMax rewrite the prompt for better results. |

### Billing

$0.19 for 6 seconds, $0.32 for 10 seconds.

| Output | Price |
|---|---|
| 6s (default) | $0.19 |
| 10s | $0.32 |

Failed runs are not charged.

### Prompting

- Describe the motion and camera in one or two sentences.

### Limits

- No audio track.

### Also on SandBase

Other Hailuo 2.3 endpoints: `minimax/hailuo/2.3/pro/text-to-video`, `minimax/hailuo/2.3/pro/image-to-video`, `minimax/hailuo/2.3/standard/text-to-video`, `minimax/hailuo/2.3/standard/image-to-video`, `minimax/hailuo/2.3-fast/pro/image-to-video`, `minimax/h3/text-to-video` (newer, with audio).

---
Machine-readable: [`catalog/models/minimax/hailuo/2.3-fast/standard/image-to-video.json`](../../../../../../catalog/models/minimax/hailuo/2.3-fast/standard/image-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/hailuo/2.3-fast/standard/image-to-video
