# Flux 3 Text to Video

`bfl/flux-3/text-to-video` · video · BFL

Flux 3 by BFL - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural motion, camera control, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="720p" | 0.85 |
| duration=5, resolution="1080p" | 1.45 |
| duration=6, resolution="720p" | 1.02 |
| duration=6, resolution="1080p" | 1.74 |
| duration=7, resolution="720p" | 1.19 |
| duration=7, resolution="1080p" | 2.03 |
| duration=8, resolution="720p" | 1.36 |
| duration=8, resolution="1080p" | 2.32 |
| duration=9, resolution="720p" | 1.53 |
| duration=9, resolution="1080p" | 2.61 |
| duration=10, resolution="720p" | 1.7 |
| duration=10, resolution="1080p" | 2.9 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == "1080p" ? 0.29 : 0.17)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bfl/flux-3/text-to-video", "prompt": "a red panda walking along a mossy log"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bfl/flux-3/text-to-video', {'prompt': 'a red panda walking along a mossy log'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bfl/flux-3/text-to-video", {
  "prompt": "a red panda walking along a mossy log"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bfl/flux-3/text-to-video", sandbase.Params{
	"prompt": "a red panda walking along a mossy log",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `prompt` | string | yes | The text prompt describing the video you want to generate.  |
| `duration` | integer |  | Video duration in seconds (5-20). one of: `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16` …; default `5` |
| `resolution` | string |  | Resolution of the generated video. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `21:9`, `2:1`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Whether to generate audio for the video. default `true` |

## Details

FLUX 3 text-to-video: 5–20 second clips with optional native audio at 720p or 1080p.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `2:1` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | 5–20 | 5 | Output length in seconds. |
| `generate_audio` | boolean | true | Native audio. Same price on or off. |

### Billing

You pay for output seconds: $0.17 at 720p and $0.29 at 1080p.

| Output | 720p | 1080p |
|---|---|---|
| 5s (default) | $0.85 | $1.45 |
| 10s | $1.70 | $2.90 |
| 20s | $3.40 | $5.80 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Limits

- Clips are 5–20 seconds.

### Also on SandBase

Other FLUX 3 endpoints: `bfl/flux-3/text-to-image`, `bfl/flux-3/edit`, `bfl/flux-3/image-to-video`.

---
Machine-readable: [`catalog/models/bfl/flux-3/text-to-video.json`](../../../../catalog/models/bfl/flux-3/text-to-video.json) · Store page: https://www.sandbase.ai/model/bfl/flux-3/text-to-video
