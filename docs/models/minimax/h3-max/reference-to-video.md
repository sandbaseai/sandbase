# MiniMax H3 Max Reference to Video API: pricing, parameters and code examples

`minimax/h3-max/reference-to-video` · video generation model · MiniMax · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.4 per call · **Modes:** async

MiniMax H3 Max by MiniMax generates a 5-15 second video with native audio at 480P or 768P that keeps subjects, motion, and voice consistent with reference images, videos, and audio.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.reference_tokens`).

Formula: `(params.duration ?? 5) * ((params.resolution ?? "768P") == "480P" ? 0.05 : 0.08) + Math.max((usage.reference_tokens ?? 4096.0) - 4096.0, 0.0) * 0.00002`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3-max/reference-to-video", "aspect_ratio": "16:9", "audios": ["https://static.sandbase.ai/examples/c1934625-e6b2-40d7-bf17-9017e8ca6191/input/233a82cc-7618-4314-967c-b14207086234.mp3"], "duration": 9, "images": ["https://static.sandbase.ai/examples/c1934625-e6b2-40d7-bf17-9017e8ca6191/input/26f1c4a1-bfb2-4db6-a27f-aafabd36b0d5.png"], "prompt": "Image 1 is the male character. Audio1 is him talking.  Lipsync Image1 to Audio1", "prompt_expansion_mode": "balanced", "resolution": "480P"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3-max/reference-to-video', {'aspect_ratio': '16:9', 'audios': ['https://static.sandbase.ai/examples/c1934625-e6b2-40d7-bf17-9017e8ca6191/input/233a82cc-7618-4314-967c-b14207086234.mp3'], 'duration': 9, 'images': ['https://static.sandbase.ai/examples/c1934625-e6b2-40d7-bf17-9017e8ca6191/input/26f1c4a1-bfb2-4db6-a27f-aafabd36b0d5.png'], 'prompt': 'Image 1 is the male character. Audio1 is him talking.  Lipsync Image1 to Audio1', 'prompt_expansion_mode': 'balanced', 'resolution': '480P'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3-max/reference-to-video", {
  "aspect_ratio": "16:9",
  "audios": [
    "https://static.sandbase.ai/examples/c1934625-e6b2-40d7-bf17-9017e8ca6191/input/233a82cc-7618-4314-967c-b14207086234.mp3"
  ],
  "duration": 9,
  "images": [
    "https://static.sandbase.ai/examples/c1934625-e6b2-40d7-bf17-9017e8ca6191/input/26f1c4a1-bfb2-4db6-a27f-aafabd36b0d5.png"
  ],
  "prompt": "Image 1 is the male character. Audio1 is him talking.  Lipsync Image1 to Audio1",
  "prompt_expansion_mode": "balanced",
  "resolution": "480P"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3-max/reference-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"audios": []any{"https://static.sandbase.ai/examples/c1934625-e6b2-40d7-bf17-9017e8ca6191/input/233a82cc-7618-4314-967c-b14207086234.mp3"},
	"duration": 9,
	"images": []any{"https://static.sandbase.ai/examples/c1934625-e6b2-40d7-bf17-9017e8ca6191/input/26f1c4a1-bfb2-4db6-a27f-aafabd36b0d5.png"},
	"prompt": "Image 1 is the male character. Audio1 is him talking.  Lipsync Image1 to Audio1",
	"prompt_expansion_mode": "balanced",
	"resolution": "480P",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audios` | array |  | Up to 3 reference audio URLs (2-15 seconds each, at most 15 seconds combined), referenced in the prompt as Audio 1, Audio 2, and so on. Audio requires at least one reference image or video.  |
| `images` | array |  | Up to 9 subject or style reference image URLs, referenced in the prompt as Image 1, Image 2, and so on.  |
| `prompt` | string | yes | Text prompt for video generation. Refer to reference assets by their modality and order in the reference lists: Image 1, Image 2, Video 1, Audio 1, and so on.  |
| `videos` | array |  | Up to 3 motion or reference video URLs (2-15 seconds each, at most 15 seconds combined), referenced in the prompt as Video 1, Video 2, and so on.  |
| `duration` | integer |  | The duration of the video in seconds. default `5`; range 5–15 |
| `resolution` | string |  | The native generation resolution of the video. one of: `480P`, `768P`; default `"768P"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose from the prompt and reference inputs. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `prompt_expansion_mode` | string |  | How much effort to spend rewriting the prompt before generation. `balanced` returns in about a second; `quality` spends up to ~30 seconds on a richer prompt. one of: `balanced`, `quality`; default `"balanced"` |

## Details

MiniMax H3 Max reference-to-video: images, videos, and audio references keep subjects, motion, and voice consistent in a 5–15 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | — | Output frame shape. |
| `resolution` | `480P` / `768P` | `768P` | Sets the per-second rate. |
| `duration` | integer 5–15 | 5 | Output length in seconds. |
| `images` | image URL[] (≤9) | — | Reference images, Image 1, Image 2, … |
| `prompt_expansion_mode` | `balanced` / `quality` | `balanced` | `balanced` rewrites the prompt lightly; `quality` expands it more for richer detail. |
| `videos` | video URL[] (≤3) | — | Reference clips, Video 1, … |
| `audios` | audio URL[] (≤3) | — | Reference audio, Audio 1, … |

### Billing

You pay for output seconds: $0.08 at 768P and $0.05 at 480P. Very large reference sets (over 4,096 reference tokens) add $0.02 per 1,000 extra tokens.

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

Other MiniMax H3 Max endpoints: `minimax/h3-max/text-to-video`, `minimax/h3-max/image-to-video`, `minimax/h3/reference-to-video` (2K).

---
Machine-readable: [`catalog/models/minimax/h3-max/reference-to-video.json`](../../../../catalog/models/minimax/h3-max/reference-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/h3-max/reference-to-video
