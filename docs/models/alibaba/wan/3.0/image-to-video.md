# Wan 3.0 Image to Video API: pricing, parameters and code examples

`alibaba/wan/3.0/image-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.1 to $1.2 per run, depending on parameters · **Modes:** async

Wan 3.0 by Alibaba - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `usage.duration`).

| parameters | USD |
|---|---|
| duration=2, resolution="480p" | 0.1 * |
| duration=2, resolution="720p" | 0.2 * |
| duration=2, resolution="1080p" | 0.4 * |
| duration=3, resolution="480p" | 0.15 * |
| duration=3, resolution="720p" | 0.3 * |
| duration=3, resolution="1080p" | 0.6 * |
| duration=4, resolution="480p" | 0.2 * |
| duration=4, resolution="720p" | 0.4 * |
| duration=4, resolution="1080p" | 0.8 * |
| duration=5, resolution="480p" | 0.25 * |
| duration=5, resolution="720p" | 0.5 * |
| duration=5, resolution="1080p" | 1 * |
| duration=6, resolution="480p" | 0.3 * |
| duration=6, resolution="720p" | 0.6 * |
| duration=6, resolution="1080p" | 1.2 * |

\* estimate: assumes output duration equals requested duration.

Formula: `((params.duration ?? 5) == "auto" ? Math.round(usage.duration ?? 30.0) : (params.duration ?? 5)) * ((params.resolution ?? "720p") == "1080p" ? 0.20 : (params.resolution ?? "720p") == "480p" ? 0.05 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/3.0/image-to-video", "duration": 20, "image": "https://static.sandbase.ai/examples/d2093d34-17ff-42a9-8b36-45e0c52f8028/input/0e8430dd-0e38-49d9-b437-96faa0d0bbc1.png", "prompt": "(0:00 - 0:03) Camera: Medium shot. Scene: A ink-wash bamboo forest scene from Image 1. A swordsman wearing a bamboo hat and dressed in a dark robe, his silhouette standing in the center surrounded by thick fog and swaying bamboo shadows. Action: The swordsman'\''s left hand lightly rests on the sword hilt, bamboo leaves fall with the wind. Atmosphere: Silent, oppressive, with clearly visible ink-wash grain texture. (0:03 - 0:08) Plot introduction. Camera: Close-up. Plot: The swordsman senses killing intent. Scene: The camera rapidly pushes in to a close-up beneath the swordsman'\''s bamboo hat. Detail: Beneath the hat brim, a pair of sharp, resolute eyes appear, gaze like a blade. Ink-wash \"sweat drops\" slide down from the forehead. Action: The swordsman'\''s right hand slowly grips the sword hilt, knuckles turning white. The bamboo leaves fall faster. (0:08 - 0:13) Camera: Fast orbit. Scene: The camera rapidly orbits around the swordsman. Plot: Two assassins, also ink-wash silhouettes, burst out from deep in the bamboo forest, wielding twin hooks and short blades. Detail: The assassins'\'' movements are also composed of ink-wash brushstrokes, flowing like ink traces. The camera sweeps past the assassins'\'' figures rapidly, emphasizing speed. (0:13 - 0:18) Camera: Handheld feel, high-speed capture. Combat: The swordsman draws his blade sharply — the blade light is a pure white ink-wash crack. The assassin attacks with twin hooks. Detail: Strike one — the swordsman spins and slashes, blade colliding with the assassin'\''s twin hooks, sending sparks of black and white with calligraphic flair and ink drops flying. Strike two — the swordsman feints, uses a bamboo pole to catapult himself, and strikes down from above. The assassin rolls to dodge. The bamboo pole shatters into scattered ink traces. Strike three — the swordsman'\''s blade tip points at the other assassin'\''s throat; the assassin blocks with a short blade, and the camera captures the fine detail of ink traces cracking where the blades grind. (0:18 - 0:20) Camera: Slow motion to freeze frame. * Scene: The swordsman'\''s blade stops at the assassin'\''s neck, the assassin frozen. * Detail: The swordsman'\''s bamboo hat is slightly tilted from the fight. The bamboo forest returns to calm, more bamboo leaves dancing. * Atmosphere: The camera slowly pulls back to medium shot, freezing on the swordsman sheathing his blade and the assassin falling. * Text (optional): Ink-wash style text appears at the bottom: \"The world of martial arts — settled with a single stroke.\" Style note: Throughout, maintain the highly black-and-white, ink-wash painting style of Image 1 . Actions must have a calligraphic brush feel, speed must be fast, details must be rich (ink drops, sparks, ink crack marks)."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/3.0/image-to-video', {'duration': 20, 'image': 'https://static.sandbase.ai/examples/d2093d34-17ff-42a9-8b36-45e0c52f8028/input/0e8430dd-0e38-49d9-b437-96faa0d0bbc1.png', 'prompt': '(0:00 - 0:03) Camera: Medium shot. Scene: A ink-wash bamboo forest scene from Image 1. A swordsman wearing a bamboo hat and dressed in a dark robe, his silhouette standing in the center surrounded by thick fog and swaying bamboo shadows. Action: The swordsman\'s left hand lightly rests on the sword hilt, bamboo leaves fall with the wind. Atmosphere: Silent, oppressive, with clearly visible ink-wash grain texture. (0:03 - 0:08) Plot introduction. Camera: Close-up. Plot: The swordsman senses killing intent. Scene: The camera rapidly pushes in to a close-up beneath the swordsman\'s bamboo hat. Detail: Beneath the hat brim, a pair of sharp, resolute eyes appear, gaze like a blade. Ink-wash "sweat drops" slide down from the forehead. Action: The swordsman\'s right hand slowly grips the sword hilt, knuckles turning white. The bamboo leaves fall faster. (0:08 - 0:13) Camera: Fast orbit. Scene: The camera rapidly orbits around the swordsman. Plot: Two assassins, also ink-wash silhouettes, burst out from deep in the bamboo forest, wielding twin hooks and short blades. Detail: The assassins\' movements are also composed of ink-wash brushstrokes, flowing like ink traces. The camera sweeps past the assassins\' figures rapidly, emphasizing speed. (0:13 - 0:18) Camera: Handheld feel, high-speed capture. Combat: The swordsman draws his blade sharply — the blade light is a pure white ink-wash crack. The assassin attacks with twin hooks. Detail: Strike one — the swordsman spins and slashes, blade colliding with the assassin\'s twin hooks, sending sparks of black and white with calligraphic flair and ink drops flying. Strike two — the swordsman feints, uses a bamboo pole to catapult himself, and strikes down from above. The assassin rolls to dodge. The bamboo pole shatters into scattered ink traces. Strike three — the swordsman\'s blade tip points at the other assassin\'s throat; the assassin blocks with a short blade, and the camera captures the fine detail of ink traces cracking where the blades grind. (0:18 - 0:20) Camera: Slow motion to freeze frame. * Scene: The swordsman\'s blade stops at the assassin\'s neck, the assassin frozen. * Detail: The swordsman\'s bamboo hat is slightly tilted from the fight. The bamboo forest returns to calm, more bamboo leaves dancing. * Atmosphere: The camera slowly pulls back to medium shot, freezing on the swordsman sheathing his blade and the assassin falling. * Text (optional): Ink-wash style text appears at the bottom: "The world of martial arts — settled with a single stroke." Style note: Throughout, maintain the highly black-and-white, ink-wash painting style of Image 1 . Actions must have a calligraphic brush feel, speed must be fast, details must be rich (ink drops, sparks, ink crack marks).'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/3.0/image-to-video", {
  "duration": 20,
  "image": "https://static.sandbase.ai/examples/d2093d34-17ff-42a9-8b36-45e0c52f8028/input/0e8430dd-0e38-49d9-b437-96faa0d0bbc1.png",
  "prompt": "(0:00 - 0:03) Camera: Medium shot. Scene: A ink-wash bamboo forest scene from Image 1. A swordsman wearing a bamboo hat and dressed in a dark robe, his silhouette standing in the center surrounded by thick fog and swaying bamboo shadows. Action: The swordsman's left hand lightly rests on the sword hilt, bamboo leaves fall with the wind. Atmosphere: Silent, oppressive, with clearly visible ink-wash grain texture. (0:03 - 0:08) Plot introduction. Camera: Close-up. Plot: The swordsman senses killing intent. Scene: The camera rapidly pushes in to a close-up beneath the swordsman's bamboo hat. Detail: Beneath the hat brim, a pair of sharp, resolute eyes appear, gaze like a blade. Ink-wash \"sweat drops\" slide down from the forehead. Action: The swordsman's right hand slowly grips the sword hilt, knuckles turning white. The bamboo leaves fall faster. (0:08 - 0:13) Camera: Fast orbit. Scene: The camera rapidly orbits around the swordsman. Plot: Two assassins, also ink-wash silhouettes, burst out from deep in the bamboo forest, wielding twin hooks and short blades. Detail: The assassins' movements are also composed of ink-wash brushstrokes, flowing like ink traces. The camera sweeps past the assassins' figures rapidly, emphasizing speed. (0:13 - 0:18) Camera: Handheld feel, high-speed capture. Combat: The swordsman draws his blade sharply — the blade light is a pure white ink-wash crack. The assassin attacks with twin hooks. Detail: Strike one — the swordsman spins and slashes, blade colliding with the assassin's twin hooks, sending sparks of black and white with calligraphic flair and ink drops flying. Strike two — the swordsman feints, uses a bamboo pole to catapult himself, and strikes down from above. The assassin rolls to dodge. The bamboo pole shatters into scattered ink traces. Strike three — the swordsman's blade tip points at the other assassin's throat; the assassin blocks with a short blade, and the camera captures the fine detail of ink traces cracking where the blades grind. (0:18 - 0:20) Camera: Slow motion to freeze frame. * Scene: The swordsman's blade stops at the assassin's neck, the assassin frozen. * Detail: The swordsman's bamboo hat is slightly tilted from the fight. The bamboo forest returns to calm, more bamboo leaves dancing. * Atmosphere: The camera slowly pulls back to medium shot, freezing on the swordsman sheathing his blade and the assassin falling. * Text (optional): Ink-wash style text appears at the bottom: \"The world of martial arts — settled with a single stroke.\" Style note: Throughout, maintain the highly black-and-white, ink-wash painting style of Image 1 . Actions must have a calligraphic brush feel, speed must be fast, details must be rich (ink drops, sparks, ink crack marks)."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/3.0/image-to-video", sandbase.Params{
	"duration": 20,
	"image": "https://static.sandbase.ai/examples/d2093d34-17ff-42a9-8b36-45e0c52f8028/input/0e8430dd-0e38-49d9-b437-96faa0d0bbc1.png",
	"prompt": "(0:00 - 0:03) Camera: Medium shot. Scene: A ink-wash bamboo forest scene from Image 1. A swordsman wearing a bamboo hat and dressed in a dark robe, his silhouette standing in the center surrounded by thick fog and swaying bamboo shadows. Action: The swordsman's left hand lightly rests on the sword hilt, bamboo leaves fall with the wind. Atmosphere: Silent, oppressive, with clearly visible ink-wash grain texture. (0:03 - 0:08) Plot introduction. Camera: Close-up. Plot: The swordsman senses killing intent. Scene: The camera rapidly pushes in to a close-up beneath the swordsman's bamboo hat. Detail: Beneath the hat brim, a pair of sharp, resolute eyes appear, gaze like a blade. Ink-wash \"sweat drops\" slide down from the forehead. Action: The swordsman's right hand slowly grips the sword hilt, knuckles turning white. The bamboo leaves fall faster. (0:08 - 0:13) Camera: Fast orbit. Scene: The camera rapidly orbits around the swordsman. Plot: Two assassins, also ink-wash silhouettes, burst out from deep in the bamboo forest, wielding twin hooks and short blades. Detail: The assassins' movements are also composed of ink-wash brushstrokes, flowing like ink traces. The camera sweeps past the assassins' figures rapidly, emphasizing speed. (0:13 - 0:18) Camera: Handheld feel, high-speed capture. Combat: The swordsman draws his blade sharply — the blade light is a pure white ink-wash crack. The assassin attacks with twin hooks. Detail: Strike one — the swordsman spins and slashes, blade colliding with the assassin's twin hooks, sending sparks of black and white with calligraphic flair and ink drops flying. Strike two — the swordsman feints, uses a bamboo pole to catapult himself, and strikes down from above. The assassin rolls to dodge. The bamboo pole shatters into scattered ink traces. Strike three — the swordsman's blade tip points at the other assassin's throat; the assassin blocks with a short blade, and the camera captures the fine detail of ink traces cracking where the blades grind. (0:18 - 0:20) Camera: Slow motion to freeze frame. * Scene: The swordsman's blade stops at the assassin's neck, the assassin frozen. * Detail: The swordsman's bamboo hat is slightly tilted from the fight. The bamboo forest returns to calm, more bamboo leaves dancing. * Atmosphere: The camera slowly pulls back to medium shot, freezing on the swordsman sheathing his blade and the assassin falling. * Text (optional): Ink-wash style text appears at the bottom: \"The world of martial arts — settled with a single stroke.\" Style note: Throughout, maintain the highly black-and-white, ink-wash painting style of Image 1 . Actions must have a calligraphic brush feel, speed must be fast, details must be rich (ink drops, sparks, ink crack marks).",
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
| `image` | string | yes | URL of the image used as the first frame (JPEG, PNG, BMP, or WebP). Cannot be combined with `images`, `videos`, or `audios`.  |
| `prompt` | string | yes | Text prompt describing the motion to generate.  |
| `duration` | enum |  | Output duration in seconds (2-30), or `auto` to let the model pick a length from the prompt and inputs. `auto` is pre-authorized at 30 seconds and billed on the actual output length. one of: `auto`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12` …; default `5` |
| `end_image` | string |  | URL of the image used as the last frame (JPEG, PNG, BMP, or WebP). Cannot be combined with `images`, `videos`, or `audios`.  |
| `resolution` | string |  | Output video resolution tier. one of: `480p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to match the input image. one of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `generate_audio` | boolean |  | Generate a synchronized audio track. Pricing is the same either way. default `true` |

## Details

Start a clip from your own picture. `image` becomes the exact first frame; add `end_image` and the model interpolates the motion between the two. Clips run 2–30 seconds with native audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 5,000 characters. |
| `image` | image URL, required | — | First frame. JPEG/PNG/BMP/WebP, 240–8000px per side, ≤20MB, no transparency. |
| `end_image` | image URL | — | Last frame; needs `image`. |
| `duration` | 2–30 or `auto` | 5 | `auto` lets the model pick the length. |
| `resolution` | `480p` / `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `aspect_ratio` | `adaptive` / `21:9` / `16:9` / `4:3` / `1:1` / `3:4` / `9:16` | `adaptive` | `adaptive` follows the prompt and inputs. |
| `generate_audio` | boolean | true | Native dialogue, music, and effects. Same price on or off. |
| `seed` | integer 0–2147483647 | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds only: $0.05 at 480p, $0.10 at 720p, $0.20 at 1080p. Input images, audio, and video are not metered. The frame images are free.

| Output | Billed | 480p | 720p | 1080p |
|---|---|---|---|---|
| 2s | 2s | $0.10 | $0.20 | $0.40 |
| 5s (default) | 5s | $0.25 | $0.50 | $1.00 |
| 10s | 10s | $0.50 | $1.00 | $2.00 |
| 30s | 30s | $1.50 | $3.00 | $6.00 |

With `duration: "auto"` the run is pre-authorized at 30 seconds, then settled on the length that was actually generated. Failed runs are not charged. Output files are copied to SandBase storage and the returned URL stays valid for 7 days; download anything you need to keep.

### Prompting

- Describe what moves, not what is already visible: “she turns toward the lens as wind lifts her scarf”.
- With two frames, keep them compatible in framing and lighting, or describe the transition explicitly.
- Leave `aspect_ratio` on `adaptive` to keep the image's own proportions.

> The subject slowly turns toward the camera as a breeze moves the fabric; subtle handheld push-in, natural daylight, no dialogue.

### Limits

- Reference images, videos, and audio are not accepted here; use reference-to-video instead.

### Also on SandBase

Other Wan 3.0 endpoints: `alibaba/wan/3.0/video` (all modes in one schema), `alibaba/wan/3.0/text-to-video`, `alibaba/wan/3.0/reference-to-video`, `alibaba/wan/3.0/video-edit`, `alibaba/wan/3.0/video-extend`.

---
Machine-readable: [`catalog/models/alibaba/wan/3.0/image-to-video.json`](../../../../../catalog/models/alibaba/wan/3.0/image-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/3.0/image-to-video
