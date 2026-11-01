# Kling V2.5 Turbo Standard Image to Video

`kwaivgi/kling-video/v2.5-turbo/standard/image-to-video` · video · KwaiVGI

Kling V2.5 Turbo Standard Image to Video by Kuaishou animates a start image into a 5 or 10 second 720p video.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=5 | 0.21 |
| duration=10 | 0.42 |

Formula: `(params.duration ?? 5) * 0.042`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v2.5-turbo/standard/image-to-video", "image": "https://static.sandbase.ai/examples/e4ba3afb-2028-4b80-9685-5dfc3c506634/input/ba3214f2-96a8-4a28-b7e4-a4250999105e.jpg", "prompt": "Fine grains of salt drift across the flats in a slow, low wind, streaming past the figure'\''s feet. The figure'\''s robe ripples. Light crawls down the face of the monolith as the sun rises millimeter by millimeter — a slow wash of coral replacing indigo. The figure tilts their head upward. Camera creeps forward almost imperceptibly. Monumental, spiritual, glacial."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v2.5-turbo/standard/image-to-video', {'image': 'https://static.sandbase.ai/examples/e4ba3afb-2028-4b80-9685-5dfc3c506634/input/ba3214f2-96a8-4a28-b7e4-a4250999105e.jpg', 'prompt': "Fine grains of salt drift across the flats in a slow, low wind, streaming past the figure's feet. The figure's robe ripples. Light crawls down the face of the monolith as the sun rises millimeter by millimeter — a slow wash of coral replacing indigo. The figure tilts their head upward. Camera creeps forward almost imperceptibly. Monumental, spiritual, glacial."})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v2.5-turbo/standard/image-to-video", {
  "image": "https://static.sandbase.ai/examples/e4ba3afb-2028-4b80-9685-5dfc3c506634/input/ba3214f2-96a8-4a28-b7e4-a4250999105e.jpg",
  "prompt": "Fine grains of salt drift across the flats in a slow, low wind, streaming past the figure's feet. The figure's robe ripples. Light crawls down the face of the monolith as the sun rises millimeter by millimeter — a slow wash of coral replacing indigo. The figure tilts their head upward. Camera creeps forward almost imperceptibly. Monumental, spiritual, glacial."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v2.5-turbo/standard/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/e4ba3afb-2028-4b80-9685-5dfc3c506634/input/ba3214f2-96a8-4a28-b7e4-a4250999105e.jpg",
	"prompt": "Fine grains of salt drift across the flats in a slow, low wind, streaming past the figure's feet. The figure's robe ripples. Light crawls down the face of the monolith as the sun rises millimeter by millimeter — a slow wash of coral replacing indigo. The figure tilts their head upward. Camera creeps forward almost imperceptibly. Monumental, spiritual, glacial.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | URL of the image to be used for the video  |
| `prompt` | string | yes | Prompt  |
| `duration` | integer |  | The duration of the generated video in seconds one of: `5`, `10`; default `5` |

## Details

Kling V2.5 Turbo Standard image-to-video: fast, low-cost 5 or 10 second clips without audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |

### Billing

$0.042 per output second.

| Output | Price |
|---|---|
| 5s (default) | $0.21 |
| 10s | $0.42 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order.

### Limits

- Clips are 5 or 10 seconds; no audio.

### Also on SandBase

Other V2.5 Turbo endpoints: `kwaivgi/kling-video/v2.5-turbo/pro/image-to-video`, `kwaivgi/kling-video/v2.5-turbo/pro/text-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v2.5-turbo/standard/image-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v2.5-turbo/standard/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v2.5-turbo/standard/image-to-video
