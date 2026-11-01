# Wan 2.2 Animate Move

`alibaba/wan/2.2/animate/move` · video · Alibaba

Wan 2.2 Animate Move animates the character in the image with the motion of the reference video.

## Pricing

- Depends on parameters (`params.resolution`, `params.video`, `usage.duration`, `usage.fps`).

Formula: `((usage.duration ?? media_duration(params.video) ?? 5.0) * (usage.fps ?? 30.0) / 16.0) * ((params.resolution ?? "720p") == "720p" ? 0.08 : (params.resolution ?? "720p") == "580p" ? 0.06 : 0.04)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.2/animate/move", "image": "https://static.sandbase.ai/examples/ba85e11e-bed1-49d9-beef-110d08b1ba84/input/c7c1186b-1e49-4d8c-8e54-d630bc7fb8b1.png", "video": "https://static.sandbase.ai/examples/ba85e11e-bed1-49d9-beef-110d08b1ba84/input/4dcec186-db5d-4690-bcf1-c6ecdfbbeecd.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.2/animate/move', {'image': 'https://static.sandbase.ai/examples/ba85e11e-bed1-49d9-beef-110d08b1ba84/input/c7c1186b-1e49-4d8c-8e54-d630bc7fb8b1.png', 'video': 'https://static.sandbase.ai/examples/ba85e11e-bed1-49d9-beef-110d08b1ba84/input/4dcec186-db5d-4690-bcf1-c6ecdfbbeecd.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.2/animate/move", {
  "image": "https://static.sandbase.ai/examples/ba85e11e-bed1-49d9-beef-110d08b1ba84/input/c7c1186b-1e49-4d8c-8e54-d630bc7fb8b1.png",
  "video": "https://static.sandbase.ai/examples/ba85e11e-bed1-49d9-beef-110d08b1ba84/input/4dcec186-db5d-4690-bcf1-c6ecdfbbeecd.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.2/animate/move", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/ba85e11e-bed1-49d9-beef-110d08b1ba84/input/c7c1186b-1e49-4d8c-8e54-d630bc7fb8b1.png",
	"video": "https://static.sandbase.ai/examples/ba85e11e-bed1-49d9-beef-110d08b1ba84/input/4dcec186-db5d-4690-bcf1-c6ecdfbbeecd.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility. range 0–2147483647 |
| `image` | string | yes | Input image URL (face / character).  |
| `video` | string | yes | Reference video.  |
| `use_turbo` | boolean |  | Faster generation with quality enhancement. default `false` |
| `resolution` | string |  | Output resolution. one of: `480p`, `580p`, `720p`; default `"720p"` |

## Details

Make the character in `image` perform the motion of a reference `video`. The picture supplies identity and outfit; the video supplies body movement, expression, and timing.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Character image. JPEG, PNG, or WebP URL. |
| `video` | video URL, required | — | Reference video that supplies the motion. |
| `resolution` | `480p` / `580p` / `720p` | `720p` | Sets the rate. |
| `use_turbo` | boolean | false | Faster generation at some quality cost. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

Billing follows the upstream unit: output seconds counted at 16 frames per second, so a 30fps output bills about 1.9× its wall-clock length. Rates per counted second: $0.04 at 480p, $0.06 at 580p, $0.08 at 720p. The quote before submission assumes a 5-second, 30fps result; the final charge uses the measured output.

| Output | 480p | 580p | 720p |
|---|---|---|---|
| 5s at 30fps | $0.375 | $0.5625 | $0.75 |
| 10s at 30fps | $0.75 | $1.125 | $1.50 |
| 10s at 16fps | $0.40 | $0.60 | $0.80 |

Failed runs are not charged.

### Prompting

- Use a full-body or half-body character image with the limbs visible.
- Pick a reference video with one person, a steady camera, and clear movement.

### Limits

- Output length follows the reference video.

### Also on SandBase

Other Wan 2.2 endpoints: `alibaba/wan/2.2/animate/replace`, `alibaba/wan/2.2/speech-to-video`.

---
Machine-readable: [`catalog/models/alibaba/wan/2.2/animate/move.json`](../../../../../../catalog/models/alibaba/wan/2.2/animate/move.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.2/animate/move
