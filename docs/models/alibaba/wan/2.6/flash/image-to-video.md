# Wan 2.6 Flash Image to Video API: pricing, parameters and code examples

`alibaba/wan/2.6/flash/image-to-video` · video generation model · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.25 to $1.125 per run, depending on parameters · **Modes:** async

Wan 2.6 Flash by Alibaba - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera movement, and optional audio generation.

## Pricing

- Depends on parameters (`params.duration`, `params.resolution`).

| parameters | USD |
|---|---|
| duration=5, resolution="720p" | 0.25 |
| duration=5, resolution="1080p" | 0.375 |
| duration=10, resolution="720p" | 0.5 |
| duration=10, resolution="1080p" | 0.75 |
| duration=15, resolution="720p" | 0.75 |
| duration=15, resolution="1080p" | 1.125 |

Formula: `(params.resolution ?? "720p") == "1080p" ? (params.duration ?? 5) * 0.075 : (params.duration ?? 5) * 0.05`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/wan/2.6/flash/image-to-video", "image": "https://static.sandbase.ai/examples/1c66bd9f-8155-4927-a5f3-d1a461ddaa02/input/c7880d2b-2ceb-4e39-bf4e-0a3051024917.png", "prompt": "A comedic cinematic demo where typed prompts physically transform reality. Photoreal, strong match cuts, coherent main character, no subtitles.\n\nShot 1 [0-4s] Continue from first frame. The creator presses \"PRINT\". The machine clunks like a spaceship. Creator whispers: \"Okay… I'\''m pressing enter.\"\nShot 2 [4-8s] Smash cut: the printed paper flies into the air and unfolds into a full desert canyon scene around the desk, like reality is being unrolled. Creator says: \"Wait—my prompt has physics?\"\nShot 3 [8-12s] Hard cut: the paper tears and reveals a tropical jungle behind it, perfectly lit, cinematic sun. Creator laughs: \"This is exactly why we do AI.\"\nShot 4 [12-15s] Hard cut back to studio. The printer prints a final line (not shown clearly). Creator looks to camera: \"Multi-scene. Single prompt.\""}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/wan/2.6/flash/image-to-video', {'image': 'https://static.sandbase.ai/examples/1c66bd9f-8155-4927-a5f3-d1a461ddaa02/input/c7880d2b-2ceb-4e39-bf4e-0a3051024917.png', 'prompt': 'A comedic cinematic demo where typed prompts physically transform reality. Photoreal, strong match cuts, coherent main character, no subtitles.\n\nShot 1 [0-4s] Continue from first frame. The creator presses "PRINT". The machine clunks like a spaceship. Creator whispers: "Okay… I\'m pressing enter."\nShot 2 [4-8s] Smash cut: the printed paper flies into the air and unfolds into a full desert canyon scene around the desk, like reality is being unrolled. Creator says: "Wait—my prompt has physics?"\nShot 3 [8-12s] Hard cut: the paper tears and reveals a tropical jungle behind it, perfectly lit, cinematic sun. Creator laughs: "This is exactly why we do AI."\nShot 4 [12-15s] Hard cut back to studio. The printer prints a final line (not shown clearly). Creator looks to camera: "Multi-scene. Single prompt."'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/wan/2.6/flash/image-to-video", {
  "image": "https://static.sandbase.ai/examples/1c66bd9f-8155-4927-a5f3-d1a461ddaa02/input/c7880d2b-2ceb-4e39-bf4e-0a3051024917.png",
  "prompt": "A comedic cinematic demo where typed prompts physically transform reality. Photoreal, strong match cuts, coherent main character, no subtitles.\n\nShot 1 [0-4s] Continue from first frame. The creator presses \"PRINT\". The machine clunks like a spaceship. Creator whispers: \"Okay… I'm pressing enter.\"\nShot 2 [4-8s] Smash cut: the printed paper flies into the air and unfolds into a full desert canyon scene around the desk, like reality is being unrolled. Creator says: \"Wait—my prompt has physics?\"\nShot 3 [8-12s] Hard cut: the paper tears and reveals a tropical jungle behind it, perfectly lit, cinematic sun. Creator laughs: \"This is exactly why we do AI.\"\nShot 4 [12-15s] Hard cut back to studio. The printer prints a final line (not shown clearly). Creator looks to camera: \"Multi-scene. Single prompt.\""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/wan/2.6/flash/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/1c66bd9f-8155-4927-a5f3-d1a461ddaa02/input/c7880d2b-2ceb-4e39-bf4e-0a3051024917.png",
	"prompt": "A comedic cinematic demo where typed prompts physically transform reality. Photoreal, strong match cuts, coherent main character, no subtitles.\n\nShot 1 [0-4s] Continue from first frame. The creator presses \"PRINT\". The machine clunks like a spaceship. Creator whispers: \"Okay… I'm pressing enter.\"\nShot 2 [4-8s] Smash cut: the printed paper flies into the air and unfolds into a full desert canyon scene around the desk, like reality is being unrolled. Creator says: \"Wait—my prompt has physics?\"\nShot 3 [8-12s] Hard cut: the paper tears and reveals a tropical jungle behind it, perfectly lit, cinematic sun. Creator laughs: \"This is exactly why we do AI.\"\nShot 4 [12-15s] Hard cut back to studio. The printer prints a final line (not shown clearly). Creator looks to camera: \"Multi-scene. Single prompt.\"",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `seed` | integer |  | Random seed for reproducibility. If None, a random seed is chosen.  |
