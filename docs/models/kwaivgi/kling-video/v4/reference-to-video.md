# Kling V4 Reference to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/v4/reference-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $1.175 per call · **Modes:** async

Kling V4 Reference to Video by Kuaishou generates a 3-30 second video that keeps characters, objects and motion from reference images and videos.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `params.videos`).

Formula: `len(params.videos ?? []) > 0 ? ((params.resolution ?? "1080p") == "720p" ? 0.094 : 0.141) * ((params.duration ?? 5) * 1.0 + Math.max((params.duration ?? 5) * 1.0, media_duration(params.videos) ?? 30.0)) : (params.duration ?? 5) * ((params.resolution ?? "1080p") == "720p" ? 0.157 : 0.235)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v4/reference-to-video", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/d5022210-6b33-4763-915b-1bf6b20f4f81/input/454d9f12-340e-487a-8f25-e83ddd48a57b.png"], "prompt": "The rabbit from @Image1 sits at a wooden table in a cozy cafe, sipping tea from a tiny cup. Warm afternoon light."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v4/reference-to-video', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/d5022210-6b33-4763-915b-1bf6b20f4f81/input/454d9f12-340e-487a-8f25-e83ddd48a57b.png'], 'prompt': 'The rabbit from @Image1 sits at a wooden table in a cozy cafe, sipping tea from a tiny cup. Warm afternoon light.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v4/reference-to-video", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/d5022210-6b33-4763-915b-1bf6b20f4f81/input/454d9f12-340e-487a-8f25-e83ddd48a57b.png"
  ],
  "prompt": "The rabbit from @Image1 sits at a wooden table in a cozy cafe, sipping tea from a tiny cup. Warm afternoon light."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v4/reference-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/d5022210-6b33-4763-915b-1bf6b20f4f81/input/454d9f12-340e-487a-8f25-e83ddd48a57b.png"},
	"prompt": "The rabbit from @Image1 sits at a wooden table in a cozy cafe, sipping tea from a tiny cup. Warm afternoon light.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array |  | Up to 10 reference images, referenced as @Image1, @Image2, ...  |
| `prompt` | string | yes | Text prompt. Refer to references as @Image1, @Video1, ...  |
| `videos` | array |  | Up to 5 reference videos (3-30s each, 30s combined), referenced as @Video1, ... Video references switch to the input-plus-output price.  |
| `duration` | integer |  | Output length in seconds (3-30). default `5`; range 3–30 |
| `voice_ids` | array |  | Up to 2 custom voice IDs so characters speak in that voice. Create one by uploading a 5-30s voice recording at https://www.sandbase.ai/model/kwaivgi/kling-video/create-voice (Kling Create Voice). Cannot be combined…  |
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output frame shape. Leave empty to follow the references (adaptive). one of: `21:9`, `16:9`, `9:16`, `1:1` |

## Details

Kling V4 reference-to-video keeps characters, objects and motion from reference images and videos in a new 3–30 second clip.
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Refer to inputs as `@Image1`, `@Video1`, … |
| `images` | image URL[] | — | Up to 10 reference images. |
| `videos` | video URL[] | — | Up to 5 reference videos, 3–30s each, 30s combined. |
| `voice_ids` | string[] | — | Up to 2 custom voice IDs. Create one at [Kling Create Voice](https://www.sandbase.ai/model/kwaivgi/kling-video/create-voice). Not combinable with `videos`. |
| `aspect_ratio` | `21:9` / `16:9` / `9:16` / `1:1` | — | Leave empty to follow the references. |
| `resolution` | `720p` / `1080p` | `1080p` | Output resolution. |
| `duration` | 3–30 | 5 | Output length in seconds. |
### Billing
Without reference videos: $0.157 per output second at 720p, $0.235 at 1080p.
With reference videos: $0.094 (720p) or $0.141 (1080p) per second of output plus input, where the input side counts at least as long as the output. The quote before submission assumes 30 seconds of reference video when the length cannot be read.
| Request | Price |
|---|---|
| 5s, 1080p, images only (default) | $1.175 |
| 5s, 720p, images only | $0.785 |
| 5s, 1080p, 8s reference video | $1.833 |
| 10s, 720p, 4s reference video | $1.88 |
Failed runs are not charged.
### Prompting
- Name each reference in the prompt, e.g. "@Image1 walks into the scene from @Video1".
- To make a character speak in a cloned voice, upload a 5–30 second recording at [Kling Create Voice](https://www.sandbase.ai/model/kwaivgi/kling-video/create-voice) to get a `voice_id`, pass its ID in `voice_ids`, and write the line in the prompt, e.g. "The man from @Image1 says: \"Welcome back.\"". Every clip has a soundtrack; without `voice_ids` the voice is chosen by the model.
### Limits
- Clips are 3–30 seconds; reference videos 3–30 seconds.
### Also on SandBase
Other Kling V4 endpoints: `kwaivgi/kling-video/v4/text-to-video`, `kwaivgi/kling-video/v4/image-to-video`, `kwaivgi/kling-video/v4/reference-to-video`, `kwaivgi/kling-video/v4/video-edit`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v4/reference-to-video.json`](../../../../../catalog/models/kwaivgi/kling-video/v4/reference-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v4/reference-to-video
