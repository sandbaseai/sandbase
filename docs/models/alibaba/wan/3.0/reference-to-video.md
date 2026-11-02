# Wan 3.0 Reference to Video API: pricing, parameters and code examples

`alibaba/wan/3.0/reference-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.5 per call · **Modes:** async

Wan 3.0 by Alibaba generates up to 30-second videos with native audio from reference images, videos, and audio, keeping subjects, motion, and voice consistent with the references.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `params.videos`, `usage.duration`).

Formula: `(((params.duration ?? 5) == "auto" ? Math.round(usage.duration ?? 30.0) : (params.duration ?? 5)) + (len(params.videos ?? []) > 0 ? Math.ceil(Math.min(media_duration(params.videos) ?? 15.0, 15.0)) : 0.0)) * ((params.resolution ?? "720p") == "1080p" ? 0.20 : (params.resolution ?? "720p") == "480p" ? 0.05 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/3.0/reference-to-video", "aspect_ratio": "9:16", "duration": 15, "images": ["https://static.sandbase.ai/examples/825e2704-ea2e-446d-bae9-bfaabb6928c9/input/e6ff2dc2-df0d-49cc-870e-198b092f5883.png"], "prompt": "Using the lip gloss product in Image 1, generate a model swatch video, 15 seconds, vertical screen, highlighting the lip color effect"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/3.0/reference-to-video', {'aspect_ratio': '9:16', 'duration': 15, 'images': ['https://static.sandbase.ai/examples/825e2704-ea2e-446d-bae9-bfaabb6928c9/input/e6ff2dc2-df0d-49cc-870e-198b092f5883.png'], 'prompt': 'Using the lip gloss product in Image 1, generate a model swatch video, 15 seconds, vertical screen, highlighting the lip color effect'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/3.0/reference-to-video", {
  "aspect_ratio": "9:16",
  "duration": 15,
  "images": [
    "https://static.sandbase.ai/examples/825e2704-ea2e-446d-bae9-bfaabb6928c9/input/e6ff2dc2-df0d-49cc-870e-198b092f5883.png"
  ],
  "prompt": "Using the lip gloss product in Image 1, generate a model swatch video, 15 seconds, vertical screen, highlighting the lip color effect"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/3.0/reference-to-video", sandbase.Params{
	"aspect_ratio": "9:16",
	"duration": 15,
	"images": []any{"https://static.sandbase.ai/examples/825e2704-ea2e-446d-bae9-bfaabb6928c9/input/e6ff2dc2-df0d-49cc-870e-198b092f5883.png"},
	"prompt": "Using the lip gloss product in Image 1, generate a model swatch video, 15 seconds, vertical screen, highlighting the lip color effect",
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
| `audios` | array |  | Up to 5 reference audio URLs (WAV or MP3; 1-15s each, 15s total, under 15MB each). Cannot be combined with `image` or `end_image`.  |
| `images` | array |  | Up to 10 reference image URLs (JPEG, PNG, BMP, or WebP; up to 20MB each, 240-8000px per side). Refer to them in the prompt as Image 1, Image 2, and so on. Provide at least one of `images`, `videos`, or `audios`.  |
| `prompt` | string | yes | Text prompt directing how the reference media is used. Reference media can be addressed positionally, e.g. 'the subject in Image 1 walks past Video 1'.  |
| `videos` | array |  | Up to 5 reference video URLs (MP4 or MOV; 1-15s each, 15s total, under 100MB each). Cannot be combined with `image` or `end_image`.  |
| `duration` | enum |  | Output duration in seconds (2-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` …; default `5` |
| `resolution` | string |  | Output video resolution tier. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to let the model choose from the prompt and reference inputs. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Generate a new shot that reuses what you already have: faces and products from images, motion and framing from clips, voices and music from audio. The prompt decides how the references come together.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `images` | image URL[] (≤10) | — | Referenced as Image 1, Image 2, … |
| `videos` | video URL[] (≤5) | — | MP4/MOV, 1–15s each, 15s total, ≤100MB. Referenced as Video 1, … |
| `audios` | audio URL[] (≤5) | — | WAV/MP3, 1–15s each, 15s total, ≤15MB. Referenced as Audio 1, … |
| `duration` | 2–30 or `auto` | 5 | `auto` lets the model pick the length. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `adaptive` / `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `adaptive` | `adaptive` follows the prompt and inputs. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

Send at least one of `images`, `videos`, or `audios`; any combination works.

### Billing

You pay per second of output plus, when you send reference `videos`, their total length (rounded up, counted up to 15s): $0.05 at 480p, $0.10 at 720p, $0.20 at 1080p. Input images and audio are not metered. If the reference video length cannot be read, 15s is assumed.

| Request | Billed | 480p | 720p | 1080p |
|---|---|---|---|---|
| 5s output (default) | 5s | $0.25 | $0.50 | $1.00 |
| 10s output | 10s | $0.50 | $1.00 | $2.00 |
| 30s output | 30s | $1.50 | $3.00 | $6.00 |
| 5s output + 8s reference video | 13s | $0.65 | $1.30 | $2.60 |
| 5s output + 15s reference videos | 20s | $1.00 | $2.00 | $4.00 |

With `duration: "auto"` the run is pre-authorized at 30 seconds, then settled on the length that was actually generated. Failed runs are not charged. Output files are copied to SandBase storage and the returned URL stays valid for 7 days; download anything you need to keep.

### Prompting

- Give every reference a job: “Image 1 is the cyclist, Video 1 provides the camera move.”
- Several images of the same subject from different angles hold identity better than one.
- Keep reference audio short and focused on the voice or sound you want carried over.

> Image 1 is the cyclist; Video 1 supplies the camera movement. She rides through a rainy city at night in the same red jacket, with quiet traffic in the background.

### Limits

- Up to 10 images, 5 videos (15s total), and 5 audio clips (15s total).
- Reference video length plus output length must stay within 30 seconds.
- First/last frames are not accepted here; use image-to-video.

### Also on SandBase

Other Wan 3.0 endpoints: `alibaba/wan/3.0/video` (all modes in one schema), `alibaba/wan/3.0/text-to-video`, `alibaba/wan/3.0/image-to-video`, `alibaba/wan/3.0/video-edit`, `alibaba/wan/3.0/video-extend`.

---
Machine-readable: [`catalog/models/alibaba/wan/3.0/reference-to-video.json`](../../../../../catalog/models/alibaba/wan/3.0/reference-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/3.0/reference-to-video
