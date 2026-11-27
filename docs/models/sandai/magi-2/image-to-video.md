# MAGI-2 Image to Video API: pricing, parameters and code examples

`sandai/magi-2/image-to-video` · video generation model · Sand AI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.32 to $2.4 per run, depending on parameters · **Modes:** async

MAGI-2 by Sand AI animates a first frame, or a first and last frame, into a 1080p video of 4 to 30 seconds with native audio.

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
  -d '{"model": "sandai/magi-2/image-to-video", "aspect_ratio": "16:9", "duration": 5, "image": "https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp", "prompt": "The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sandai/magi-2/image-to-video', {'aspect_ratio': '16:9', 'duration': 5, 'image': 'https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp', 'prompt': 'The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sandai/magi-2/image-to-video", {
  "aspect_ratio": "16:9",
  "duration": 5,
  "image": "https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp",
  "prompt": "The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sandai/magi-2/image-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"duration": 5,
	"image": "https://static.sandbase.ai/examples/cf7d3354-3c3c-475c-93c0-74f31c6b084a/input/241be84a-97d7-4d77-9ca9-7fdb51507601.webp",
	"prompt": "The player jumps and shoots; the ball drops through the hoop and the friends on the court cheer. Handheld camera follows the shot.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility (0-4294967295). Omit for a random seed. range 0–4294967295 |
| `image` | string | yes | First frame (upload or public HTTPS URL). JPEG, PNG, WebP, BMP, TIFF, GIF or HEIC, under 30 MB.  |
| `prompt` | string |  | Optional. Describe the motion and sound.  |
| `duration` | integer |  | Output video duration in seconds (4-30). Billed per second. default `5`; range 4–30 |
| `end_image` | string |  | Optional last frame (upload or public HTTPS URL).  |
| `resolution` | string |  | Output resolution. MAGI-2 renders 1080p only. one of: `1080p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate a native audio track with the video. Included in the price. default `true` |

## Details

MAGI-2 image-to-video API by Sand AI: animate a first frame, or move from a first frame to a last frame, in a 1080p video of 4 to 30 seconds with native audio. Use it through SandBase with one API key, pay per second of output, and switch providers automatically if one is unavailable.
### Quickstart
```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sandai/magi-2/image-to-video",
    "image": "https://example.com/first-frame.jpg",
    "prompt": "The woman leans toward the microphone, smiles and says: \"Welcome back to the show.\" Slow push-in. Sound: quiet room tone and her voice.",
    "duration": 5,
    "aspect_ratio": "16:9"
  }'
```
The response contains an `id`. Poll the run every 10 seconds until `status` is `completed`, then download `outputs[0].url`:
```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID \
  -H "Authorization: Bearer $SANDBASE_API_KEY"
```
Stop polling when `status` is `failed` and read the error message. You can also run the same request in the Playground on this page without writing code.
### Two ways to call MAGI-2
| | This model (SandBase API) | [MAGI-2, Sand AI format](/models/sandai/magi-2) |
|---|---|---|
| Request | `POST /v1/run` with `"model": "sandai/magi-2/image-to-video"` and the fields below | `POST /api/v3/contents/generations/tasks` with `"model": "magi-2"` and a `content` array |
| Inputs | A first frame, optional last frame | Text, first and last frame, or references, all in one model |
| Providers | Switches to another provider if one is unavailable | One provider |
| Price | $0.08 per second | $0.08 per second |
Use this model for new integrations: it takes the same request format as other SandBase models. Use [MAGI-2 in the Sand AI format](/models/sandai/magi-2) if your code already calls Sand AI's API or the Ark SDK. [Compare both on the MAGI-2 page](/models/magi-2).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Optional. Describe the motion and sound. |
| `image` | string, required | — | First frame (upload or public HTTPS URL). JPEG, PNG, WebP, BMP, TIFF, GIF or HEIC, under 30 MB. |
| `end_image` | string | — | Optional last frame (upload or public HTTPS URL). |
| `duration` | integer 4–30 | 5 | Output video duration in seconds (4-30). Billed per second. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | 16:9 | Output aspect ratio. |
| `resolution` | `1080p` | 1080p | Output resolution. MAGI-2 renders 1080p only. |
| `generate_audio` | boolean | true | Generate a native audio track with the video. Included in the price. |
| `seed` | integer 0–4294967295 | random | Random seed for reproducibility (0-4294967295). Omit for a random seed. |
### Prompt tips
- Describe the scene that is already in the image, then the movement you want. A prompt that describes a different scene can change the image a lot.
- With a last frame (`end_image`), describe the action that connects the two frames. Frames with a similar setting, lighting and subject give the smoothest transition.
- Choose an `aspect_ratio` that matches your image to avoid cropping.
- Put spoken lines in quotes to make the subject talk, and add a `Sound:` line for ambience and effects.
- Keep one or two actions and one camera move per clip.
### Billing
$0.08 per second of output video, with native audio included in the price. Resolution is fixed at 1080p. Failed runs are not billed.
| Output length | Price |
|---|---|
| 4s | $0.32 |
| 5s (default) | $0.40 |
| 10s | $0.80 |
| 30s | $2.40 |
### FAQ
#### Can I set both a first and a last frame?
Yes. Send the first frame as `image` and the last frame as `end_image`. The video starts on the first image and ends on the second. The prompt is optional.
#### Which image formats can I use?
JPEG, PNG, WebP, BMP, TIFF, GIF or HEIC under 30 MB, as an upload in the Playground or a public HTTPS URL.
#### How long can a MAGI-2 video be?
Any whole number of seconds from 4 to 30, set with `duration`. The video is rendered at 1080p and 25 fps in one of six aspect ratios: 16:9, 9:16, 1:1, 4:3, 3:4 or 21:9.
#### Does MAGI-2 generate sound?
Yes. Dialogue, sound effects, ambience and music are generated together with the picture. Set `generate_audio` to `false` for a silent video; the price is the same.
#### How is MAGI-2 billed?
$0.08 per second of output video, from your SandBase balance. A 5-second clip costs $0.40 and a 30-second clip $2.40. Failed runs, including ones rejected by content moderation, are not billed.
#### Can I use Sand AI's API format instead?
Yes. If your code already calls Sand AI's API or the Ark SDK, use [MAGI-2 in the Sand AI format](/models/sandai/magi-2) with `"model": "magi-2"` at `https://api.sandbase.ai/api/v3`. [Compare both ways](/models/magi-2).
### See what people made
Browse the most-liked MAGI-2 videos on X, credited to the people who made them: [MAGI-2 videos from X](https://www.sandbase.ai/lab/ai-videos/magi-2). Short films, ads and anime.
### Other MAGI-2 modes
- [MAGI-2 Text to Video](/models/sandai/magi-2/text-to-video)
- [MAGI-2 Reference to Video](/models/sandai/magi-2/reference-to-video)

---
Machine-readable: [`catalog/models/sandai/magi-2/image-to-video.json`](../../../../catalog/models/sandai/magi-2/image-to-video.json) · Store page: https://www.sandbase.ai/model/sandai/magi-2/image-to-video
