# Seedance 2.0 Fast Reference to Video

`bytedance/seedance/2.0/fast/reference-to-video` · video · Bytedance

ByteDance's most advanced reference-to-video model in its fast tier  delivering lower latency and cost without compromising on cinematic output, native audio, multi-shot editing, and director-level camera control for professional-grade video creation.

## Pricing

- Depends on parameters (`params.duration`, `params.has_input_videos`, `params.resolution`, `usage.duration`, `usage.input_video_seconds`).

Formula: see the JSON record.

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seedance/2.0/fast/reference-to-video", "duration": 5, "images": ["https://static.sandbase.ai/examples/79689fb0-69ec-46be-aec5-bd3e552c32e9/input/29d43a66-db4e-46d7-998b-3e10e7b88cd1.jpg"], "prompt": "A hyper-realistic UGC-style medium close-up of a woman in her late 20s standing in her sunlit bedroom in front of a slightly messy bed with white linen sheets, filmed vertically as if she'\''s holding her phone at arm'\''s length for a TikTok or Instagram Reel; she has shoulder-length honey blonde waves, light freckles, natural glowy skin with minimal makeup, wearing a cream ribbed tank top and high-waisted jeans, holding up a compact mirrorless camera on [Image1] in one hand close to the lens so it'\''s clearly visible, her expression bright and genuine — not overly polished — as she says directly to the camera: \"Okay I never do this, but I genuinely have to talk about this camera — I'\''ve had it for three weeks and it has not left my bag, the photos look like film straight out of it, no editing, and it literally fits in my jacket pocket\"; she then turns the camera around to briefly show its compact size against her hand, the background featuring a wooden dresser with scattered jewelry, a small vase of dried flowers, soft morning light pouring through sheer white curtains, a framed poster slightly crooked on the wall, and a houseplant in the corner, all captured with the slightly wider phone-lens distortion, natural skin texture including pores, subtle handheld shake, ambient room tone, and unfiltered warm color grading that feels like an authentic creator review rather than a produced advertisement.", "resolution": "720p"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bytedance/seedance/2.0/fast/reference-to-video', {'duration': 5, 'images': ['https://static.sandbase.ai/examples/79689fb0-69ec-46be-aec5-bd3e552c32e9/input/29d43a66-db4e-46d7-998b-3e10e7b88cd1.jpg'], 'prompt': 'A hyper-realistic UGC-style medium close-up of a woman in her late 20s standing in her sunlit bedroom in front of a slightly messy bed with white linen sheets, filmed vertically as if she\'s holding her phone at arm\'s length for a TikTok or Instagram Reel; she has shoulder-length honey blonde waves, light freckles, natural glowy skin with minimal makeup, wearing a cream ribbed tank top and high-waisted jeans, holding up a compact mirrorless camera on [Image1] in one hand close to the lens so it\'s clearly visible, her expression bright and genuine — not overly polished — as she says directly to the camera: "Okay I never do this, but I genuinely have to talk about this camera — I\'ve had it for three weeks and it has not left my bag, the photos look like film straight out of it, no editing, and it literally fits in my jacket pocket"; she then turns the camera around to briefly show its compact size against her hand, the background featuring a wooden dresser with scattered jewelry, a small vase of dried flowers, soft morning light pouring through sheer white curtains, a framed poster slightly crooked on the wall, and a houseplant in the corner, all captured with the slightly wider phone-lens distortion, natural skin texture including pores, subtle handheld shake, ambient room tone, and unfiltered warm color grading that feels like an authentic creator review rather than a produced advertisement.', 'resolution': '720p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bytedance/seedance/2.0/fast/reference-to-video", {
  "duration": 5,
  "images": [
    "https://static.sandbase.ai/examples/79689fb0-69ec-46be-aec5-bd3e552c32e9/input/29d43a66-db4e-46d7-998b-3e10e7b88cd1.jpg"
  ],
  "prompt": "A hyper-realistic UGC-style medium close-up of a woman in her late 20s standing in her sunlit bedroom in front of a slightly messy bed with white linen sheets, filmed vertically as if she's holding her phone at arm's length for a TikTok or Instagram Reel; she has shoulder-length honey blonde waves, light freckles, natural glowy skin with minimal makeup, wearing a cream ribbed tank top and high-waisted jeans, holding up a compact mirrorless camera on [Image1] in one hand close to the lens so it's clearly visible, her expression bright and genuine — not overly polished — as she says directly to the camera: \"Okay I never do this, but I genuinely have to talk about this camera — I've had it for three weeks and it has not left my bag, the photos look like film straight out of it, no editing, and it literally fits in my jacket pocket\"; she then turns the camera around to briefly show its compact size against her hand, the background featuring a wooden dresser with scattered jewelry, a small vase of dried flowers, soft morning light pouring through sheer white curtains, a framed poster slightly crooked on the wall, and a houseplant in the corner, all captured with the slightly wider phone-lens distortion, natural skin texture including pores, subtle handheld shake, ambient room tone, and unfiltered warm color grading that feels like an authentic creator review rather than a produced advertisement.",
  "resolution": "720p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bytedance/seedance/2.0/fast/reference-to-video", sandbase.Params{
	"duration": 5,
	"images": []any{"https://static.sandbase.ai/examples/79689fb0-69ec-46be-aec5-bd3e552c32e9/input/29d43a66-db4e-46d7-998b-3e10e7b88cd1.jpg"},
	"prompt": "A hyper-realistic UGC-style medium close-up of a woman in her late 20s standing in her sunlit bedroom in front of a slightly messy bed with white linen sheets, filmed vertically as if she's holding her phone at arm's length for a TikTok or Instagram Reel; she has shoulder-length honey blonde waves, light freckles, natural glowy skin with minimal makeup, wearing a cream ribbed tank top and high-waisted jeans, holding up a compact mirrorless camera on [Image1] in one hand close to the lens so it's clearly visible, her expression bright and genuine — not overly polished — as she says directly to the camera: \"Okay I never do this, but I genuinely have to talk about this camera — I've had it for three weeks and it has not left my bag, the photos look like film straight out of it, no editing, and it literally fits in my jacket pocket\"; she then turns the camera around to briefly show its compact size against her hand, the background featuring a wooden dresser with scattered jewelry, a small vase of dried flowers, soft morning light pouring through sheer white curtains, a framed poster slightly crooked on the wall, and a houseplant in the corner, all captured with the slightly wider phone-lens distortion, natural skin texture including pores, subtle handheld shake, ambient room tone, and unfiltered warm color grading that feels like an authentic creator review rather than a produced advertisement.",
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
| `audios` | array |  | The URLs of reference audio files to guide video generation.  |
| `images` | array |  | The URLs of reference images to guide video generation.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"Room is slowly getting filled from empty state to fully organized with furnitures. Camera is fixed timelapse."` |
| `videos` | array |  | The URLs of reference videos to guide video generation. Up to 3 MP4 or MOV files, 2-15 seconds combined duration, under 50 MB total.  |
| `duration` | enum |  | Output duration in seconds (4-15), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 15 seconds and billed on the actual output length. When a reference video is edited or… one of: `auto`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `480p`, `720p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose from the prompt and reference inputs. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Seedance 2.0 Fast reference-to-video: combine reference images, up to 3 reference videos, and reference audio to lock a character, set, motion, or voice in a new clip.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `images` | image URL[] | — | Reference images, Image 1, Image 2, … |
| `videos` | video URL[] (≤3) | — | Reference clips (up to 3), Video 1, Video 2, … |
| `audios` | audio URL[] | — | Reference audio, Audio 1, Audio 2, … |
| `duration` | `auto` / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 / 13 / 14 / 15 | 5 | Output length in seconds (4–15), or `auto` to let the model choose. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` | — | Output frame shape. |
| `resolution` | `480p` / `720p` | `720p` | Sets the per-second rate. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer -1–4294967295 | random | Fix it to compare prompt changes; `-1` is random. |

### Billing

Without reference videos you pay for output seconds: $0.10 at 480p, $0.20 at 720p. With reference videos, the input video seconds (at least 2) are added to the output length and billed at a lower rate: $0.065 at 480p, $0.13 at 720p. With `duration: "auto"` the quote assumes 15 seconds and the final charge uses the generated length.

| Output | 480p | 720p |
|---|---|---|
| 5s, images only | $0.50 | $1.00 |
| 10s, images only | $1.00 | $2.00 |
| 5s + 5s reference video | $0.65 | $1.30 |
| 10s + 10s reference video | $1.30 | $2.60 |

Failed runs are not charged.

### Prompting

- Give each reference a role: “Image 1 is the dancer, Video 1 sets the choreography, Audio 1 is the music”.
- Numbering follows array order within each type.

### Limits

- Reference video seconds count toward billing (minimum 2, up to 15).

### Also on SandBase

Other Seedance 2.0 Fast endpoints and tiers: `bytedance/seedance/2.0/fast/text-to-video`, `bytedance/seedance/2.0/fast/image-to-video`, `bytedance/seedance/2.5/reference-to-video`, `bytedance/seedance/2.0/reference-to-video`, `bytedance/seedance/2.0/mini/reference-to-video`.

---
Machine-readable: [`catalog/models/bytedance/seedance/2.0/fast/reference-to-video.json`](../../../../../../catalog/models/bytedance/seedance/2.0/fast/reference-to-video.json) · Store page: https://www.sandbase.ai/model/bytedance/seedance/2.0/fast/reference-to-video
