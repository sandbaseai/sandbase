# Vidu Q3 Image to Video Turbo API: pricing, parameters and code examples

`vidu/q3/image-to-video/turbo` · video generation model · Vidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.04 to $1.28 per run, depending on parameters · **Modes:** async

Vidu Q3 Turbo by Shengshu - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="360p" | 0.04 |
| duration=1, resolution="540p" | 0.04 |
| duration=1, resolution="720p" | 0.077 |
| duration=1, resolution="1080p" | 0.08 |
| duration=5, resolution="360p" | 0.2 |
| duration=5, resolution="540p" | 0.2 |
| duration=5, resolution="720p" | 0.385 |
| duration=5, resolution="1080p" | 0.4 |
| duration=16, resolution="360p" | 0.64 |
| duration=16, resolution="540p" | 0.64 |
| duration=16, resolution="720p" | 1.232 |
| duration=16, resolution="1080p" | 1.28 |

Formula: `(params.duration ?? 5) * ((params.resolution ?? "720p") == "1080p" ? 0.08 : (params.resolution ?? "720p") == "720p" ? 0.077 : 0.04)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vidu/q3/image-to-video/turbo", "image": "https://static.sandbase.ai/examples/d23baf96-6c95-47f5-b9d9-3b246879c202/input/c243944a-cc2d-487d-9953-47cd2bd754f7.png", "prompt": "The astronaut waved and the camera moved up."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vidu/q3/image-to-video/turbo', {'image': 'https://static.sandbase.ai/examples/d23baf96-6c95-47f5-b9d9-3b246879c202/input/c243944a-cc2d-487d-9953-47cd2bd754f7.png', 'prompt': 'The astronaut waved and the camera moved up.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vidu/q3/image-to-video/turbo", {
  "image": "https://static.sandbase.ai/examples/d23baf96-6c95-47f5-b9d9-3b246879c202/input/c243944a-cc2d-487d-9953-47cd2bd754f7.png",
  "prompt": "The astronaut waved and the camera moved up."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vidu/q3/image-to-video/turbo", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/d23baf96-6c95-47f5-b9d9-3b246879c202/input/c243944a-cc2d-487d-9953-47cd2bd754f7.png",
	"prompt": "The astronaut waved and the camera moved up.",
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
| `audio` | boolean |  | Whether to use direct audio-video generation. When true, outputs video with sound (including dialogue and sound effects). default `true` |
| `image` | string | yes | URL or base64 image to use as the starting frame  |
| `prompt` | string | yes | Text prompt for video generation, max 2000 characters default `""` |
| `duration` | integer |  | Duration of the video in seconds (1-16 for Q3 models) default `5`; range 1–16 |
| `end_image` | string |  | URL of the image to use as the ending frame. When provided, generates a transition video between start and end frames.  |
| `resolution` | string |  | Output video resolution. Note: 360p is not available when end_image_url is provided. one of: `360p`, `540p`, `720p`, `1080p`; default `"720p"` |

## Details

Vidu Q3 Turbo image-to-video: animate a first frame, optionally toward a last frame, into a 1–16 second clip with native audio. Turbo is faster and cheaper.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `audio` | boolean | true | Generate native audio. Same price on or off. |
| `resolution` | `360p` / `540p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–16 | 5 | Output length in seconds. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.04 at 360p or 540p, $0.077 at 720p, $0.08 at 1080p.

| Output | 540p | 720p | 1080p |
|---|---|---|---|
| 4s | $0.16 | $0.308 | $0.32 |
| 5s (default) | $0.20 | $0.385 | $0.40 |
| 8s | $0.32 | $0.616 | $0.64 |
| 16s | $0.64 | $1.232 | $1.28 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Vidu Q3 endpoints: `vidu/q3/text-to-video`, `vidu/q3/image-to-video`, `vidu/q3/reference-to-video/mix`, `vidu/q3/text-to-video/turbo`.

---
Machine-readable: [`catalog/models/vidu/q3/image-to-video/turbo.json`](../../../../../catalog/models/vidu/q3/image-to-video/turbo.json) · Store page: https://www.sandbase.ai/model/vidu/q3/image-to-video/turbo
