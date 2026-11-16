# Kling V4 Flash Text to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/v4/flash/text-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.282 to $1.88 per run, depending on parameters · **Modes:** async

Kling V4 Flash Text to Video by Kuaishou turns a text prompt into a 3-20 second 720p video at a lower price than Kling V4.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=3 | 0.282 |
| duration=5 | 0.47 |
| duration=20 | 1.88 |

Formula: `(params.duration ?? 5) * 0.094`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v4/flash/text-to-video", "aspect_ratio": "16:9", "prompt": "Elegant luxury resort film, one continuous camera move with no cuts: from an unmade bed, out through open glass doors, across a teak deck and down to the waterline as a guest dives in for the first swim of the day just as the sun breaks the horizon. Soft golden light, gentle lens flare, sound of waves and birds."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v4/flash/text-to-video', {'aspect_ratio': '16:9', 'prompt': 'Elegant luxury resort film, one continuous camera move with no cuts: from an unmade bed, out through open glass doors, across a teak deck and down to the waterline as a guest dives in for the first swim of the day just as the sun breaks the horizon. Soft golden light, gentle lens flare, sound of waves and birds.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v4/flash/text-to-video", {
  "aspect_ratio": "16:9",
  "prompt": "Elegant luxury resort film, one continuous camera move with no cuts: from an unmade bed, out through open glass doors, across a teak deck and down to the waterline as a guest dives in for the first swim of the day just as the sun breaks the horizon. Soft golden light, gentle lens flare, sound of waves and birds."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v4/flash/text-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "Elegant luxury resort film, one continuous camera move with no cuts: from an unmade bed, out through open glass doors, across a teak deck and down to the waterline as a guest dives in for the first swim of the day just as the sun breaks the horizon. Soft golden light, gentle lens flare, sound of waves and birds.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Describe subject, action, camera and light.  |
| `duration` | integer |  | Output length in seconds (3-20). default `5`; range 3–20 |
| `aspect_ratio` | string |  | Output frame shape. one of: `16:9`, `9:16`, `1:1`, `21:9`; default `"16:9"` |

## Details

Kling V4 Flash text-to-video is the faster, lower-cost tier of Kling V4: write a scene and get back a 3–20 second 720p clip with sound.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Describe subject, action, camera and light. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `21:9` | `16:9` | Output frame shape. |
| `duration` | 3–20 | 5 | Output length in seconds. |
### Billing
Billed per output second: $0.094 at 720p.
| Output | Price |
|---|---|
| 5s (default) | $0.47 |
| 10s | $0.94 |
| 20s | $1.88 |
Failed runs are not charged.
### Prompting
- Describe subject, action, camera move and light in order.
### Limits
- Output is 720p only; clips are 3–20 seconds.
### Also on SandBase
Other Kling V4 Flash endpoints: `kwaivgi/kling-video/v4/flash/text-to-video`, `kwaivgi/kling-video/v4/flash/image-to-video`, `kwaivgi/kling-video/v4/flash/reference-to-video`, `kwaivgi/kling-video/v4/flash/video-edit`. For 1080p or clips up to 30 seconds, use Kling V4 (`kwaivgi/kling-video/v4/text-to-video` and its siblings).

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v4/flash/text-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v4/flash/text-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v4/flash/text-to-video
