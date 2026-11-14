# Wan 3.0 Prime Image to Video API: pricing, parameters and code examples

`alibaba/wan/3.0/prime/image-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.136 to $1.68 per run, depending on parameters · **Modes:** async

Wan 3.0 Prime by Alibaba - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=2, resolution="480p" | 0.136 * |
| duration=2, resolution="720p" | 0.28 * |
| duration=2, resolution="1080p" | 0.56 * |
| duration=3, resolution="480p" | 0.204 * |
| duration=3, resolution="720p" | 0.42 * |
| duration=3, resolution="1080p" | 0.84 * |
| duration=4, resolution="480p" | 0.272 * |
| duration=4, resolution="720p" | 0.56 * |
| duration=4, resolution="1080p" | 1.12 * |
| duration=5, resolution="480p" | 0.34 * |
| duration=5, resolution="720p" | 0.7 * |
| duration=5, resolution="1080p" | 1.4 * |
| duration=6, resolution="480p" | 0.408 * |
| duration=6, resolution="720p" | 0.84 * |
| duration=6, resolution="1080p" | 1.68 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == "auto" ? Math.round(usage.duration ?? 30.0) : (params.duration ?? 5)) * ((params.resolution ?? "720p") == "1080p" ? 0.28 : (params.resolution ?? "720p") == "480p" ? 0.068 : 0.14)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/3.0/prime/image-to-video", "duration": 8, "image": "https://static.sandbase.ai/examples/f1e7d4ee-e775-4ab7-89cd-02262aef21d0/input/0b5c42d8-eb51-4b41-b7b5-b7e31f9d0466.png", "prompt": "(0:00 - 0:03) Camera: Medium shot. Scene: A ink-wash bamboo forest scene from Image 1. A swordsman wearing a bamboo hat and dressed in a dark robe, his silhouette standing in the center surrounded by thick fog and swaying bamboo shadows. Action: The swordsman'\''s left hand lightly rests on the sword hilt, bamboo leaves fall with the wind. Atmosphere: Silent, oppressive, with clearly visible ink-wash grain texture. (0:03 - 0:08) Plot introduction. Camera: Close-up. Plot: The swordsman senses killing intent. Scene: The camera rapidly pushes in to a close-up beneath the swordsman'\''s bamboo hat. Detail: Beneath the hat brim, a pair of sharp, resolute eyes appear, gaze like a blade. Ink-wash \"sweat drops\" slide down from the forehead. Action: The swordsman'\''s right hand slowly grips the sword hilt, knuckles turning white. The bamboo leaves fall faster. Style note: Throughout, maintain the highly black-and-white, ink-wash painting style of Image 1 . Actions must have a calligraphic brush feel, speed must be fast, details must be rich (ink drops, sparks, ink crack marks)."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/3.0/prime/image-to-video', {'duration': 8, 'image': 'https://static.sandbase.ai/examples/f1e7d4ee-e775-4ab7-89cd-02262aef21d0/input/0b5c42d8-eb51-4b41-b7b5-b7e31f9d0466.png', 'prompt': '(0:00 - 0:03) Camera: Medium shot. Scene: A ink-wash bamboo forest scene from Image 1. A swordsman wearing a bamboo hat and dressed in a dark robe, his silhouette standing in the center surrounded by thick fog and swaying bamboo shadows. Action: The swordsman\'s left hand lightly rests on the sword hilt, bamboo leaves fall with the wind. Atmosphere: Silent, oppressive, with clearly visible ink-wash grain texture. (0:03 - 0:08) Plot introduction. Camera: Close-up. Plot: The swordsman senses killing intent. Scene: The camera rapidly pushes in to a close-up beneath the swordsman\'s bamboo hat. Detail: Beneath the hat brim, a pair of sharp, resolute eyes appear, gaze like a blade. Ink-wash "sweat drops" slide down from the forehead. Action: The swordsman\'s right hand slowly grips the sword hilt, knuckles turning white. The bamboo leaves fall faster. Style note: Throughout, maintain the highly black-and-white, ink-wash painting style of Image 1 . Actions must have a calligraphic brush feel, speed must be fast, details must be rich (ink drops, sparks, ink crack marks).'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/3.0/prime/image-to-video", {
  "duration": 8,
  "image": "https://static.sandbase.ai/examples/f1e7d4ee-e775-4ab7-89cd-02262aef21d0/input/0b5c42d8-eb51-4b41-b7b5-b7e31f9d0466.png",
  "prompt": "(0:00 - 0:03) Camera: Medium shot. Scene: A ink-wash bamboo forest scene from Image 1. A swordsman wearing a bamboo hat and dressed in a dark robe, his silhouette standing in the center surrounded by thick fog and swaying bamboo shadows. Action: The swordsman's left hand lightly rests on the sword hilt, bamboo leaves fall with the wind. Atmosphere: Silent, oppressive, with clearly visible ink-wash grain texture. (0:03 - 0:08) Plot introduction. Camera: Close-up. Plot: The swordsman senses killing intent. Scene: The camera rapidly pushes in to a close-up beneath the swordsman's bamboo hat. Detail: Beneath the hat brim, a pair of sharp, resolute eyes appear, gaze like a blade. Ink-wash \"sweat drops\" slide down from the forehead. Action: The swordsman's right hand slowly grips the sword hilt, knuckles turning white. The bamboo leaves fall faster. Style note: Throughout, maintain the highly black-and-white, ink-wash painting style of Image 1 . Actions must have a calligraphic brush feel, speed must be fast, details must be rich (ink drops, sparks, ink crack marks)."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/3.0/prime/image-to-video", sandbase.Params{
	"duration": 8,
	"image": "https://static.sandbase.ai/examples/f1e7d4ee-e775-4ab7-89cd-02262aef21d0/input/0b5c42d8-eb51-4b41-b7b5-b7e31f9d0466.png",
	"prompt": "(0:00 - 0:03) Camera: Medium shot. Scene: A ink-wash bamboo forest scene from Image 1. A swordsman wearing a bamboo hat and dressed in a dark robe, his silhouette standing in the center surrounded by thick fog and swaying bamboo shadows. Action: The swordsman's left hand lightly rests on the sword hilt, bamboo leaves fall with the wind. Atmosphere: Silent, oppressive, with clearly visible ink-wash grain texture. (0:03 - 0:08) Plot introduction. Camera: Close-up. Plot: The swordsman senses killing intent. Scene: The camera rapidly pushes in to a close-up beneath the swordsman's bamboo hat. Detail: Beneath the hat brim, a pair of sharp, resolute eyes appear, gaze like a blade. Ink-wash \"sweat drops\" slide down from the forehead. Action: The swordsman's right hand slowly grips the sword hilt, knuckles turning white. The bamboo leaves fall faster. Style note: Throughout, maintain the highly black-and-white, ink-wash painting style of Image 1 . Actions must have a calligraphic brush feel, speed must be fast, details must be rich (ink drops, sparks, ink crack marks).",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed (0-2147483647) for reproducible results. Omit for a random seed; the same seed may still produce slightly different results. range 0–2147483647 |
| `image` | string | yes | URL of the image used as the first frame (JPEG, PNG, BMP, or WebP). Cannot be combined with `images`, `videos`, or `audios`.  |
| `prompt` | string | yes | Text prompt describing the motion to generate.  |
| `duration` | enum |  | Output duration in seconds (2-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` …; default `5` |
| `end_image` | string |  | URL of the image used as the last frame (JPEG, PNG, BMP, or WebP). Cannot be combined with `images`, `videos`, or `audios`.  |
| `resolution` | string |  | Output video resolution tier. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Start a clip from your own picture. `image` becomes the exact first frame; add `end_image` and the model interpolates the motion between the two. Clips run 2–30 seconds with native audio.

