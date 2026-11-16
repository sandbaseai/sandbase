# Seedance 2.5 Flash Image to Video API: pricing, parameters and code examples

`bytedance/seedance/2.5/flash/image-to-video` · video generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.48 to $1.92 per run, depending on parameters · **Modes:** async

ByteDance's Seedance 2.5 Flash image-to-video model, a faster and lower-cost tier of Seedance 2.5 that animates a still (with an optional end frame) into a native clip up to 30 seconds at 480p or 720p with native audio.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=4, resolution="480p" | 0.48 * |
| duration=4, resolution="720p" | 0.96 * |
| duration=5, resolution="480p" | 0.6 * |
| duration=5, resolution="720p" | 1.2 * |
| duration=6, resolution="480p" | 0.72 * |
| duration=6, resolution="720p" | 1.44 * |
| duration=7, resolution="480p" | 0.84 * |
| duration=7, resolution="720p" | 1.68 * |
| duration=8, resolution="480p" | 0.96 * |
| duration=8, resolution="720p" | 1.92 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == 'auto' ? Math.round(usage.duration ?? 30.0) : (params.duration ?? 5)) * ((params.resolution ?? '720p') == '480p' ? 0.12 : (params.resolution ?? '720p') == '720p' ? 0.24 : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.5/flash/image-to-video", "image": "https://static.sandbase.ai/examples/8f3371d9-f08d-4e79-afc9-d2ca972a7fb9/input/d9f737cf-fd70-4bc1-bc99-d15f0d8dcd9d.png", "prompt": "She slowly turns her head toward the camera and gives a soft smile as warm sunlight drifts across her face. Gentle push-in. Sound: quiet room tone and a soft exhale."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.5/flash/image-to-video', {'image': 'https://static.sandbase.ai/examples/8f3371d9-f08d-4e79-afc9-d2ca972a7fb9/input/d9f737cf-fd70-4bc1-bc99-d15f0d8dcd9d.png', 'prompt': 'She slowly turns her head toward the camera and gives a soft smile as warm sunlight drifts across her face. Gentle push-in. Sound: quiet room tone and a soft exhale.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.5/flash/image-to-video", {
  "image": "https://static.sandbase.ai/examples/8f3371d9-f08d-4e79-afc9-d2ca972a7fb9/input/d9f737cf-fd70-4bc1-bc99-d15f0d8dcd9d.png",
  "prompt": "She slowly turns her head toward the camera and gives a soft smile as warm sunlight drifts across her face. Gentle push-in. Sound: quiet room tone and a soft exhale."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.5/flash/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/8f3371d9-f08d-4e79-afc9-d2ca972a7fb9/input/d9f737cf-fd70-4bc1-bc99-d15f0d8dcd9d.png",
	"prompt": "She slowly turns her head toward the camera and gives a soft smile as warm sunlight drifts across her face. Gentle push-in. Sound: quiet room tone and a soft exhale.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible results. Omit or use -1 for a random seed. range -1–4294967295 |
| `image` | string | yes | The URL of the starting image for video generation.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"Create a 360-degree orbiting camera shot based on this photo."` |
| `duration` | enum |  | Output duration in seconds (4-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `end_image` | string |  | The URL of the ending image for video generation.  |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`; default `"720p"` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio (voice, SFX, BGM) for the video. default `true` |

## Details

Seedance 2.5 Flash image-to-video is the faster, lower-cost tier of Seedance 2.5: `image` becomes the first frame and the prompt directs motion, camera, and sound. Add `end_image` to set the final frame. Output is 480p or 720p.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | `auto` / 4–30 | 5 | Output length in seconds (4–30), or `auto` to let the model choose. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

You pay for output seconds: $0.12 at 480p, $0.24 at 720p. Audio is included. With `duration: "auto"` the quote assumes 30 seconds and the final charge uses the generated length.

| Output | 480p | 720p |
|---|---|---|
| 4s | $0.48 | $0.96 |
| 5s (default) | $0.60 | $1.20 |
| 10s | $1.20 | $2.40 |
| 15s | $1.80 | $3.60 |
| 30s | $3.60 | $7.20 |

Failed runs are not charged.

### Prompting

- Describe what moves and how the camera behaves, not what is already visible.
- With two frames, describe the transition between them.

### Limits

- Clips are 4–30 seconds.
- Output is 480p or 720p. For 1080p or draft mode, use `bytedance/seedance/2.5/image-to-video`.

### Also on SandBase

Other Seedance 2.5 endpoints and tiers: `bytedance/seedance/2.5/flash/text-to-video`, `bytedance/seedance/2.5/flash/reference-to-video`, `bytedance/seedance/2.5/image-to-video`, `bytedance/seedance/2.0/fast/image-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.5/flash/image-to-video.json`](../../../../../../catalog/models/bytedance/seedance/2.5/flash/image-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.5/flash/image-to-video
