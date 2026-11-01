# Veo 3.1 Fast First-Last Frame to Video

`google/veo3.1/fast/first-last-frame-to-video` · video · Google

Veo3.1 Fast First Last Frame To Video is Google's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=4, generate_audio=false, resolution="720p" | 0.32 |
| duration=4, generate_audio=false, resolution="1080p" | 0.4 |
| duration=4, generate_audio=false, resolution="4k" | 1 |
| duration=4, generate_audio=true, resolution="720p" | 0.4 |
| duration=4, generate_audio=true, resolution="1080p" | 0.48 |
| duration=4, generate_audio=true, resolution="4k" | 1.2 |
| duration=6, generate_audio=false, resolution="720p" | 0.48 |
| duration=6, generate_audio=false, resolution="1080p" | 0.6 |
| duration=6, generate_audio=false, resolution="4k" | 1.5 |
| duration=6, generate_audio=true, resolution="720p" | 0.6 |
| duration=6, generate_audio=true, resolution="1080p" | 0.72 |
| duration=6, generate_audio=true, resolution="4k" | 1.8 |
| duration=8, generate_audio=false, resolution="720p" | 0.64 |
| duration=8, generate_audio=false, resolution="1080p" | 0.8 |
| duration=8, generate_audio=false, resolution="4k" | 2 |
| duration=8, generate_audio=true, resolution="720p" | 0.8 |
| duration=8, generate_audio=true, resolution="1080p" | 0.96 |
| duration=8, generate_audio=true, resolution="4k" | 2.4 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "720p" ? ((params.generate_audio ?? true) ? 0.10 : 0.08) : (params.resolution ?? "720p") == "1080p" ? ((params.generate_audio ?? true) ? 0.12 : 0.10) : (params.resolution ?? "720p") == "4k" ? ((params.generate_audio ?? true) ? 0.30 : 0.25) : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/veo3.1/fast/first-last-frame-to-video", "prompt": "<prompt>", "image": "<image>", "end_image": "<end_image>"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/veo3.1/fast/first-last-frame-to-video', {'prompt': '<prompt>', 'image': '<image>', 'end_image': '<end_image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/veo3.1/fast/first-last-frame-to-video", {
  "prompt": "<prompt>",
  "image": "<image>",
  "end_image": "<end_image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/veo3.1/fast/first-last-frame-to-video", sandbase.Params{
	"prompt": "<prompt>",
	"image": "<image>",
	"end_image": "<end_image>",
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
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input image. one of: `16:9`, `9:16` |
| `generate_audio` | boolean |  | Generate synchronized audio. Videos without audio are cheaper. default `true` |
| `negative_prompt` | string |  | What to avoid in the video.  |

## Details

Veo 3.1 Fast with first and last frame control: send a start image and an end image and Veo generates the motion between them, with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL, required | — | Last frame. JPEG, PNG, or WebP URL. |
| `duration` | 4 / 6 / 8 | 8 | Output length in seconds. |
| `resolution` | `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `16:9` / `9:16` | — | Output frame shape. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects; turning it off lowers the rate. |
| `negative_prompt` | string | — | What to avoid. |
| `seed` | integer 0–4294967295 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds, Google's list price. With audio: $0.10 at 720p, $0.12 at 1080p, $0.30 at 4k. Without audio: $0.08 / $0.10 / $0.25 respectively.

| Output | 720p | 1080p | 4k |
|---|---|---|---|
| 4s with audio | $0.40 | $0.48 | $1.20 |
| 6s with audio | $0.60 | $0.72 | $1.80 |
| 8s with audio (default) | $0.80 | $0.96 | $2.40 |
| 8s without audio | $0.64 | $0.80 | $2.00 |

Failed runs are not charged.

### Prompting

- Keep both frames compatible in framing and lighting, or describe the transition explicitly.
- Describe how the subject travels from the first frame to the last.

### Limits

- Both frames are required.
- Use Veo 3.1 for the highest quality.

### Also on SandBase

Other Veo 3.1 Fast endpoints: `google/veo3.1/fast/text-to-video`, `google/veo3.1/fast/image-to-video`, `google/veo3.1/fast/reference-to-video`, `google/veo3.1/fast/video-extend`, `google/veo3.1/text-to-video`, `google/veo3.1/lite/text-to-video`.

---
Machine-readable: [`catalog/models/google/veo3.1/fast/first-last-frame-to-video.json`](../../../../../catalog/models/google/veo3.1/fast/first-last-frame-to-video.json) · Store page: https://www.sandbase.ai/model/google/veo3.1/fast/first-last-frame-to-video
