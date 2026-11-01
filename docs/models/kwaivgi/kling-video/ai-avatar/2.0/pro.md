# Kling AI Avatar 2.0 Pro

`kwaivgi/kling-video/ai-avatar/2.0/pro` · video · KwaiVGI

Kling AI Avatar 2.0 Pro by Kuaishou animates a portrait image into a talking-head video lip-synced to an input audio track, at Pro quality.

## Pricing

- Depends on parameters (`params.audio`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.audio) ?? 5.0) * 0.115`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kwaivgi/kling-video/ai-avatar/2.0/pro", "audio": "https://static.sandbase.ai/examples/2344becd-9196-4cec-b002-593f3c58ad87/input/2cddcd9d-dc34-447a-b542-a333350592b9.mp3", "image": "https://static.sandbase.ai/examples/2344becd-9196-4cec-b002-593f3c58ad87/input/fea5b189-ea59-4ce0-bc86-0b3ec493a3f8.jpg", "prompt": "."}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kwaivgi/kling-video/ai-avatar/2.0/pro', {'audio': 'https://static.sandbase.ai/examples/2344becd-9196-4cec-b002-593f3c58ad87/input/2cddcd9d-dc34-447a-b542-a333350592b9.mp3', 'image': 'https://static.sandbase.ai/examples/2344becd-9196-4cec-b002-593f3c58ad87/input/fea5b189-ea59-4ce0-bc86-0b3ec493a3f8.jpg', 'prompt': '.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kwaivgi/kling-video/ai-avatar/2.0/pro", {
  "audio": "https://static.sandbase.ai/examples/2344becd-9196-4cec-b002-593f3c58ad87/input/2cddcd9d-dc34-447a-b542-a333350592b9.mp3",
  "image": "https://static.sandbase.ai/examples/2344becd-9196-4cec-b002-593f3c58ad87/input/fea5b189-ea59-4ce0-bc86-0b3ec493a3f8.jpg",
  "prompt": "."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kwaivgi/kling-video/ai-avatar/2.0/pro", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/2344becd-9196-4cec-b002-593f3c58ad87/input/2cddcd9d-dc34-447a-b542-a333350592b9.mp3",
	"image": "https://static.sandbase.ai/examples/2344becd-9196-4cec-b002-593f3c58ad87/input/fea5b189-ea59-4ce0-bc86-0b3ec493a3f8.jpg",
	"prompt": ".",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audio` | string | yes | The URL of the audio file.  |
| `image` | string | yes | The URL of the image to use as your avatar  |
| `prompt` | string | yes | The prompt to use for the video generation. default `"."` |

## Details

Kling AI Avatar 2.0 Pro: a talking-head video from one portrait and an audio track, with lip sync and natural head motion.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | `.` | Gesture, expression, and scene direction. |
| `image` | image URL, required | — | Portrait. JPEG, PNG, or WebP URL. |
| `audio` | audio URL, required | — | Speech that drives the lips. |

### Billing

$0.115 per output second; the output is as long as the audio. The quote before submission assumes 5 seconds.

| Audio | Price |
|---|---|
| 5s audio | $0.575 |
| 30s audio | $3.45 |
| 60s audio | $6.90 |

Failed runs are not charged.

### Prompting

- Use a front-facing portrait with the mouth visible.

### Limits

- Output length follows the audio.

### Also on SandBase

Related: `kwaivgi/kling-video/ai-avatar/2.0/standard`.

---
Machine-readable: [`catalog/models/kwaivgi/kling-video/ai-avatar/2.0/pro.json`](../../../../../../catalog/models/kwaivgi/kling-video/ai-avatar/2.0/pro.json) · Store page: https://www.sandbase.ai/model/kwaivgi/kling-video/ai-avatar/2.0/pro
