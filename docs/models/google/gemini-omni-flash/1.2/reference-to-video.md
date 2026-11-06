# Gemini Omni Flash 1.2 Reference to Video API: pricing, parameters and code examples

`google/gemini-omni-flash/1.2/reference-to-video` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.069 to $3.15 per run, depending on parameters · **Modes:** async

Gemini Omni Flash 1.2 Reference to Video by Google generates a clip with synchronized audio guided by up to ten reference images and up to three reference videos, keeping faces, products, and style consistent.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=3, resolution="360p" | 0.069 |
| duration=3, resolution="720p" | 0.21 |
| duration=3, resolution="1080p" | 0.315 |
| duration=3, resolution="4k" | 0.63 |
| duration=8, resolution="360p" | 0.184 |
| duration=8, resolution="720p" | 0.56 |
| duration=8, resolution="1080p" | 0.84 |
| duration=8, resolution="4k" | 1.68 |
| duration=15, resolution="360p" | 0.345 |
| duration=15, resolution="720p" | 1.05 |
| duration=15, resolution="1080p" | 1.575 |
| duration=15, resolution="4k" | 3.15 |

Formula: `(params.duration ?? 8) * ((params.resolution ?? "720p") == "360p" ? 0.023 : (params.resolution ?? "720p") == "1080p" ? 0.105 : (params.resolution ?? "720p") == "4k" ? 0.21 : 0.07)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-omni-flash/1.2/reference-to-video", "prompt": "A cat inspired by <IMAGE_REF_0> walks through the setting in <VIDEO_REF_0>."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-omni-flash/1.2/reference-to-video', {'prompt': 'A cat inspired by <IMAGE_REF_0> walks through the setting in <VIDEO_REF_0>.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-omni-flash/1.2/reference-to-video", {
  "prompt": "A cat inspired by <IMAGE_REF_0> walks through the setting in <VIDEO_REF_0>."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-omni-flash/1.2/reference-to-video", sandbase.Params{
	"prompt": "A cat inspired by <IMAGE_REF_0> walks through the setting in <VIDEO_REF_0>.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array |  | URLs of up to ten reference images to incorporate.  |
| `prompt` | string | yes | The text prompt describing the video. Reference media is sent in list order before the prompt.  |
| `videos` | array |  | URLs of up to three reference videos. Each video must be at most 15 seconds long.  |
| `duration` | integer |  | The duration of the generated video, in seconds. default `8`; range 3–15 |
| `resolution` | string |  | The resolution of the generated video. one of: `360p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`; default `"16:9"` |

## Details

Gemini Omni Flash 1.2 reference-to-video: up to 10 reference images and 3 reference videos keep characters, products, typography, and style consistent in a new clip with synchronized audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `images` | image URL[] (≤10) | — | Reference images, Image 1, Image 2, … |
| `videos` | video URL[] (≤3) | — | Reference clips, Video 1, Video 2, … Google recommends short motion clips of up to 3 seconds. |
| `resolution` | `360p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `duration` | integer 3–15 | 8 | Output length in seconds. |
| `aspect_ratio` | `16:9` / `9:16` | `16:9` | Output frame shape. |

### Billing

You pay for output seconds: $0.023 at 360p, $0.07 at 720p, $0.105 at 1080p, and $0.21 at 4K.

| Output | 360p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 3s | $0.07 | $0.21 | $0.32 | $0.63 |
| 8s (default) | $0.18 | $0.56 | $0.84 | $1.68 |
| 10s | $0.23 | $0.70 | $1.05 | $2.10 |
| 15s | $0.34 | $1.05 | $1.57 | $3.15 |

Failed runs are not charged.

### Prompting

- Give each reference a role and refer to it by number.

### Limits

- Send at least one reference image or video.

### Also on SandBase

Other Gemini Omni Flash 1.2 endpoints: `google/gemini-omni-flash/1.2/text-to-video`, `google/gemini-omni-flash/1.2/image-to-video`, `google/gemini-omni-flash/1.2/edit`, `google/gemini-omni-flash/1.1/reference-to-video` (previous version).

---
Machine-readable: [`catalog/models/google/gemini-omni-flash/1.2/reference-to-video.json`](../../../../../catalog/models/google/gemini-omni-flash/1.2/reference-to-video.json) · Store page: https://www.sandbase.ai/model/google/gemini-omni-flash/1.2/reference-to-video
