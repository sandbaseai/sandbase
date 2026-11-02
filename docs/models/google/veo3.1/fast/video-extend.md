# Veo 3.1 Fast Video Extend API: pricing, parameters and code examples

`google/veo3.1/fast/video-extend` · video generation model · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.56 to $0.7 per run, depending on parameters · **Modes:** async

Veo3.1 Fast Extend Video by Google - AI-powered video editing and transformation. Apply style transfer, motion control, lip-sync, and visual effects to existing videos with natural language instructions.

## Pricing

- Depends on parameters (`params.duration`, `params.generate_audio`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=7, generate_audio=false, resolution="720p" | 0.56 |
| duration=7, generate_audio=true, resolution="720p" | 0.7 |

Formula: `(params.duration ?? 7) * ((params.resolution ?? "720p") == "720p" ? ((params.generate_audio ?? true) ? 0.10 : 0.08) : (params.resolution ?? "720p") == "1080p" ? ((params.generate_audio ?? true) ? 0.12 : 0.10) : (params.resolution ?? "720p") == "4k" ? ((params.generate_audio ?? true) ? 0.30 : 0.25) : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/veo3.1/fast/video-extend", "generate_audio": false, "prompt": "The lantern keeps swaying as the light fades", "video": "https://static.sandbase.ai/examples/42a4309a-059e-4430-83c2-3c5f78e9156d/input/b83f9c6c-19d6-425a-baff-93c56720073b.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/veo3.1/fast/video-extend', {'generate_audio': False, 'prompt': 'The lantern keeps swaying as the light fades', 'video': 'https://static.sandbase.ai/examples/42a4309a-059e-4430-83c2-3c5f78e9156d/input/b83f9c6c-19d6-425a-baff-93c56720073b.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/veo3.1/fast/video-extend", {
  "generate_audio": false,
  "prompt": "The lantern keeps swaying as the light fades",
  "video": "https://static.sandbase.ai/examples/42a4309a-059e-4430-83c2-3c5f78e9156d/input/b83f9c6c-19d6-425a-baff-93c56720073b.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/veo3.1/fast/video-extend", sandbase.Params{
	"generate_audio": false,
	"prompt": "The lantern keeps swaying as the light fades",
	"video": "https://static.sandbase.ai/examples/42a4309a-059e-4430-83c2-3c5f78e9156d/input/b83f9c6c-19d6-425a-baff-93c56720073b.mp4",
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
| `video` | string | yes | Video to extend: MP4 at 24 fps, 720p (for example a Veo output). Veo appends the requested duration to it.  |
| `prompt` | string | yes | The text prompt describing how the video should be extended  |
| `duration` | integer |  | Length of the generated extension in seconds. one of: `7`; default `7` |
| `resolution` | string |  | Output resolution. Extensions are generated at 720p. one of: `720p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input video. one of: `16:9`, `9:16` |
| `generate_audio` | boolean |  | Generate synchronized audio. Videos without audio are cheaper. default `true` |
| `negative_prompt` | string |  | What to avoid in the video.  |

## Details

Veo 3.1 Fast video extend: continue an existing Veo clip by 7 seconds, keeping its subject, motion, and audio consistent.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 20,000 characters. |
| `video` | video URL, required | — | Clip to continue (a Veo-generated video works best). |
| `duration` | 7 | 7 | Output length in seconds. |
| `resolution` | `720p` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `16:9` / `9:16` | — | Output frame shape. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects; turning it off lowers the rate. |
| `negative_prompt` | string | — | What to avoid. |
| `seed` | integer 0–4294967295 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds, Google's list price. With audio: $0.10 at 720p. Without audio: $0.08 respectively.

| Output | 720p |
|---|---|
| 7s with audio (default) | $0.70 |
| 7s without audio | $0.56 |

Failed runs are not charged.

### Prompting

- Describe what happens next, not what is already in the clip.

### Limits

- Each call adds 7 seconds at 720p; call again on the result to keep extending.
- Use Veo 3.1 for the highest quality.

### Also on SandBase

Other Veo 3.1 Fast endpoints: `google/veo3.1/fast/text-to-video`, `google/veo3.1/fast/image-to-video`, `google/veo3.1/fast/first-last-frame-to-video`, `google/veo3.1/fast/reference-to-video`, `google/veo3.1/text-to-video`, `google/veo3.1/lite/text-to-video`.

---
Machine-readable: [`catalog/models/google/veo3.1/fast/video-extend.json`](../../../../../catalog/models/google/veo3.1/fast/video-extend.json) · Store page: https://www.sandbase.ai/model/google/veo3.1/fast/video-extend
