# Kling V2.5 Turbo Pro Image to Video

`kwaivgi/kling-video/v2.5-turbo/pro/image-to-video` · video · KwaiVGI

Kling V2.5 Turbo Pro Image to Video by Kuaishou animates a start image, optionally toward an end image, into a 5 or 10 second 1080p video.

## Pricing

- Depends on parameters (`params.duration`).

| parameters | USD |
|---|---|
| duration=5 | 0.35 |
| duration=10 | 0.7 |

Formula: `(params.duration ?? 5) * 0.07`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/v2.5-turbo/pro/image-to-video", "image": "https://static.sandbase.ai/examples/dc8717a4-7f50-4560-acb5-05b147c2fc36/input/90d04b52-8c2a-4087-bc91-e210cecde31d.jpg", "prompt": "A stark starting line divides two powerful cars, engines revving for the challenge ahead. They surge forward in the heat of competition, a blur of speed and chrome. The finish line looms as they vie for victory."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/v2.5-turbo/pro/image-to-video', {'image': 'https://static.sandbase.ai/examples/dc8717a4-7f50-4560-acb5-05b147c2fc36/input/90d04b52-8c2a-4087-bc91-e210cecde31d.jpg', 'prompt': 'A stark starting line divides two powerful cars, engines revving for the challenge ahead. They surge forward in the heat of competition, a blur of speed and chrome. The finish line looms as they vie for victory.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/v2.5-turbo/pro/image-to-video", {
  "image": "https://static.sandbase.ai/examples/dc8717a4-7f50-4560-acb5-05b147c2fc36/input/90d04b52-8c2a-4087-bc91-e210cecde31d.jpg",
  "prompt": "A stark starting line divides two powerful cars, engines revving for the challenge ahead. They surge forward in the heat of competition, a blur of speed and chrome. The finish line looms as they vie for victory."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/v2.5-turbo/pro/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/dc8717a4-7f50-4560-acb5-05b147c2fc36/input/90d04b52-8c2a-4087-bc91-e210cecde31d.jpg",
	"prompt": "A stark starting line divides two powerful cars, engines revving for the challenge ahead. They surge forward in the heat of competition, a blur of speed and chrome. The finish line looms as they vie for victory.",
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
| `end_image` | string |  | URL of the image to be used for the end of the video  |

## Details

Kling V2.5 Turbo Pro image-to-video: fast, low-cost 5 or 10 second clips without audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | 5 / 10 | 5 | Output length in seconds. |

### Billing

$0.07 per output second.

| Output | Price |
|---|---|
| 5s (default) | $0.35 |
| 10s | $0.70 |

Failed runs are not charged.

### Prompting

- Describe subject, action, camera move, and light in order.

### Limits

- Clips are 5 or 10 seconds; no audio.

### Also on SandBase

Other V2.5 Turbo endpoints: `kwaivgi/kling-video/v2.5-turbo/pro/text-to-video`, `kwaivgi/kling-video/v2.5-turbo/standard/image-to-video`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/v2.5-turbo/pro/image-to-video.json`](../../../../../../catalog/models/kwaivgi/kling-video/v2.5-turbo/pro/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/v2.5-turbo/pro/image-to-video
