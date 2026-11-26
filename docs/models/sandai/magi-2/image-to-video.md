# MAGI-2 Image to Video API: pricing, parameters and code examples

`sandai/magi-2/image-to-video` · video generation model · Sand AI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.32 to $2.4 per run, depending on parameters · **Modes:** async

MAGI-2 by Sand AI animates a first frame, or a first and last frame, into a 1080p video of 4 to 30 seconds with native audio.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=4 | 0.32 |
| duration=5 | 0.4 |
| duration=30 | 2.4 |

Formula: `(params.duration ?? 5) * 0.08`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sandai/magi-2/image-to-video", "aspect_ratio": "16:9", "duration": 5, "image": "https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp", "prompt": "The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sandai/magi-2/image-to-video', {'aspect_ratio': '16:9', 'duration': 5, 'image': 'https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp', 'prompt': 'The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sandai/magi-2/image-to-video", {
  "aspect_ratio": "16:9",
  "duration": 5,
  "image": "https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp",
  "prompt": "The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sandai/magi-2/image-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"duration": 5,
	"image": "https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp",
	"prompt": "The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-4294967295). Omit for a random seed. range 0–4294967295 |
| `image` | string | yes | First frame (upload or public HTTPS URL). JPEG, PNG, WebP, BMP, TIFF, GIF or HEIC, under 30 MB.  |
| `prompt` | string |  | Optional. Describe the motion and sound.  |
| `duration` | integer |  | Output video duration in seconds (4-30). Billed per second. default `5`; range 4–30 |
| `end_image` | string |  | Optional last frame (upload or public HTTPS URL).  |
| `resolution` | string |  | Output resolution. MAGI-2 renders 1080p only. one of: `1080p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate a native audio track with the video. Included in the price. default `true` |

## Details

MAGI-2 image-to-video: animate a first frame, or a first and last frame, into a 1080p clip of 4 to 30 seconds with native audio.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Optional. Describe the motion and sound. |
| `image` | string, required | — | First frame (upload or public HTTPS URL). JPEG, PNG, WebP, BMP, TIFF, GIF or HEIC, under 30 MB. |
| `end_image` | string | — | Optional last frame (upload or public HTTPS URL). |
| `duration` | integer 4–30 | 5 | Output video duration in seconds (4-30). Billed per second. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | 16:9 | Output aspect ratio. |
| `resolution` | `1080p` | 1080p | Output resolution. MAGI-2 renders 1080p only. |
| `generate_audio` | boolean | true | Generate a native audio track with the video. Included in the price. |
| `seed` | integer 0–4294967295 | random | Random seed for reproducibility (0-4294967295). Omit for a random seed. |
### Billing
$0.08 per second of output video, with native audio included in the price. Resolution is fixed at 1080p. Failed runs are not billed.
| Output length | Price |
|---|---|
| 4s | $0.32 |
| 5s (default) | $0.40 |
| 10s | $0.80 |
| 30s | $2.40 |
### See what people made
Browse the most-liked MAGI-2 videos on X, credited to the people who made them: [MAGI-2 videos from X](https://www.sandbase.ai/lab/ai-videos/magi-2). Short films, ads and anime.
### Other MAGI-2 modes
- [MAGI-2 Text to Video](/models/sandai/magi-2/text-to-video)
- [MAGI-2 Reference to Video](/models/sandai/magi-2/reference-to-video)

---
Machine-readable: [`catalog/models/sandai/magi-2/image-to-video.json`](../../../../catalog/models/sandai/magi-2/image-to-video.json) · Store page: https://www.sandbase.ai/model/sandai/magi-2/image-to-video
