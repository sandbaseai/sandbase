# Kling O3 Standard Video Reference

`kwaivgi/kling-video/o3/standard/video-to-video` · video · KwaiVGI

Kling O3 Standard Video Reference by Kuaishou generates a new 720p shot that follows the style and camera motion of a reference video, optionally guided by reference images.

## Pricing

- Depends on parameters (`params.duration`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=3 | 0.378 * |
| duration=4 | 0.504 * |
| duration=5 | 0.63 * |
| duration=6 | 0.756 * |
| duration=7 | 0.882 * |
| duration=8 | 1.008 * |

\* estimate: assumes output duration equals requested duration.

Formula: `(params.duration ?? Math.ceil(usage.duration ?? 5.0)) * 0.126`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/o3/standard/video-to-video", "prompt": "Replace both character with @Element1 and @Element2", "video": "https://static.sandbase.ai/examples/3578d398-d3ec-4c4a-8a7a-d5decf3638f2/input/8dd9cbc1-5dd3-4a80-86c7-ba9a597b9c81.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/o3/standard/video-to-video', {'prompt': 'Replace both character with @Element1 and @Element2', 'video': 'https://static.sandbase.ai/examples/3578d398-d3ec-4c4a-8a7a-d5decf3638f2/input/8dd9cbc1-5dd3-4a80-86c7-ba9a597b9c81.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/o3/standard/video-to-video", {
  "prompt": "Replace both character with @Element1 and @Element2",
  "video": "https://static.sandbase.ai/examples/3578d398-d3ec-4c4a-8a7a-d5decf3638f2/input/8dd9cbc1-5dd3-4a80-86c7-ba9a597b9c81.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/o3/standard/video-to-video", sandbase.Params{
	"prompt": "Replace both character with @Element1 and @Element2",
	"video": "https://static.sandbase.ai/examples/3578d398-d3ec-4c4a-8a7a-d5decf3638f2/input/8dd9cbc1-5dd3-4a80-86c7-ba9a597b9c81.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | Reference video URL. Only .mp4/.mov formats, 3-10s duration, 720-2160px resolution, max 200MB.  |
| `images` | array |  | Reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 4 total (elements + reference images) when using video.  |
| `prompt` | string | yes | Text prompt for video generation. Reference video as @Video1.  |
| `duration` | integer |  | Video duration in seconds (3-15s for reference video). one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` … |
| `shot_type` | string |  | The type of multi-shot video generation. default `"customize"` |
| `keep_audio` | boolean |  | Whether to keep the original audio from the reference video. default `true` |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `1:1`; default `"16:9"` |

## Details

Kling O3 Standard video reference: generate new shots that follow the motion and camera language of a reference video, while the prompt and optional reference images set the new scene and look.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `images` | image URL[] | — | Reference images, referred to as @Image1, @Image2, … in the prompt. |
| `video` | video URL, required | — | Reference video, @Video1 in the prompt. |
| `duration` | 3–15 | — | Output length; omit to match the reference. |
| `shot_type` | string | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |
| `keep_audio` | boolean | true | Keep the source video's audio track. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` | `16:9` | Output frame shape. |

### Billing

You pay $0.126 per output second. Without `duration` the output matches the reference length; the quote assumes 5 seconds.

| Output | Price |
|---|---|
| 3s | $0.378 |
| 5s | $0.63 |
| 10s | $1.26 |
| 15s | $1.89 |

Failed runs are not charged.

### Prompting

- Describe the new scene; the reference video supplies motion and camera.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling O3 Standard endpoints and tiers: `kwaivgi/kling-video/o3/standard/text-to-video`, `kwaivgi/kling-video/o3/standard/image-to-video`, `kwaivgi/kling-video/o3/standard/reference-to-video`, `kwaivgi/kling-video/o3/standard/edit`, `kwaivgi/kling-video/o3/pro/video-to-video`, `kwaivgi/kling-video/o3/4k/video-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/o3/standard/video-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/o3/standard/video-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/o3/standard/video-to-video
