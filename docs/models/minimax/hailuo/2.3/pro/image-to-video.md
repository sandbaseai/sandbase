# MiniMax Hailuo 2.3 Pro Image to Video

`minimax/hailuo/2.3/pro/image-to-video` · video · MiniMax

MiniMax Hailuo 2.3 Pro by MiniMax animates a still image into a 6-second 1080P video with realistic motion and expressive characters.

## Pricing

- **$0.49 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/hailuo/2.3/pro/image-to-video", "image": "https://static.sandbase.ai/examples/de44ef69-c470-4b15-9301-767263198fdf/input/11bdc5d4-7794-4c9d-92b2-006b6b46071d.jpg", "prompt": "The camera follows the mountain biker as they navigate a technical forest trail at high speed, wheels bouncing over roots and rocks. The rider approaches a jump, launching into the air with the bike, both rider and machine perfectly synchronized. They land smoothly and continue through tight turns, splashing through a stream crossing. Mud and water spray as the bike powers through challenging terrain. The atmosphere is wild and adventurous. Audio: Tires gripping dirt, gears shifting, heavy breathing, branches whipping past, and water splashing."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/hailuo/2.3/pro/image-to-video', {'image': 'https://static.sandbase.ai/examples/de44ef69-c470-4b15-9301-767263198fdf/input/11bdc5d4-7794-4c9d-92b2-006b6b46071d.jpg', 'prompt': 'The camera follows the mountain biker as they navigate a technical forest trail at high speed, wheels bouncing over roots and rocks. The rider approaches a jump, launching into the air with the bike, both rider and machine perfectly synchronized. They land smoothly and continue through tight turns, splashing through a stream crossing. Mud and water spray as the bike powers through challenging terrain. The atmosphere is wild and adventurous. Audio: Tires gripping dirt, gears shifting, heavy breathing, branches whipping past, and water splashing.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/hailuo/2.3/pro/image-to-video", {
  "image": "https://static.sandbase.ai/examples/de44ef69-c470-4b15-9301-767263198fdf/input/11bdc5d4-7794-4c9d-92b2-006b6b46071d.jpg",
  "prompt": "The camera follows the mountain biker as they navigate a technical forest trail at high speed, wheels bouncing over roots and rocks. The rider approaches a jump, launching into the air with the bike, both rider and machine perfectly synchronized. They land smoothly and continue through tight turns, splashing through a stream crossing. Mud and water spray as the bike powers through challenging terrain. The atmosphere is wild and adventurous. Audio: Tires gripping dirt, gears shifting, heavy breathing, branches whipping past, and water splashing."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/hailuo/2.3/pro/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/de44ef69-c470-4b15-9301-767263198fdf/input/11bdc5d4-7794-4c9d-92b2-006b6b46071d.jpg",
	"prompt": "The camera follows the mountain biker as they navigate a technical forest trail at high speed, wheels bouncing over roots and rocks. The rider approaches a jump, launching into the air with the bike, both rider and machine perfectly synchronized. They land smoothly and continue through tight turns, splashing through a stream crossing. Mud and water spray as the bike powers through challenging terrain. The atmosphere is wild and adventurous. Audio: Tires gripping dirt, gears shifting, heavy breathing, branches whipping past, and water splashing.",
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

Hailuo 2.3 Pro animates a still image into a 6-second 1080P video with expressive characters.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
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

Other Hailuo 2.3 endpoints: `minimax/hailuo/2.3/pro/text-to-video`, `minimax/hailuo/2.3/standard/text-to-video`, `minimax/hailuo/2.3/standard/image-to-video`, `minimax/hailuo/2.3-fast/pro/image-to-video`, `minimax/hailuo/2.3-fast/standard/image-to-video`, `minimax/h3/text-to-video` (newer, with audio).

---
Machine-readable: [`catalog/models/minimax/hailuo/2.3/pro/image-to-video.json`](../../../../../../catalog/models/minimax/hailuo/2.3/pro/image-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/hailuo/2.3/pro/image-to-video
