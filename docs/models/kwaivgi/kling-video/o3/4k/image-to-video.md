# Kling O3 4K Image to Video

`kwaivgi/kling-video/o3/4k/image-to-video` · video · KwaiVGI

Kling O3 4K Image to Video by Kuaishou animates a start image, optionally toward an end image, into a 3-15 second native 4K video with optional native audio.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=3 | 1.26 |
| duration=4 | 1.68 |
| duration=5 | 2.1 |
| duration=6 | 2.52 |
| duration=7 | 2.94 |
| duration=8 | 3.36 |

Formula: `(params.duration ?? 5) * 0.42`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/o3/4k/image-to-video", "image": "https://static.sandbase.ai/examples/1da1e017-a69d-43e2-bcf3-7ad0f703587d/input/45c64ba6-ca51-437c-ae18-1cb9202a0b6e.png", "prompt": "The character walks forward slowly, with the camera following from behind."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/o3/4k/image-to-video', {'image': 'https://static.sandbase.ai/examples/1da1e017-a69d-43e2-bcf3-7ad0f703587d/input/45c64ba6-ca51-437c-ae18-1cb9202a0b6e.png', 'prompt': 'The character walks forward slowly, with the camera following from behind.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/o3/4k/image-to-video", {
  "image": "https://static.sandbase.ai/examples/1da1e017-a69d-43e2-bcf3-7ad0f703587d/input/45c64ba6-ca51-437c-ae18-1cb9202a0b6e.png",
  "prompt": "The character walks forward slowly, with the camera following from behind."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/o3/4k/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/1da1e017-a69d-43e2-bcf3-7ad0f703587d/input/45c64ba6-ca51-437c-ae18-1cb9202a0b6e.png",
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

Kling O3 4K image-to-video, native 4K output in one pass, without a separate upscale. `image` anchors the first frame and an optional `end_image` sets the last; the prompt directs action and camera over 3–15 seconds.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | 3–15 | 5 | Output length in seconds. |
| `generate_audio` | boolean | false | Generate native audio with the clip. |
| `shot_type` | `customize` / `intelligent` | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |
| `multi_prompt` | object[] | — | Optional list of shots, each with its own prompt and duration. |

### Billing

You pay $0.42 per output second, with or without audio.

| Output | Price |
|---|---|
| 3s | $1.26 |
| 5s (default) | $2.10 |
| 10s | $4.20 |
| 15s | $6.30 |

Failed runs are not charged.

### Prompting

- Describe what moves, not what is already visible.
- With two frames, describe the transition between them.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling O3 4K endpoints and tiers: `kwaivgi/kling-video/o3/4k/text-to-video`, `kwaivgi/kling-video/o3/4k/reference-to-video`, `kwaivgi/kling-video/o3/4k/edit`, `kwaivgi/kling-video/o3/4k/video-to-video`, `kwaivgi/kling-video/o3/standard/image-to-video`, `kwaivgi/kling-video/o3/pro/image-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/o3/4k/image-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/o3/4k/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/o3/4k/image-to-video
