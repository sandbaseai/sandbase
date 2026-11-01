# HeyGen Video Text to Video

`heygen/heygen-video/text-to-video` · video · HeyGen

HeyGen Video Text to Video turns a text prompt into a 5-15 second video at up to 2K resolution.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="480p" | 0.1 |
| duration=5, resolution="768p" | 0.18 |
| duration=5, resolution="1080p" | 0.3 |
| duration=5, resolution="2k" | 0.3 |
| duration=15, resolution="480p" | 0.3 |
| duration=15, resolution="768p" | 0.54 |
| duration=15, resolution="1080p" | 0.9 |
| duration=15, resolution="2k" | 0.9 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "768p") == "480p" ? 0.02 : (params.resolution ?? "768p") == "768p" ? 0.036 : 0.06)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/heygen-video/text-to-video", "aspect_ratio": "16:9", "prompt": "A red paper boat drifting on a calm misty lake at sunrise, gentle camera push-in, soft golden light, birds calling in the distance."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/heygen-video/text-to-video', {'aspect_ratio': '16:9', 'prompt': 'A red paper boat drifting on a calm misty lake at sunrise, gentle camera push-in, soft golden light, birds calling in the distance.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/heygen-video/text-to-video", {
  "aspect_ratio": "16:9",
  "prompt": "A red paper boat drifting on a calm misty lake at sunrise, gentle camera push-in, soft golden light, birds calling in the distance."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/heygen-video/text-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "A red paper boat drifting on a calm misty lake at sunrise, gentle camera push-in, soft golden light, birds calling in the distance.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Describe the scene, action, camera and sound.  |
| `duration` | integer |  | Output length in seconds (5-15). default `5`; range 5–15 |
| `resolution` | string |  | Output resolution. 1080p and 2k cost more. one of: `480p`, `768p`, `1080p`, `2k`; default `"768p"` |
| `aspect_ratio` | string |  | Output frame shape. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; default `"16:9"` |

## Details

HeyGen Video turns a text prompt into a 5–15 second video at up to 2K resolution.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Scene, action, camera and sound. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `480p` / `768p` / `1080p` / `2k` | `768p` | Output resolution; 1080p and 2k cost more. |
| `duration` | 5–15 | 5 | Output length in seconds. |
### Billing
Billed per output second: $0.02 at 480p, $0.036 at 768p, $0.06 at 1080p and 2k.
| Output | Price |
|---|---|
| 5s, 768p (default) | $0.18 |
| 5s, 480p | $0.10 |
| 10s, 1080p | $0.60 |
| 15s, 2k | $0.90 |
Failed runs are not charged.
### Prompting
- Describe subject, action, camera move and light in order.
### Limits
- Clips are 5–15 seconds.
### Also on SandBase
Other HeyGen Video endpoints: `heygen/heygen-video/image-to-video`, `heygen/heygen-video/reference-to-video`.

---
Machine-readable: [`catalog/models/heygen/heygen-video/text-to-video.json`](../../../../catalog/models/heygen/heygen-video/text-to-video.json) · Store page: https://www.sandbase.ai/model/heygen/heygen-video/text-to-video
