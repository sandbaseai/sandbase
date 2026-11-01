# MiniMax H3 Text to Video

`minimax/h3/text-to-video` · video · MiniMax

Generate native-stereo 2K video from text with MiniMax H3.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.total_seconds`).

Formula: `(usage.total_seconds ?? params.duration ?? 5) * ((params.resolution ?? "2K") == "768P" ? 0.06 : 0.13)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3/text-to-video", "aspect_ratio": "16:9", "duration": 4, "prompt": "A slow macro tracking shot reveals creamy, steamed milk pouring smoothly into a rustic ceramic cup of rich espresso, creating elegant latte art. Warm morning sunlight streams in from the side, illuminating the rising steam. A shallow depth of field blurs the cozy coffee shop background. The atmosphere is warm, premium, and inviting as the liquids mix realistically.", "resolution": "768P"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3/text-to-video', {'aspect_ratio': '16:9', 'duration': 4, 'prompt': 'A slow macro tracking shot reveals creamy, steamed milk pouring smoothly into a rustic ceramic cup of rich espresso, creating elegant latte art. Warm morning sunlight streams in from the side, illuminating the rising steam. A shallow depth of field blurs the cozy coffee shop background. The atmosphere is warm, premium, and inviting as the liquids mix realistically.', 'resolution': '768P'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3/text-to-video", {
  "aspect_ratio": "16:9",
  "duration": 4,
  "prompt": "A slow macro tracking shot reveals creamy, steamed milk pouring smoothly into a rustic ceramic cup of rich espresso, creating elegant latte art. Warm morning sunlight streams in from the side, illuminating the rising steam. A shallow depth of field blurs the cozy coffee shop background. The atmosphere is warm, premium, and inviting as the liquids mix realistically.",
  "resolution": "768P"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3/text-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"duration": 4,
	"prompt": "A slow macro tracking shot reveals creamy, steamed milk pouring smoothly into a rustic ceramic cup of rich espresso, creating elegant latte art. Warm morning sunlight streams in from the side, illuminating the rising steam. A shallow depth of field blurs the cozy coffee shop background. The atmosphere is warm, premium, and inviting as the liquids mix realistically.",
	"resolution": "768P",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | Prompt default `"A cinematic wide shot of an astronaut walking across a red desert at sunset, wind lifting fine dust, with natural footsteps and distant ambient sound."` |
| `duration` | integer | yes | Duration one of: `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`; default `5` |
| `resolution` | string |  | Output resolution. 768P is generated natively; 2K is upscaled via an in-context regeneration pass. one of: `768P`, `2K`; default `"2K"` |
| `aspect_ratio` | string |  | Aspect Ratio one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; default `"16:9"` |
| `aigc_watermark` | boolean |  | Whether to add an AIGC label watermark to the generated video. default `false` |

## Details

MiniMax H3 generates native-stereo 2K video with sound from a written prompt, 4–15 seconds long.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 7,000 characters. |
| `duration` | 4–15, required | 5 | Output length in seconds. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `768P` / `2K` | `2K` | Sets the per-second rate. |
| `aigc_watermark` | boolean | false | Add MiniMax's AI-generated watermark. |

### Billing

You pay for output seconds: $0.13 at 2K (the default) and $0.06 at 768P.

| Output | 2K | 768P |
|---|---|---|
| 4s | $0.52 | $0.24 |
| 5s (default) | $0.65 | $0.30 |
| 10s | $1.30 | $0.60 |
| 15s | $1.95 | $0.90 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound in order.
- Quote dialogue and name the speaker.

### Limits

- `duration` is required.

### Also on SandBase

Other MiniMax H3 endpoints: `minimax/h3/image-to-video`, `minimax/h3/reference-to-video`, `minimax/h3-max/text-to-video` (faster, cheaper).

---
Machine-readable: [`catalog/models/minimax/h3/text-to-video.json`](../../../../catalog/models/minimax/h3/text-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/h3/text-to-video
