# MAGI-2 Reference to Video API: pricing, parameters and code examples

`sandai/magi-2/reference-to-video` · video generation model · Sand AI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.32 to $2.4 per run, depending on parameters · **Modes:** async

MAGI-2 by Sand AI creates a 1080p video of 4 to 30 seconds with native audio, guided by up to 10 reference images, 5 video clips and 5 audio clips.

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
  -d '{"model": "sandai/magi-2/reference-to-video", "aspect_ratio": "16:9", "duration": 5, "images": ["https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/776a14fa-b948-478b-bae6-a45c68da5ac7.jpg", "https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/e53fed62-fd62-44db-a206-3cf944d6d8e8.webp"], "prompt": "The pink-haired basketball player in the blue jersey from image 2 walks into the jazz bar from image 1 and dances in front of the band while the camera tracks alongside."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sandai/magi-2/reference-to-video', {'aspect_ratio': '16:9', 'duration': 5, 'images': ['https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/776a14fa-b948-478b-bae6-a45c68da5ac7.jpg', 'https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/e53fed62-fd62-44db-a206-3cf944d6d8e8.webp'], 'prompt': 'The pink-haired basketball player in the blue jersey from image 2 walks into the jazz bar from image 1 and dances in front of the band while the camera tracks alongside.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sandai/magi-2/reference-to-video", {
  "aspect_ratio": "16:9",
  "duration": 5,
  "images": [
    "https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/776a14fa-b948-478b-bae6-a45c68da5ac7.jpg",
    "https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/e53fed62-fd62-44db-a206-3cf944d6d8e8.webp"
  ],
  "prompt": "The pink-haired basketball player in the blue jersey from image 2 walks into the jazz bar from image 1 and dances in front of the band while the camera tracks alongside."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sandai/magi-2/reference-to-video", sandbase.Params{
	"aspect_ratio": "16:9",
	"duration": 5,
	"images": []any{"https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/776a14fa-b948-478b-bae6-a45c68da5ac7.jpg", "https://static.sandbase.ai/examples/eeb92b90-3c1a-4979-9860-1c508e732417/input/e53fed62-fd62-44db-a206-3cf944d6d8e8.webp"},
	"prompt": "The pink-haired basketball player in the blue jersey from image 2 walks into the jazz bar from image 1 and dances in front of the band while the camera tracks alongside.",
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
| `audios` | array |  | Up to 5 WAV/MP3 files or URLs, 2-30 s each and 30 s in total, up to 15 MB each.  |
| `images` | array |  | Up to 10 images (upload or public HTTPS URL), each under 30 MB.  |
| `prompt` | string | yes | Describe how to use the references, the scene, motion and sound.  |
| `videos` | array |  | Up to 5 MP4/MOV files or URLs, 2-30 s each and 30 s in total, up to 200 MB each.  |
| `duration` | integer |  | Output video duration in seconds (4-30). Billed per second. default `5`; range 4–30 |
| `resolution` | string |  | Output resolution. MAGI-2 renders 1080p only. one of: `1080p`; default `"1080p"` |
| `aspect_ratio` | string |  | Output aspect ratio. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; default `"16:9"` |
| `generate_audio` | boolean |  | Generate a native audio track with the video. Included in the price. default `true` |

## Details

MAGI-2 reference-to-video API by Sand AI: guide a 1080p video of 4 to 30 seconds with up to 10 reference images, 5 videos and 5 audio clips, to keep a character, a location, a camera move or a voice consistent. Sound is generated with the picture. Use it through SandBase with one API key, pay per second of output, and switch providers automatically if one is unavailable.
### Quickstart
```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sandai/magi-2/reference-to-video",
    "prompt": "Use the woman in image 1 as the lead and keep her face, hair and outfit the same. She walks into a sunlit flower market, picks up white tulips, turns to the camera and says: \"These are for you.\" Slow tracking shot. Sound: soft market chatter and her voice from audio 1.",
    "images": [
      "https://example.com/character.jpg"
    ],
    "audios": [
      "https://example.com/voice.wav"
    ],
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
| Request | `POST /v1/run` with `"model": "sandai/magi-2/reference-to-video"` and the fields below | `POST /api/v3/contents/generations/tasks` with `"model": "magi-2"` and a `content` array |
| Inputs | Reference images, videos and audio | Text, first and last frame, or references, all in one model |
| Providers | Switches to another provider if one is unavailable | One provider |
| Price | $0.08 per second | $0.08 per second |
Use this model for new integrations: it takes the same request format as other SandBase models. Use [MAGI-2 in the Sand AI format](/models/sandai/magi-2) if your code already calls Sand AI's API or the Ark SDK. [Compare both on the MAGI-2 page](/models/magi-2).
### Fields
| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Describe how to use the references, the scene, motion and sound. |
| `images` | string[] (≤10) | — | Up to 10 images (upload or public HTTPS URL), each under 30 MB. |
| `videos` | string[] (≤5) | — | Up to 5 MP4/MOV files or URLs, 2-30 s each and 30 s in total, up to 200 MB each. |
| `audios` | string[] (≤5) | — | Up to 5 WAV/MP3 files or URLs, 2-30 s each and 30 s in total, up to 15 MB each. |
| `duration` | integer 4–30 | 5 | Output video duration in seconds (4-30). Billed per second. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` / `21:9` | 16:9 | Output aspect ratio. |
| `resolution` | `1080p` | 1080p | Output resolution. MAGI-2 renders 1080p only. |
| `generate_audio` | boolean | true | Generate a native audio track with the video. Included in the price. |
| `seed` | integer 0–4294967295 | random | Random seed for reproducibility (0-4294967295). Omit for a random seed. |
### Prompt tips
- Refer to each reference by type and order: image 1, image 2, video 1, audio 1.
- Say what each reference controls, for example `keep the face and outfit from image 1`, `use the location in image 2`, `follow the camera move in video 1` or `use the voice in audio 1`.
- Use clear, well-lit reference images of the character and the location, and describe them in the prompt as well.
- Keep one or two actions and one camera move per clip, and put spoken lines in quotes.
- References cannot be combined with a first or last frame. To start from a specific image, use [MAGI-2 Image to Video](/models/sandai/magi-2/image-to-video).
### Billing
$0.08 per second of output video, with native audio included in the price. Resolution is fixed at 1080p. Failed runs are not billed.
| Output length | Price |
|---|---|
| 4s | $0.32 |
| 5s (default) | $0.40 |
| 10s | $0.80 |
| 30s | $2.40 |
### FAQ
#### How many reference files can I use?
Up to 10 images, 5 videos and 5 audio clips in one request. Each video or audio clip must be 2 to 30 seconds long, and all clips of one type together at most 30 seconds. Reference files do not change the price.
#### Which file formats are supported?
Images: JPEG, PNG, WebP and other common formats under 30 MB. Videos: MP4 or MOV up to 200 MB. Audio: WAV or MP3 up to 15 MB. Upload them in the Playground or pass public HTTPS URLs.
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
- [MAGI-2 Image to Video](/models/sandai/magi-2/image-to-video)

---
Machine-readable: [`catalog/models/sandai/magi-2/reference-to-video.json`](../../../../catalog/models/sandai/magi-2/reference-to-video.json) · Store page: https://www.sandbase.ai/model/sandai/magi-2/reference-to-video
