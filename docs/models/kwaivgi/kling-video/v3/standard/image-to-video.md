# Kling V3 Standard Image to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/v3/standard/image-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.252 to $1.008 per run, depending on parameters · **Modes:** async

Kling V3 Standard Image to Video by Kuaishou animates a start image, optionally toward an end image, into a 3-15 second 720p video with optional native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`).

| parameters | USD |
|---|---|
| duration=3, generate_audio=false | 0.252 |
| duration=3, generate_audio=true | 0.378 |
| duration=4, generate_audio=false | 0.336 |
| duration=4, generate_audio=true | 0.504 |
| duration=5, generate_audio=false | 0.42 |
| duration=5, generate_audio=true | 0.63 |
| duration=6, generate_audio=false | 0.504 |
| duration=6, generate_audio=true | 0.756 |
| duration=7, generate_audio=false | 0.588 |
| duration=7, generate_audio=true | 0.882 |
| duration=8, generate_audio=false | 0.672 |
| duration=8, generate_audio=true | 1.008 |

Formula: `(params.generate_audio ?? true) ? (params.duration ?? 5) * 0.126 : (params.duration ?? 5) * 0.084`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v3/standard/image-to-video", "image": "https://static.sandbase.ai/examples/86a7f854-cf40-44b5-8e5c-11f9defeecb0/input/2561aa12-c21e-4d85-8d4c-a076cd6fe14a.png", "prompt": "Camera slowly orbits around the vase. Soft light shifts across the ceramic surface. The pampas grass sways gently. Shadows move elegantly. Smooth continuous motion, premium feel."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v3/standard/image-to-video', {'image': 'https://static.sandbase.ai/examples/86a7f854-cf40-44b5-8e5c-11f9defeecb0/input/2561aa12-c21e-4d85-8d4c-a076cd6fe14a.png', 'prompt': 'Camera slowly orbits around the vase. Soft light shifts across the ceramic surface. The pampas grass sways gently. Shadows move elegantly. Smooth continuous motion, premium feel.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v3/standard/image-to-video", {
  "image": "https://static.sandbase.ai/examples/86a7f854-cf40-44b5-8e5c-11f9defeecb0/input/2561aa12-c21e-4d85-8d4c-a076cd6fe14a.png",
  "prompt": "Camera slowly orbits around the vase. Soft light shifts across the ceramic surface. The pampas grass sways gently. Shadows move elegantly. Smooth continuous motion, premium feel."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v3/standard/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/86a7f854-cf40-44b5-8e5c-11f9defeecb0/input/2561aa12-c21e-4d85-8d4c-a076cd6fe14a.png",
	"prompt": "Camera slowly orbits around the vase. Soft light shifts across the ceramic surface. The pampas grass sways gently. Shadows move elegantly. Smooth continuous motion, premium feel.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the image to be used for the video  |
| `prompt` | string | yes | Text prompt for video generation. Either prompt or multi_prompt must be provided, but not both.  |
| `duration` | integer |  | The duration of the generated video in seconds one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `end_image` | string |  | URL of the image to be used for the end of the video  |
| `shot_type` | string |  | The type of multi-shot video generation. 'intelligent' lets the model automatically determine shot structure. one of: `customize`, `intelligent`; default `"customize"` |
| `multi_prompt` | array |  | List of prompts for multi-shot video generation. If provided, divides the video into multiple shots.  |
| `generate_audio` | boolean |  | Whether to generate native audio for the video. Supports Chinese and English voice output. Other languages are automatically translated to English. For English speech, use lowercase letters; for acronyms or proper… default `true` |

## Details

Kling V3 Standard image-to-video: `image` anchors the first frame, `end_image` optionally the last, with native audio and multi-shot control.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `generate_audio` | boolean | true | Generate native audio with the clip. |
| `shot_type` | `customize` / `intelligent` | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |
| `multi_prompt` | object[] | — | Optional list of shots, each with its own prompt and duration. |

### Billing

You pay for output seconds: $0.126 with audio (the default) and $0.084 without.

| Output | With audio | Without audio |
|---|---|---|
| 3s | $0.378 | $0.252 |
| 5s (default) | $0.63 | $0.42 |
| 10s | $1.26 | $0.84 |
| 15s | $1.89 | $1.26 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order.
- For several shots, use `multi_prompt` with one entry per shot.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling V3 Standard endpoints and tiers: `kwaivgi/kling-video/v3/standard/text-to-video`, `kwaivgi/kling-video/v3/standard/motion-control`, `kwaivgi/kling-video/v3/pro/image-to-video`, `kwaivgi/kling-video/v3/4k/image-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v3/standard/image-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v3/standard/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v3/standard/image-to-video
