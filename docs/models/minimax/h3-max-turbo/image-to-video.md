# MiniMax H3 Max Turbo Image to Video

`minimax/h3-max-turbo/image-to-video` · video · MiniMax

MiniMax H3 Max Turbo, the fastest tier of the H3 family, animates a first frame (and optional last frame) into a 5-15 second video with native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="480P" | 0.125 |
| duration=5, resolution="768P" | 0.2 |
| duration=5, resolution="1080P" | 0.4 |
| duration=15, resolution="480P" | 0.375 |
| duration=15, resolution="768P" | 0.6 |
| duration=15, resolution="1080P" | 1.2 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "768P") == "480P" ? 0.025 : (params.resolution ?? "768P") == "1080P" ? 0.08 : 0.04)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3-max-turbo/image-to-video", "duration": 5, "image": "https://static.sandbase.ai/examples/d0ca90ac-ba2c-41a6-b0af-8394e87434f3/input/481d37f1-03eb-46bf-ace0-761493d07fac.png", "prompt": "the camera slowly zooms in", "resolution": "480P"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3-max-turbo/image-to-video', {'duration': 5, 'image': 'https://static.sandbase.ai/examples/d0ca90ac-ba2c-41a6-b0af-8394e87434f3/input/481d37f1-03eb-46bf-ace0-761493d07fac.png', 'prompt': 'the camera slowly zooms in', 'resolution': '480P'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3-max-turbo/image-to-video", {
  "duration": 5,
  "image": "https://static.sandbase.ai/examples/d0ca90ac-ba2c-41a6-b0af-8394e87434f3/input/481d37f1-03eb-46bf-ace0-761493d07fac.png",
  "prompt": "the camera slowly zooms in",
  "resolution": "480P"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3-max-turbo/image-to-video", sandbase.Params{
	"duration": 5,
	"image": "https://static.sandbase.ai/examples/d0ca90ac-ba2c-41a6-b0af-8394e87434f3/input/481d37f1-03eb-46bf-ace0-761493d07fac.png",
	"prompt": "the camera slowly zooms in",
	"resolution": "480P",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed. A random seed is selected when omitted.  |
| `image` | string | yes | Optional URL of the image to use as the first frame. When provided, the output canvas follows this image. If only end_image_url is provided, the canvas follows that last frame instead. If both images are omitted, the…  |
| `prompt` | string | yes | Text prompt for video generation  |
| `duration` | integer |  | Video duration in seconds (5-15). default `5`; range 5–15 |
| `end_image` | string |  | Optional URL of the image to use as the last frame. It may be provided alone for end-only keyframe generation; in that case the output canvas follows this image.  |
| `resolution` | string |  | The native generation resolution, or 1080P latent refinement from a native 768P source. one of: `480P`, `768P`, `1080P`; default `"768P"` |
| `target_audio_url` | string |  | Optional URL of an audio clip at least 2 seconds long (maximum 15 MB) to pin to the generated soundtrack. Longer clips are trimmed to the requested video duration, keeping the beginning. The original audio replaces the…  |
| `prompt_expansion_mode` | string |  | How much effort to spend rewriting the prompt before generation. 'disabled' skips prompt expansion. 'balanced' returns in about a second. 'quality' spends up to ~30s on a richer prompt. default `"balanced"` |

## Details

MiniMax H3 Max Turbo image-to-video: the fastest H3 tier, animating a first frame (and optional last frame) into a 5–15 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `resolution` | `480P` / `768P` / `1080P` | `768P` | Sets the per-second rate. |
| `duration` | integer 5–15 | 5 | Output length in seconds. |
| `target_audio_url` | audio URL | — | Optional audio the clip should follow. |
| `prompt_expansion_mode` | string | `balanced` | `balanced` rewrites the prompt lightly; `quality` expands it more for richer detail. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for new seconds: $0.025 at 480P, $0.04 at 768P, $0.08 at 1080P.

| Output | 480P | 768P | 1080P |
|---|---|---|---|
| 5s (default) | $0.125 | $0.20 | $0.40 |
| 10s | $0.25 | $0.40 | $0.80 |
| 15s | $0.375 | $0.60 | $1.20 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound in order.
- Quote dialogue and name the speaker.

### Also on SandBase

Other H3 Max Turbo endpoints: `minimax/h3-max-turbo/text-to-video`, `minimax/h3-max-turbo/video-extend`, `minimax/h3-max/text-to-video` (H3 Max).

---
Machine-readable: [`catalog/models/minimax/h3-max-turbo/image-to-video.json`](../../../../catalog/models/minimax/h3-max-turbo/image-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/h3-max-turbo/image-to-video
