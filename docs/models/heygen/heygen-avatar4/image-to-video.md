# HeyGen Avatar 4 Image to Video

`heygen/heygen-avatar4/image-to-video` · video · HeyGen

Heygen Avatar4 is HeyGen's image-to-video AI model. Bring static images to life with fluid animation, consistent character motion, and professional-grade video output.

## Pricing

- Depends on parameters (`params.audio`, `usage.duration`).

Formula: `(usage.duration ?? ((params.audio ?? "") != "" ? media_duration(params.audio) : nil) ?? 5.0) * 0.1`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/heygen-avatar4/image-to-video", "image": "https://static.sandbase.ai/examples/58f680f7-93d6-4f27-9255-0043d7b5c44c/input/48d5dacb-cf6b-4678-a54d-dd7bc01337fb.png", "prompt": "Hey friends! Welcome to the GPU force podcast and today we are going to discuss about the rising GPU cost!"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/heygen-avatar4/image-to-video', {'image': 'https://static.sandbase.ai/examples/58f680f7-93d6-4f27-9255-0043d7b5c44c/input/48d5dacb-cf6b-4678-a54d-dd7bc01337fb.png', 'prompt': 'Hey friends! Welcome to the GPU force podcast and today we are going to discuss about the rising GPU cost!'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/heygen-avatar4/image-to-video", {
  "image": "https://static.sandbase.ai/examples/58f680f7-93d6-4f27-9255-0043d7b5c44c/input/48d5dacb-cf6b-4678-a54d-dd7bc01337fb.png",
  "prompt": "Hey friends! Welcome to the GPU force podcast and today we are going to discuss about the rising GPU cost!"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/heygen-avatar4/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/58f680f7-93d6-4f27-9255-0043d7b5c44c/input/48d5dacb-cf6b-4678-a54d-dd7bc01337fb.png",
	"prompt": "Hey friends! Welcome to the GPU force podcast and today we are going to discuss about the rising GPU cost!",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audio` | string |  | URL of an audio file for the avatar to lip-sync to. When provided, overrides prompt and voice.  |
| `image` | string | yes | URL of the image to animate. The image should contain a clear face.  |
| `voice` | string |  | The voice ID to use for the avatar. default `"Melissa"` |
| `prompt` | string |  | The text the avatar will speak  |
| `resolution` | string |  | Video resolution preset. one of: `360p`, `480p`, `540p`, `720p`, `1080p`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to keep the source aspect ratio (falls back to 16:9 when it cannot be read). one of: `16:9`, `9:16`, `4:5`, `5:4`, `1:1` |
| `talking_style` | string |  | Talking style: 'stable' for minimal movement, 'expressive' for more animation. one of: `stable`, `expressive`; default `"stable"` |

## Details

HeyGen Avatar 4: turn a single photo into a talking presenter, driven by a script or an audio track.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Script to speak. |
| `image` | image URL, required | — | Photo of the presenter. JPEG, PNG, or WebP URL. |
| `audio` | audio URL | — | Optional voice track. |
| `aspect_ratio` | `16:9` / `9:16` / `4:5` / `5:4` / `1:1` | — | Output frame shape. |
| `voice` | string | `Melissa` | Voice for the script. |
| `resolution` | `360p` / `480p` / `540p` / `720p` / `1080p` | `720p` | Video resolution preset. |
| `talking_style` | `stable` / `expressive` | `stable` | `expressive` adds more head and hand motion. |

### Billing

$0.10 per output second; length follows the audio or the spoken script. The quote before submission assumes 5 seconds.

| Output | Price |
|---|---|
| 5s | $0.50 |
| 30s | $3.00 |
| 60s | $6.00 |

Failed runs are not charged.

### Prompting

- Use a front-facing photo with the face clearly visible.

### Also on SandBase

Related: `heygen/avatar5/digital-twin`.

---
Machine-readable: [`catalog/models/heygen/heygen-avatar4/image-to-video.json`](../../../../catalog/models/heygen/heygen-avatar4/image-to-video.json) · Store page: https://www.sandbase.ai/model/heygen/heygen-avatar4/image-to-video
