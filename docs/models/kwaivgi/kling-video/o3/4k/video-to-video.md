# Kling O3 4K Video Reference

`kwaivgi/kling-video/o3/4k/video-to-video` · video · KwaiVGI

Kling O3 4K Video Reference by Kuaishou generates a new native 4K shot that follows the style and camera motion of a reference video, optionally guided by reference images.

## Pricing

- Depends on parameters (`params.duration`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=3 | 1.26 * |
| duration=4 | 1.68 * |
| duration=5 | 2.1 * |
| duration=6 | 2.52 * |
| duration=7 | 2.94 * |
| duration=8 | 3.36 * |

\* estimate: assumes output duration equals requested duration.

Formula: `(params.duration ?? Math.ceil(usage.duration ?? 5.0)) * 0.42`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/o3/4k/video-to-video", "prompt": "Integrate @Element1 in the scene. Style video should be following watercolor style of @Image1", "video": "https://static.sandbase.ai/examples/efb9ed85-8d55-48df-956f-2f5c72ee7fd8/input/b8d4e379-e81f-4fb1-9009-75af47153760.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/o3/4k/video-to-video', {'prompt': 'Integrate @Element1 in the scene. Style video should be following watercolor style of @Image1', 'video': 'https://static.sandbase.ai/examples/efb9ed85-8d55-48df-956f-2f5c72ee7fd8/input/b8d4e379-e81f-4fb1-9009-75af47153760.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/o3/4k/video-to-video", {
  "prompt": "Integrate @Element1 in the scene. Style video should be following watercolor style of @Image1",
  "video": "https://static.sandbase.ai/examples/efb9ed85-8d55-48df-956f-2f5c72ee7fd8/input/b8d4e379-e81f-4fb1-9009-75af47153760.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/o3/4k/video-to-video", sandbase.Params{
	"prompt": "Integrate @Element1 in the scene. Style video should be following watercolor style of @Image1",
	"video": "https://static.sandbase.ai/examples/efb9ed85-8d55-48df-956f-2f5c72ee7fd8/input/b8d4e379-e81f-4fb1-9009-75af47153760.mp4",
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

Kling O3 4K video reference: generate new shots that follow the motion and camera language of a reference video, while the prompt and optional reference images set the new scene and look.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `images` | image URL[] | — | Reference images, referred to as @Image1, @Image2, … in the prompt. |
| `video` | video URL, required | — | Reference video, @Video1 in the prompt. |
| `duration` | 3–15 | — | Output length; omit to match the reference. |
| `keep_audio` | boolean | true | Keep the source video's audio track. |
| `shot_type` | string | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` | `16:9` | Output frame shape. |

### Billing

You pay $0.42 per output second. Without `duration` the output matches the reference length; the quote assumes 5 seconds.

| Output | Price |
|---|---|
| 3s | $1.26 |
| 5s | $2.10 |
| 10s | $4.20 |
| 15s | $6.30 |

Failed runs are not charged.

### Prompting

- Describe the new scene; the reference video supplies motion and camera.

### Limits

- Clips are 3–15 seconds.

### Also on SandBase

Other Kling O3 4K endpoints and tiers: `kwaivgi/kling-video/o3/4k/text-to-video`, `kwaivgi/kling-video/o3/4k/image-to-video`, `kwaivgi/kling-video/o3/4k/reference-to-video`, `kwaivgi/kling-video/o3/4k/edit`, `kwaivgi/kling-video/o3/standard/video-to-video`, `kwaivgi/kling-video/o3/pro/video-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/o3/4k/video-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/o3/4k/video-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/o3/4k/video-to-video
