# Kling O3 Pro Image to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/o3/pro/image-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.336 to $1.12 per run, depending on parameters · **Modes:** async

Kling O3 Pro Image to Video by Kuaishou animates a start image, optionally toward an end image, into a 3-15 second 1080p video with optional native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`).

| parameters | USD |
|---|---|
| duration=3, generate_audio=false | 0.336 |
| duration=3, generate_audio=true | 0.42 |
| duration=4, generate_audio=false | 0.448 |
| duration=4, generate_audio=true | 0.56 |
| duration=5, generate_audio=false | 0.56 |
| duration=5, generate_audio=true | 0.7 |
| duration=6, generate_audio=false | 0.672 |
| duration=6, generate_audio=true | 0.84 |
| duration=7, generate_audio=false | 0.784 |
| duration=7, generate_audio=true | 0.98 |
| duration=8, generate_audio=false | 0.896 |
| duration=8, generate_audio=true | 1.12 |

Formula: `(params.generate_audio ?? false) ? (params.duration ?? 5) * 0.14 : (params.duration ?? 5) * 0.112`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/o3/pro/image-to-video", "image": "https://static.sandbase.ai/examples/c6322fde-5914-45ea-9f6e-c5fe4046e468/input/75bc0aa2-3ce0-4abc-bf6a-8aa52557b53d.png", "prompt": "The character walks forward slowly, with the camera following from behind."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/o3/pro/image-to-video', {'image': 'https://static.sandbase.ai/examples/c6322fde-5914-45ea-9f6e-c5fe4046e468/input/75bc0aa2-3ce0-4abc-bf6a-8aa52557b53d.png', 'prompt': 'The character walks forward slowly, with the camera following from behind.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/o3/pro/image-to-video", {
  "image": "https://static.sandbase.ai/examples/c6322fde-5914-45ea-9f6e-c5fe4046e468/input/75bc0aa2-3ce0-4abc-bf6a-8aa52557b53d.png",
  "prompt": "The character walks forward slowly, with the camera following from behind."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/o3/pro/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/c6322fde-5914-45ea-9f6e-c5fe4046e468/input/75bc0aa2-3ce0-4abc-bf6a-8aa52557b53d.png",
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

Kling O3 Pro image-to-video, the quality-first O3 tier. `image` anchors the first frame and an optional `end_image` sets the last; the prompt directs action and camera over 3–15 seconds.

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

You pay for output seconds: $0.112 without audio and $0.14 with `generate_audio`.

| Output | Without audio | With audio |
|---|---|---|
| 3s | $0.336 | $0.42 |
| 5s (default) | $0.56 | $0.70 |
| 10s | $1.12 | $1.40 |
| 15s | $1.68 | $2.10 |

Failed runs are not charged.

### Prompting

- Describe what moves, not what is already visible.
- With two frames, describe the transition between them.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling O3 Pro endpoints and tiers: `kwaivgi/kling-video/o3/pro/text-to-video`, `kwaivgi/kling-video/o3/pro/reference-to-video`, `kwaivgi/kling-video/o3/pro/edit`, `kwaivgi/kling-video/o3/pro/video-to-video`, `kwaivgi/kling-video/o3/standard/image-to-video`, `kwaivgi/kling-video/o3/4k/image-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/o3/pro/image-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/o3/pro/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/o3/pro/image-to-video
