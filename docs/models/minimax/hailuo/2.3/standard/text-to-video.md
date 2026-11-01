# MiniMax Hailuo 2.3 Standard Text to Video

`minimax/hailuo/2.3/standard/text-to-video` · video · MiniMax

MiniMax Hailuo 2.3 Standard by MiniMax turns a text prompt into a 6 or 10 second 768P video with realistic motion.

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
  -d '{"model": "minimax/hailuo/2.3/standard/text-to-video", "prompt": "An intense electrical storm rages over a modern city skyline at night. Multiple lightning bolts strike simultaneously, illuminating the towering skyscrapers in brilliant white flashes. Thunder clouds roil and churn overhead while constant lightning creates a strobe effect. Rain pours in heavy sheets, visible in the glow of city lights. The camera captures the drama from across a river as lightning reflects in the water. Lightning branches across the sky in intricate patterns. Atmosphere: dramatic, powerful, electrifying urban storm."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/hailuo/2.3/standard/text-to-video', {'prompt': 'An intense electrical storm rages over a modern city skyline at night. Multiple lightning bolts strike simultaneously, illuminating the towering skyscrapers in brilliant white flashes. Thunder clouds roil and churn overhead while constant lightning creates a strobe effect. Rain pours in heavy sheets, visible in the glow of city lights. The camera captures the drama from across a river as lightning reflects in the water. Lightning branches across the sky in intricate patterns. Atmosphere: dramatic, powerful, electrifying urban storm.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/hailuo/2.3/standard/text-to-video", {
  "prompt": "An intense electrical storm rages over a modern city skyline at night. Multiple lightning bolts strike simultaneously, illuminating the towering skyscrapers in brilliant white flashes. Thunder clouds roil and churn overhead while constant lightning creates a strobe effect. Rain pours in heavy sheets, visible in the glow of city lights. The camera captures the drama from across a river as lightning reflects in the water. Lightning branches across the sky in intricate patterns. Atmosphere: dramatic, powerful, electrifying urban storm."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/hailuo/2.3/standard/text-to-video", sandbase.Params{
	"prompt": "An intense electrical storm rages over a modern city skyline at night. Multiple lightning bolts strike simultaneously, illuminating the towering skyscrapers in brilliant white flashes. Thunder clouds roil and churn overhead while constant lightning creates a strobe effect. Rain pours in heavy sheets, visible in the glow of city lights. The camera captures the drama from across a river as lightning reflects in the water. Lightning branches across the sky in intricate patterns. Atmosphere: dramatic, powerful, electrifying urban storm.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Prompt  |
| `duration` | integer |  | The duration of the video in seconds. one of: `6`, `10`; default `6` |
| `prompt_optimizer` | boolean |  | Whether to use the model's prompt optimizer default `true` |

## Details

Hailuo 2.3 Standard: 6 or 10 second 768P video from a prompt.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
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

Other Hailuo 2.3 endpoints: `minimax/hailuo/2.3/pro/text-to-video`, `minimax/hailuo/2.3/pro/image-to-video`, `minimax/hailuo/2.3/standard/image-to-video`, `minimax/hailuo/2.3-fast/pro/image-to-video`, `minimax/hailuo/2.3-fast/standard/image-to-video`, `minimax/h3/text-to-video` (newer, with audio).

---
Machine-readable: [`catalog/models/minimax/hailuo/2.3/standard/text-to-video.json`](../../../../../../catalog/models/minimax/hailuo/2.3/standard/text-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/hailuo/2.3/standard/text-to-video
