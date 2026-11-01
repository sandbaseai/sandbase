# Kling O3 Pro Reference to Video

`kwaivgi/kling-video/o3/pro/reference-to-video` · video · KwaiVGI

Kling O3 Pro Reference to Video by Kuaishou generates a 3-15 second 1080p video that keeps characters and objects from reference images consistent with optional native audio.

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
  -d '{"model": "kwaivgi/kling-video/o3/pro/reference-to-video", "image": "https://static.sandbase.ai/examples/00305a50-ad70-47d4-a341-44f6307e4de7/input/8e4efa71-0572-4785-b669-3be2232325a8.png", "prompt": "@Element1 and @Element2 enters the scene from two sides. Elephant starts to play with the ball"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/o3/pro/reference-to-video', {'image': 'https://static.sandbase.ai/examples/00305a50-ad70-47d4-a341-44f6307e4de7/input/8e4efa71-0572-4785-b669-3be2232325a8.png', 'prompt': '@Element1 and @Element2 enters the scene from two sides. Elephant starts to play with the ball'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/o3/pro/reference-to-video", {
  "image": "https://static.sandbase.ai/examples/00305a50-ad70-47d4-a341-44f6307e4de7/input/8e4efa71-0572-4785-b669-3be2232325a8.png",
  "prompt": "@Element1 and @Element2 enters the scene from two sides. Elephant starts to play with the ball"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/o3/pro/reference-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/00305a50-ad70-47d4-a341-44f6307e4de7/input/8e4efa71-0572-4785-b669-3be2232325a8.png",
	"prompt": "@Element1 and @Element2 enters the scene from two sides. Elephant starts to play with the ball",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Image to use as the first frame of the video.  |
| `images` | array |  | Additional reference image URLs. Together with `image`, at most 7 images are accepted; do not repeat `image` in this list.  |
| `prompt` | string | yes | Text prompt for video generation. Either prompt or multi_prompt must be provided, but not both.  |
| `duration` | integer |  | Video duration in seconds (3-15s). one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `end_image` | string |  | Image to use as the last frame of the video.  |
| `shot_type` | string |  | The type of multi-shot video generation. 'intelligent' lets the model automatically determine shot structure. one of: `customize`, `intelligent`; default `"customize"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `1:1`; default `"16:9"` |
| `multi_prompt` | array |  | List of prompts for multi-shot video generation.  |
| `generate_audio` | boolean |  | Whether to generate native audio for the video. default `false` |

## Details

Kling O3 Pro reference-to-video, the quality-first O3 tier. A start frame plus up to 6 reference images keep characters, objects, and style consistent; refer to them as @Image1, @Image2 in the prompt.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | Start frame. JPEG, PNG, or WebP URL. |
| `images` | image URL[] (≤6) | — | Reference images, referred to as @Image1, @Image2, … in the prompt. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `generate_audio` | boolean | false | Generate native audio with the clip. |
| `shot_type` | `customize` / `intelligent` | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |
| `multi_prompt` | object[] | — | Optional list of shots, each with its own prompt and duration. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` | `16:9` | Output frame shape. |

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

- Name each reference in the prompt: “@Image1 walks into the room from @Image2”.
- Keep one clear subject per reference image.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling O3 Pro endpoints and tiers: `kwaivgi/kling-video/o3/pro/text-to-video`, `kwaivgi/kling-video/o3/pro/image-to-video`, `kwaivgi/kling-video/o3/pro/edit`, `kwaivgi/kling-video/o3/pro/video-to-video`, `kwaivgi/kling-video/o3/standard/reference-to-video`, `kwaivgi/kling-video/o3/4k/reference-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/o3/pro/reference-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/o3/pro/reference-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/o3/pro/reference-to-video
