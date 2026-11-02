# Wan 2.6 Image to Video API: pricing, parameters and code examples

`alibaba/wan/2.6/image-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.5 to $1.5 per run, depending on parameters · **Modes:** async

Alibaba Wan 2.6 image-to-video model transforming still images into video. Supports first-frame-to-video only.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="720p" | 0.5 |
| duration=5, resolution="1080p" | 0.75 |
| duration=10, resolution="720p" | 1 |
| duration=10, resolution="1080p" | 1.5 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == '1080p' ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.6/image-to-video", "audio": "https://static.sandbase.ai/examples/5b422d5a-e1be-4e4b-95cb-8f7b4e17e17b/input/cb1853ea-67d2-4a97-b2b4-1b93b5f24d73.mp3", "image": "https://static.sandbase.ai/examples/5b422d5a-e1be-4e4b-95cb-8f7b4e17e17b/input/80632427-d7b9-441c-b64d-6cc247f55788.webp", "prompt": "An urban fantasy art scene. A dynamic graffiti art character. A boy made of spray paint comes to life from a concrete wall. He raps an English song at a very fast pace, striking a classic, energetic rapper pose. The scene is set at night under an urban railway bridge. The lighting comes from a single street lamp, creating a cinematic atmosphere, full of high energy and amazing detail. The audio part of the video consists entirely of rap, with no other dialogue or background noise."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.6/image-to-video', {'audio': 'https://static.sandbase.ai/examples/5b422d5a-e1be-4e4b-95cb-8f7b4e17e17b/input/cb1853ea-67d2-4a97-b2b4-1b93b5f24d73.mp3', 'image': 'https://static.sandbase.ai/examples/5b422d5a-e1be-4e4b-95cb-8f7b4e17e17b/input/80632427-d7b9-441c-b64d-6cc247f55788.webp', 'prompt': 'An urban fantasy art scene. A dynamic graffiti art character. A boy made of spray paint comes to life from a concrete wall. He raps an English song at a very fast pace, striking a classic, energetic rapper pose. The scene is set at night under an urban railway bridge. The lighting comes from a single street lamp, creating a cinematic atmosphere, full of high energy and amazing detail. The audio part of the video consists entirely of rap, with no other dialogue or background noise.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.6/image-to-video", {
  "audio": "https://static.sandbase.ai/examples/5b422d5a-e1be-4e4b-95cb-8f7b4e17e17b/input/cb1853ea-67d2-4a97-b2b4-1b93b5f24d73.mp3",
  "image": "https://static.sandbase.ai/examples/5b422d5a-e1be-4e4b-95cb-8f7b4e17e17b/input/80632427-d7b9-441c-b64d-6cc247f55788.webp",
  "prompt": "An urban fantasy art scene. A dynamic graffiti art character. A boy made of spray paint comes to life from a concrete wall. He raps an English song at a very fast pace, striking a classic, energetic rapper pose. The scene is set at night under an urban railway bridge. The lighting comes from a single street lamp, creating a cinematic atmosphere, full of high energy and amazing detail. The audio part of the video consists entirely of rap, with no other dialogue or background noise."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.6/image-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/5b422d5a-e1be-4e4b-95cb-8f7b4e17e17b/input/cb1853ea-67d2-4a97-b2b4-1b93b5f24d73.mp3",
	"image": "https://static.sandbase.ai/examples/5b422d5a-e1be-4e4b-95cb-8f7b4e17e17b/input/80632427-d7b9-441c-b64d-6cc247f55788.webp",
	"prompt": "An urban fantasy art scene. A dynamic graffiti art character. A boy made of spray paint comes to life from a concrete wall. He raps an English song at a very fast pace, striking a classic, energetic rapper pose. The scene is set at night under an urban railway bridge. The lighting comes from a single street lamp, creating a cinematic atmosphere, full of high energy and amazing detail. The audio part of the video consists entirely of rap, with no other dialogue or background noise.",
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
| `image` | string | yes | The URL of the starting image for video generation (first-frame-to-video only).  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"Realistic style, a small black cat curiously gazes up at the sky. The camera gradually rises from eye level, ending with an overhead angle capturing its curious eyes."` |
| `duration` | integer |  | The duration of the generated video in seconds. Valid values are 5 and 10. one of: `5`, `10`; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |

## Details

Animate a picture into a 5 or 10 second clip. `image` becomes the first frame and the prompt says what moves; an optional audio track can drive speech or rhythm.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `audio` | audio URL | — | Optional WAV/MP3 URL that drives speech or rhythm. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.10 at 720p and $0.15 at 1080p, Alibaba's list price. Input images and audio are not metered.

| Output | 720p | 1080p |
|---|---|---|
| 5s (default) | $0.50 | $0.75 |
| 10s | $1.00 | $1.50 |

Failed runs are not charged.

### Prompting

- Describe the motion and camera, not what is already in the picture.
- Keep one main action per clip.

### Limits

- Durations are 5 or 10 seconds only.
- No end-frame control; Wan 2.7 image-to-video adds an optional last frame.

### Also on SandBase

Other Wan 2.6 endpoints: `alibaba/wan/2.6/text-to-video`, `alibaba/wan/2.6/reference-to-video`, `alibaba/wan/2.6/flash/image-to-video`, `alibaba/wan/2.6/flash/reference-to-video`, `alibaba/wan/2.6/text-to-image`, `alibaba/wan/2.6/image-to-image`, `alibaba/wan/2.7/text-to-video` (newer).

---
Machine-readable: [`catalog/models/alibaba/wan/2.6/image-to-video.json`](../../../../../catalog/models/alibaba/wan/2.6/image-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.6/image-to-video
