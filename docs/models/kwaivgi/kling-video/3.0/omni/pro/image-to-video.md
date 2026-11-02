# Kling 3.0 Omni Pro Image to Video API: pricing, parameters and code examples

`kwaivgi/kling-video/3.0/omni/pro/image-to-video` · video generation model · KwaiVGI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.336 to $0.896 per run, depending on parameters · **Modes:** async

Kling 3.0 Omni Pro Image to Video by Kuaishou animates a start image, optionally toward an end image, into a 3-10 second 1080p video.

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
  -d '{"model": "kwaivgi/kling-video/3.0/omni/pro/image-to-video", "image": "https://static.sandbase.ai/examples/7f4e8da8-e302-4874-b924-fdaf5f2cd499/input/60106a2d-39fe-470a-b171-aec331266b39.png", "prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k."}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/3.0/omni/pro/image-to-video', {'image': 'https://static.sandbase.ai/examples/7f4e8da8-e302-4874-b924-fdaf5f2cd499/input/60106a2d-39fe-470a-b171-aec331266b39.png', 'prompt': 'Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/3.0/omni/pro/image-to-video", {
  "image": "https://static.sandbase.ai/examples/7f4e8da8-e302-4874-b924-fdaf5f2cd499/input/60106a2d-39fe-470a-b171-aec331266b39.png",
  "prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/3.0/omni/pro/image-to-video", sandbase.Params{
	"image": "https://static.sandbase.ai/examples/7f4e8da8-e302-4874-b924-fdaf5f2cd499/input/60106a2d-39fe-470a-b171-aec331266b39.png",
	"prompt": "Create a magical timelapse transition. The snow melts rapidly to reveal green grass, and the tree branches burst into bloom with pink flowers in real-time. The lighting shifts from cold winter light to warm spring sunshine. The camera pushes in slowly towards the tree. Disney-style magical transformation, cinematic, 8k.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `image` | string | yes | Image to use as the first frame of the video. Max file size: 10.0MB, Min width: 300px, Min height: 300px, Min aspect ratio: 0.40, Max aspect ratio: 2.50, Timeout: 20.0s  |
| `prompt` | string | yes | Use @Image1 to reference the start frame, @Image2 to reference the end frame.  |
| `duration` | integer |  | Video duration in seconds. one of: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`; default `5` |
| `end_image` | string |  | Image to use as the last frame of the video.  |

## Details

Kling 3.0 Omni Pro image-to-video: animate a first frame, optionally toward an end frame, over 3–10 seconds.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Up to 2,500 characters. |
| `image` | image URL, required | — | First frame. JPEG, PNG, or WebP URL. |
| `end_image` | image URL | — | Optional last frame. |
| `duration` | 3–10 | 5 | Output length in seconds. |

### Billing

$0.112 per output second.

| Output | Price |
|---|---|
| 3s | $0.336 |
| 5s (default) | $0.56 |
| 10s | $1.12 |

Failed runs are not charged.

### Prompting

- Describe what moves and how the camera behaves.

### Limits

- Clips are 3–10 seconds.

### Also on SandBase

Other Kling 3.0 Omni endpoints: `kwaivgi/kling-video/3.0/omni/pro/reference-to-video`, `kwaivgi/kling-video/3.0/omni/pro/video-to-video/edit`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/3.0/omni/pro/image-to-video.json`](../../../../../../../catalog/models/kwaivgi/kling-video/3.0/omni/pro/image-to-video.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/3.0/omni/pro/image-to-video
