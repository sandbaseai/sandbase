# Wan 2.7 Image to Video

`alibaba/wan/2.7/image-to-video` · video · Alibaba

Alibaba Wan 2.7 image-to-video model transforming still images into video with native audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=2, resolution="720p" | 0.2 |
| duration=2, resolution="1080p" | 0.3 |
| duration=3, resolution="720p" | 0.3 |
| duration=3, resolution="1080p" | 0.45 |
| duration=4, resolution="720p" | 0.4 |
| duration=4, resolution="1080p" | 0.6 |
| duration=5, resolution="720p" | 0.5 |
| duration=5, resolution="1080p" | 0.75 |
| duration=6, resolution="720p" | 0.6 |
| duration=6, resolution="1080p" | 0.9 |
| duration=7, resolution="720p" | 0.7 |
| duration=7, resolution="1080p" | 1.05 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == '1080p' ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.7/image-to-video", "end_image": "https://static.sandbase.ai/examples/4c735020-6541-4ca8-8445-37403e34c9f2/input/3b9dd46d-a90b-4041-942f-25713579cec6.webp", "image": "https://static.sandbase.ai/examples/4c735020-6541-4ca8-8445-37403e34c9f2/input/4d31c6ec-bcfc-46ba-923a-99fbe366820c.webp", "prompt": "In the early morning as the sun rises, a small pumpkin with dewdrops sits in a pumpkin patch. Suddenly, the pumpkin cracks open with a \"CRACK\". A golden light emanates from the fissure as the pumpkin splits apart, releasing a puff of white mist. A small rabbit appears in the center of the opened pumpkin."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.7/image-to-video', {'end_image': 'https://static.sandbase.ai/examples/4c735020-6541-4ca8-8445-37403e34c9f2/input/3b9dd46d-a90b-4041-942f-25713579cec6.webp', 'image': 'https://static.sandbase.ai/examples/4c735020-6541-4ca8-8445-37403e34c9f2/input/4d31c6ec-bcfc-46ba-923a-99fbe366820c.webp', 'prompt': 'In the early morning as the sun rises, a small pumpkin with dewdrops sits in a pumpkin patch. Suddenly, the pumpkin cracks open with a "CRACK". A golden light emanates from the fissure as the pumpkin splits apart, releasing a puff of white mist. A small rabbit appears in the center of the opened pumpkin.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.7/image-to-video", {
  "end_image": "https://static.sandbase.ai/examples/4c735020-6541-4ca8-8445-37403e34c9f2/input/3b9dd46d-a90b-4041-942f-25713579cec6.webp",
  "image": "https://static.sandbase.ai/examples/4c735020-6541-4ca8-8445-37403e34c9f2/input/4d31c6ec-bcfc-46ba-923a-99fbe366820c.webp",
  "prompt": "In the early morning as the sun rises, a small pumpkin with dewdrops sits in a pumpkin patch. Suddenly, the pumpkin cracks open with a \"CRACK\". A golden light emanates from the fissure as the pumpkin splits apart, releasing a puff of white mist. A small rabbit appears in the center of the opened pumpkin."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.7/image-to-video", sandbase.Params{
	"end_image": "https://static.sandbase.ai/examples/4c735020-6541-4ca8-8445-37403e34c9f2/input/3b9dd46d-a90b-4041-942f-25713579cec6.webp",
	"image": "https://static.sandbase.ai/examples/4c735020-6541-4ca8-8445-37403e34c9f2/input/4d31c6ec-bcfc-46ba-923a-99fbe366820c.webp",
	"prompt": "In the early morning as the sun rises, a small pumpkin with dewdrops sits in a pumpkin patch. Suddenly, the pumpkin cracks open with a \"CRACK\". A golden light emanates from the fissure as the pumpkin splits apart, releasing a puff of white mist. A small rabbit appears in the center of the opened pumpkin.",
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
| `audio` | string |  | The URL of an audio file to guide video generation.  |
| `image` | string | yes | The URL of the starting image for video generation.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"The bus starts moving slowly down the street, rain begins to fall, pedestrians open umbrellas, camera follows the bus"` |
| `duration` | integer |  | The duration of the generated video in seconds. one of: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13` …; default `5` |
| `end_image` | string |  | The URL of the ending image for video generation.  |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |

## Details

Animate your own picture. `image` becomes the first frame; add `end_image` and Wan 2.7 interpolates the motion between the two. Clips run 2–15 seconds, optionally driven by an audio track.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `audio` | audio URL | — | Optional WAV/MP3 URL that drives speech or rhythm. |
| `duration` | 2–15 | 5 | Output length in seconds. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` | — | Omit to follow the input image. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.10 at 720p and $0.15 at 1080p, the same as Alibaba's list price. Input images and audio are not metered.

| Output | 720p | 1080p |
|---|---|---|
| 2s | $0.20 | $0.30 |
| 5s (default) | $0.50 | $0.75 |
| 10s | $1.00 | $1.50 |
| 15s | $1.50 | $2.25 |

Failed runs are not charged.

### Prompting

- Describe what moves, not what is already visible: “the bus pulls away as rain starts and umbrellas open”.
- With two frames, keep framing and lighting compatible or describe the transition explicitly.
- Leave `aspect_ratio` unset to keep the image's own proportions.

### Limits

- One start image and one optional end image per request; for multi-subject references use `alibaba/wan/2.7/reference-to-video`.

### Also on SandBase

Other Wan 2.7 endpoints: `alibaba/wan/2.7/text-to-video`, `alibaba/wan/2.7/reference-to-video`, `alibaba/wan/2.7/video-edit`, `alibaba/wan/2.7/video-extend`, `alibaba/wan/3.0/video` (newer, up to 30s).

---
Machine-readable: [`catalog/models/alibaba/wan/2.7/image-to-video.json`](../../../../../catalog/models/alibaba/wan/2.7/image-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.7/image-to-video
