# Vidu Q3 Reference to Video Mix

`vidu/q3/reference-to-video/mix` · video · Vidu

Vidu Q3 Mix by Shengshu - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="360p" | 0.07 |
| duration=1, resolution="540p" | 0.07 |
| duration=1, resolution="720p" | 0.154 |
| duration=1, resolution="1080p" | 0.154 |
| duration=5, resolution="360p" | 0.35 |
| duration=5, resolution="540p" | 0.35 |
| duration=5, resolution="720p" | 0.77 |
| duration=5, resolution="1080p" | 0.77 |
| duration=16, resolution="360p" | 1.12 |
| duration=16, resolution="540p" | 1.12 |
| duration=16, resolution="720p" | 2.464 |
| duration=16, resolution="1080p" | 2.464 |

Formula: `(params.resolution ?? "720p") == "720p" || (params.resolution ?? "720p") == "1080p" ? (params.duration ?? 5) * 0.07 * 2.2 : (params.duration ?? 5) * 0.07`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vidu/q3/reference-to-video/mix", "prompt": "A character walking through a beach catching an apple.", "reference_image_urls": ["https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/aa16b50e-ec40-47df-bda1-3cf46278a584.png", "https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/a35599ea-7845-46e2-b591-0a51da11c67c.png", "https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/faffe658-17e3-41a9-ade8-f307be1c4ff7.png"]}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vidu/q3/reference-to-video/mix', {'prompt': 'A character walking through a beach catching an apple.', 'reference_image_urls': ['https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/aa16b50e-ec40-47df-bda1-3cf46278a584.png', 'https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/a35599ea-7845-46e2-b591-0a51da11c67c.png', 'https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/faffe658-17e3-41a9-ade8-f307be1c4ff7.png']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vidu/q3/reference-to-video/mix", {
  "prompt": "A character walking through a beach catching an apple.",
  "reference_image_urls": [
    "https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/aa16b50e-ec40-47df-bda1-3cf46278a584.png",
    "https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/a35599ea-7845-46e2-b591-0a51da11c67c.png",
    "https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/faffe658-17e3-41a9-ade8-f307be1c4ff7.png"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vidu/q3/reference-to-video/mix", sandbase.Params{
	"prompt": "A character walking through a beach catching an apple.",
	"reference_image_urls": []any{"https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/aa16b50e-ec40-47df-bda1-3cf46278a584.png", "https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/a35599ea-7845-46e2-b591-0a51da11c67c.png", "https://static.sandbase.ai/examples/6491437f-a95b-4ada-aea8-35a842416abf/input/faffe658-17e3-41a9-ade8-f307be1c4ff7.png"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility. If None, a random seed is chosen.  |
| `audio` | boolean |  | Whether to use direct audio-video generation. When true, outputs video with sound. default `true` |
| `prompt` | string | yes | Text prompt for video generation, max 2000 characters  |
| `duration` | integer |  | Duration of the video in seconds (1-16 for Q3 models) default `5`; range 1–16 |
| `resolution` | string |  | Output video resolution one of: `360p`, `540p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`; default `"16:9"` |
| `reference_image_urls` | array | yes | URLs of 1 to 4 reference images used to keep subjects or scenes consistent  |

## Details

Vidu Q3 Mix reference-to-video: reference images keep characters and objects consistent in a 1–16 second clip with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
| `aspect_ratio` | `16:9` / `9:16` / `4:3` / `3:4` / `1:1` | `16:9` | Output frame shape. |
| `audio` | boolean | true | Generate native audio. Same price on or off. |
| `resolution` | `360p` / `540p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–16 | 5 | Output length in seconds. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `reference_image_urls` | image URL[], required | — | Reference images, Image 1, Image 2, … |

### Billing

You pay for output seconds: $0.07 at 360p or 540p and $0.154 at 720p or 1080p.

| Output | 540p | 720p | 1080p |
|---|---|---|---|
| 4s | $0.28 | $0.616 | $0.616 |
| 5s (default) | $0.35 | $0.77 | $0.77 |
| 8s | $0.56 | $1.232 | $1.232 |
| 16s | $1.12 | $2.464 | $2.464 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Vidu Q3 endpoints: `vidu/q3/text-to-video`, `vidu/q3/image-to-video`, `vidu/q3/text-to-video/turbo`, `vidu/q3/image-to-video/turbo`.

---
Machine-readable: [`catalog/models/vidu/q3/reference-to-video/mix.json`](../../../../../catalog/models/vidu/q3/reference-to-video/mix.json) · Store page: https://www.sandbase.ai/model/vidu/q3/reference-to-video/mix
