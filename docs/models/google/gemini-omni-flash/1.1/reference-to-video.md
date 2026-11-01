# Gemini Omni Flash 1.1 Reference to Video

`google/gemini-omni-flash/1.1/reference-to-video` · video · Google

Gemini Omni Flash 1.1 Reference to Video by Google generates a short video with synchronized audio guided by up to ten reference images and up to three short reference videos.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="360p" | 0.09 |
| duration=3, resolution="720p" | 0.3 |
| duration=3, resolution="1080p" | 0.45 |
| duration=3, resolution="4k" | 0.9 |
| duration=8, resolution="360p" | 0.24 |
| duration=8, resolution="720p" | 0.8 |
| duration=8, resolution="1080p" | 1.2 |
| duration=8, resolution="4k" | 2.4 |
| duration=10, resolution="360p" | 0.3 |
| duration=10, resolution="720p" | 1 |
| duration=10, resolution="1080p" | 1.5 |
| duration=10, resolution="4k" | 3 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "360p" ? 0.03 : (params.resolution ?? "720p") == "1080p" ? 0.15 : (params.resolution ?? "720p") == "4k" ? 0.30 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/1.1/reference-to-video", "duration": 3, "images": ["https://static.sandbase.ai/examples/00cd0e80-87f9-48ed-94fa-79c7696a5c10/input/a9b65d84-d4bb-40f4-8034-34fa30833553.jpg"], "prompt": "A calm shoreline in the style of <IMAGE_REF_0>, with the motion of <VIDEO_REF_0>, no dialogue", "resolution": "360p", "videos": ["https://static.sandbase.ai/examples/00cd0e80-87f9-48ed-94fa-79c7696a5c10/input/0cb76cda-f2e8-44b8-b5bd-ab13ef90a846.mp4"]}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/1.1/reference-to-video', {'duration': 3, 'images': ['https://static.sandbase.ai/examples/00cd0e80-87f9-48ed-94fa-79c7696a5c10/input/a9b65d84-d4bb-40f4-8034-34fa30833553.jpg'], 'prompt': 'A calm shoreline in the style of <IMAGE_REF_0>, with the motion of <VIDEO_REF_0>, no dialogue', 'resolution': '360p', 'videos': ['https://static.sandbase.ai/examples/00cd0e80-87f9-48ed-94fa-79c7696a5c10/input/0cb76cda-f2e8-44b8-b5bd-ab13ef90a846.mp4']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/1.1/reference-to-video", {
  "duration": 3,
  "images": [
    "https://static.sandbase.ai/examples/00cd0e80-87f9-48ed-94fa-79c7696a5c10/input/a9b65d84-d4bb-40f4-8034-34fa30833553.jpg"
  ],
  "prompt": "A calm shoreline in the style of <IMAGE_REF_0>, with the motion of <VIDEO_REF_0>, no dialogue",
  "resolution": "360p",
  "videos": [
    "https://static.sandbase.ai/examples/00cd0e80-87f9-48ed-94fa-79c7696a5c10/input/0cb76cda-f2e8-44b8-b5bd-ab13ef90a846.mp4"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/1.1/reference-to-video", sandbase.Params{
	"duration": 3,
	"images": []any{"https://static.sandbase.ai/examples/00cd0e80-87f9-48ed-94fa-79c7696a5c10/input/a9b65d84-d4bb-40f4-8034-34fa30833553.jpg"},
	"prompt": "A calm shoreline in the style of <IMAGE_REF_0>, with the motion of <VIDEO_REF_0>, no dialogue",
	"resolution": "360p",
	"videos": []any{"https://static.sandbase.ai/examples/00cd0e80-87f9-48ed-94fa-79c7696a5c10/input/0cb76cda-f2e8-44b8-b5bd-ab13ef90a846.mp4"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array |  | URLs of reference images to incorporate into the video.  |
| `prompt` | string | yes | The text prompt describing the video. Reference media is sent in list order before the prompt.  |
| `videos` | array |  | URLs of up to three reference videos. Each video must be at most three seconds long.  |
| `duration` | integer |  | The duration of the generated video, in seconds. default `8`; range 3–10 |
| `resolution` | string |  | The resolution of the generated video. one of: `360p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Gemini Omni Flash 1.1 reference-to-video: up to 10 reference images and 3 short reference videos keep subjects, products, or style consistent in a new clip with synchronized audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `images` | image URL[] (≤10) | — | Up to 10 reference images, Image 1, Image 2, … |
| `resolution` | `360p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `duration` | integer 3–10 | 8 | Output length in seconds (3–10). |
| `videos` | video URL[] (≤3) | — | Up to 3 short reference clips, Video 1, Video 2, … |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |

### Billing

You pay for output seconds: $0.03 at 360p, $0.10 at 720p, $0.15 at 1080p, and $0.30 at 4K.

| Output | 360p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 3s | $0.09 | $0.30 | $0.45 | $0.90 |
| 8s (default) | $0.24 | $0.80 | $1.20 | $2.40 |
| 10s | $0.30 | $1.00 | $1.50 | $3.00 |

Failed runs are not charged.

### Prompting

- Give each reference a role and refer to it by number.

### Limits

- Send at least one reference.

### Also on SandBase

Other Gemini Omni Flash 1.1 endpoints: `google/gemini-omni-flash/1.1/text-to-video`, `google/gemini-omni-flash/1.1/image-to-video`, `google/gemini-omni-flash/1.1/edit`, `google/gemini-omni-flash/reference-to-video` (previous version).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/1.1/reference-to-video.json`](../../../../../catalog/models/google/gemini-omni-flash/1.1/reference-to-video.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/1.1/reference-to-video