| `audio` | string |  | URL of the audio to use as the background music. Must be publicly accessible. Limit handling: If the audio duration exceeds the duration value (5, 10, or 15 seconds), the audio is truncated to the first N seconds, and…  |
| `image` | string | yes | URL of the image to use as the first frame. Must be publicly accessible or base64 data URI. Image dimensions must be between 240 and 7680.  |
| `prompt` | string | yes | The text prompt describing the desired video motion. Max 800 characters.  |
| `duration` | integer |  | Duration of the generated video in seconds. Choose between 5, 10 or 15 seconds. one of: `5`, `10`, `15`; default `5` |
| `resolution` | string |  | Video resolution. Valid values: 720p, 1080p one of: `720p`, `1080p`; default `"720p"` |
| `multi_shots` | boolean |  | When true, enables intelligent multi-shot segmentation. Only active when enable_prompt_expansion is True. Set to false for single-shot generation. default `false` |

## Details

The fast, lower-cost Wan 2.6 image-to-video tier. Animate a picture into a 5, 10, or 15 second clip; turn on `multi_shots` to let the model cut between shots.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Text instruction. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `audio` | audio URL | — | Optional WAV/MP3 URL that drives speech or rhythm. |
| `resolution` | `720p` / `1080p` | `720p` | Sets the per-second rate. |
| `duration` | 5 / 10 / 15 | 5 | Output length in seconds. |
| `multi_shots` | boolean | false | Let the model cut between several shots. |
| `seed` | integer | random | Fix it to compare prompt changes. |

### Billing

You pay for output seconds: $0.05 at 720p and $0.075 at 1080p.

| Output | 720p | 1080p |
|---|---|---|
| 5s (default) | $0.25 | $0.375 |
| 10s | $0.50 | $0.75 |
| 15s | $0.75 | $1.125 |

Failed runs are not charged.

### Prompting

- Describe the motion and camera move in one or two sentences.
- With `multi_shots`, list the shots in order.

### Limits

- Use the non-Flash tier when motion quality matters more than speed and cost.

### Also on SandBase

Other Wan 2.6 endpoints: `alibaba/wan/2.6/text-to-video`, `alibaba/wan/2.6/image-to-video`, `alibaba/wan/2.6/reference-to-video`, `alibaba/wan/2.6/flash/reference-to-video`, `alibaba/wan/2.6/text-to-image`, `alibaba/wan/2.6/image-to-image`, `alibaba/wan/2.7/text-to-video` (newer).

---
Machine-readable: [`catalog/models/alibaba/wan/2.6/flash/image-to-video.json`](../../../../../../catalog/models/alibaba/wan/2.6/flash/image-to-video.json) · Store page: https://www.sandbase.ai/model/alibaba/wan/2.6/flash/image-to-video
