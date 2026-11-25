# Seedance 2.5 Text to Video HD API: pricing, parameters and code examples

`bytedance/seedance/2.5/text-to-video-hd` · video generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.398188 to $7.153 per run, depending on parameters · **Modes:** async

ByteDance's next-generation text-to-video model, generating native single-shot clips up to 30 seconds at 720p with coherent motion, native audio, and director-level camera control for professional-grade video creation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=4, resolution="480p" | 0.398188 * |
| duration=4, resolution="720p" | 0.897328 * |
| duration=4, resolution="1080p" | 2.220892 * |
| duration=4, resolution="4k" | 3.5765 * |
| duration=5, resolution="480p" | 0.497735 * |
| duration=5, resolution="720p" | 1.12166 * |
| duration=5, resolution="1080p" | 2.776115 * |
| duration=5, resolution="4k" | 4.470625 * |
| duration=6, resolution="480p" | 0.597282 * |
| duration=6, resolution="720p" | 1.345992 * |
| duration=6, resolution="1080p" | 3.331338 * |
| duration=6, resolution="4k" | 5.36475 * |
| duration=7, resolution="480p" | 0.696829 * |
| duration=7, resolution="720p" | 1.570324 * |
| duration=7, resolution="1080p" | 3.886561 * |
| duration=7, resolution="4k" | 6.258875 * |
| duration=8, resolution="480p" | 0.796376 * |
| duration=8, resolution="720p" | 1.794656 * |
| duration=8, resolution="1080p" | 4.441784 * |
| duration=8, resolution="4k" | 7.153 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == 'auto' ? Math.round(usage.duration ?? 15.0) : (params.duration ?? 5)) * ((params.resolution ?? '720p') == '4k' ? 0.894125 : (params.resolution ?? '720p') == '1080p' ? 0.555223 : (params.resolution ?? '720p') == '720p' ? 0.224332 : 0.099547)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.5/text-to-video-hd"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.5/text-to-video-hd', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.5/text-to-video-hd", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.5/text-to-video-hd", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducible results. Omit or use -1 for a random seed. range -1–4294967295 |
| `prompt` | string |  | The text prompt to generate a video from. default `"Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals."` |
| `duration` | enum |  | Output duration in seconds (4-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Defaults to 16:9. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; default `"16:9"` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio (voice, SFX, BGM) for the video. default `true` |

## Details

Seedance 2.5 text-to-video, ByteDance's newest video model: coherent single-shot clips up to 30 seconds with native audio and director-level camera control. Write the scene, including dialogue and sound, and get back a 4–30 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 / 16 / 17 / 18 / 19 / 20 / 21 / 22 / 23 / 24 / 25 / 26 / 27 / 28 / 29 / 30 | 5 | Output length in seconds (4–30), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | `16:9` | Output frame shape. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

You pay for output seconds: $0.18 at 480p, $0.36 at 720p, $0.90 at 1080p. Audio is included. With `duration: "auto"` the quote assumes 30 seconds and the final charge uses the generated length.

| Output | 480p | 720p | 1080p |
|---|---|---|---|
| 4s | $0.72 | $1.44 | $3.60 |
| 5s (default) | $0.90 | $1.80 | $4.50 |
| 10s | $1.80 | $3.60 | $9.00 |
| 15s | $2.70 | $5.40 | $13.50 |
| 30s | $5.40 | $10.80 | $27.00 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order; add the sound last.
- Quote dialogue and name the speaker.
- For several shots, number them and give each a camera direction.

### Limits

- Clips are 4–30 seconds.

### Draft mode

Draft mode is two calls to this same model:

1. **Draft**: add `"draft": true`. The output is a 480p preview billed at the 480p rate, and `outputs[0].draft_id` identifies it.
2. **Final**: send `{"draft_id": "<outputs[0].draft_id>"}` (optionally `watermark`). The same shot is rendered at 1080p and billed at the 1080p output rate for the actual output length.

The final reuses the draft's prompt, media, duration, aspect ratio, seed and audio setting; those fields are ignored when `draft_id` is set. A draft can be finalized within 7 days, only with the model that created it.

```json
{"prompt": "A red toy sailboat drifts slowly from left to right across calm blue water. Fixed camera.", "duration": 4, "aspect_ratio": "16:9", "generate_audio": false, "draft": true}
```

```json
{"draft_id": "<outputs[0].draft_id from the draft>"}
```

### Also on SandBase

Other Seedance 2.5 endpoints and tiers: `bytedance/seedance/2.5/image-to-video`, `bytedance/seedance/2.5/reference-to-video`, `bytedance/seedance/2.0/text-to-video`, `bytedance/seedance/2.0/fast/text-to-video`, `bytedance/seedance/2.0/mini/text-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.5/text-to-video-hd.json`](../../../../../catalog/models/bytedance/seedance/2.5/text-to-video-hd.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.5/text-to-video-hd
