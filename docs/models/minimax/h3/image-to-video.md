# MiniMax H3 Image to Video

`minimax/h3/image-to-video` · video · MiniMax

Generate native-stereo 2K video from a first frame and optional last frame with MiniMax H3.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.total_seconds`).

Formula: `(usage.total_seconds ?? params.duration ?? 5) * ((params.resolution ?? "2K") == "768P" ? 0.06 : 0.13)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/h3/image-to-video", "duration": 15, "image": "https://static.sandbase.ai/examples/23ca8902-929b-4b32-912d-ce1d7dd40a79/input/9a0ddc5e-266d-45c2-a34f-9db1ce9044ab.jpeg", "prompt": "make my cleavage bigger and fatter and jigglier  and my bottom part too\nwith my body and clothes are all sweaty and with some milk on it i seductively dance then turn around and jiggle my lower behind part up and down\nthen i drop on the floor knees first all hot and tired but enjoying my self the i grab a cucumber from the camera and i lick and suck it seductively \nthen  loads of milk drop on me from the camera while i laugh and enjoy myself", "resolution": "768P"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('minimax/h3/image-to-video', {'duration': 15, 'image': 'https://static.sandbase.ai/examples/23ca8902-929b-4b32-912d-ce1d7dd40a79/input/9a0ddc5e-266d-45c2-a34f-9db1ce9044ab.jpeg', 'prompt': 'make my cleavage bigger and fatter and jigglier  and my bottom part too\nwith my body and clothes are all sweaty and with some milk on it i seductively dance then turn around and jiggle my lower behind part up and down\nthen i drop on the floor knees first all hot and tired but enjoying my self the i grab a cucumber from the camera and i lick and suck it seductively \nthen  loads of milk drop on me from the camera while i laugh and enjoy myself', 'resolution': '768P'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("minimax/h3/image-to-video", {
  "duration": 15,
  "image": "https://static.sandbase.ai/examples/23ca8902-929b-4b32-912d-ce1d7dd40a79/input/9a0ddc5e-266d-45c2-a34f-9db1ce9044ab.jpeg",
  "prompt": "make my cleavage bigger and fatter and jigglier  and my bottom part too\nwith my body and clothes are all sweaty and with some milk on it i seductively dance then turn around and jiggle my lower behind part up and down\nthen i drop on the floor knees first all hot and tired but enjoying my self the i grab a cucumber from the camera and i lick and suck it seductively \nthen  loads of milk drop on me from the camera while i laugh and enjoy myself",
  "resolution": "768P"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "minimax/h3/image-to-video", sandbase.Params{
	"duration": 15,
	"image": "https://static.sandbase.ai/examples/23ca8902-929b-4b32-912d-ce1d7dd40a79/input/9a0ddc5e-266d-45c2-a34f-9db1ce9044ab.jpeg",
	"prompt": "make my cleavage bigger and fatter and jigglier  and my bottom part too\nwith my body and clothes are all sweaty and with some milk on it i seductively dance then turn around and jiggle my lower behind part up and down\nthen i drop on the floor knees first all hot and tired but enjoying my self the i grab a cucumber from the camera and i lick and suck it seductively \nthen  loads of milk drop on me from the camera while i laugh and enjoy myself",
	"resolution": "768P",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | The first frame of the generated video.  |
| `prompt` | string | yes | Prompt default `"The camera slowly pulls back, revealing the full landscape as clouds drift overhead and light shifts across the terrain."` |
| `duration` | integer | yes | Duration one of: `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`; default `5` |
| `end_image` | string |  | Optional last frame for first-to-last keyframe control.  |
| `resolution` | string |  | Output resolution. 768P is generated natively; 2K is upscaled via an in-context regeneration pass. one of: `768P`, `2K`; default `"2K"` |
| `aigc_watermark` | boolean |  | Whether to add an AIGC label watermark to the generated video. default `false` |

## Details

MiniMax H3 image-to-video: animate a first frame, optionally toward a last frame, into a 4–15 second native-stereo 2K clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 7,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | 4–15, required | 5 | Output length in seconds. |
| `resolution` | `768P` / `2K` | `2K` | Sets the per-second rate. |
| `aigc_watermark` | boolean | false | Add MiniMax's AI-generated watermark. |

### Billing

You pay for output seconds: $0.13 at 2K (the default) and $0.06 at 768P.

| Output | 2K | 768P |
|---|---|---|
| 4s | $0.52 | $0.24 |
| 5s (default) | $0.65 | $0.30 |
| 10s | $1.30 | $0.60 |
| 15s | $1.95 | $0.90 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera, and sound in order.
- Quote dialogue and name the speaker.

### Limits

- `duration` is required.

### Also on SandBase

Other MiniMax H3 endpoints: `minimax/h3/text-to-video`, `minimax/h3/reference-to-video`, `minimax/h3-max/image-to-video` (faster, cheaper).

---
Machine-readable: [`catalog/models/minimax/h3/image-to-video.json`](../../../../catalog/models/minimax/h3/image-to-video.json) · Store page: https://www.sandbase.ai/model/minimax/h3/image-to-video
