# Luma Ray 3.2 Text to Video API: pricing, parameters and code examples

`luma/ray/3.2/text-to-video` · video generation model · Luma · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.5 to $4 per run, depending on parameters · **Modes:** async

Agent Ray 3.2 is Luma's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="540p" | 0.5 |
| duration=5, resolution="720p" | 1 |
| duration=5, resolution="1080p" | 2 |
| duration=10, resolution="540p" | 1 |
| duration=10, resolution="720p" | 2 |
| duration=10, resolution="1080p" | 4 |

Formula: `((params.duration ?? 5) == 10 ? 2 : 1) * ((params.resolution ?? "720p") == "1080p" ? 2.0 : (params.resolution ?? "720p") == "720p" ? 1.0 : 0.5)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "luma/ray/3.2/text-to-video", "prompt": "A herd of wild horses galloping across a dusty desert plain under a blazing midday sun, their manes flying in the wind; wide tracking shot."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('luma/ray/3.2/text-to-video', {'prompt': 'A herd of wild horses galloping across a dusty desert plain under a blazing midday sun, their manes flying in the wind; wide tracking shot.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("luma/ray/3.2/text-to-video", {
  "prompt": "A herd of wild horses galloping across a dusty desert plain under a blazing midday sun, their manes flying in the wind; wide tracking shot."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "luma/ray/3.2/text-to-video", sandbase.Params{
	"prompt": "A herd of wild horses galloping across a dusty desert plain under a blazing midday sun, their manes flying in the wind; wide tracking shot.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hdr` | boolean |  | Generate an HDR-encoded MP4. Requires HDR access on the account and a resolution of 720p or 1080p; not supported with 10s or loop. default `false` |
| `loop` | boolean |  | Generate a seamless loop. Only valid for 5s, standard-dynamic-range generations without an end frame. default `false` |
| `prompt` | string | yes | Text prompt describing the video to generate.  |
| `duration` | integer |  | Duration of the generated video. one of: `5`, `10`; default `5` |
| `exr_export` | boolean |  | Also export an EXR file alongside the MP4. Requires hdr=true and HDR access. default `false` |
| `resolution` | string |  | Resolution of the generated video. Higher resolutions cost more. one of: `540p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; default `"16:9"` |

## Details

Luma Ray 3.2 turns a prompt into a 5 or 10 second clip at 540p to 1080p, with optional HDR and looping.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 6,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `540p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `loop` | boolean | false | Make the clip loop. |
| `hdr` | boolean | false | 16-bit HDR output (720p and 1080p); doubles the price. |
| `exr_export` | boolean | false | Also export EXR frames with HDR; triples the price. |

### Billing

$0.50 per 5-second clip at 540p, $1.00 at 720p, $2.00 at 1080p; 10 seconds costs double.

| Output | 540p | 720p | 1080p |
|---|---|---|---|
| 5s (default) | $0.50 | $1.00 | $2.00 |
| 10s | $1.00 | $2.00 | $4.00 |

Failed runs are not charged.

### Prompting

- Describe the shot like a cinematographer: subject, motion, lens, and light.

### Limits

- Clips are 5 or 10 seconds.

### Also on SandBase

Related: `luma/ray/3.2/image-to-video`.

---
Machine-readable: [`catalog/models/luma/ray/3.2/text-to-video.json`](../../../../../catalog/models/luma/ray/3.2/text-to-video.json) · Store page: https://www.sandbase.ai/model/luma/ray/3.2/text-to-video
