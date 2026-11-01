# Seedance 2.0 Fast Text to Video

`bytedance/seedance/2.0/fast/text-to-video` · video · Bytedance

ByteDance's most advanced text-to-video model in its fast tier  delivering lower latency and cost without compromising on cinematic output, native audio, multi-shot editing, and director-level camera control for professional-grade video creation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=4, resolution="480p" | 0.4 * |
| duration=4, resolution="720p" | 0.8 * |
| duration=5, resolution="480p" | 0.5 * |
| duration=5, resolution="720p" | 1 * |
| duration=6, resolution="480p" | 0.6 * |
| duration=6, resolution="720p" | 1.2 * |
| duration=7, resolution="480p" | 0.7 * |
| duration=7, resolution="720p" | 1.4 * |
| duration=8, resolution="480p" | 0.8 * |
| duration=8, resolution="720p" | 1.6 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == 'auto' ? Math.round(usage.duration ?? 15.0) : (params.duration ?? 5)) * ((params.resolution ?? '720p') == '480p' ? 0.10 : (params.resolution ?? '720p') == '720p' ? 0.20 : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.0/fast/text-to-video", "aspect_ratio": "16:9", "duration": 5, "prompt": "Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals.", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.0/fast/text-to-video', {'aspect_ratio': '16:9', 'duration': 5, 'prompt': 'Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals.', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.0/fast/text-to-video", {
  "aspect_ratio": "16:9",
  "duration": 5,
  "prompt": "Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals.",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.0/fast/text-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"duration": 5,
	"prompt": "Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals.",
	"resolution": "720p",
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
| `prompt` | string | yes | The text prompt to generate a video from. default `"Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals."` |
| `duration` | enum |  | Output duration in seconds (4-15), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 15 seconds and billed on the actual output length. one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Defaults to 16:9. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Seedance 2.0 Fast text-to-video, the lower-latency, lower-cost Seedance 2.0 tier. Write the scene, including dialogue and sound, and get back a 4–15 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 | 5 | Output length in seconds (4–15), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` | `16:9` | Output frame shape. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

You pay for output seconds: $0.10 at 480p, $0.20 at 720p. Audio is included. With `duration: "auto"` the quote assumes 15 seconds and the final charge uses the generated length.

| Output | 480p | 720p |
|---|---|---|
| 4s | $0.40 | $0.80 |
| 5s (default) | $0.50 | $1.00 |
| 10s | $1.00 | $2.00 |
| 15s | $1.50 | $3.00 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order; add the sound last.
- Quote dialogue and name the speaker.
- For several shots, number them and give each a camera direction.

### Limits

- Clips are 4–15 seconds.

### Also on SandBase

Other Seedance 2.0 Fast endpoints and tiers: `bytedance/seedance/2.0/fast/image-to-video`, `bytedance/seedance/2.0/fast/reference-to-video`, `bytedance/seedance/2.5/text-to-video`, `bytedance/seedance/2.0/text-to-video`, `bytedance/seedance/2.0/mini/text-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.0/fast/text-to-video.json`](../../../../../../catalog/models/bytedance/seedance/2.0/fast/text-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.0/fast/text-to-video
