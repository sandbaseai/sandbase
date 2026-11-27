# MAGI-2 API: pricing, parameters and code examples

`sandai/magi-2` · video generation model · Sand AI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.32 to $2.4 per run, depending on parameters · **Modes:** async

MAGI-2 by Sand AI turns text, a first and last frame, or reference images, videos and audio into a 1080p video of 4 to 30 seconds with native audio. Call it from this page, through /v1/run, or with the Volcengine Ark compatible API that Sand AI documents for MAGI-2.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=4 | 0.32 |
| duration=5 | 0.4 |
| duration=30 | 2.4 |

Formula: `(params.duration ?? 5) * 0.08`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sandai/magi-2"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sandai/magi-2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sandai/magi-2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sandai/magi-2", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-4294967295). Omit for a random seed. range 0–4294967295 |
| `image` | string |  | Optional first frame (upload or public HTTPS URL). Cannot be combined with reference images, videos or audio.  |
| `audios` | array |  | Up to 5 WAV/MP3 files or URLs, 2-30 s each and 30 s in total, up to 15 MB each.  |
| `images` | array |  | Up to 10 reference images (upload or public HTTPS URL), each under 30 MB. Cannot be combined with a first or last frame.  |
| `prompt` | string |  | Describe the scene, motion and sound. Up to 15,000 characters. Required when no image, video or audio is given.  |
| `videos` | array |  | Up to 5 MP4/MOV files or URLs, 2-30 s each and 30 s in total, up to 200 MB each.  |
| `duration` | integer |  | Output video duration in seconds (4-30). Billed per second. default `5`; range 4–30 |
| `end_image` | string |  | Optional last frame; requires a first frame.  |
| `resolution` | string |  | Output resolution. MAGI-2 renders 1080p only. one of: `1080p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; default `"16:9"` |
| `enhance_prompt` | boolean |  | Turn prompt enhancement on or off. Omit to use the model default.  |
| `generate_audio` | boolean |  | Generate a native audio track with the video. Included in the price. default `true` |
| `omni_reference_task_type` | string |  | Optional. Only auto is supported. one of: `auto` |

## Details

[MAGI-2](https://sand.ai/blog/magi-2/) by [Sand AI](https://sand.ai/) generates a 1080p video of 4 to 30 seconds from text, a first and last frame, or reference images, videos and audio, with dialogue, sound effects and music generated together with the picture. [See MAGI-2 results](https://www.sandbase.ai/lab/ai-videos/magi-2) first if you want to judge the quality.

Use the form on this page, call `sandai/magi-2` through `/v1/run`, or use the Volcengine Ark compatible API below with the request body Sand AI documents.
### Inputs
Pick one way to guide the video:
- **Text only**: a prompt.
- **First and last frame**: `image`, optionally `end_image`, with an optional prompt.
- **References**: up to 10 `images`, 5 `videos` and 5 `audios` (videos and audio 2 to 30 seconds each and 30 seconds in total), with an optional prompt. Refer to them in the prompt as @Image1, @Video1, @Audio1.

Frames and references cannot be combined in one request.
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Scene, motion and sound. Up to 15,000 characters. Required for text only. |
| `image` | image | — | First frame. |
| `end_image` | image | — | Last frame. Requires `image`. |
| `images` | image list, up to 10 | — | Reference images. |
| `videos` | video list, up to 5 | — | Reference videos, MP4 or MOV. |
| `audios` | audio list, up to 5 | — | Reference audio, WAV or MP3. |
| `duration` | integer 4–30 | 5 | Output length in seconds. Billed per second. |
| `aspect_ratio` | `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | 16:9 | Output aspect ratio. |
| `resolution` | `1080p` | 1080p | MAGI-2 renders 1080p only. |
| `generate_audio` | boolean | true | Native audio track, included in the price. |
| `seed` | integer 0–4294967295 | random | Fix the seed for reproducible results. |
| `enhance_prompt` | boolean | model default | Turn prompt enhancement on or off. |
| `omni_reference_task_type` | `auto` | — | Optional. |
### Volcengine Ark compatible API
SandBase implements Sand AI's [Ark compatibility API](https://platform.sand.ai/docs/ark-generations/) for `magi-2`. Use your SandBase API key and point the Ark SDK or HTTP client at SandBase:
| | Sand AI | SandBase |
|---|---|---|
| Base URL | `https://api.sand.ai/compatible/ark/api/v3` | `https://api.sandbase.ai/api/v3` |
| Create a task | `POST /contents/generations/tasks` | `POST /contents/generations/tasks` |
| Retrieve a task | `GET /contents/generations/tasks/{id}` | `GET /contents/generations/tasks/{id}` |
| `model` | `magi-2` | `magi-2` |
```bash
curl https://api.sandbase.ai/api/v3/contents/generations/tasks \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "magi-2",
    "content": [
      {"type": "text", "text": "The camera moves from a clear dawn shore to sunset."},
      {"type": "image_url", "role": "first_frame", "image_url": {"url": "https://example.com/first.jpg"}},
      {"type": "image_url", "role": "last_frame", "image_url": {"url": "https://example.com/last.jpg"}}
    ],
    "duration": 5,
    "ratio": "16:9",
    "resolution": "1080p"
  }'
```
In this API, `duration` (4 to 30) and `ratio` are required, either as top-level fields or as prompt suffixes such as `--rt 16:9 --dur 5`; top-level fields win. Omit `watermark` and the other fields Sand AI lists as unsupported: any value other than `null` returns 400.

