# Happy Horse Image to Video

`alibaba/happy-horse/image-to-video` · video · Alibaba

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
  -d '{"model": "alibaba/happy-horse/image-to-video", "duration": 3, "image": "https://static.sandbase.ai/examples/7c2cda62-fedf-4b96-85d4-46f905309272/input/10329729-dbe9-455b-8a28-d97fb57cb0c5.png", "prompt": "The black cat slowly looks up", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/happy-horse/image-to-video', {'duration': 3, 'image': 'https://static.sandbase.ai/examples/7c2cda62-fedf-4b96-85d4-46f905309272/input/10329729-dbe9-455b-8a28-d97fb57cb0c5.png', 'prompt': 'The black cat slowly looks up', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/happy-horse/image-to-video", {
  "duration": 3,
  "image": "https://static.sandbase.ai/examples/7c2cda62-fedf-4b96-85d4-46f905309272/input/10329729-dbe9-455b-8a28-d97fb57cb0c5.png",
  "prompt": "The black cat slowly looks up",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/happy-horse/image-to-video", sandbase.Params{
	"duration": 3,
	"image": "https://static.sandbase.ai/examples/7c2cda62-fedf-4b96-85d4-46f905309272/input/10329729-dbe9-455b-8a28-d97fb57cb0c5.png",
	"prompt": "The black cat slowly looks up",
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
| `image` | string | yes | The URL of the source image to animate into a video.  |
| `prompt` | string |  | Optional text prompt to guide the video generation. default `"Bring the scene in the image to life."` |
| `duration` | integer |  | The duration of the generated video in seconds. one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |

## Details

Happy Horse 1.0 image-to-video: animate a picture over 3–15 seconds. `prompt` is optional; without it the model brings the scene to life on its own.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `prompt` | string | `Bring the scene in the image to life.` | Optional direction for motion and camera. |
| `duration` | 3–15 | 5 | Output length in seconds. |
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

- Describe the motion and camera, not what is already in the picture.

### Limits

- 720p and 1080p only.

### Also on SandBase

Other Happy Horse endpoints: `alibaba/happy-horse/text-to-video`, `alibaba/happy-horse/reference-to-video`, `alibaba/happy-horse/video-edit`, `alibaba/happy-horse/1.1/image-to-video` (newer).

---
Machine-readable: [`catalog/models/alibaba/happy-horse/image-to-video.json`](../../../../catalog/models/alibaba/happy-horse/image-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/happy-horse/image-to-video
