# Seedance 2.5 Flash Text to Video API: pricing, parameters and code examples

`bytedance/seedance/2.5/flash/text-to-video` · video generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.48 to $1.92 per run, depending on parameters · **Modes:** async

ByteDance's Seedance 2.5 Flash text-to-video model, a faster and lower-cost tier of Seedance 2.5 that generates native single-shot clips up to 30 seconds at 480p or 720p with coherent motion, native audio, and camera control.

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
  -d '{"model": "bytedance/seedance/2.5/flash/text-to-video", "aspect_ratio": "16:9", "prompt": "Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.5/flash/text-to-video', {'aspect_ratio': '16:9', 'prompt': 'Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.5/flash/text-to-video", {
  "aspect_ratio": "16:9",
  "prompt": "Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.5/flash/text-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"prompt": "Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals.",
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
| `duration` | enum |  | Output duration in seconds (4-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Defaults to 16:9. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; default `"16:9"` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio (voice, SFX, BGM) for the video. default `true` |

## Details

Seedance 2.5 Flash text-to-video is the faster, lower-cost tier of Seedance 2.5: coherent single-shot clips up to 30 seconds with native audio and camera control, at 480p or 720p. Write the scene, including dialogue and sound, and get back a 4–30 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `duration` | `auto` / 4–30 | 5 | Output length in seconds (4–30), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | `16:9` | Output frame shape. |
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

- Describe subject, action, camera move, and light in order; add the sound last.
- Quote dialogue and name the speaker.
- For several shots, number them and give each a camera direction.

### Limits

- Clips are 4–30 seconds.
- Output is 480p or 720p. For 1080p or draft mode, use `bytedance/seedance/2.5/text-to-video`.

### Also on SandBase

Other Seedance 2.5 endpoints and tiers: `bytedance/seedance/2.5/flash/image-to-video`, `bytedance/seedance/2.5/flash/reference-to-video`, `bytedance/seedance/2.5/text-to-video`, `bytedance/seedance/2.0/fast/text-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.5/flash/text-to-video.json`](../../../../../../catalog/models/bytedance/seedance/2.5/flash/text-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.5/flash/text-to-video