The response is `{"id": "..."}`. Poll `GET /api/v3/contents/generations/tasks/{id}` every 10 seconds. `queued` and `running` mean keep polling. On `succeeded`, download `content.video_url`; the task also reports `duration`, `framespersecond`, `resolution`, `ratio` and `generate_audio` when known. `failed`, `expired` and `cancelled` are final; failed and expired tasks carry `error.code` and `error.message`.

Requests and responses use the format in the [Sand AI documentation](https://platform.sand.ai/docs/ark-generations/). Media URLs can be public HTTPS or `data:` URLs: images JPEG, PNG, WebP, GIF, BMP, TIFF, HEIC or HEIF under 30,000,000 bytes, audio MP3 or WAV up to 15,000,000 bytes. A request body can be up to 64,000,000 bytes, of which at most 2 MiB is not media; put `model` near the start of large requests. Also note:
- `X-Request-Id` is returned only when a task is created.
- References are sent to the model grouped by type (images, then videos, then audio); the order within each type is kept.
- MAGI-2 runs on one provider here. The per-mode models below can switch providers.
### Billing
$0.08 per second of output video, with native audio included in the price. Resolution is fixed at 1080p. Failed runs are not billed.
| Output length | Price |
|---|---|
| 4s | $0.32 |
| 5s (default) | $0.40 |
| 10s | $0.80 |
| 30s | $2.40 |
### One mode at a time
These models take one input mode each and can switch between providers if one is unavailable:
- [MAGI-2 Text to Video](/models/sandai/magi-2/text-to-video)
- [MAGI-2 Image to Video](/models/sandai/magi-2/image-to-video)
- [MAGI-2 Reference to Video](/models/sandai/magi-2/reference-to-video)
### See what MAGI-2 can do
- [MAGI-2 videos from X](https://www.sandbase.ai/lab/ai-videos/magi-2): the most-liked MAGI-2 clips, credited to the people who made them. Short films, ads and anime.
- Open a mode page above to try it and see its examples.
### Learn more
- [Sand AI Ark compatibility API](https://platform.sand.ai/docs/ark-generations/): the official request and response reference, to compare with SandBase.
- [MAGI-2 announcement from Sand AI](https://sand.ai/blog/magi-2/): model overview and release notes.
- [Sand AI](https://sand.ai/): the team behind MAGI-2.

---
Machine-readable: [`catalog/models/sandai/magi-2.json`](../../../catalog/models/sandai/magi-2.json) · Store page: https://www.sandbase.ai/model/sandai/magi-2
