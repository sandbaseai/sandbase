# Kling 3.0 Omni Pro Reference to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/3.0/omni/pro/reference-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.336 to $0.896 per run, depending on parameters · **Modes:** async

Kling 3.0 Omni Pro Reference to Video by Kuaishou generates a 3-10 second 1080p video that keeps characters and objects from reference images consistent.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=3 | 0.336 |
| duration=4 | 0.448 |
| duration=5 | 0.56 |
| duration=6 | 0.672 |
| duration=7 | 0.784 |
| duration=8 | 0.896 |

Formula: `(params.duration ?? 5) * 0.112`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/3.0/omni/pro/reference-to-video", "images": ["https://static.sandbase.ai/examples/kwaivgi/kling-video/omni/pro/reference-to-video/input_images_0.png", "https://static.sandbase.ai/examples/kwaivgi/kling-video/omni/pro/reference-to-video/input_images_1.png"], "prompt": "Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2."}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/3.0/omni/pro/reference-to-video', {'images': ['https://static.sandbase.ai/examples/kwaivgi/kling-video/omni/pro/reference-to-video/input_images_0.png', 'https://static.sandbase.ai/examples/kwaivgi/kling-video/omni/pro/reference-to-video/input_images_1.png'], 'prompt': 'Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/3.0/omni/pro/reference-to-video", {
  "images": [
    "https://static.sandbase.ai/examples/kwaivgi/kling-video/omni/pro/reference-to-video/input_images_0.png",
    "https://static.sandbase.ai/examples/kwaivgi/kling-video/omni/pro/reference-to-video/input_images_1.png"
  ],
  "prompt": "Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/3.0/omni/pro/reference-to-video", sandbase.Params{
	"images": []any{"https://static.sandbase.ai/examples/kwaivgi/kling-video/omni/pro/reference-to-video/input_images_0.png", "https://static.sandbase.ai/examples/kwaivgi/kling-video/omni/pro/reference-to-video/input_images_1.png"},
	"prompt": "Take @Image1 as the start frame. Start with a high-angle satellite view of the ancient greenhouse ruin surrounded by nature. The camera swoops down and flies inside the building, revealing the character from @Element1 standing in the sun-drenched center. The camera then seamlessly transitions into a smooth 180-degree orbit around the character, moving to the back view. As the open backpack comes into focus, the camera continues to push forward, zooming deep inside the bag to reveal the glowing stone from @Element2 nestled inside. Cinematic lighting, hopeful atmosphere, 35mm lens. Make sure to keep it as the style of @Image2.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `images` | array | yes | Additional reference images for style/appearance. Reference in prompt as @Image1, @Image2, etc. Maximum 7 total (elements + reference images + start image).  |
| `prompt` | string | yes | Take @Element1, @Element2 to reference elements and @Image1, @Image2 to reference images in order.  |
| `duration` | integer |  | Video duration in seconds. one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`; default `5` |
| `elements` | array |  | Elements (characters/objects) to include in the video. Reference in prompt as @Element1, @Element2, etc. Maximum 7 total (elements + reference images + start image).  |
| `aspect_ratio` | string |  | The aspect ratio of the generated image. one of: `16:9`, `9:16`, `1:1`; default `"16:9"` |

## Details

Kling 3.0 Omni Pro reference-to-video: cast characters and objects from reference images (and optional elements) into a new 3–10 second scene.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `images` | image URL[], required | — | Reference images, referred to as @Image1, @Image2, … in the prompt. |
| `duration` | 3–10 | 5 | Output length in seconds. |
| `elements` | object[] | — | Optional character or object elements to keep consistent. |
| `aspect_ratio` | `16:9` / `9:16` / `1:1` | `16:9` | Output frame shape. |

### Billing

$0.112 per output second.

| Output | Price |
|---|---|
| 3s | $0.336 |
| 5s (default) | $0.56 |
| 10s | $1.12 |

Failed runs are not charged.

### Prompting

- Refer to each reference as @Image1, @Image2 and give it a role.

### Limits

- Clips are 3–10 seconds.

### Also on SandBase

Other Kling 3.0 Omni endpoints: `kwaivgi/kling-video/3.0/omni/pro/image-to-video`, `kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/3.0/omni/pro/reference-to-video.json`](../../../../../../../catalog/models/kwaivgi/kling-video/3.0/omni/pro/reference-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/3.0/omni/pro/reference-to-video
