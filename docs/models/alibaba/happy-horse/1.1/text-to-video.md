# Happy Horse 1.1 Text to Video API: pricing, parameters and code examples

`alibaba/happy-horse/1.1/text-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.21 to $1.44 per run, depending on parameters · **Modes:** async

Happy Horse 1.1 is Alibaba's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="480p" | 0.21 |
| duration=3, resolution="720p" | 0.42 |
| duration=3, resolution="1080p" | 0.54 |
| duration=4, resolution="480p" | 0.28 |
| duration=4, resolution="720p" | 0.56 |
| duration=4, resolution="1080p" | 0.72 |
| duration=5, resolution="480p" | 0.35 |
| duration=5, resolution="720p" | 0.7 |
| duration=5, resolution="1080p" | 0.9 |
| duration=6, resolution="480p" | 0.42 |
| duration=6, resolution="720p" | 0.84 |
| duration=6, resolution="1080p" | 1.08 |
| duration=7, resolution="480p" | 0.49 |
| duration=7, resolution="720p" | 0.98 |
| duration=7, resolution="1080p" | 1.26 |
| duration=8, resolution="480p" | 0.56 |
| duration=8, resolution="720p" | 1.12 |
| duration=8, resolution="1080p" | 1.44 |

Formula: `(params.resolution ?? "720p") == "1080p" ? (params.duration ?? 5) * 0.18 : (params.resolution ?? "720p") == "480p" ? (params.duration ?? 5) * 0.07 : (params.duration ?? 5) * 0.14`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/happy-horse/1.1/text-to-video", "aspect_ratio": "3:2", "duration": 3, "prompt": "A red paper boat floating on a calm lake", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/happy-horse/1.1/text-to-video', {'aspect_ratio': '3:2', 'duration': 3, 'prompt': 'A red paper boat floating on a calm lake', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/happy-horse/1.1/text-to-video", {
  "aspect_ratio": "3:2",
  "duration": 3,
  "prompt": "A red paper boat floating on a calm lake",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/happy-horse/1.1/text-to-video", sandbase.Params{
	"aspect_ratio": "3:2",
	"duration": 3,
	"prompt": "A red paper boat floating on a calm lake",
	"resolution": "720p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-2147483647).  |
| `prompt` | string | yes | Text prompt describing the desired video. Max 2500 characters.  |
| `duration` | integer |  | Output video duration in seconds (3-15). one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | Output video resolution tier. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"16:9"` |

## Details

Happy Horse 1.1 turns a written script into a 3–15 second cinematic clip with realistic motion, lighting, and fine detail. Version 1.1 adds a 480p draft tier and lowers the 1080p rate compared with 1.0.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.07 at 480p, $0.14 at 720p, and $0.18 at 1080p, Alibaba's list price.

| Output | 480p | 720p | 1080p |
|---|---|---|---|
| 3s | $0.21 | $0.42 | $0.54 |
| 5s (default) | $0.35 | $0.70 | $0.90 |
| 10s | $0.70 | $1.40 | $1.80 |
| 15s | $1.05 | $2.10 | $2.70 |

Failed runs are not charged.

### Prompting

- Describe the shot in order: subject, action, setting, camera move, light, and sound.
- Give camera timing explicitly, e.g. “holds for two seconds, then pushes in slowly”.
- Put spoken lines in quotes and say who speaks them.

### Limits

- Text only; to start from a picture use `alibaba/happy-horse/1.1/image-to-video`.

### Also on SandBase

Other Happy Horse endpoints: `alibaba/happy-horse/1.1/image-to-video`, `alibaba/happy-horse/1.1/reference-to-video`, `alibaba/happy-horse/video-edit` (edit an existing clip).

---
Machine-readable: [`catalog/models/alibaba/happy-horse/1.1/text-to-video.json`](../../../../../catalog/models/alibaba/happy-horse/1.1/text-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/happy-horse/1.1/text-to-video
