# Seedance 2.5 Flash Reference to Video API: pricing, parameters and code examples

`bytedance/seedance/2.5/flash/reference-to-video` · video generation model · Bytedance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $1.2 per call · **Modes:** async

ByteDance's Seedance 2.5 Flash reference-to-video model, a faster and lower-cost tier of Seedance 2.5 that generates up to 30 seconds of 480p or 720p video from reference images, videos, and audio, and can edit or extend a reference clip.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `params.task_type`, `params.videos`, `usage.duration`).

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.5/flash/reference-to-video", "aspect_ratio": "16:9", "images": ["https://static.sandbase.ai/examples/e54610d1-6a03-417d-9966-e9af7d62a688/input/b5c0e60c-f747-4424-b5f9-40ec17f196e8.jpg"], "prompt": "Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people.", "videos": ["https://static.sandbase.ai/examples/e54610d1-6a03-417d-9966-e9af7d62a688/input/f6f98664-8888-482b-a862-cf4a80a6b0e8.mp4"]}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.5/flash/reference-to-video', {'aspect_ratio': '16:9', 'images': ['https://static.sandbase.ai/examples/e54610d1-6a03-417d-9966-e9af7d62a688/input/b5c0e60c-f747-4424-b5f9-40ec17f196e8.jpg'], 'prompt': 'Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people.', 'videos': ['https://static.sandbase.ai/examples/e54610d1-6a03-417d-9966-e9af7d62a688/input/f6f98664-8888-482b-a862-cf4a80a6b0e8.mp4']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.5/flash/reference-to-video", {
  "aspect_ratio": "16:9",
  "images": [
    "https://static.sandbase.ai/examples/e54610d1-6a03-417d-9966-e9af7d62a688/input/b5c0e60c-f747-4424-b5f9-40ec17f196e8.jpg"
  ],
  "prompt": "Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people.",
  "videos": [
    "https://static.sandbase.ai/examples/e54610d1-6a03-417d-9966-e9af7d62a688/input/f6f98664-8888-482b-a862-cf4a80a6b0e8.mp4"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.5/flash/reference-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"images": []any{"https://static.sandbase.ai/examples/e54610d1-6a03-417d-9966-e9af7d62a688/input/b5c0e60c-f747-4424-b5f9-40ec17f196e8.jpg"},
	"prompt": "Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people.",
	"videos": []any{"https://static.sandbase.ai/examples/e54610d1-6a03-417d-9966-e9af7d62a688/input/f6f98664-8888-482b-a862-cf4a80a6b0e8.mp4"},
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
| `audios` | array |  | The URLs of reference audio files to guide video generation. Up to 5 files; combined duration must not exceed 30 seconds.  |
| `images` | array |  | The URLs of reference images to guide video generation. Up to 10 images. Refer to them in the prompt as @Image1, @Image2, etc.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"Use Image1 as the visual reference and Video1 as the motion reference. Create a peaceful cinematic shoreline scene with rolling ocean waves at golden hour, soft foam, natural water movement, and no people."` |
| `videos` | array |  | The URLs of reference videos to guide video generation. Up to 5 MP4 or MOV files; combined duration must not exceed 30 seconds.  |
| `duration` | enum |  | Output duration in seconds (4-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. When a reference video is edited or… one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `task_type` | string |  | `reference` generates a new video from the references, `edit` edits a reference video (replace subjects, add or remove objects, repaint), `extend` extends a reference video forward or backward, `auto` (or omitted) lets… one of: `auto`, `reference`, `edit`, `extend` |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose from the prompt and reference inputs. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `adaptive` |
| `generate_audio` | boolean |  | Whether to generate synchronized audio (voice, SFX, BGM) for the video. default `true` |

## Details

Seedance 2.5 Flash reference-to-video is the faster, lower-cost tier of Seedance 2.5: combine up to 10 reference images, 5 reference videos, and 5 reference audio clips to lock a character, set, motion, or voice in a new 480p or 720p clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `images` | image URL[] (≤10) | — | Reference images, Image 1, Image 2, … |
| `videos` | video URL[] (≤5) | — | Reference clips, Video 1, Video 2, … Combined length up to 30 seconds. |
| `audios` | audio URL[] (≤5) | — | Reference audio, Audio 1, Audio 2, … Combined length up to 30 seconds. |
| `task_type` | `auto` / `reference` / `edit` / `extend` | `auto` | Reference sub-task; see below. |
| `duration` | `auto` / 4–30 | 5 | Output length in seconds (4–30), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` / `adaptive` | — | Output frame shape. Omit to let the model choose. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

Without reference videos you pay for output seconds: $0.12 at 480p, $0.24 at 720p. With reference videos, the input video seconds (at least 2) are added to the output length and billed at a lower rate: $0.075 at 480p, $0.15 at 720p. With `duration: "auto"` the quote assumes 30 seconds and the final charge uses the generated length.

| Output | 480p | 720p |
|---|---|---|
| 5s, images only | $0.60 | $1.20 |
| 10s, images only | $1.20 | $2.40 |
| 5s + 5s reference video | $0.75 | $1.50 |
| 10s + 10s reference video | $1.50 | $3.00 |

Failed runs are not charged.

### Prompting

- Give each reference a role: “Image 1 is the dancer, Video 1 sets the choreography, Audio 1 is the music”.
- Numbering follows array order within each type.

### Limits

- Up to 10 images, 5 videos, and 5 audio clips per request.
- Reference video seconds count toward billing (minimum 2, up to 30).
- Output is 480p or 720p. For 1080p, draft mode, or more references, use `bytedance/seedance/2.5/reference-to-video`.

### Task types

`task_type` selects the reference sub-task: `reference` (new video guided by the references), `edit` (edit a reference video), `extend` (extend a reference video forward or backward), or `auto` (default, inferred from the prompt). `edit` and `extend` need at least one video and use the source clip's aspect ratio; `edit` also follows the source clip's length and is billed on the actual output length. If the prompt contradicts an explicit `task_type`, the task fails.

```json
{"prompt": "Replace the man in @Video1 with the character in @Image1.", "images": ["https://example.com/character.png"], "videos": ["https://example.com/source.mp4"], "task_type": "edit"}
```

### Also on SandBase

Other Seedance 2.5 endpoints and tiers: `bytedance/seedance/2.5/flash/text-to-video`, `bytedance/seedance/2.5/flash/image-to-video`, `bytedance/seedance/2.5/reference-to-video`, `bytedance/seedance/2.0/fast/reference-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.5/flash/reference-to-video.json`](../../../../../../catalog/models/bytedance/seedance/2.5/flash/reference-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.5/flash/reference-to-video
