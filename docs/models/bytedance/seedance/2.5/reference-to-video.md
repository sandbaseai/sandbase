# Seedance 2.5 Reference to Video

`bytedance/seedance/2.5/reference-to-video` · video · Bytedance

ByteDance's next-generation reference-to-video model, generating video from multimodal references (images, videos, audio) and locking a character, set, and palette across a full take up to 30 seconds for production-grade consistency.

## Pricing

- Depends on parameters (`params.draft`, `params.draft_id`, `params.duration`, `params.has_input_videos`, `params.resolution`, `params.task_type`, `usage.duration`, `usage.input_video_seconds`).

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.5/reference-to-video", "prompt": "Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.5/reference-to-video', {'prompt': 'Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.5/reference-to-video", {
  "prompt": "Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.5/reference-to-video", sandbase.Params{
	"prompt": "Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people.",
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
| `audios` | array |  | The URLs of reference audio files to guide video generation.  |
| `images` | array |  | The URLs of reference images to guide video generation. Refer to them in the prompt as @Image1, @Image2, etc.  |
| `prompt` | string |  | The text prompt to generate a video from. default `"Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people."` |
| `videos` | array |  | The URLs of reference videos to guide video generation. Up to 10 MP4 or MOV files; combined duration must not exceed 30 seconds.  |
| `draft_id` | string |  | Draft mode step 2: the `outputs[0].draft_id` of a succeeded draft from this same model (created with `draft: true` in the last 7 days). Renders the same shot at 1080p, billed at the 1080p rate for the actual output…  |
| `duration` | enum |  | Output duration in seconds (4-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. When a reference video is edited or… one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `task_type` | string |  | `reference` generates a new video from the references, `edit` edits a reference video (replace subjects, add or remove objects, repaint), `extend` extends a reference video forward or backward, `auto` (or omitted) lets… one of: `auto`, `reference`, `edit`, `extend` |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose from the prompt and reference inputs. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `adaptive` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio (voice, SFX, BGM) for the video. default `true` |

## Details

Seedance 2.5 reference-to-video: combine reference images, up to 10 reference videos, and reference audio to lock a character, set, motion, or voice in a new clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `images` | image URL[] | — | Reference images, Image 1, Image 2, … |
| `videos` | video URL[] (≤10) | — | Reference clips (up to 10), Video 1, Video 2, … |
| `audios` | audio URL[] | — | Reference audio, Audio 1, Audio 2, … |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 / 16 / 17 / 18 / 19 / 20 / 21 / 22 / 23 / 24 / 25 / 26 / 27 / 28 / 29 / 30 | 5 | Output length in seconds (4–30), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | — | Output frame shape. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

Without reference videos you pay for output seconds: $0.18 at 480p, $0.36 at 720p, $0.90 at 1080p. With reference videos, the input video seconds (at least 2) are added to the output length and billed at a lower rate: $0.11 at 480p, $0.22 at 720p, $0.55 at 1080p. With `duration: "auto"` the quote assumes 30 seconds and the final charge uses the generated length.

| Output | 480p | 720p | 1080p |
|---|---|---|---|
| 5s, images only | $0.90 | $1.80 | $4.50 |
| 10s, images only | $1.80 | $3.60 | $9.00 |
| 5s + 5s reference video | $1.10 | $2.20 | $5.50 |
| 10s + 10s reference video | $2.20 | $4.40 | $11.00 |

Failed runs are not charged.

### Prompting

- Give each reference a role: “Image 1 is the dancer, Video 1 sets the choreography, Audio 1 is the music”.
- Numbering follows array order within each type.

### Limits

- Reference video seconds count toward billing (minimum 2, up to 30).

### Task types

`task_type` selects the reference sub-task: `reference` (new video guided by the references), `edit` (edit a reference video), `extend` (extend a reference video forward or backward), or `auto` (default, inferred from the prompt). `edit` and `extend` need at least one video and use the source clip's aspect ratio; `edit` also follows the source clip's length and is billed on the actual output length. If the prompt contradicts an explicit `task_type`, the task fails.

```json
{"prompt": "Replace the man in @Video1 with the character in @Image1.", "images": ["https://example.com/character.png"], "videos": ["https://example.com/source.mp4"], "task_type": "edit"}
```

### Draft mode

Draft mode is two calls to this same model:

1. **Draft**: add `"draft": true`. The output is a 480p preview billed at the 480p rate, and `outputs[0].draft_id` identifies it.
2. **Final**: send `{"draft_id": "<outputs[0].draft_id>"}` (optionally `watermark`). The same shot is rendered at 1080p and billed at the 1080p output rate for the actual output length.

The final reuses the draft's prompt, media, duration, aspect ratio, seed and audio setting; those fields are ignored when `draft_id` is set. A draft can be finalized within 7 days, only with the model that created it.

```json
{"prompt": "@Image1 walks along the shoreline in the style of @Video1.", "images": ["https://example.com/character.png"], "videos": ["https://example.com/style.mp4"], "draft": true}
```

```json
{"draft_id": "<outputs[0].draft_id from the draft>"}
```

### Also on SandBase

Other Seedance 2.5 endpoints and tiers: `bytedance/seedance/2.5/text-to-video`, `bytedance/seedance/2.5/image-to-video`, `bytedance/seedance/2.0/reference-to-video`, `bytedance/seedance/2.0/fast/reference-to-video`, `bytedance/seedance/2.0/mini/reference-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.5/reference-to-video.json`](../../../../../catalog/models/bytedance/seedance/2.5/reference-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.5/reference-to-video
