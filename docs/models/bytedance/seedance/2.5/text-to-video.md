# Seedance 2.5 Text to Video API: pricing, parameters and code examples

`bytedance/seedance/2.5/text-to-video` · video generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.72 to $7.2 per run, depending on parameters · **Modes:** async

ByteDance's next-generation text-to-video model, generating native single-shot clips up to 30 seconds at 720p with coherent motion, native audio, and director-level camera control for professional-grade video creation.

## Pricing

- Depends on parameters (`params.draft`, `params.draft_id`, `params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| draft=false, duration=4, resolution="480p" | 0.72 * |
| draft=false, duration=4, resolution="720p" | 1.44 * |
| draft=false, duration=4, resolution="1080p" | 3.6 * |
| draft=false, duration=5, resolution="480p" | 0.9 * |
| draft=false, duration=5, resolution="720p" | 1.8 * |
| draft=false, duration=5, resolution="1080p" | 4.5 * |
| draft=false, duration=6, resolution="480p" | 1.08 * |
| draft=false, duration=6, resolution="720p" | 2.16 * |
| draft=false, duration=6, resolution="1080p" | 5.4 * |
| draft=false, duration=7, resolution="480p" | 1.26 * |
| draft=false, duration=7, resolution="720p" | 2.52 * |
| draft=false, duration=7, resolution="1080p" | 6.3 * |
| draft=false, duration=8, resolution="480p" | 1.44 * |
| draft=false, duration=8, resolution="720p" | 2.88 * |
| draft=false, duration=8, resolution="1080p" | 7.2 * |
| draft=true, duration=4, resolution="480p" | 0.72 * |
| draft=true, duration=4, resolution="720p" | 0.72 * |
| draft=true, duration=4, resolution="1080p" | 0.72 * |
| draft=true, duration=5, resolution="480p" | 0.9 * |
| draft=true, duration=5, resolution="720p" | 0.9 * |
| draft=true, duration=5, resolution="1080p" | 0.9 * |
| draft=true, duration=6, resolution="480p" | 1.08 * |
| draft=true, duration=6, resolution="720p" | 1.08 * |
| draft=true, duration=6, resolution="1080p" | 1.08 * |

\* estimate: assumes output duration equals requested duration.

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.5/text-to-video", "aspect_ratio": "16:9", "duration": 5, "prompt": "A bright modern kitchen with one wooden dining chair standing in the middle of the tiled floor. A round black robot vacuum glides across the floor, reaches the chair, steers around its legs, passes briefly behind them and reappears on the other side, continuing in the same direction. Static wide camera, no people, realistic lighting.", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.5/text-to-video', {'aspect_ratio': '16:9', 'duration': 5, 'prompt': 'A bright modern kitchen with one wooden dining chair standing in the middle of the tiled floor. A round black robot vacuum glides across the floor, reaches the chair, steers around its legs, passes briefly behind them and reappears on the other side, continuing in the same direction. Static wide camera, no people, realistic lighting.', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.5/text-to-video", {
  "aspect_ratio": "16:9",
  "duration": 5,
  "prompt": "A bright modern kitchen with one wooden dining chair standing in the middle of the tiled floor. A round black robot vacuum glides across the floor, reaches the chair, steers around its legs, passes briefly behind them and reappears on the other side, continuing in the same direction. Static wide camera, no people, realistic lighting.",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.5/text-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"duration": 5,
	"prompt": "A bright modern kitchen with one wooden dining chair standing in the middle of the tiled floor. A round black robot vacuum glides across the floor, reaches the chair, steers around its legs, passes briefly behind them and reappears on the other side, continuing in the same direction. Static wide camera, no people, realistic lighting.",
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
| `draft` | boolean |  | Draft mode step 1: render a fast, low-cost 480p draft (overrides `resolution`, billed at the 480p rate). Pass the result's `outputs[0].draft_id` back as `draft_id` within 7 days to render the same shot at 1080p. default `false` |
| `prompt` | string |  | The text prompt to generate a video from. default `"Photorealistic style: Under a clear blue sky, a vast expanse of white daisy fields stretches out. The camera gradually zooms in and finally fixates on a close-up of a single daisy, with several glistening dewdrops resting on its petals."` |
| `draft_id` | string |  | Draft mode step 2: the `outputs[0].draft_id` of a succeeded draft from this same model (created with `draft: true` in the last 7 days). Renders the same shot at 1080p, billed at the 1080p rate for the actual output…  |
| `duration` | enum |  | Output duration in seconds (4-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`, `1080p`; default `"720p"` |
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
Machine-readable: [`catalog/models/bytedance/seedance/2.5/text-to-video.json`](../../../../../catalog/models/bytedance/seedance/2.5/text-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.5/text-to-video
