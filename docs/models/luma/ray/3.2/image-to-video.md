# Luma Ray 3.2 Image to Video API: pricing, parameters and code examples

`luma/ray/3.2/image-to-video` · video generation model · Luma · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.5 to $12 per run, depending on parameters · **Modes:** async

Agent Ray 3.2 by Luma - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.exr_export`, `params.hdr`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, exr_export=false, hdr=false, resolution="540p" | 0.5 |
| duration=5, exr_export=false, hdr=false, resolution="720p" | 1 |
| duration=5, exr_export=false, hdr=false, resolution="1080p" | 2 |
| duration=5, exr_export=false, hdr=true, resolution="540p" | 0.5 |
| duration=5, exr_export=false, hdr=true, resolution="720p" | 2 |
| duration=5, exr_export=false, hdr=true, resolution="1080p" | 4 |
| duration=5, exr_export=true, hdr=false, resolution="540p" | 0.5 |
| duration=5, exr_export=true, hdr=false, resolution="720p" | 1 |
| duration=5, exr_export=true, hdr=false, resolution="1080p" | 2 |
| duration=5, exr_export=true, hdr=true, resolution="540p" | 0.5 |
| duration=5, exr_export=true, hdr=true, resolution="720p" | 3 |
| duration=5, exr_export=true, hdr=true, resolution="1080p" | 6 |
| duration=10, exr_export=false, hdr=false, resolution="540p" | 1 |
| duration=10, exr_export=false, hdr=false, resolution="720p" | 2 |
| duration=10, exr_export=false, hdr=false, resolution="1080p" | 4 |
| duration=10, exr_export=false, hdr=true, resolution="540p" | 1 |
| duration=10, exr_export=false, hdr=true, resolution="720p" | 4 |
| duration=10, exr_export=false, hdr=true, resolution="1080p" | 8 |
| duration=10, exr_export=true, hdr=false, resolution="540p" | 1 |
| duration=10, exr_export=true, hdr=false, resolution="720p" | 2 |
| duration=10, exr_export=true, hdr=false, resolution="1080p" | 4 |
| duration=10, exr_export=true, hdr=true, resolution="540p" | 1 |
| duration=10, exr_export=true, hdr=true, resolution="720p" | 6 |
| duration=10, exr_export=true, hdr=true, resolution="1080p" | 12 |

Formula: `((params.duration ?? 5) == 10 ? 2 : 1) * ((params.resolution ?? "720p") == "1080p" ? 2.0 : (params.resolution ?? "720p") == "720p" ? 1.0 : 0.5) * (((params.resolution ?? "720p") != "540p" && (params.hdr ?? false)) ? ((params.exr_export ?? false) ? 3.0 : 2.0) : 1.0)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "luma/ray/3.2/image-to-video", "prompt": "<prompt>", "image": "<image>"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('luma/ray/3.2/image-to-video', {'prompt': '<prompt>', 'image': '<image>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("luma/ray/3.2/image-to-video", {
  "prompt": "<prompt>",
  "image": "<image>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "luma/ray/3.2/image-to-video", sandbase.Params{
	"prompt": "<prompt>",
	"image": "<image>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hdr` | boolean |  | Generate an HDR-encoded MP4. Requires HDR access on the account and a resolution of 720p or 1080p; not supported with loop. default `false` |
| `loop` | boolean |  | Generate a seamless loop. Only valid for standard-dynamic-range generations without an end frame or keyframes. default `false` |
| `image` | string | yes | URL of the image used as the first frame of the video. Provide either image_url (optionally with end_image_url) or keyframes — the two anchoring modes are mutually exclusive.  |
| `prompt` | string | yes | Text prompt describing the motion/scene to generate.  |
| `duration` | integer |  | Duration of the generated video. 10s requires multi-keyframe input (keyframes / keyframe_indexes); it is not supported with a single image_url / end_image_url anchor. one of: `5`, `10`; default `5` |
| `end_image` | string |  | Optional URL of an image used as the last frame. When set, the model interpolates between image_url and end_image_url. Cannot be combined with keyframes.  |
| `keyframes` | array |  | Multi-keyframe image-to-video guide frames: 1-64 image URLs pinned at the positions given by keyframe_indexes. Mutually exclusive with image_url, end_image_url, and loop; unlocks 10s and HDR. Provide keyframes and…  |
| `exr_export` | boolean |  | Also export an EXR file alongside the MP4. Requires hdr=true and HDR access. default `false` |
| `resolution` | string |  | Resolution of the generated video. Higher resolutions cost more. one of: `540p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`; default `"16:9"` |
| `keyframe_indexes` | array |  | Output-frame positions (duration x 24fps: 5s -> 0-120, 10s -> 0-240) where each keyframes[i] is anchored. Non-negative, unique, and the same length as keyframes.  |

## Details

Luma Ray 3.2 image-to-video: animate a first frame (optionally toward an end frame or keyframes) into a 5 or 10 second clip, with optional HDR.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 6,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `resolution` | `540p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |
| `loop` | boolean | false | Make the clip loop. |
| `keyframes` | string[] | — | Optional keyframe images. |
| `keyframe_indexes` | integer[] | — | Frame positions for `keyframes`. |
| `exr_export` | boolean | false | Also export EXR frames with HDR; triples the price. |
| `hdr` | boolean | false | 16-bit HDR output (720p and 1080p); doubles the price. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `16:9` | Output frame shape. |

### Billing

$0.50 per 5-second clip at 540p, $1.00 at 720p, $2.00 at 1080p; 10 seconds costs double. HDR doubles and HDR with EXR export triples the 720p/1080p price.

| Output | 540p | 720p | 1080p |
|---|---|---|---|
| 5s (default) | $0.50 | $1.00 | $2.00 |
| 10s | $1.00 | $2.00 | $4.00 |
| 5s HDR | $0.50 | $2.00 | $4.00 |

Failed runs are not charged.

### Prompting

- Describe what moves and how the camera behaves.

### Limits

- Clips are 5 or 10 seconds.

### Also on SandBase

Related: `luma/ray/3.2/text-to-video`.

---
Machine-readable: [`catalog/models/luma/ray/3.2/image-to-video.json`](../../../../../catalog/models/luma/ray/3.2/image-to-video.json) · Store page: https://www.sandbase.ai/model/luma/ray/3.2/image-to-video
