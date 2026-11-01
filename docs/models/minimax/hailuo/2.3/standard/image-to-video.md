# MiniMax Hailuo 2.3 Standard Image to Video

`minimax/hailuo/2.3/standard/image-to-video` · video · MiniMax

MiniMax Hailuo 2.3 Standard by MiniMax animates a still image into a 6 or 10 second 768P video with realistic motion.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=6 | 0.28 |
| duration=10 | 0.56 |

Formula: `(params.duration ?? 6) == 10 ? 0.56 : 0.28`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/hailuo/2.3/standard/image-to-video", "image": "https://static.sandbase.ai/examples/e9aed9c8-7fe4-4ee2-8220-cf4a6a900059/input/0fc605d5-9fe7-4069-a474-95d002581dfc.jpg", "prompt": "The space station slowly rotates in orbit, its solar panels tracking the sun. Earth rotates majestically in the background with weather patterns and landmasses drifting by. The station'\''s communication arrays adjust position. A small spacecraft approaches one of the docking ports. The scene captures the silent majesty of space and human engineering."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/hailuo/2.3/standard/image-to-video', {'image': 'https://static.sandbase.ai/examples/e9aed9c8-7fe4-4ee2-8220-cf4a6a900059/input/0fc605d5-9fe7-4069-a474-95d002581dfc.jpg', 'prompt': "The space station slowly rotates in orbit, its solar panels tracking the sun. Earth rotates majestically in the background with weather patterns and landmasses drifting by. The station's communication arrays adjust position. A small spacecraft approaches one of the docking ports. The scene captures the silent majesty of space and human engineering."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/hailuo/2.3/standard/image-to-video", {
  "image": "https://static.sandbase.ai/examples/e9aed9c8-7fe4-4ee2-8220-cf4a6a900059/input/0fc605d5-9fe7-4069-a474-95d002581dfc.jpg",
  "prompt": "The space station slowly rotates in orbit, its solar panels tracking the sun. Earth rotates majestically in the background with weather patterns and landmasses drifting by. The station's communication arrays adjust position. A small spacecraft approaches one of the docking ports. The scene captures the silent majesty of space and human engineering."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/hailuo/2.3/standard/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/e9aed9c8-7fe4-4ee2-8220-cf4a6a900059/input/0fc605d5-9fe7-4069-a474-95d002581dfc.jpg",
	"prompt": "The space station slowly rotates in orbit, its solar panels tracking the sun. Earth rotates majestically in the background with weather patterns and landmasses drifting by. The station's communication arrays adjust position. A small spacecraft approaches one of the docking ports. The scene captures the silent majesty of space and human engineering.",
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

Hailuo 2.3 Standard: animate an image into a 6 or 10 second 768P video.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `duration` | 6 / 10 | 6 | Output length in seconds. |
| `prompt_optimizer` | boolean | true | Let MiniMax rewrite the prompt for better results. |

### Billing

$0.28 for 6 seconds, $0.56 for 10 seconds.

| Output | Price |
|---|---|
| 6s (default) | $0.28 |
| 10s | $0.56 |

Failed runs are not charged.

### Prompting

- Describe the motion and camera in one or two sentences.

### Limits

- No audio track.

### Also on SandBase

Other Hailuo 2.3 endpoints: `minimax/hailuo/2.3/pro/text-to-video`, `minimax/hailuo/2.3/pro/image-to-video`, `minimax/hailuo/2.3/standard/text-to-video`, `minimax/hailuo/2.3-fast/pro/image-to-video`, `minimax/hailuo/2.3-fast/standard/image-to-video`, `minimax/h3/text-to-video` (newer, with audio).

---
Machine-readable: [`catalog/models/minimax/hailuo/2.3/standard/image-to-video.json`](../../../../../../catalog/models/minimax/hailuo/2.3/standard/image-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/hailuo/2.3/standard/image-to-video
