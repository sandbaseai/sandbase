# Veo 3.1 Lite First-Last Frame to Video API: pricing, parameters and code examples

`google/veo3.1/lite/first-last-frame-to-video` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.12 to $0.64 per run, depending on parameters · **Modes:** async

Veo3.1 Lite First Last Frame To Video is Google's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=4, generate_audio=false, resolution="720p" | 0.12 |
| duration=4, generate_audio=false, resolution="1080p" | 0.2 |
| duration=4, generate_audio=true, resolution="720p" | 0.2 |
| duration=4, generate_audio=true, resolution="1080p" | 0.32 |
| duration=6, generate_audio=false, resolution="720p" | 0.18 |
| duration=6, generate_audio=false, resolution="1080p" | 0.3 |
| duration=6, generate_audio=true, resolution="720p" | 0.3 |
| duration=6, generate_audio=true, resolution="1080p" | 0.48 |
| duration=8, generate_audio=false, resolution="720p" | 0.24 |
| duration=8, generate_audio=false, resolution="1080p" | 0.4 |
| duration=8, generate_audio=true, resolution="720p" | 0.4 |
| duration=8, generate_audio=true, resolution="1080p" | 0.64 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "720p" ? ((params.generate_audio ?? true) ? 0.05 : 0.03) : (params.resolution ?? "720p") == "1080p" ? ((params.generate_audio ?? true) ? 0.08 : 0.05) : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/veo3.1/lite/first-last-frame-to-video", "duration": 4, "end_image": "https://static.sandbase.ai/examples/4a2bc59f-d1ae-4599-a231-ffca7087c6b6/input/93e6f9de-e7ff-4b54-aa84-aa06f1f5e743.png", "generate_audio": false, "image": "https://static.sandbase.ai/examples/4a2bc59f-d1ae-4599-a231-ffca7087c6b6/input/53ce9f26-81ff-461b-b429-6a62efb3d5a5.png", "prompt": "The lantern slowly turns"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/veo3.1/lite/first-last-frame-to-video', {'duration': 4, 'end_image': 'https://static.sandbase.ai/examples/4a2bc59f-d1ae-4599-a231-ffca7087c6b6/input/93e6f9de-e7ff-4b54-aa84-aa06f1f5e743.png', 'generate_audio': False, 'image': 'https://static.sandbase.ai/examples/4a2bc59f-d1ae-4599-a231-ffca7087c6b6/input/53ce9f26-81ff-461b-b429-6a62efb3d5a5.png', 'prompt': 'The lantern slowly turns'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/veo3.1/lite/first-last-frame-to-video", {
  "duration": 4,
  "end_image": "https://static.sandbase.ai/examples/4a2bc59f-d1ae-4599-a231-ffca7087c6b6/input/93e6f9de-e7ff-4b54-aa84-aa06f1f5e743.png",
  "generate_audio": false,
  "image": "https://static.sandbase.ai/examples/4a2bc59f-d1ae-4599-a231-ffca7087c6b6/input/53ce9f26-81ff-461b-b429-6a62efb3d5a5.png",
  "prompt": "The lantern slowly turns"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/veo3.1/lite/first-last-frame-to-video", sandbase.Params{
	"duration": 4,
	"end_image": "https://static.sandbase.ai/examples/4a2bc59f-d1ae-4599-a231-ffca7087c6b6/input/93e6f9de-e7ff-4b54-aa84-aa06f1f5e743.png",
	"generate_audio": false,
	"image": "https://static.sandbase.ai/examples/4a2bc59f-d1ae-4599-a231-ffca7087c6b6/input/53ce9f26-81ff-461b-b429-6a62efb3d5a5.png",
	"prompt": "The lantern slowly turns",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for more reproducible results. range 0–4294967295 |
| `image` | string | yes | First frame of the video. 720p or higher in 16:9 or 9:16 works best.  |
| `prompt` | string | yes | The text prompt describing the video you want to generate  |
| `duration` | integer |  | Duration of the generated video in seconds. one of: `4`, `6`, `8`; default `8` |
| `end_image` | string | yes | Last frame of the video.  |
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input image. one of: `16:9`, `9:16` |
| `generate_audio` | boolean |  | Generate synchronized audio. Videos without audio are cheaper. default `true` |
| `negative_prompt` | string |  | What to avoid in the video.  |

## Details

Veo 3.1 Lite with first and last frame control: send a start image and an end image and Veo generates the motion between them, with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL, required | — | Last frame. JPEG, PNG, or WebP URL. |
| `duration` | 4 / 6 / 8 | 8 | Output length in seconds. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `16:9` / `9:16` | — | Output frame shape. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects; turning it off lowers the rate. |
| `negative_prompt` | string | — | What to avoid. |
| `seed` | integer 0–4294967295 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds, Google's list price. With audio: $0.05 at 720p, $0.08 at 1080p. Without audio: $0.03 / $0.05 respectively.

| Output | 720p | 1080p |
|---|---|---|
| 4s with audio | $0.20 | $0.32 |
| 6s with audio | $0.30 | $0.48 |
| 8s with audio (default) | $0.40 | $0.64 |
| 8s without audio | $0.24 | $0.40 |

Failed runs are not charged.

### Prompting

- Keep both frames compatible in framing and lighting, or describe the transition explicitly.
- Describe how the subject travels from the first frame to the last.

### Limits

- Both frames are required.
- No 4K on this tier.

### Also on SandBase

Other Veo 3.1 Lite endpoints: `google/veo3.1/lite/text-to-video`, `google/veo3.1/lite/image-to-video`, `google/veo3.1/text-to-video`, `google/veo3.1/fast/text-to-video`.

---
Machine-readable: [`catalog/models/google/veo3.1/lite/first-last-frame-to-video.json`](../../../../../catalog/models/google/veo3.1/lite/first-last-frame-to-video.json) · Store page: https://www.sandbase.ai/model/google/veo3.1/lite/first-last-frame-to-video
