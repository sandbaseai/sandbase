# MiniMax H3 Max Text to Video

`minimax/h3-max/text-to-video` · video · MiniMax

MiniMax H3 Max by MiniMax turns a text prompt into a 5-15 second video with native audio at 480P or 768P, generating faster than MiniMax H3.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="480P" | 0.25 |
| duration=5, resolution="768P" | 0.4 |
| duration=15, resolution="480P" | 0.75 |
| duration=15, resolution="768P" | 1.2 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "768P") == "480P" ? 0.05 : 0.08)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3-max/text-to-video", "prompt": "A white kitten chases a butterfly across a sunlit garden. Gentle camera tracking, natural movement, soft afternoon light filtering through the leaves."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3-max/text-to-video', {'prompt': 'A white kitten chases a butterfly across a sunlit garden. Gentle camera tracking, natural movement, soft afternoon light filtering through the leaves.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3-max/text-to-video", {
  "prompt": "A white kitten chases a butterfly across a sunlit garden. Gentle camera tracking, natural movement, soft afternoon light filtering through the leaves."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3-max/text-to-video", sandbase.Params{
	"prompt": "A white kitten chases a butterfly across a sunlit garden. Gentle camera tracking, natural movement, soft afternoon light filtering through the leaves.",
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
| `duration` | integer |  | The duration of the video in seconds. default `5`; range 5–15 |
| `resolution` | string |  | The native generation resolution of the video. one of: `480P`, `768P`; default `"768P"` |
| `aspect_ratio` | string |  | Aspect ratio of the generated video. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; default `"16:9"` |
| `prompt_expansion_mode` | string |  | How much effort to spend rewriting the prompt before generation. `balanced` returns in about a second; `quality` spends up to ~30 seconds on a richer prompt. one of: `balanced`, `quality`; default `"balanced"` |

## Details

MiniMax H3 Max turns a prompt into a 5–15 second video with native audio at 480P or 768P, faster than H3.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `480P` / `768P` | `768P` | Sets the per-second rate. |
| `duration` | integer 5–15 | 5 | Output length in seconds. |
| `prompt_expansion_mode` | `balanced` / `quality` | `balanced` | `balanced` rewrites the prompt lightly; `quality` expands it more for richer detail. |

### Billing

You pay for output seconds: $0.08 at 768P and $0.05 at 480P.

| Output | 768P | 480P |
|---|---|---|
| 5s (default) | $0.40 | $0.25 |
| 10s | $0.80 | $0.50 |
| 15s | $1.20 | $0.75 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound in order.
- Quote dialogue and name the speaker.

### Limits

- Clips are 5–15 seconds.

### Also on SandBase

Other MiniMax H3 Max endpoints: `minimax/h3-max/image-to-video`, `minimax/h3-max/reference-to-video`, `minimax/h3/text-to-video` (2K).

---
Machine-readable: [`catalog/models/minimax/h3-max/text-to-video.json`](../../../../catalog/models/minimax/h3-max/text-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/h3-max/text-to-video
