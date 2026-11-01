# Veo 3.1 Fast Reference to Video

`google/veo3.1/fast/reference-to-video` · video · Google

Veo3.1 Fast by Google - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=8, generate_audio=false, resolution="720p" | 0.64 |
| duration=8, generate_audio=false, resolution="1080p" | 0.8 |
| duration=8, generate_audio=false, resolution="4k" | 2 |
| duration=8, generate_audio=true, resolution="720p" | 0.8 |
| duration=8, generate_audio=true, resolution="1080p" | 0.96 |
| duration=8, generate_audio=true, resolution="4k" | 2.4 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "720p" ? ((params.generate_audio ?? true) ? 0.10 : 0.08) : (params.resolution ?? "720p") == "1080p" ? ((params.generate_audio ?? true) ? 0.12 : 0.10) : (params.resolution ?? "720p") == "4k" ? ((params.generate_audio ?? true) ? 0.30 : 0.25) : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/veo3.1/fast/reference-to-video", "generate_audio": false, "images": ["https://static.sandbase.ai/examples/125d9dc1-5e3b-48a2-8e64-959cda106511/input/d87b669d-dbbf-4605-b8b8-24378c5b2202.png"], "prompt": "The lantern from the reference floats over a calm lake"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/veo3.1/fast/reference-to-video', {'generate_audio': False, 'images': ['https://static.sandbase.ai/examples/125d9dc1-5e3b-48a2-8e64-959cda106511/input/d87b669d-dbbf-4605-b8b8-24378c5b2202.png'], 'prompt': 'The lantern from the reference floats over a calm lake'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/veo3.1/fast/reference-to-video", {
  "generate_audio": false,
  "images": [
    "https://static.sandbase.ai/examples/125d9dc1-5e3b-48a2-8e64-959cda106511/input/d87b669d-dbbf-4605-b8b8-24378c5b2202.png"
  ],
  "prompt": "The lantern from the reference floats over a calm lake"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/veo3.1/fast/reference-to-video", sandbase.Params{
	"generate_audio": false,
	"images": []any{"https://static.sandbase.ai/examples/125d9dc1-5e3b-48a2-8e64-959cda106511/input/d87b669d-dbbf-4605-b8b8-24378c5b2202.png"},
	"prompt": "The lantern from the reference floats over a calm lake",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for more reproducible results. range 0–4294967295 |
| `images` | array | yes | Up to 3 reference images of subjects to keep consistent in the video.  |
| `prompt` | string | yes | The text prompt describing the video you want to generate  |
| `duration` | integer |  | Reference-to-video only supports 8 seconds. one of: `8`; default `8` |
| `resolution` | string |  | Output resolution. one of: `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate synchronized audio. Videos without audio are cheaper. default `true` |

## Details

Veo 3.1 Fast reference-to-video: up to 3 reference images keep a character, product, or style consistent in a new 8 second clip with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `images` | image URL[] (≤3), required | — | Up to 3 reference images, Image 1 to Image 3. |
| `duration` | 8 | 8 | Output length in seconds. |
| `resolution` | `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects; turning it off lowers the rate. |
| `seed` | integer 0–4294967295 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds, Google's list price. With audio: $0.10 at 720p, $0.12 at 1080p, $0.30 at 4k. Without audio: $0.08 / $0.10 / $0.25 respectively.

| Output | 720p | 1080p | 4k |
|---|---|---|---|
| 8s with audio (default) | $0.80 | $0.96 | $2.40 |
| 8s without audio | $0.64 | $0.80 | $2.00 |

Failed runs are not charged.

### Prompting

- Say what each reference is: “Image 1 is the host, Image 2 is the studio”.
- Describe the action and the sound; the references set appearance.

### Limits

- Up to 3 reference images; clips are 8 seconds.
- Use Veo 3.1 for the highest quality.

### Also on SandBase

Other Veo 3.1 Fast endpoints: `google/veo3.1/fast/text-to-video`, `google/veo3.1/fast/image-to-video`, `google/veo3.1/fast/first-last-frame-to-video`, `google/veo3.1/fast/video-extend`, `google/veo3.1/text-to-video`, `google/veo3.1/lite/text-to-video`.

---
Machine-readable: [`catalog/models/google/veo3.1/fast/reference-to-video.json`](../../../../../catalog/models/google/veo3.1/fast/reference-to-video.json) · Store page: https://www.sandbase.ai/model/google/veo3.1/fast/reference-to-video