Prime is the faster Wan 3.0 tier: the same inputs and output quality as standard Wan 3.0, with significantly shorter end-to-end generation time and a higher per-second rate. Use standard Wan 3.0 for batch or background jobs where turnaround does not matter.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `image` | image URL, required | — | First frame. JPEG/PNG/BMP/WebP, 240–8000px per side, ≤20MB, no transparency. |
| `end_image` | image URL | — | Last frame; needs `image`. |
| `duration` | 2–30 or `auto` | 5 | `auto` lets the model pick the length. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `adaptive` / `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `adaptive` | `adaptive` follows the prompt and inputs. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds only: $0.068 at 480p, $0.14 at 720p, $0.28 at 1080p. Input images, audio, and video are not metered. The frame images are free.

| Output | Billed | 480p | 720p | 1080p |
|---|---|---|---|---|
| 2s | 2s | $0.136 | $0.28 | $0.56 |
| 5s (default) | 5s | $0.34 | $0.70 | $1.40 |
| 10s | 10s | $0.68 | $1.40 | $2.80 |
| 30s | 30s | $2.04 | $4.20 | $8.40 |

With `duration: "auto"` the run is pre-authorized at 30 seconds, then settled on the length that was actually generated. Failed runs are not charged. Output files are copied to SandBase storage and the returned URL stays valid for 7 days; download anything you need to keep.

### Prompting

- Describe what moves, not what is already visible: “she turns toward the lens as wind lifts her scarf”.
- With two frames, keep them compatible in framing and lighting, or describe the transition explicitly.
- Leave `aspect_ratio` on `adaptive` to keep the image's own proportions.

> The subject slowly turns toward the camera as a breeze moves the fabric; subtle handheld push-in, natural daylight, no dialogue.

### Limits

- Reference images, videos, and audio are not accepted here; use reference-to-video instead.

### Also on SandBase

Other Wan 3.0 Prime endpoints: `alibaba/wan/3.0/prime/video` (all modes in one schema), `alibaba/wan/3.0/prime/text-to-video`, `alibaba/wan/3.0/prime/reference-to-video`, `alibaba/wan/3.0/prime/video-edit`, `alibaba/wan/3.0/prime/video-extend`. Standard tier: `alibaba/wan/3.0/image-to-video`.

---
Machine-readable: [`catalog/models/alibaba/wan/3.0/prime/image-to-video.json`](../../../../../../catalog/models/alibaba/wan/3.0/prime/image-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/3.0/prime/image-to-video
