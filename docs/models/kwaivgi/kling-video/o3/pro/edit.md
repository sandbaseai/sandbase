# Kling O3 Pro Video Edit

`kwaivgi/kling-video/o3/pro/edit` · video · KwaiVGI

Kling O3 Pro Video Edit by Kuaishou edits an input video from a text instruction, optionally guided by reference images, at 1080p.

## Pricing

- Depends on parameters (`params.video`).

Formula: `(media_duration(params.video) ?? 15.0) * 0.168`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/o3/pro/edit", "prompt": "Change environment to be fully snow as @Image1. Replace animal with @Element1", "video": "https://static.sandbase.ai/examples/f2a6296e-188b-460a-9d91-c0a68096ad4d/input/6cbd685e-53b2-47f5-8076-57ab4e2684e4.mp4"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/o3/pro/edit', {'prompt': 'Change environment to be fully snow as @Image1. Replace animal with @Element1', 'video': 'https://static.sandbase.ai/examples/f2a6296e-188b-460a-9d91-c0a68096ad4d/input/6cbd685e-53b2-47f5-8076-57ab4e2684e4.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/o3/pro/edit", {
  "prompt": "Change environment to be fully snow as @Image1. Replace animal with @Element1",
  "video": "https://static.sandbase.ai/examples/f2a6296e-188b-460a-9d91-c0a68096ad4d/input/6cbd685e-53b2-47f5-8076-57ab4e2684e4.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/o3/pro/edit", sandbase.Params{
	"prompt": "Change environment to be fully snow as @Image1. Replace animal with @Element1",
	"video": "https://static.sandbase.ai/examples/f2a6296e-188b-460a-9d91-c0a68096ad4d/input/6cbd685e-53b2-47f5-8076-57ab4e2684e4.mp4",
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
| `shot_type` | string |  | The type of multi-shot video generation. default `"customize"` |
| `keep_audio` | boolean |  | Whether to keep the original audio from the reference video. default `true` |

## Details

Kling O3 Pro video edit: change an existing clip with an instruction, such as restyling it or swapping objects or people, while motion and camera are kept. Reference images can supply the new look.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `images` | image URL[] | — | Optional reference images, @Image1, @Image2, … |
| `video` | video URL, required | — | Source clip, @Video1 in the prompt. |
| `shot_type` | string | `customize` | `customize` follows your `multi_prompt` shot list; `intelligent` lets the model plan the cuts. |
| `keep_audio` | boolean | true | Keep the source video's audio track. |

### Billing

You pay $0.168 per second of the source video. The quote before submission assumes 15 seconds; the final charge uses the measured length.

| Source clip | Price |
|---|---|
| 3s source | $0.504 |
| 5s source | $0.84 |
| 10s source | $1.68 |
| 15s source | $2.52 |

Failed runs are not charged.

### Prompting

- Lead with the change and say what must stay: “replace the jacket with @Image1; keep the walk and the camera”.

### Limits

- Output length follows the source video.

### Also on SandBase

Other Kling O3 Pro endpoints and tiers: `kwaivgi/kling-video/o3/pro/text-to-video`, `kwaivgi/kling-video/o3/pro/image-to-video`, `kwaivgi/kling-video/o3/pro/reference-to-video`, `kwaivgi/kling-video/o3/pro/video-to-video`, `kwaivgi/kling-video/o3/standard/edit`, `kwaivgi/kling-video/o3/4k/edit`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/o3/pro/edit.json`](../../../../../../catalog/models/kwaivgi/kling-video/o3/pro/edit.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/o3/pro/edit
