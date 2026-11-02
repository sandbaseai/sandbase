# MiniMax H3 Reference to Video API: pricing, parameters and code examples

`minimax/h3/reference-to-video` · video generation model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.65 per call · **Modes:** async

Generate native-stereo 2K video guided by image, video, and audio references with MiniMax H3.

## Pricing

- Depends on parameters (`params.duration`, `params.images`, `params.resolution`, `usage.total_seconds`).

Formula: `((usage.total_seconds ?? params.duration ?? 5) * ((params.resolution ?? "2K") == "768P" ? 0.06 : 0.13)) + (Math.max(float(len(params.images ?? [])) - 5.0, 0.0) * 0.04)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3/reference-to-video", "aigc_watermark": false, "audios": [], "duration": 7, "images": ["https://static.sandbase.ai/examples/bff323df-f593-467c-b6a7-96a7bf473983/input/4c91f51e-f6d9-426a-8896-4678c7a115c7.jpg"], "prompt": "anime scene, two-shot on a campus path: the reference character (male student) stops and faces a middle-aged female dormitory counselor in her 40s, counselor has chestnut bob hair, glasses, navy blazer, holding a small key, slightly serious expression, noon lighting, calm atmosphere, cinematic composition, Hyouka-style", "resolution": "768P", "videos": []}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3/reference-to-video', {'aigc_watermark': False, 'audios': [], 'duration': 7, 'images': ['https://static.sandbase.ai/examples/bff323df-f593-467c-b6a7-96a7bf473983/input/4c91f51e-f6d9-426a-8896-4678c7a115c7.jpg'], 'prompt': 'anime scene, two-shot on a campus path: the reference character (male student) stops and faces a middle-aged female dormitory counselor in her 40s, counselor has chestnut bob hair, glasses, navy blazer, holding a small key, slightly serious expression, noon lighting, calm atmosphere, cinematic composition, Hyouka-style', 'resolution': '768P', 'videos': []})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3/reference-to-video", {
  "aigc_watermark": false,
  "audios": [],
  "duration": 7,
  "images": [
    "https://static.sandbase.ai/examples/bff323df-f593-467c-b6a7-96a7bf473983/input/4c91f51e-f6d9-426a-8896-4678c7a115c7.jpg"
  ],
  "prompt": "anime scene, two-shot on a campus path: the reference character (male student) stops and faces a middle-aged female dormitory counselor in her 40s, counselor has chestnut bob hair, glasses, navy blazer, holding a small key, slightly serious expression, noon lighting, calm atmosphere, cinematic composition, Hyouka-style",
  "resolution": "768P",
  "videos": []
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3/reference-to-video", sandbase.Params{
	"aigc_watermark": false,
	"audios": []any{},
	"duration": 7,
	"images": []any{"https://static.sandbase.ai/examples/bff323df-f593-467c-b6a7-96a7bf473983/input/4c91f51e-f6d9-426a-8896-4678c7a115c7.jpg"},
	"prompt": "anime scene, two-shot on a campus path: the reference character (male student) stops and faces a middle-aged female dormitory counselor in her 40s, counselor has chestnut bob hair, glasses, navy blazer, holding a small key, slightly serious expression, noon lighting, calm atmosphere, cinematic composition, Hyouka-style",
	"resolution": "768P",
	"videos": []any{},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audios` | array |  | Audio requires at least one reference image or video.  |
| `images` | array |  | Reference Images  |
| `prompt` | string | yes | Prompt default `"Keep the referenced character and motion consistent while creating a cinematic garden scene with synchronized ambient sound."` |
| `videos` | array |  | Each clip must be 2–15 seconds; combined duration must not exceed 15 seconds.  |
| `duration` | integer | yes | Duration one of: `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`; default `5` |
| `resolution` | string |  | Output resolution. 768P is generated natively; 2K is upscaled via an in-context regeneration pass. one of: `768P`, `2K`; default `"2K"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose from the prompt and reference inputs. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `aigc_watermark` | boolean |  | Whether to add an AIGC label watermark to the generated video. default `false` |

## Details

MiniMax H3 reference-to-video: up to 9 images, 3 videos, and 3 audio clips keep characters, motion, and voice consistent in a new 2K clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 7,000 characters. |
| `images` | image URL[] (≤9) | — | Reference images, Image 1, Image 2, … |
| `videos` | video URL[] (≤3) | — | Reference clips, Video 1, … |
| `audios` | audio URL[] (≤3) | — | Reference audio, Audio 1, … |
| `duration` | 4–15, required | 5 | Output length in seconds. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | — | Output frame shape. |
| `resolution` | `768P` / `2K` | `2K` | Sets the per-second rate. |
| `aigc_watermark` | boolean | false | Add MiniMax's AI-generated watermark. |

### Billing

You pay for output seconds: $0.13 at 2K (the default) and $0.06 at 768P. Each reference image beyond the fifth adds $0.04.

| Output | 2K | 768P |
|---|---|---|
| 4s | $0.52 | $0.24 |
| 5s (default) | $0.65 | $0.30 |
| 10s | $1.30 | $0.60 |
| 15s | $1.95 | $0.90 |
| 5s with 9 images | $0.81 | $0.46 |

Failed runs are not charged.

### Prompting

- Give each reference a role: “Image 1 is the singer, Audio 1 is her voice, Video 1 sets the dance”.

### Limits

- `duration` is required.

### Also on SandBase

Other MiniMax H3 endpoints: `minimax/h3/text-to-video`, `minimax/h3/image-to-video`, `minimax/h3-max/reference-to-video` (faster, cheaper).

---
Machine-readable: [`catalog/models/minimax/h3/reference-to-video.json`](../../../../catalog/models/minimax/h3/reference-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/h3/reference-to-video
