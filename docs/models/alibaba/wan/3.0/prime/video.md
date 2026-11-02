# Wan 3.0 Prime Video API: pricing, parameters and code examples

`alibaba/wan/3.0/prime/video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.7 per call · **Modes:** async

Alibaba Wan 3.0 Prime Video generates videos up to 30 seconds with native audio from text, a first/last frame, or reference images, videos, and audio.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `params.videos`, `usage.duration`).

Formula: `(((params.duration ?? 5) == "auto" ? Math.round(usage.duration ?? 30.0) : (params.duration ?? 5)) + (len(params.videos ?? []) > 0 ? Math.ceil(Math.min(media_duration(params.videos) ?? 15.0, 15.0)) : 0.0)) * ((params.resolution ?? "720p") == "1080p" ? 0.28 : (params.resolution ?? "720p") == "480p" ? 0.068 : 0.14)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/3.0/prime/video", "prompt": "A cinematic tracking shot of a sailboat crossing a glowing sea at sunset"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/3.0/prime/video', {'prompt': 'A cinematic tracking shot of a sailboat crossing a glowing sea at sunset'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/3.0/prime/video", {
  "prompt": "A cinematic tracking shot of a sailboat crossing a glowing sea at sunset"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/3.0/prime/video", sandbase.Params{
	"prompt": "A cinematic tracking shot of a sailboat crossing a glowing sea at sunset",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed (0-2147483647) for reproducible results. Omit for a random seed; the same seed may still produce slightly different results. range 0–2147483647 |
| `image` | string |  | URL of the image used as the first frame (JPEG, PNG, BMP, or WebP). Cannot be combined with `images`, `videos`, or `audios`.  |
| `audios` | array |  | Up to 5 reference audio URLs (WAV or MP3; 1-15s each, 15s total, under 15MB each). Cannot be combined with `image` or `end_image`.  |
| `images` | array |  | Up to 10 reference image URLs (JPEG, PNG, BMP, or WebP; up to 20MB each, 240-8000px per side). Refer to them in the prompt as Image 1, Image 2, and so on. Cannot be combined with `image` or `end_image`.  |
| `prompt` | string | yes | Text instruction for the generated video. default `"A cinematic tracking shot of a sailboat crossing a glowing sea at sunset"` |
| `videos` | array |  | Up to 5 reference video URLs (MP4 or MOV; 1-15s each, 15s total, under 100MB each). Cannot be combined with `image` or `end_image`.  |
| `duration` | enum |  | Output duration in seconds (2-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` …; default `5` |
| `end_image` | string |  | URL of the image used as the last frame (JPEG, PNG, BMP, or WebP). Cannot be combined with `images`, `videos`, or `audios`.  |
| `resolution` | string |  | Output video resolution. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose: 16:9 for text-only requests, otherwise matching the input image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

A single endpoint for the whole Wan 3.0 model. Send only a prompt for text-to-video, a first/last frame for image-to-video, or any mix of reference images, videos, and audio for reference-driven generation. Clips run 2–30 seconds at 30fps with sound generated alongside the picture.

Prime is the faster Wan 3.0 tier: the same inputs and output quality as standard Wan 3.0, with significantly shorter end-to-end generation time and a higher per-second rate. Use standard Wan 3.0 for batch or background jobs where turnaround does not matter.

### Pick an input mode

| Mode | Send | Can't combine with |
|---|---|---|
| Text | `prompt` only | — |
| Frames | `image`, optional `end_image` | `images`, `videos`, `audios` |
| References | any of `images`, `videos`, `audios` | `image`, `end_image` |

Mixing frames and references is rejected with a 400 before anything is billed. A reference video plus an edit or continuation instruction also works here; the dedicated video-edit and video-extend endpoints give those cases a simpler schema.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `image` | image URL | — | First frame. JPEG/PNG/BMP/WebP, 240–8000px per side, ≤20MB, no transparency. |
| `end_image` | image URL | — | Last frame; needs `image`. |
| `images` | image URL[] (≤10) | — | Referenced as Image 1, Image 2, … |
| `videos` | video URL[] (≤5) | — | MP4/MOV, 1–15s each, 15s total, ≤100MB. Referenced as Video 1, … |
| `audios` | audio URL[] (≤5) | — | WAV/MP3, 1–15s each, 15s total, ≤15MB. Referenced as Audio 1, … |
| `duration` | 2–30 or `auto` | 5 | `auto` lets the model pick the length. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `adaptive` / `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `adaptive` | `adaptive` follows the prompt and inputs. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

Following the official Wan 3.0 rule, billed seconds are the output length plus the total length of any reference `videos` (rounded up, counted up to 15s): $0.068 at 480p, $0.14 at 720p, $0.28 at 1080p. Input images and audio are not metered. If the reference video length cannot be read, 15s is assumed.

| Request | Billed | 480p | 720p | 1080p |
|---|---|---|---|---|
| 5s output (default) | 5s | $0.34 | $0.70 | $1.40 |
| 10s output | 10s | $0.68 | $1.40 | $2.80 |
| 30s output | 30s | $2.04 | $4.20 | $8.40 |
| 5s output + 8s reference video | 13s | $0.884 | $1.82 | $3.64 |
| 5s output + 15s reference videos | 20s | $1.36 | $2.80 | $5.60 |

With `duration: "auto"` the run is pre-authorized at 30 seconds, then settled on the length that was actually generated. Failed runs are not charged. Output files are copied to SandBase storage and the returned URL stays valid for 7 days; download anything you need to keep.

### Prompting

- Assign each reference a role: “Image 1 is the courier, Video 1 sets the camera move, Audio 1 is her voice.”
- Numbering is per type and follows array order, so reordering `images` changes what “Image 2” means.
- Put spoken lines in quotes and name the speaker.
- Wan 3.0 has no negative prompt; say what you want rather than what to avoid.

### Limits

- Reference video length plus output length must stay within 30 seconds.
- Up to 10 images, 5 videos (15s total), and 5 audio clips (15s total) per request.
- Older integrations that send `media: [{type, url}]` are still accepted and treated as reference images; new integrations should use the fields above.

### Also on SandBase

Other Wan 3.0 Prime endpoints: `alibaba/wan/3.0/prime/text-to-video`, `alibaba/wan/3.0/prime/image-to-video`, `alibaba/wan/3.0/prime/reference-to-video`, `alibaba/wan/3.0/prime/video-edit`, `alibaba/wan/3.0/prime/video-extend`. Standard tier: `alibaba/wan/3.0/video`.

---
Machine-readable: [`catalog/models/alibaba/wan/3.0/prime/video.json`](../../../../../../catalog/models/alibaba/wan/3.0/prime/video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/3.0/prime/video
