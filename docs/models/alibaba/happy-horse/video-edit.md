# Happy Horse Video Edit

`alibaba/happy-horse/video-edit` · video · Alibaba

Happy Horse Video Edit by Alibaba - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual effects to existing videos with natural language instructions.

## Pricing

- Depends on parameters (`params.resolution`, `params.video`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.video) ?? 5.0) * 2.0 * ((params.resolution ?? "720p") == "720p" ? 0.14 : 0.24)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/happy-horse/video-edit", "prompt": "Make the scene snowy", "resolution": "720p", "video": "https://static.sandbase.ai/examples/d40d74d4-3ccc-4e10-8d82-cb6d7040edc4/input/19f9589e-def6-4f7b-a519-2d17f8de3364.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/happy-horse/video-edit', {'prompt': 'Make the scene snowy', 'resolution': '720p', 'video': 'https://static.sandbase.ai/examples/d40d74d4-3ccc-4e10-8d82-cb6d7040edc4/input/19f9589e-def6-4f7b-a519-2d17f8de3364.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/happy-horse/video-edit", {
  "prompt": "Make the scene snowy",
  "resolution": "720p",
  "video": "https://static.sandbase.ai/examples/d40d74d4-3ccc-4e10-8d82-cb6d7040edc4/input/19f9589e-def6-4f7b-a519-2d17f8de3364.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/happy-horse/video-edit", sandbase.Params{
	"prompt": "Make the scene snowy",
	"resolution": "720p",
	"video": "https://static.sandbase.ai/examples/d40d74d4-3ccc-4e10-8d82-cb6d7040edc4/input/19f9589e-def6-4f7b-a519-2d17f8de3364.mp4",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-2147483647).  |
| `video` | string | yes | URL of the source video to edit. Formats: MP4, MOV (H.264 recommended). Duration: 3-60 s. Longer side ≤ 2160 px, shorter side ≥ 320 px. Aspect ratio between 1:2.5 and 2.5:1. Frame rate > 8 fps. Max 100 MB. The output…  |
| `prompt` | string | yes | Text prompt describing the desired edit. Reference any supplied reference images using @Image1, @Image2, ... up to @Image5. Max 2500 characters.  |
| `resolution` | string |  | Output video resolution tier. one of: `720p`, `1080p`; default `"720p"` |
| `audio_setting` | string |  | Audio handling. 'auto': model decides whether to regenerate audio. 'origin': preserve the original audio from the input video. one of: `auto`, `origin`; default `"auto"` |
| `reference_image_urls` | array |  | Optional reference images used to guide the edit (up to 5). Formats: JPEG, JPG, PNG, WEBP. Dimensions must be at least 300px. Aspect ratio between 1:2.5 and 2.5:1. Max 10 MB each.  |

## Details

Edit an existing clip with Happy Horse: restyle it, change objects or wardrobe, or rework the scene with an instruction. Optional reference images show the target look; the source motion and length are kept.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `video` | video URL, required | — | Source clip, Video 1 in the prompt. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |
| `reference_image_urls` | image URL[] | — | Optional reference images for the new look. |
| `audio_setting` | `auto` / `origin` | `auto` | `auto` regenerates audio to match the edit; `origin` keeps the source track. |

### Billing

Alibaba bills the source and the edited output, which are the same length, so each source second bills twice: $0.28 at 720p and $0.48 at 1080p. The quote before submission assumes a 5-second source; the final charge uses the measured length.

| Source clip | 720p | 1080p |
|---|---|---|
| 3s | $0.84 | $1.44 |
| 5s | $1.40 | $2.40 |
| 10s | $2.80 | $4.80 |
| 15s | $4.20 | $7.20 |

Failed runs are not charged.

### Prompting

- Lead with the change and say what must stay: “make it a watercolor animation; keep her face and the camera move”.
- Draft at 720p; edits bill twice the source length.

### Limits

- Output length and framing follow the source video.

### Also on SandBase

Other Happy Horse endpoints: `alibaba/happy-horse/text-to-video`, `alibaba/happy-horse/image-to-video`, `alibaba/happy-horse/reference-to-video`, `alibaba/wan/2.7/video-edit` (Wan alternative, bills output only).

---
Machine-readable: [`catalog/models/alibaba/happy-horse/video-edit.json`](../../../../catalog/models/alibaba/happy-horse/video-edit.json) · Store page: https://www.sandbase.ai/model/alibaba/happy-horse/video-edit
