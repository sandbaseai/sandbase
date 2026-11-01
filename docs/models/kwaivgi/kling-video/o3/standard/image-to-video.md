# Kling O3 Standard Image to Video

`kwaivgi/kling-video/o3/standard/image-to-video` · video · KwaiVGI

Kling O3 Standard Image to Video by Kuaishou animates a start image, optionally toward an end image, into a 3-15 second 720p video with optional native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`).

| parameters | USD |
|---|---|
| duration=3, generate_audio=false | 0.252 |
| duration=3, generate_audio=true | 0.336 |
| duration=4, generate_audio=false | 0.336 |
| duration=4, generate_audio=true | 0.448 |
| duration=5, generate_audio=false | 0.42 |
| duration=5, generate_audio=true | 0.56 |
| duration=6, generate_audio=false | 0.504 |
| duration=6, generate_audio=true | 0.672 |
| duration=7, generate_audio=false | 0.588 |
| duration=7, generate_audio=true | 0.784 |
| duration=8, generate_audio=false | 0.672 |
| duration=8, generate_audio=true | 0.896 |

Formula: `(params.generate_audio ?? false) ? (params.duration ?? 5) * 0.112 : (params.duration ?? 5) * 0.084`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/o3/standard/image-to-video", "image": "https://static.sandbase.ai/examples/182211e7-4369-4ad2-ae63-0e50f87b03d3/input/b6fc0b61-31c0-4922-aea3-b5231ea1937c.png", "prompt": "The character walks forward slowly, with the camera following from behind."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/o3/standard/image-to-video', {'image': 'https://static.sandbase.ai/examples/182211e7-4369-4ad2-ae63-0e50f87b03d3/input/b6fc0b61-31c0-4922-aea3-b5231ea1937c.png', 'prompt': 'The character walks forward slowly, with the camera following from behind.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/o3/standard/image-to-video", {
  "image": "https://static.sandbase.ai/examples/182211e7-4369-4ad2-ae63-0e50f87b03d3/input/b6fc0b61-31c0-4922-aea3-b5231ea1937c.png",
  "prompt": "The character walks forward slowly, with the camera following from behind."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/o3/standard/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/182211e7-4369-4ad2-ae63-0e50f87b03d3/input/b6fc0b61-31c0-4922-aea3-b5231ea1937c.png",
	"prompt": "The character walks forward slowly, with the camera following from behind.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the start frame image.  |
| `prompt` | string | yes | Text prompt for video generation. Either prompt or multi_prompt must be provided, but not both.  |
| `duration` | integer |  | Video duration in seconds (3-15s). one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `end_image` | string |  | URL of the end frame image (optional).  |
| `shot_type` | string |  | The type of multi-shot video generation. 'intelligent' lets the model automatically determine shot structure. one of: `customize`, `intelligent`; default `"customize"` |
| `multi_prompt` | array |  | List of prompts for multi-shot video generation.  |
| `generate_audio` | boolean |  | Whether to generate native audio for the video. default `false` |

## Details

Kling O3 Standard image-to-video, the cost-efficient O3 tier. `image` anchors the first frame and an optional `end_image` sets the last; the prompt directs action and camera over 3–15 seconds.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `generate_audio` | boolean | false | Generate native audio with the clip. |
| `multi_prompt` | object[] | — | Optional list of shots, each with its own prompt and duration. |
| `shot_type` | `customize` / `intelligent` | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |

### Billing

You pay for output seconds: $0.084 without audio and $0.112 with `generate_audio`.

| Output | Without audio | With audio |
|---|---|---|
| 3s | $0.252 | $0.336 |
| 5s (default) | $0.42 | $0.56 |
| 10s | $0.84 | $1.12 |
| 15s | $1.26 | $1.68 |

Failed runs are not charged.

### Prompting

- Describe what moves, not what is already visible.
- With two frames, describe the transition between them.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling O3 Standard endpoints and tiers: `kwaivgi/kling-video/o3/standard/text-to-video`, `kwaivgi/kling-video/o3/standard/reference-to-video`, `kwaivgi/kling-video/o3/standard/edit`, `kwaivgi/kling-video/o3/standard/video-to-video`, `kwaivgi/kling-video/o3/pro/image-to-video`, `kwaivgi/kling-video/o3/4k/image-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/o3/standard/image-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/o3/standard/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/o3/standard/image-to-video
