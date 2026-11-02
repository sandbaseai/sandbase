# Kling V4 Image to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/v4/image-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.471 to $7.05 per run, depending on parameters · **Modes:** async

Kling V4 Image to Video by Kuaishou animates a start image, optionally toward an end image, into a 3-30 second video.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="720p" | 0.471 |
| duration=3, resolution="1080p" | 0.705 |
| duration=5, resolution="720p" | 0.785 |
| duration=5, resolution="1080p" | 1.175 |
| duration=30, resolution="720p" | 4.71 |
| duration=30, resolution="1080p" | 7.05 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "1080p") == "720p" ? 0.157 : 0.235)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v4/image-to-video", "image": "https://static.sandbase.ai/examples/746c1af3-e60b-4a50-a599-53df4d3da1ae/input/fae6ad50-5dc0-4015-8e2f-4ff7689f448b.png", "prompt": "The rabbit looks around curiously, its ears twitch, then it hops toward the camera. Soft breeze moves the grass."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v4/image-to-video', {'image': 'https://static.sandbase.ai/examples/746c1af3-e60b-4a50-a599-53df4d3da1ae/input/fae6ad50-5dc0-4015-8e2f-4ff7689f448b.png', 'prompt': 'The rabbit looks around curiously, its ears twitch, then it hops toward the camera. Soft breeze moves the grass.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v4/image-to-video", {
  "image": "https://static.sandbase.ai/examples/746c1af3-e60b-4a50-a599-53df4d3da1ae/input/fae6ad50-5dc0-4015-8e2f-4ff7689f448b.png",
  "prompt": "The rabbit looks around curiously, its ears twitch, then it hops toward the camera. Soft breeze moves the grass."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v4/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/746c1af3-e60b-4a50-a599-53df4d3da1ae/input/fae6ad50-5dc0-4015-8e2f-4ff7689f448b.png",
	"prompt": "The rabbit looks around curiously, its ears twitch, then it hops toward the camera. Soft breeze moves the grass.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | First frame. Min 300x300 px, aspect ratio 0.4-2.5, up to 30 MB.  |
| `prompt` | string | yes | Describe subject, action, camera and light.  |
| `duration` | integer |  | Output length in seconds (3-30). default `5`; range 3–30 |
| `end_image` | string |  | Optional last frame.  |
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`; default `"1080p"` |

## Details

Kling V4 image-to-video animates a start image, optionally toward an end image, into a 3–30 second clip.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | First frame. Min 300×300 px, aspect ratio 0.4–2.5, up to 30 MB. |
| `end_image` | image URL | — | Optional last frame. |
| `resolution` | `720p` / `1080p` | `1080p` | Output resolution. |
| `duration` | 3–30 | 5 | Output length in seconds. |
### Billing
Billed per output second: $0.157 at 720p, $0.235 at 1080p.
| Output | Price |
|---|---|
| 5s, 1080p (default) | $1.175 |
| 5s, 720p | $0.785 |
| 10s, 1080p | $2.35 |
| 30s, 1080p | $7.05 |
Failed runs are not charged.
### Prompting
- Describe what moves and how the camera moves; the image sets the look.
### Limits
- Clips are 3–30 seconds.
### Also on SandBase
Other Kling V4 endpoints: `kwaivgi/kling-video/v4/text-to-video`, `kwaivgi/kling-video/v4/image-to-video`, `kwaivgi/kling-video/v4/reference-to-video`, `kwaivgi/kling-video/v4/video-edit`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v4/image-to-video.json`](../../../../../catalog/models/kwaivgi/kling-video/v4/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v4/image-to-video
