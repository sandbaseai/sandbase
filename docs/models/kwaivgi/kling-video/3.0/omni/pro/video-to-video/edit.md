# Kling 3.0 Omni Pro Video Edit API: pricing, parameters and code examples

`kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.84 per call · **Modes:** async

Kling 3.0 Omni Pro Video Edit by Kuaishou edits an input video from a text instruction, optionally guided by reference images, at 1080p.

## Pricing

- Depends on parameters (`params.video`).

Formula: `(media_duration(params.video) ?? 15.0) * 0.168`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit", "prompt": "Replace the character in the video with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1", "video": "https://static.sandbase.ai/examples/d8e6723f-c5f2-49ea-8e92-d15dbfdb8702/input/e08df747-4f43-46f7-b259-dbfde5b1a6c6.mp4"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit', {'prompt': 'Replace the character in the video with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1', 'video': 'https://static.sandbase.ai/examples/d8e6723f-c5f2-49ea-8e92-d15dbfdb8702/input/e08df747-4f43-46f7-b259-dbfde5b1a6c6.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit", {
  "prompt": "Replace the character in the video with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1",
  "video": "https://static.sandbase.ai/examples/d8e6723f-c5f2-49ea-8e92-d15dbfdb8702/input/e08df747-4f43-46f7-b259-dbfde5b1a6c6.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit", sandbase.Params{
	"prompt": "Replace the character in the video with @Element1, maintaining the same movements and camera angles. Transform the landscape into @Image1",
	"video": "https://static.sandbase.ai/examples/d8e6723f-c5f2-49ea-8e92-d15dbfdb8702/input/e08df747-4f43-46f7-b259-dbfde5b1a6c6.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | Reference video URL. Only .mp4/.mov formats supported, 3-10 seconds duration, 720-2160px resolution, max 200MB. Max file size: 200.0MB, Min width: 720px, Min height: 720px, Max width: 2160px, Max height: 2160px, Min…  |
| `images` | array |  | Reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 4 total (elements + reference images) when using video.  |
| `prompt` | string | yes | Use @Element1, @Element2 to reference elements and @Image1, @Image2 to reference images in order.  |
| `elements` | array |  | Elements (characters/objects) to include. Reference in prompt as @Element1, @Element2, etc. Maximum 4 total (elements + reference images) when using video.  |
| `keep_audio` | boolean |  | Whether to keep the original audio from the video. default `false` |

## Details

Kling 3.0 Omni Pro video edit: change an existing clip with an instruction and optional reference images, keeping its motion and timing.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `images` | image URL[] | — | Optional reference images, @Image1, … |
| `video` | video URL, required | — | Source clip, @Video1 in the prompt. |
| `elements` | object[] | — | Optional character or object elements to keep consistent. |
| `keep_audio` | boolean | false | Keep the source video's audio track. |

### Billing

$0.168 per second of the source video. The quote before submission assumes 15 seconds; the final charge uses the measured length.

| Source clip | Price |
|---|---|
| 3s source | $0.504 |
| 5s source | $0.84 |
| 10s source | $1.68 |
| 15s source | $2.52 |

Failed runs are not charged.

### Prompting

- Lead with the change and say what must stay.

### Limits

- Output length follows the source.

### Also on SandBase

Other Kling 3.0 Omni endpoints: `kwaivgi/kling-video/3.0/omni/pro/image-to-video`, `kwaivgi/kling-video/3.0/omni/pro/reference-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit.json`](../../../../../../../../catalog/models/kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit
