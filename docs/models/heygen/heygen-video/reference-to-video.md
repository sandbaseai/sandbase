# HeyGen Video Reference to Video API: pricing, parameters and code examples

`heygen/heygen-video/reference-to-video` · video generation model · HeyGen · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.35 to $2.7 per run, depending on parameters · **Modes:** async

HeyGen Video Reference to Video generates a 5-15 second video guided by reference images, videos and audio.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="480p" | 0.35 |
| duration=5, resolution="768p" | 0.5 |
| duration=5, resolution="1080p" | 0.9 |
| duration=5, resolution="2k" | 0.9 |
| duration=15, resolution="480p" | 1.05 |
| duration=15, resolution="768p" | 1.5 |
| duration=15, resolution="1080p" | 2.7 |
| duration=15, resolution="2k" | 2.7 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "768p") == "480p" ? 0.07 : (params.resolution ?? "768p") == "768p" ? 0.1 : 0.18)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/heygen-video/reference-to-video", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/dbd3acd5-a7f8-4bc6-a1c3-a6abe02c545f/input/f31c8ffc-a03e-43e6-9873-619009a711c2.png"], "prompt": "The tiger from the reference image walks through a snowy pine forest at dusk, snowflakes falling, low-angle shot."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/heygen-video/reference-to-video', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/dbd3acd5-a7f8-4bc6-a1c3-a6abe02c545f/input/f31c8ffc-a03e-43e6-9873-619009a711c2.png'], 'prompt': 'The tiger from the reference image walks through a snowy pine forest at dusk, snowflakes falling, low-angle shot.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/heygen-video/reference-to-video", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/dbd3acd5-a7f8-4bc6-a1c3-a6abe02c545f/input/f31c8ffc-a03e-43e6-9873-619009a711c2.png"
  ],
  "prompt": "The tiger from the reference image walks through a snowy pine forest at dusk, snowflakes falling, low-angle shot."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/heygen-video/reference-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/dbd3acd5-a7f8-4bc6-a1c3-a6abe02c545f/input/f31c8ffc-a03e-43e6-9873-619009a711c2.png"},
	"prompt": "The tiger from the reference image walks through a snowy pine forest at dusk, snowflakes falling, low-angle shot.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audios` | array |  | Up to 3 reference audio clips (voice or music).  |
| `images` | array |  | Up to 9 reference images (characters, products, scenes).  |
| `prompt` | string | yes | Describe the scene, action, camera and sound.  |
| `videos` | array |  | Up to 3 reference videos for motion or style.  |
| `duration` | integer |  | Output length in seconds (5-15). default `5`; range 5–15 |
| `resolution` | string |  | Output resolution. 1080p and 2k cost more. one of: `480p`, `768p`, `1080p`, `2k`; default `"768p"` |
| `aspect_ratio` | string |  | Output frame shape. Leave empty to follow the references (adaptive). one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |

## Details

HeyGen Video Reference to Video generates a 5–15 second video guided by reference images, videos and audio clips.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Scene and action; describe how each reference is used. |
| `images` | image URL[] | — | Up to 9 reference images (characters, products, scenes). |
| `videos` | video URL[] | — | Up to 3 reference videos for motion or style. |
| `audios` | audio URL[] | — | Up to 3 reference audio clips (voice or music). |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | — | Leave empty to follow the references. |
| `resolution` | `480p` / `768p` / `1080p` / `2k` | `768p` | Output resolution; 1080p and 2k cost more. |
| `duration` | 5–15 | 5 | Output length in seconds. |
### Billing
Billed per output second: $0.07 at 480p, $0.10 at 768p, $0.18 at 1080p and 2k. References are not billed separately.
| Output | Price |
|---|---|
| 5s, 768p (default) | $0.50 |
| 5s, 480p | $0.35 |
| 10s, 1080p | $1.80 |
Failed runs are not charged.
### Prompting
- Say which reference is the subject and which sets motion, style or sound.
### Limits
- Clips are 5–15 seconds.
### Also on SandBase
Other HeyGen Video endpoints: `heygen/heygen-video/text-to-video`, `heygen/heygen-video/image-to-video`.

---
Machine-readable: [`catalog/models/heygen/heygen-video/reference-to-video.json`](../../../../catalog/models/heygen/heygen-video/reference-to-video.json) · Store page: https://www.sandbase.ai/model/heygen/heygen-video/reference-to-video
