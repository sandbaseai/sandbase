# Seedance 2.0 Mini Reference to Video

`bytedance/seedance/2.0/mini/reference-to-video` · video · Bytedance

Seedance 2.0 Mini by Bytedance - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.has_input_videos`, `params.resolution`, `usage.duration`, `usage.input_video_seconds`).

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.0/mini/reference-to-video", "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.0/mini/reference-to-video', {'prompt': 'An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.0/mini/reference-to-video", {
  "prompt": "An octopus finds a football in the ocean and excitedly calls its octopus friends to come and play. Cut scene to an octopus football game under the sea."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.0/mini/reference-to-video", sandbase.Params{
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
| `audios` | array |  | Reference audio URLs (voice or music) for the generated video.  |
| `images` | array |  | Reference images to guide video generation. Refer to them in the prompt as @Image1, @Image2, etc. Supported formats: JPEG, PNG, WebP. Max 30 MB per image. Up to 9 images. Total files across all modalities must not…  |
| `prompt` | string | yes | The text prompt used to generate the video.  |
| `videos` | array |  | Reference videos to guide video generation. Refer to them in the prompt as @Video1, @Video2, etc. Supported formats: MP4, MOV. Up to 3 videos, combined duration must be between 2 and 15 seconds, total size under 50 MB.…  |
| `duration` | enum |  | Output duration in seconds (4-15), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 15 seconds and billed on the actual output length. When a reference video is edited or… one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | Video resolution - 480p for faster generation, 720p for balance. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose from the prompt and reference inputs. one of: `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio for the video, including sound effects, ambient sounds, and lip-synced speech. The cost of video generation is the same regardless of whether audio is generated or not. default `true` |

## Details

Seedance 2.0 Mini reference-to-video: combine reference images, up to 3 reference videos, and reference audio to lock a character, set, motion, or voice in a new clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `images` | image URL[] | — | Reference images, Image 1, Image 2, … |
| `videos` | video URL[] | — | Reference clips (up to 3), Video 1, Video 2, … |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 | 5 | Output length in seconds (4–15), or `auto` to let the model choose. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `aspect_ratio` | `21:9` / `16:9` / `3:2` / `4:3` / `5:4` / `1:1` / `4:5` / `3:4` / `2:3` / `9:16` | — | Output frame shape. |
| `audios` | audio URL[] | — | Reference audio, Audio 1, Audio 2, … |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

Without reference videos you pay for output seconds: $0.06 at 480p, $0.12 at 720p. With reference videos, the input video seconds (at least 2) are added to the output length and billed at a lower rate: $0.0375 at 480p, $0.075 at 720p. With `duration: "auto"` the quote assumes 15 seconds and the final charge uses the generated length.

| Output | 480p | 720p |
|---|---|---|
| 5s, images only | $0.30 | $0.60 |
| 10s, images only | $0.60 | $1.20 |
| 5s + 5s reference video | $0.375 | $0.75 |
| 10s + 10s reference video | $0.75 | $1.50 |

Failed runs are not charged.

### Prompting

- Give each reference a role: “Image 1 is the dancer, Video 1 sets the choreography, Audio 1 is the music”.
- Numbering follows array order within each type.

### Limits

- Reference video seconds count toward billing (minimum 2, up to 15).

### Also on SandBase

Other Seedance 2.0 Mini endpoints and tiers: `bytedance/seedance/2.0/mini/text-to-video`, `bytedance/seedance/2.0/mini/image-to-video`, `bytedance/seedance/2.5/reference-to-video`, `bytedance/seedance/2.0/reference-to-video`, `bytedance/seedance/2.0/fast/reference-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.0/mini/reference-to-video.json`](../../../../../../catalog/models/bytedance/seedance/2.0/mini/reference-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.0/mini/reference-to-video
