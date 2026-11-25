# MAGI-2 Reference to Video API: pricing, parameters and code examples

`sandai/magi-2/reference-to-video` · video generation model · Sand AI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.32 to $2.4 per run, depending on parameters · **Modes:** async

MAGI-2 by Sand AI creates a 1080p video of 4 to 30 seconds with native audio, guided by up to 10 reference images, 5 video clips and 5 audio clips.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=4 | 0.32 |
| duration=5 | 0.4 |
| duration=30 | 2.4 |

Formula: `(params.duration ?? 5) * 0.08`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sandai/magi-2/reference-to-video", "aspect_ratio": "16:9", "duration": 5, "images": ["https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/776a14fa-b948-478b-bae6-a45c68da5ac7.jpg", "https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/e53fed62-fd62-44db-a206-3cf944d6d8e8.webp"], "prompt": "The pink-haired basketball player in the blue jersey from image 2 walks into the jazz bar from image 1 and dances in front of the band while the camera tracks alongside."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sandai/magi-2/reference-to-video', {'aspect_ratio': '16:9', 'duration': 5, 'images': ['https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/776a14fa-b948-478b-bae6-a45c68da5ac7.jpg', 'https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/e53fed62-fd62-44db-a206-3cf944d6d8e8.webp'], 'prompt': 'The pink-haired basketball player in the blue jersey from image 2 walks into the jazz bar from image 1 and dances in front of the band while the camera tracks alongside.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sandai/magi-2/reference-to-video", {
  "aspect_ratio": "16:9",
  "duration": 5,
  "images": [
    "https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/776a14fa-b948-478b-bae6-a45c68da5ac7.jpg",
    "https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/e53fed62-fd62-44db-a206-3cf944d6d8e8.webp"
  ],
  "prompt": "The pink-haired basketball player in the blue jersey from image 2 walks into the jazz bar from image 1 and dances in front of the band while the camera tracks alongside."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sandai/magi-2/reference-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"duration": 5,
	"images": []any{"https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/776a14fa-b948-478b-bae6-a45c68da5ac7.jpg", "https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/e53fed62-fd62-44db-a206-3cf944d6d8e8.webp"},
	"prompt": "The pink-haired basketball player in the blue jersey from image 2 walks into the jazz bar from image 1 and dances in front of the band while the camera tracks alongside.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-4294967295). Omit for a random seed. range 0–4294967295 |
| `audios` | array |  | Up to 5 WAV/MP3 URLs, 2-30 s each and 30 s in total, up to 15 MB each.  |
| `images` | array |  | Up to 10 public HTTPS image URLs, each under 30 MB.  |
| `prompt` | string | yes | Describe how to use the references, the scene, motion and sound.  |
| `videos` | array |  | Up to 5 MP4/MOV URLs, 2-30 s each and 30 s in total, up to 200 MB each.  |
| `duration` | integer |  | Output video duration in seconds (4-30). Billed per second. default `5`; range 4–30 |
| `resolution` | string |  | Output resolution. MAGI-2 renders 1080p only. one of: `1080p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate a native audio track with the video. Included in the price. default `true` |

---
Machine-readable: [`catalog/models/sandai/magi-2/reference-to-video.json`](../../../../catalog/models/sandai/magi-2/reference-to-video.json) · Store page: https://www.sandbase.ai/model/sandai/magi-2/reference-to-video
