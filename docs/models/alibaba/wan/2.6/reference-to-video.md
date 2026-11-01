# Wan 2.6 Reference to Video

`alibaba/wan/2.6/reference-to-video` · video · Alibaba

Alibaba Wan 2.6 reference-to-video model generating video guided by reference content.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `params.videos`).

| parameters | USD |
|---|---|
| duration=5, resolution="720p" | 1 |
| duration=5, resolution="1080p" | 1.5 |
| duration=10, resolution="720p" | 1.5 |
| duration=10, resolution="1080p" | 2.25 |

Formula: `((params.duration ?? 5) + (len(params.videos ?? []) > 0 ? 5 : 0)) * ((params.resolution ?? "720p") == "1080p" ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.6/reference-to-video", "duration": 5, "prompt": "character1 waves at the camera in a park", "resolution": "720p", "videos": ["https://static.sandbase.ai/examples/c72451c5-1f5c-4eda-a2ee-25f90d5edd48/input/066dc590-034d-4da8-a5d9-93f357a55807.mp4"]}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.6/reference-to-video', {'duration': 5, 'prompt': 'character1 waves at the camera in a park', 'resolution': '720p', 'videos': ['https://static.sandbase.ai/examples/c72451c5-1f5c-4eda-a2ee-25f90d5edd48/input/066dc590-034d-4da8-a5d9-93f357a55807.mp4']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.6/reference-to-video", {
  "duration": 5,
  "prompt": "character1 waves at the camera in a park",
  "resolution": "720p",
  "videos": [
    "https://static.sandbase.ai/examples/c72451c5-1f5c-4eda-a2ee-25f90d5edd48/input/066dc590-034d-4da8-a5d9-93f357a55807.mp4"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.6/reference-to-video", sandbase.Params{
	"duration": 5,
	"prompt": "character1 waves at the camera in a park",
	"resolution": "720p",
	"videos": []any{"https://static.sandbase.ai/examples/c72451c5-1f5c-4eda-a2ee-25f90d5edd48/input/066dc590-034d-4da8-a5d9-93f357a55807.mp4"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed (0-2147483647) for reproducible results. Omit for a random seed.  |
| `images` | array |  | Reference images, referred to in the prompt as Image1, Image2, ... Combined with videos, up to 5 references in total.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"Video1 holds Image2 and plays a soothing country folk song on the chair from Image3, saying: 'The sunshine is so nice today.' Image1 holds a bouquet of sunflowers, walks past Video1, places the flowers on the table next to Video1, and says: 'That sounds lovely, could you sing it again?'"` |
| `videos` | array |  | The URLs of reference videos to guide video generation.  |
| `duration` | integer |  | The duration of the generated video in seconds. Valid values are 5 and 10. one of: `5`, `10`; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `1:1`, `4:3`, `3:4`, `16:9`, `9:16`; default `"16:9"` |

## Details

Place characters from reference images or short reference videos into a new scene. Name each reference in the prompt and Wan 2.6 keeps their look while they act out the scene, including multi-character interactions and dialogue.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `videos` | video URL[] | — | Reference clips, Video 1, Video 2, … |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `aspect_ratio` | `1:1` / `4:3` / `3:4` / `16:9` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `images` | image URL[] | — | Reference images, Image 1, Image 2, … |

### Billing

You pay for output seconds: $0.10 at 720p and $0.15 at 1080p, Alibaba's list price. When you send reference `videos`, 5 seconds of input are added to the billed length.

| Output | 720p | 1080p |
|---|---|---|
| 5s, images only | $0.50 | $0.75 |
| 5s, with reference video | $1.00 | $1.50 |
| 10s, images only | $1.00 | $1.50 |

Failed runs are not charged.

### Prompting

- Give every reference a role and refer to it by number: “Video 1 plays guitar on the chair from Image 3”.
- Quote dialogue and name the speaker.

### Limits

- Send at least one image or video reference.

### Also on SandBase

Other Wan 2.6 endpoints: `alibaba/wan/2.6/text-to-video`, `alibaba/wan/2.6/image-to-video`, `alibaba/wan/2.6/flash/image-to-video`, `alibaba/wan/2.6/flash/reference-to-video`, `alibaba/wan/2.6/text-to-image`, `alibaba/wan/2.6/image-to-image`, `alibaba/wan/2.7/text-to-video` (newer).

---
Machine-readable: [`catalog/models/alibaba/wan/2.6/reference-to-video.json`](../../../../../catalog/models/alibaba/wan/2.6/reference-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.6/reference-to-video
