# MiniMax Hailuo 2.3 Pro Text to Video API: pricing, parameters and code examples

`minimax/hailuo/2.3/pro/text-to-video` · video generation model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.49 per call · **Modes:** async

MiniMax Hailuo 2.3 Pro by MiniMax turns a text prompt into a 6-second 1080P video with realistic motion and strong prompt following.

## Pricing

- **$0.49 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/hailuo/2.3/pro/text-to-video", "prompt": "The camera follows the snowboarder as they carve down the mountain through deep powder, each turn sending up huge rooster tails of snow. They navigate between trees, floating through the powder with smooth, flowing movements. The rider launches off a natural jump, grabbing the board mid-air before landing softly in deep snow and continuing down. Powder sprays continuously as they link turns together. The atmosphere is exhilarating and free. Audio: Board cutting through snow, powder spraying, wind rushing, the rider'\''s excited shouts, and the soft thuds of landing in deep snow."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/hailuo/2.3/pro/text-to-video', {'prompt': "The camera follows the snowboarder as they carve down the mountain through deep powder, each turn sending up huge rooster tails of snow. They navigate between trees, floating through the powder with smooth, flowing movements. The rider launches off a natural jump, grabbing the board mid-air before landing softly in deep snow and continuing down. Powder sprays continuously as they link turns together. The atmosphere is exhilarating and free. Audio: Board cutting through snow, powder spraying, wind rushing, the rider's excited shouts, and the soft thuds of landing in deep snow."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/hailuo/2.3/pro/text-to-video", {
  "prompt": "The camera follows the snowboarder as they carve down the mountain through deep powder, each turn sending up huge rooster tails of snow. They navigate between trees, floating through the powder with smooth, flowing movements. The rider launches off a natural jump, grabbing the board mid-air before landing softly in deep snow and continuing down. Powder sprays continuously as they link turns together. The atmosphere is exhilarating and free. Audio: Board cutting through snow, powder spraying, wind rushing, the rider's excited shouts, and the soft thuds of landing in deep snow."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/hailuo/2.3/pro/text-to-video", sandbase.Params{
	"prompt": "The camera follows the snowboarder as they carve down the mountain through deep powder, each turn sending up huge rooster tails of snow. They navigate between trees, floating through the powder with smooth, flowing movements. The rider launches off a natural jump, grabbing the board mid-air before landing softly in deep snow and continuing down. Powder sprays continuously as they link turns together. The atmosphere is exhilarating and free. Audio: Board cutting through snow, powder spraying, wind rushing, the rider's excited shouts, and the soft thuds of landing in deep snow.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Text prompt for video generation  |
| `prompt_optimizer` | boolean |  | Whether to use the model's prompt optimizer default `true` |

## Details

Hailuo 2.3 Pro turns a prompt into a 6-second 1080P video with realistic motion and strong prompt following.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
| `prompt_optimizer` | boolean | true | Let MiniMax rewrite the prompt for better results. |

### Billing

$0.49 per 6-second video.

| Request | Price |
|---|---|
| One video | $0.49 |

Failed runs are not charged.

### Prompting

- Describe the motion and camera in one or two sentences.

### Limits

- No audio track.

### Also on SandBase

Other Hailuo 2.3 endpoints: `minimax/hailuo/2.3/pro/image-to-video`, `minimax/hailuo/2.3/standard/text-to-video`, `minimax/hailuo/2.3/standard/image-to-video`, `minimax/hailuo/2.3-fast/pro/image-to-video`, `minimax/hailuo/2.3-fast/standard/image-to-video`, `minimax/h3/text-to-video` (newer, with audio).

---
Machine-readable: [`catalog/models/minimax/hailuo/2.3/pro/text-to-video.json`](../../../../../../catalog/models/minimax/hailuo/2.3/pro/text-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/hailuo/2.3/pro/text-to-video
