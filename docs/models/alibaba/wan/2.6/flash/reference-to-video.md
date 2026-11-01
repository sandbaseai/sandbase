# Wan 2.6 Flash Reference to Video

`alibaba/wan/2.6/flash/reference-to-video` · video · Alibaba

Alibaba Wan 2.6 Flash reference-to-video model that places characters from reference images or videos into a new scene, with optional generated audio and multi-shot control.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`, `params.resolution`, `params.videos`).

| parameters | USD |
|---|---|
| duration=5, generate_audio=false, resolution="720p" | 0.25 |
| duration=5, generate_audio=false, resolution="1080p" | 0.375 |
| duration=5, generate_audio=true, resolution="720p" | 0.5 |
| duration=5, generate_audio=true, resolution="1080p" | 0.75 |
| duration=10, generate_audio=false, resolution="720p" | 0.5 |
| duration=10, generate_audio=false, resolution="1080p" | 0.75 |
| duration=10, generate_audio=true, resolution="720p" | 1 |
| duration=10, generate_audio=true, resolution="1080p" | 1.5 |

Formula: `((params.duration ?? 5) + (len(params.videos ?? []) > 0 ? 5 : 0)) * ((params.generate_audio ?? true) ? ((params.resolution ?? "720p") == "1080p" ? 0.15 : 0.10) : ((params.resolution ?? "720p") == "1080p" ? 0.075 : 0.05))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.6/flash/reference-to-video", "prompt": "Dance battle between Character1 and Character2."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.6/flash/reference-to-video', {'prompt': 'Dance battle between Character1 and Character2.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.6/flash/reference-to-video", {
  "prompt": "Dance battle between Character1 and Character2."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.6/flash/reference-to-video", sandbase.Params{
	"prompt": "Dance battle between Character1 and Character2.",
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
| `images` | array |  | Reference images for subject consistency (0-5 images). Combined with video_urls, total references cannot exceed 5. Formats: JPEG, JPG, PNG (no alpha), BMP, WEBP. Resolution: 240-5000px. Max 10MB each. Reference order:…  |
| `prompt` | string | yes | Use Character1, Character2, etc. to reference subjects from your reference files. Works for people, animals, or objects. For multi-shot prompts: '[0-3s] Shot 1. [3-6s] Shot 2.' Max 1500 characters. Reference order:…  |
| `videos` | array |  | Reference videos for subject consistency (0-3 videos). Videos' FPS must be at least 16 FPS. Combined with image_urls, total references cannot exceed 5. Reference order: video_urls are numbered first (Character1,…  |
| `duration` | integer |  | Duration of the generated video in seconds. R2V Flash supports only 5 or 10 seconds. one of: `5`, `10`; default `5` |
| `resolution` | string |  | Video resolution tier. R2V Flash only supports 720p and 1080p. one of: `720p`, `1080p`; default `"720p"` |
| `multi_shots` | boolean |  | When true (default), enables intelligent multi-shot segmentation for coherent narrative videos with multiple shots. When false, generates single continuous shot. Only active when enable_prompt_expansion is True. default `true` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default `"16:9"` |
| `generate_audio` | boolean |  | Whether to generate a video with audio. Set to false for silent video generation. Silent videos are faster and cost half of the audio version price. default `true` |

## Details

The fast, lower-cost Wan 2.6 reference tier. Cast characters from reference images or videos into a new scene for quick iterations; audio generation and multi-shot cuts are on by default.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Reference images, Image 1, Image 2, … |
| `videos` | video URL[] | — | Reference clips, Video 1, Video 2, … |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `multi_shots` | boolean | true | Let the model cut between several shots. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` | `16:9` | Output frame shape. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `generate_audio` | boolean | true | Generate a synchronized audio track; turning it off halves the rate. |

### Billing

With audio you pay $0.10 per output second at 720p and $0.15 at 1080p; silent output costs half. When you send reference `videos`, 5 seconds of input are added to the billed length.

| Output | 720p | 1080p |
|---|---|---|
| 5s with audio | $0.50 | $0.75 |
| 5s silent | $0.25 | $0.375 |
| 5s with audio + reference video | $1.00 | $1.50 |
| 10s with audio | $1.00 | $1.50 |

Failed runs are not charged.

### Prompting

- Refer to references by number and give each a role.
- Keep the action simple for fast drafts, then rerun the winner on the non-Flash tier.

### Limits

- Durations are 5 or 10 seconds.

### Also on SandBase

Other Wan 2.6 endpoints: `alibaba/wan/2.6/text-to-video`, `alibaba/wan/2.6/image-to-video`, `alibaba/wan/2.6/reference-to-video`, `alibaba/wan/2.6/flash/image-to-video`, `alibaba/wan/2.6/text-to-image`, `alibaba/wan/2.6/image-to-image`, `alibaba/wan/2.7/text-to-video` (newer).

---
Machine-readable: [`catalog/models/alibaba/wan/2.6/flash/reference-to-video.json`](../../../../../../catalog/models/alibaba/wan/2.6/flash/reference-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.6/flash/reference-to-video
