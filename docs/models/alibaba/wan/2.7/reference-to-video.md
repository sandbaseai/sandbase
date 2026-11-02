# Wan 2.7 Reference to Video API: pricing, parameters and code examples

`alibaba/wan/2.7/reference-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.2 to $1.05 per run, depending on parameters · **Modes:** async

Alibaba Wan 2.7 reference-to-video model generating video guided by reference content.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`, `params.videos`).

| parameters | USD |
|---|---|
| duration=2, resolution="720p" | 0.2 |
| duration=2, resolution="1080p" | 0.3 |
| duration=3, resolution="720p" | 0.3 |
| duration=3, resolution="1080p" | 0.45 |
| duration=4, resolution="720p" | 0.4 |
| duration=4, resolution="1080p" | 0.6 |
| duration=5, resolution="720p" | 0.5 |
| duration=5, resolution="1080p" | 0.75 |
| duration=6, resolution="720p" | 0.6 |
| duration=6, resolution="1080p" | 0.9 |
| duration=7, resolution="720p" | 0.7 |
| duration=7, resolution="1080p" | 1.05 |

Formula: `((params.duration ?? 5) + (len(params.videos ?? []) > 0 ? 5 : 0)) * ((params.resolution ?? "720p") == "1080p" ? 0.15 : 0.10)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.7/reference-to-video", "images": ["https://static.sandbase.ai/examples/6ec7122b-e121-4332-aac6-9564b61c6067/input/b1c60c74-e701-44d8-8f6a-c50b4cb6ffa0.webp"], "prompt": "Reference image, 3D cartoon adventure movie style, chibi characters with detailed textures, smooth actions, and vibrant colors. Keep the characters and forest scene consistent. Do not add text. Atmosphere: Adventurous, lighthearted, mysterious, whimsical. Characters: Boy explorer: round hat, backpack, short cloak. Sidekick: a flying small robot with a round body and blue glowing eyes. Scene: Fantasy forest with giant tree roots, mushrooms, vines, a treasure cave entrance, and sunbeams. Storyboard: 1. Wide shot: Tall trees and interlaced light beams in a mysterious and bright fantasy forest. 2. Medium shot: The boy pushes aside vines to explore. 3. Medium shot: The small robot flies beside him, scanning ahead with a blue light. 4. Close-up: An old treasure map unfolds in the boy'\''s hands. 5. Close-up: He shows an excited expression, his eyes lighting up. 6. Action shot: The two jump over tree roots and a stream, continuing deeper into the forest. 7. Medium shot: A moss-covered treasure chest is revealed behind the vines. 8. Close-up: A golden glow shines from the edge of the treasure chest. 9. Final shot: The boy and the small robot stand before the treasure chest, looking at each other in surprise, full of adventure."}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.7/reference-to-video', {'images': ['https://static.sandbase.ai/examples/6ec7122b-e121-4332-aac6-9564b61c6067/input/b1c60c74-e701-44d8-8f6a-c50b4cb6ffa0.webp'], 'prompt': "Reference image, 3D cartoon adventure movie style, chibi characters with detailed textures, smooth actions, and vibrant colors. Keep the characters and forest scene consistent. Do not add text. Atmosphere: Adventurous, lighthearted, mysterious, whimsical. Characters: Boy explorer: round hat, backpack, short cloak. Sidekick: a flying small robot with a round body and blue glowing eyes. Scene: Fantasy forest with giant tree roots, mushrooms, vines, a treasure cave entrance, and sunbeams. Storyboard: 1. Wide shot: Tall trees and interlaced light beams in a mysterious and bright fantasy forest. 2. Medium shot: The boy pushes aside vines to explore. 3. Medium shot: The small robot flies beside him, scanning ahead with a blue light. 4. Close-up: An old treasure map unfolds in the boy's hands. 5. Close-up: He shows an excited expression, his eyes lighting up. 6. Action shot: The two jump over tree roots and a stream, continuing deeper into the forest. 7. Medium shot: A moss-covered treasure chest is revealed behind the vines. 8. Close-up: A golden glow shines from the edge of the treasure chest. 9. Final shot: The boy and the small robot stand before the treasure chest, looking at each other in surprise, full of adventure."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.7/reference-to-video", {
  "images": [
    "https://static.sandbase.ai/examples/6ec7122b-e121-4332-aac6-9564b61c6067/input/b1c60c74-e701-44d8-8f6a-c50b4cb6ffa0.webp"
  ],
  "prompt": "Reference image, 3D cartoon adventure movie style, chibi characters with detailed textures, smooth actions, and vibrant colors. Keep the characters and forest scene consistent. Do not add text. Atmosphere: Adventurous, lighthearted, mysterious, whimsical. Characters: Boy explorer: round hat, backpack, short cloak. Sidekick: a flying small robot with a round body and blue glowing eyes. Scene: Fantasy forest with giant tree roots, mushrooms, vines, a treasure cave entrance, and sunbeams. Storyboard: 1. Wide shot: Tall trees and interlaced light beams in a mysterious and bright fantasy forest. 2. Medium shot: The boy pushes aside vines to explore. 3. Medium shot: The small robot flies beside him, scanning ahead with a blue light. 4. Close-up: An old treasure map unfolds in the boy's hands. 5. Close-up: He shows an excited expression, his eyes lighting up. 6. Action shot: The two jump over tree roots and a stream, continuing deeper into the forest. 7. Medium shot: A moss-covered treasure chest is revealed behind the vines. 8. Close-up: A golden glow shines from the edge of the treasure chest. 9. Final shot: The boy and the small robot stand before the treasure chest, looking at each other in surprise, full of adventure."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.7/reference-to-video", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/6ec7122b-e121-4332-aac6-9564b61c6067/input/b1c60c74-e701-44d8-8f6a-c50b4cb6ffa0.webp"},
	"prompt": "Reference image, 3D cartoon adventure movie style, chibi characters with detailed textures, smooth actions, and vibrant colors. Keep the characters and forest scene consistent. Do not add text. Atmosphere: Adventurous, lighthearted, mysterious, whimsical. Characters: Boy explorer: round hat, backpack, short cloak. Sidekick: a flying small robot with a round body and blue glowing eyes. Scene: Fantasy forest with giant tree roots, mushrooms, vines, a treasure cave entrance, and sunbeams. Storyboard: 1. Wide shot: Tall trees and interlaced light beams in a mysterious and bright fantasy forest. 2. Medium shot: The boy pushes aside vines to explore. 3. Medium shot: The small robot flies beside him, scanning ahead with a blue light. 4. Close-up: An old treasure map unfolds in the boy's hands. 5. Close-up: He shows an excited expression, his eyes lighting up. 6. Action shot: The two jump over tree roots and a stream, continuing deeper into the forest. 7. Medium shot: A moss-covered treasure chest is revealed behind the vines. 8. Close-up: A golden glow shines from the edge of the treasure chest. 9. Final shot: The boy and the small robot stand before the treasure chest, looking at each other in surprise, full of adventure.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed (0-2147483647) for reproducible results. Omit for a random seed.  |
| `images` | array | yes | The URLs of reference images to guide video generation. Provide at least one reference image or video.  |
| `prompt` | string | yes | The text prompt to generate a video from. default `"A golden retriever puppy running through a field of wildflowers in slow motion, ears flapping, tongue out, soft backlight"` |
| `videos` | array |  | The URLs of reference videos to guide video generation.  |
| `duration` | integer |  | The duration of the generated video in seconds. one of: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13` …; default `5` |
| `resolution` | string |  | The resolution of the video to generate. one of: `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | The aspect ratio of the generated video. one of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |

## Details

Cast people, products, or characters from reference images (and optional reference videos) into a new scene. The prompt directs what they do; Wan 2.7 keeps their appearance consistent and supports several referenced characters interacting in one shot.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 50,000 characters. |
| `images` | image URL[], required | — | Reference images, referred to in the prompt as Image 1, Image 2, … |
| `videos` | video URL[] | — | Optional reference clips, referred to as Video 1, Video 2, … |
| `duration` | 2–15 | 5 | Output length in seconds. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` / `4:3` / `3:4` | — | Output frame shape. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.10 at 720p and $0.15 at 1080p, the same as Alibaba's list price. When you send reference `videos`, 5 seconds of input are added to the billed length.

| Output | 720p | 1080p |
|---|---|---|
| 5s, images only | $0.50 | $0.75 |
| 5s, with reference video | $1.00 | $1.50 |
| 10s, images only | $1.00 | $1.50 |
| 15s, images only | $1.50 | $2.25 |

Failed runs are not charged.

### Prompting

- Give every reference a role: “Image 1 is the chef, Image 2 is the kitchen, Video 1 sets the camera move”.
- Numbering follows array order, so reordering `images` changes what “Image 2” means.
- Keep each reference image to one clear subject.

### Limits

- The output is a new clip; to change an existing video use `alibaba/wan/2.7/video-edit`.

### Also on SandBase

Other Wan 2.7 endpoints: `alibaba/wan/2.7/text-to-video`, `alibaba/wan/2.7/image-to-video`, `alibaba/wan/2.7/video-edit`, `alibaba/wan/2.7/video-extend`, `alibaba/wan/3.0/video` (newer, up to 30s).

---
Machine-readable: [`catalog/models/alibaba/wan/2.7/reference-to-video.json`](../../../../../catalog/models/alibaba/wan/2.7/reference-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.7/reference-to-video
