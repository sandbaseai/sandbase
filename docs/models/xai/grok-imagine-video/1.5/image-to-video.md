# Grok Imagine Video 1.5 Image to Video API: pricing, parameters and code examples

`xai/grok-imagine-video/1.5/image-to-video` · video generation model · xAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.09 to $2.11 per run, depending on parameters · **Modes:** async

Grok Imagine Video 1.5 is xAI's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=1, resolution="480p" | 0.09 |
| duration=1, resolution="720p" | 0.15 |
| duration=6, resolution="480p" | 0.49 |
| duration=6, resolution="720p" | 0.85 |
| duration=15, resolution="480p" | 1.21 |
| duration=15, resolution="720p" | 2.11 |

Formula: `(params.duration ?? 6) * ((params.resolution ?? "720p") == "480p" ? 0.08 : 0.14) + 0.01`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xai/grok-imagine-video/1.5/image-to-video", "image": "https://static.sandbase.ai/examples/993270ca-cbd2-4063-b77f-4730e2bea815/input/f8906d8a-349b-4f34-82ce-4a2f7f5167c6.png", "prompt": "Medieval knight in ornate armor walking through a mystical forest, bioluminescent plants pulsing with light, ancient stone ruins overgrown with glowing vines, over-the-shoulder camera, dark fantasy aesthetic, volumetric fog and Lumen lighting"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xai/grok-imagine-video/1.5/image-to-video', {'image': 'https://static.sandbase.ai/examples/993270ca-cbd2-4063-b77f-4730e2bea815/input/f8906d8a-349b-4f34-82ce-4a2f7f5167c6.png', 'prompt': 'Medieval knight in ornate armor walking through a mystical forest, bioluminescent plants pulsing with light, ancient stone ruins overgrown with glowing vines, over-the-shoulder camera, dark fantasy aesthetic, volumetric fog and Lumen lighting'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xai/grok-imagine-video/1.5/image-to-video", {
  "image": "https://static.sandbase.ai/examples/993270ca-cbd2-4063-b77f-4730e2bea815/input/f8906d8a-349b-4f34-82ce-4a2f7f5167c6.png",
  "prompt": "Medieval knight in ornate armor walking through a mystical forest, bioluminescent plants pulsing with light, ancient stone ruins overgrown with glowing vines, over-the-shoulder camera, dark fantasy aesthetic, volumetric fog and Lumen lighting"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xai/grok-imagine-video/1.5/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/993270ca-cbd2-4063-b77f-4730e2bea815/input/f8906d8a-349b-4f34-82ce-4a2f7f5167c6.png",
	"prompt": "Medieval knight in ornate armor walking through a mystical forest, bioluminescent plants pulsing with light, ancient stone ruins overgrown with glowing vines, over-the-shoulder camera, dark fantasy aesthetic, volumetric fog and Lumen lighting",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the input image for video generation.  |
| `prompt` | string | yes | Text description of desired changes or motion in the video.  |
| `duration` | integer |  | Video duration in seconds. default `6`; range 1–15 |
| `resolution` | string |  | Resolution of the output video. one of: `480p`, `720p`; default `"720p"` |

## Details

Grok Imagine Video 1.5 image-to-video: animate a picture into a 1–15 second clip with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 4,096 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `duration` | integer 1–15 | 6 | Output length in seconds. |

### Billing

Per output second: $0.08 at 480p and $0.14 at 720p, plus $0.01 per request for the input image.

| Output | 480p | 720p |
|---|---|---|
| 6s (default) | $0.49 | $0.85 |
| 10s | $0.81 | $1.41 |
| 15s | $1.21 | $2.11 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound.

### Also on SandBase

Other Grok Imagine Video 1.5 endpoints: `xai/grok-imagine-video/1.5/text-to-video`, `xai/grok-imagine-video/1.5/reference-to-video`, `xai/grok-imagine-video/1.5/lite/text-to-video`, `xai/grok-imagine-video/1.5/lite/image-to-video`, `xai/grok-imagine-video/text-to-video` (previous version).

---
Machine-readable: [`catalog/models/xai/grok-imagine-video/1.5/image-to-video.json`](../../../../../catalog/models/xai/grok-imagine-video/1.5/image-to-video.json) · Store page: https://www.sandbase.ai/model/xai/grok-imagine-video/1.5/image-to-video
