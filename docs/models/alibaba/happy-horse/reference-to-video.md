# Happy Horse Reference to Video

`alibaba/happy-horse/reference-to-video` · video · Alibaba

Alibaba's #1-ranked Happy Horse 1.0 generates stunning 1080p videos with synchronized native audio and multilingual lip-sync, transforming text prompts or images into cinematic, true-to-life motion content for next-generation AIGC creation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="720p" | 0.42 |
| duration=3, resolution="1080p" | 0.72 |
| duration=4, resolution="720p" | 0.56 |
| duration=4, resolution="1080p" | 0.96 |
| duration=5, resolution="720p" | 0.7 |
| duration=5, resolution="1080p" | 1.2 |
| duration=6, resolution="720p" | 0.84 |
| duration=6, resolution="1080p" | 1.44 |
| duration=7, resolution="720p" | 0.98 |
| duration=7, resolution="1080p" | 1.68 |
| duration=8, resolution="720p" | 1.12 |
| duration=8, resolution="1080p" | 1.92 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == "1080p" ? 0.24 : 0.14)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/happy-horse/reference-to-video", "duration": 3, "images": ["https://static.sandbase.ai/examples/980bea80-d0f0-4a93-a123-a4cc00ba9a8d/input/4c5e3307-6130-44c4-8b60-6e2da3a68c0e.jpg"], "prompt": "[Image 1] waves at the camera in a park", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/happy-horse/reference-to-video', {'duration': 3, 'images': ['https://static.sandbase.ai/examples/980bea80-d0f0-4a93-a123-a4cc00ba9a8d/input/4c5e3307-6130-44c4-8b60-6e2da3a68c0e.jpg'], 'prompt': '[Image 1] waves at the camera in a park', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/happy-horse/reference-to-video", {
  "duration": 3,
  "images": [
    "https://static.sandbase.ai/examples/980bea80-d0f0-4a93-a123-a4cc00ba9a8d/input/4c5e3307-6130-44c4-8b60-6e2da3a68c0e.jpg"
  ],
  "prompt": "[Image 1] waves at the camera in a park",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/happy-horse/reference-to-video", sandbase.Params{
	"duration": 3,
	"images": []any{"https://static.sandbase.ai/examples/980bea80-d0f0-4a93-a123-a4cc00ba9a8d/input/4c5e3307-6130-44c4-8b60-6e2da3a68c0e.jpg"},
	"prompt": "[Image 1] waves at the camera in a park",
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
| `seed` | integer |  | Random seed for reproducible results. Set to -1 for random seed.  |
| `images` | array | yes | The URLs of the images to use for image-to-image generation or image editing.  |
| `prompt` | string | yes | The text prompt to generate a video from, guided by the reference image. default `"In the early morning, just as the sun begins to rise, a small pumpkin sits in the pumpkin patch with dewdrops glistening on its surface. Suddenly, with a crisp crack, a fissure appears on the little pumpkin, and golden light shines through the crack. The pumpkin splits open along with the golden glow, releasing a puff of white mist, and a little rabbit appears in the center of the cracked pumpkin."` |
| `duration` | integer |  | The duration of the generated video in seconds. one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default `"16:9"` |

## Details

Happy Horse 1.0 reference-to-video: place subjects from reference images into a new scene described by the prompt.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `images` | image URL[], required | — | Reference images, Image 1, Image 2, … |
| `prompt` | string, required | — | Up to 50,000 characters. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` | `16:9` | Output frame shape. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.14 at 720p and $0.24 at 1080p, Alibaba's list price.

| Output | 720p | 1080p |
|---|---|---|
| 3s | $0.42 | $0.72 |
| 5s (default) | $0.70 | $1.20 |
| 10s | $1.40 | $2.40 |
| 15s | $2.10 | $3.60 |

Failed runs are not charged.

### Prompting

- Refer to each reference by number and give it a role.

### Limits

- 720p and 1080p only.

### Also on SandBase

Other Happy Horse endpoints: `alibaba/happy-horse/text-to-video`, `alibaba/happy-horse/image-to-video`, `alibaba/happy-horse/video-edit`, `alibaba/happy-horse/1.1/reference-to-video` (newer).

---
Machine-readable: [`catalog/models/alibaba/happy-horse/reference-to-video.json`](../../../../catalog/models/alibaba/happy-horse/reference-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/happy-horse/reference-to-video
