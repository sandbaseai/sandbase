# Seedance 2.0 Reference to Video

`bytedance/seedance/2.0/reference-to-video` · video · Bytedance

ByteDance's most advanced reference-to-video model  generating cinematic video guided by reference content, with native audio, multi-shot editing, and director-level camera control for professional-grade video creation.

## Pricing

- Depends on parameters (`params.duration`, `params.has_input_videos`, `params.resolution`, `usage.duration`, `usage.input_video_seconds`).

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.0/reference-to-video", "prompt": "Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.0/reference-to-video', {'prompt': 'Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.0/reference-to-video", {
  "prompt": "Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.0/reference-to-video", sandbase.Params{
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
| `audios` | array |  | The URLs of reference audio files to guide video generation.  |
| `images` | array |  | The URLs of reference images to guide video generation.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people."` |
| `videos` | array |  | The URLs of reference videos to guide video generation. Up to 3 MP4 or MOV files, 2-15 seconds combined duration, under 50 MB total.  |
| `duration` | enum |  | Output duration in seconds (4-15), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 15 seconds and billed on the actual output length. When a reference video is edited or… one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose from the prompt and reference inputs. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Seedance 2.0 reference-to-video: combine reference images, up to 3 reference videos, and reference audio to lock a character, set, motion, or voice in a new clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `images` | image URL[] | — | Reference images, Image 1, Image 2, … |
| `videos` | video URL[] (≤3) | — | Reference clips (up to 3), Video 1, Video 2, … |
| `audios` | audio URL[] | — | Reference audio, Audio 1, Audio 2, … |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 | 5 | Output length in seconds (4–15), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | — | Output frame shape. |
| `resolution` | `480p` / `720p` / `1080p` / `4k` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

Without reference videos you pay for output seconds: $0.12 at 480p, $0.24 at 720p, $0.60 at 1080p, $1.20 at 4k. With reference videos, the input video seconds (at least 2) are added to the output length and billed at a lower rate: $0.075 at 480p, $0.15 at 720p, $0.375 at 1080p, $0.75 at 4k. With `duration: "auto"` the quote assumes 15 seconds and the final charge uses the generated length.

| Output | 480p | 720p | 1080p | 4k |
|---|---|---|---|---|
| 5s, images only | $0.60 | $1.20 | $3.00 | $6.00 |
| 10s, images only | $1.20 | $2.40 | $6.00 | $12.00 |
| 5s + 5s reference video | $0.75 | $1.50 | $3.75 | $7.50 |
| 10s + 10s reference video | $1.50 | $3.00 | $7.50 | $15.00 |

Failed runs are not charged.

### Prompting

- Give each reference a role: “Image 1 is the dancer, Video 1 sets the choreography, Audio 1 is the music”.
- Numbering follows array order within each type.

### Limits

- Reference video seconds count toward billing (minimum 2, up to 15).

### Also on SandBase

Other Seedance 2.0 endpoints and tiers: `bytedance/seedance/2.0/text-to-video`, `bytedance/seedance/2.0/image-to-video`, `bytedance/seedance/2.5/reference-to-video`, `bytedance/seedance/2.0/fast/reference-to-video`, `bytedance/seedance/2.0/mini/reference-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.0/reference-to-video.json`](../../../../../catalog/models/bytedance/seedance/2.0/reference-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.0/reference-to-video
