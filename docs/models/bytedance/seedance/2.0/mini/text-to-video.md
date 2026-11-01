# Seedance 2.0 Mini Text to Video

`bytedance/seedance/2.0/mini/text-to-video` · video · Bytedance

Seedance 2.0 Mini is Bytedance's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic motion, lighting, and scene composition.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=4, resolution="480p" | 0.24 * |
| duration=4, resolution="720p" | 0.48 * |
| duration=5, resolution="480p" | 0.3 * |
| duration=5, resolution="720p" | 0.6 * |
| duration=6, resolution="480p" | 0.36 * |
| duration=6, resolution="720p" | 0.72 * |
| duration=7, resolution="480p" | 0.42 * |
| duration=7, resolution="720p" | 0.84 * |
| duration=8, resolution="480p" | 0.48 * |
| duration=8, resolution="720p" | 0.96 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == 'auto' ? Math.round(usage.duration ?? 15.0) : (params.duration ?? 5)) * ((params.resolution ?? '720p') == '480p' ? 0.06 : (params.resolution ?? '720p') == '720p' ? 0.12 : (0 / 0))`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.0/mini/text-to-video", "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.0/mini/text-to-video', {'prompt': 'An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.0/mini/text-to-video", {
  "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.0/mini/text-to-video", sandbase.Params{
	"prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.",
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
| `prompt` | string | yes | The text prompt used to generate the video  |
| `duration` | enum |  | Output duration in seconds (4-15), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 15 seconds and billed on the actual output length. one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | Video resolution - 480p for faster generation, 720p for balance. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Defaults to 16:9. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`; default `"16:9"` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio for the video, including sound effects, ambient sounds, and lip-synced speech. The cost of video generation is the same regardless of whether audio is generated or not. default `true` |

## Details

Seedance 2.0 Mini text-to-video, the lowest-cost Seedance 2.0 tier for drafts and volume. Write the scene, including dialogue and sound, and get back a 4–15 second clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | `16:9` | Output frame shape. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 | 5 | Output length in seconds (4–15), or `auto` to let the model choose. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

You pay for output seconds: $0.06 at 480p, $0.12 at 720p. Audio is included. With `duration: "auto"` the quote assumes 15 seconds and the final charge uses the generated length.

| Output | 480p | 720p |
|---|---|---|
| 4s | $0.24 | $0.48 |
| 5s (default) | $0.30 | $0.60 |
| 10s | $0.60 | $1.20 |
| 15s | $0.90 | $1.80 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order; add the sound last.
- Quote dialogue and name the speaker.
- For several shots, number them and give each a camera direction.

### Limits

- Clips are 4–15 seconds.

### Also on SandBase

Other Seedance 2.0 Mini endpoints and tiers: `bytedance/seedance/2.0/mini/image-to-video`, `bytedance/seedance/2.0/mini/reference-to-video`, `bytedance/seedance/2.5/text-to-video`, `bytedance/seedance/2.0/text-to-video`, `bytedance/seedance/2.0/fast/text-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.0/mini/text-to-video.json`](../../../../../../catalog/models/bytedance/seedance/2.0/mini/text-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.0/mini/text-to-video
