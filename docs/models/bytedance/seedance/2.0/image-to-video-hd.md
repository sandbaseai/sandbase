# Seedance 2.0 Image to Video HD API: pricing, parameters and code examples

`bytedance/seedance/2.0/image-to-video-hd` · video generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2742 to $5.999288 per run, depending on parameters · **Modes:** async

ByteDance's most advanced image-to-video model  transforming still images into cinematic video with native audio, multi-shot editing, and director-level camera control for professional-grade video creation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=4, resolution="480p" | 0.2742 * |
| duration=4, resolution="720p" | 0.589672 * |
| duration=4, resolution="1080p" | 1.47098 * |
| duration=4, resolution="4k" | 2.999644 * |
| duration=5, resolution="480p" | 0.34275 * |
| duration=5, resolution="720p" | 0.73709 * |
| duration=5, resolution="1080p" | 1.838725 * |
| duration=5, resolution="4k" | 3.749555 * |
| duration=6, resolution="480p" | 0.4113 * |
| duration=6, resolution="720p" | 0.884508 * |
| duration=6, resolution="1080p" | 2.20647 * |
| duration=6, resolution="4k" | 4.499466 * |
| duration=7, resolution="480p" | 0.47985 * |
| duration=7, resolution="720p" | 1.031926 * |
| duration=7, resolution="1080p" | 2.574215 * |
| duration=7, resolution="4k" | 5.249377 * |
| duration=8, resolution="480p" | 0.5484 * |
| duration=8, resolution="720p" | 1.179344 * |
| duration=8, resolution="1080p" | 2.94196 * |
| duration=8, resolution="4k" | 5.999288 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == 'auto' ? Math.round(usage.duration ?? 15.0) : (params.duration ?? 5)) * ((params.resolution ?? '720p') == '4k' ? 0.749911 : (params.resolution ?? '720p') == '1080p' ? 0.367745 : (params.resolution ?? '720p') == '720p' ? 0.147418 : 0.06855)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.0/image-to-video-hd", "prompt": "Create a 360-degree orbiting camera shot based on this photo.", "image": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f8fc1008f23a4908b7c897e8b7eb87df~tplv-goo7wpa0wc-image.image"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.0/image-to-video-hd', {'prompt': 'Create a 360-degree orbiting camera shot based on this photo.', 'image': 'https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f8fc1008f23a4908b7c897e8b7eb87df~tplv-goo7wpa0wc-image.image'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.0/image-to-video-hd", {
  "prompt": "Create a 360-degree orbiting camera shot based on this photo.",
  "image": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f8fc1008f23a4908b7c897e8b7eb87df~tplv-goo7wpa0wc-image.image"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.0/image-to-video-hd", sandbase.Params{
	"prompt": "Create a 360-degree orbiting camera shot based on this photo.",
	"image": "https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f8fc1008f23a4908b7c897e8b7eb87df~tplv-goo7wpa0wc-image.image",
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
| `duration` | enum |  | Output duration in seconds (4-15), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 15 seconds and billed on the actual output length. one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `end_image` | string |  | The URL of the ending image for video generation.  |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input image. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio (voice, SFX, BGM) for the video. default `true` |

## Details

Seedance 2.0 image-to-video: `image` becomes the first frame and the prompt directs motion, camera, and sound. Add `end_image` to set the final frame.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 | 5 | Output length in seconds (4–15), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | — | Output frame shape. |
| `resolution` | `480p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

You pay for output seconds: $0.12 at 480p, $0.24 at 720p, $0.60 at 1080p, $1.20 at 4k. Audio is included. With `duration: "auto"` the quote assumes 15 seconds and the final charge uses the generated length.

| Output | 480p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 4s | $0.48 | $0.96 | $2.40 | $4.80 |
| 5s (default) | $0.60 | $1.20 | $3.00 | $6.00 |
| 10s | $1.20 | $2.40 | $6.00 | $12.00 |
| 15s | $1.80 | $3.60 | $9.00 | $18.00 |

Failed runs are not charged.

### Prompting

- Describe what moves and how the camera behaves, not what is already visible.
- With two frames, describe the transition between them.

### Limits

- Clips are 4–15 seconds.

### Also on SandBase

Other Seedance 2.0 endpoints and tiers: `bytedance/seedance/2.0/text-to-video`, `bytedance/seedance/2.0/reference-to-video`, `bytedance/seedance/2.5/image-to-video`, `bytedance/seedance/2.0/fast/image-to-video`, `bytedance/seedance/2.0/mini/image-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.0/image-to-video-hd.json`](../../../../../catalog/models/bytedance/seedance/2.0/image-to-video-hd.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.0/image-to-video-hd
