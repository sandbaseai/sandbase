# Seedance 2.0 Image to Video

`bytedance/seedance/2.0/image-to-video` · video · Bytedance

ByteDance's most advanced image-to-video model  transforming still images into cinematic video with native audio, multi-shot editing, and director-level camera control for professional-grade video creation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=4, resolution="480p" | 0.48 * |
| duration=4, resolution="720p" | 0.96 * |
| duration=4, resolution="1080p" | 2.4 * |
| duration=4, resolution="4k" | 4.8 * |
| duration=5, resolution="480p" | 0.6 * |
| duration=5, resolution="720p" | 1.2 * |
| duration=5, resolution="1080p" | 3 * |
| duration=5, resolution="4k" | 6 * |
| duration=6, resolution="480p" | 0.72 * |
| duration=6, resolution="720p" | 1.44 * |
| duration=6, resolution="1080p" | 3.6 * |
| duration=6, resolution="4k" | 7.2 * |
| duration=7, resolution="480p" | 0.84 * |
| duration=7, resolution="720p" | 1.68 * |
| duration=7, resolution="1080p" | 4.2 * |
| duration=7, resolution="4k" | 8.4 * |
| duration=8, resolution="480p" | 0.96 * |
| duration=8, resolution="720p" | 1.92 * |
| duration=8, resolution="1080p" | 4.8 * |
| duration=8, resolution="4k" | 9.6 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == 'auto' ? Math.round(usage.duration ?? 15.0) : (params.duration ?? 5)) * ((params.resolution ?? '720p') == '480p' ? 0.12 : (params.resolution ?? '720p') == '720p' ? 0.24 : (params.resolution ?? '720p') == '1080p' ? 0.60 : (params.resolution ?? '720p') == '4k' ? 1.20 : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.0/image-to-video", "duration": 5, "generate_audio": true, "image": "https://static.sandbase.ai/examples/7aa12455-c708-4706-a529-31b889a399f7/input/e3b7d79f-44fa-4fd9-9a74-8ca918199a97.jpg", "prompt": "Ultra high-end commercial product shot, photorealistic, 8K, cinematic lighting, macro detail, shallow depth of field, premium advertising aesthetic, VR headset suspended by invisible wires against a deep navy backdrop, slow vertical tilt down across the visor, magenta and cyan accent lighting, studio-grade color grading, immaculate reflections, subtle camera motion", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.0/image-to-video', {'duration': 5, 'generate_audio': True, 'image': 'https://static.sandbase.ai/examples/7aa12455-c708-4706-a529-31b889a399f7/input/e3b7d79f-44fa-4fd9-9a74-8ca918199a97.jpg', 'prompt': 'Ultra high-end commercial product shot, photorealistic, 8K, cinematic lighting, macro detail, shallow depth of field, premium advertising aesthetic, VR headset suspended by invisible wires against a deep navy backdrop, slow vertical tilt down across the visor, magenta and cyan accent lighting, studio-grade color grading, immaculate reflections, subtle camera motion', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.0/image-to-video", {
  "duration": 5,
  "generate_audio": true,
  "image": "https://static.sandbase.ai/examples/7aa12455-c708-4706-a529-31b889a399f7/input/e3b7d79f-44fa-4fd9-9a74-8ca918199a97.jpg",
  "prompt": "Ultra high-end commercial product shot, photorealistic, 8K, cinematic lighting, macro detail, shallow depth of field, premium advertising aesthetic, VR headset suspended by invisible wires against a deep navy backdrop, slow vertical tilt down across the visor, magenta and cyan accent lighting, studio-grade color grading, immaculate reflections, subtle camera motion",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.0/image-to-video", sandbase.Params{
	"duration": 5,
	"generate_audio": true,
	"image": "https://static.sandbase.ai/examples/7aa12455-c708-4706-a529-31b889a399f7/input/e3b7d79f-44fa-4fd9-9a74-8ca918199a97.jpg",
	"prompt": "Ultra high-end commercial product shot, photorealistic, 8K, cinematic lighting, macro detail, shallow depth of field, premium advertising aesthetic, VR headset suspended by invisible wires against a deep navy backdrop, slow vertical tilt down across the visor, magenta and cyan accent lighting, studio-grade color grading, immaculate reflections, subtle camera motion",
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
| `seed` | integer |  | Random seed for reproducible results. Omit or use -1 for a random seed. range -1–4294967295 |
| `image` | string | yes | The URL of the starting image for video generation.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"Create a 360-degree orbiting camera shot based on this photo."` |
| `duration` | enum |  | Output duration in seconds (4-15), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 15 seconds and billed on the actual output length. one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `end_image` | string |  | The URL of the ending image for video generation.  |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input image. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio (voice, SFX, BGM) for the video. default `true` |

## Details

Seedance 2.0 image-to-video: `image` becomes the first frame and the prompt directs motion, camera, and sound. Add `end_image` to set the final frame.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 | 5 | Output length in seconds (4–15), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | — | Output frame shape. |
| `resolution` | `480p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

You pay for output seconds: $0.12 at 480p, $0.24 at 720p, $0.60 at 1080p, $1.20 at 4k. Audio is included. With `duration: "auto"` the quote assumes 15 seconds and the final charge uses the generated length.

| Output | 480p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 4s | $0.48 | $0.96 | $2.40 | $4.80 |
| 5s (default) | $0.60 | $1.20 | $3.00 | $6.00 |
| 10s | $1.20 | $2.40 | $6.00 | $12.00 |
| 15s | $1.80 | $3.60 | $9.00 | $18.00 |

Failed runs are not charged.

### Prompting

- Describe what moves and how the camera behaves, not what is already visible.
- With two frames, describe the transition between them.

### Limits

- Clips are 4–15 seconds.

### Also on SandBase

Other Seedance 2.0 endpoints and tiers: `bytedance/seedance/2.0/text-to-video`, `bytedance/seedance/2.0/reference-to-video`, `bytedance/seedance/2.5/image-to-video`, `bytedance/seedance/2.0/fast/image-to-video`, `bytedance/seedance/2.0/mini/image-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.0/image-to-video.json`](../../../../../catalog/models/bytedance/seedance/2.0/image-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.0/image-to-video
