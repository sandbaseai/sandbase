# Sync 3 Avatar Image to Video

`sync/lipsync/3.0/image-to-video` · video · Sync Labs

Sync 3 animates the face in a still image so it speaks the provided audio; the output matches the audio length.

## Pricing

- Depends on parameters (`params.audio`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.audio) ?? 5.0) * 0.135`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sync/lipsync/3.0/image-to-video", "audio": "https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/b3a8612b-d1e8-4efb-97c0-34d3cd05a581.wav", "image": "https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/0b00a2c7-affa-4bef-9e70-4f1526d9579a.png"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sync/lipsync/3.0/image-to-video', {'audio': 'https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/b3a8612b-d1e8-4efb-97c0-34d3cd05a581.wav', 'image': 'https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/0b00a2c7-affa-4bef-9e70-4f1526d9579a.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sync/lipsync/3.0/image-to-video", {
  "audio": "https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/b3a8612b-d1e8-4efb-97c0-34d3cd05a581.wav",
  "image": "https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/0b00a2c7-affa-4bef-9e70-4f1526d9579a.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sync/lipsync/3.0/image-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/b3a8612b-d1e8-4efb-97c0-34d3cd05a581.wav",
	"image": "https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/0b00a2c7-affa-4bef-9e70-4f1526d9579a.png",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `audio` | string | yes | Input audio URL.  |
| `image` | string | yes | Input image URL (face / character).  |

## Details

Sync 3 Avatar animates the face in a still image so it speaks the provided audio.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `image` | image URL, required | — | Face to animate. JPEG, PNG, or WebP URL. |
| `audio` | audio URL, required | — | Speech to sync. |

### Billing

$0.135 per output second. The quote before submission assumes 5 seconds; the final charge uses the measured length.

| Output | Price |
|---|---|
| 5s | $0.675 |
| 30s | $4.05 |
| 60s | $8.10 |

Failed runs are not charged.

### Also on SandBase

Related: `sync/lipsync/3.0/video-to-video`.

---
Machine-readable: [`catalog/models/sync/lipsync/3.0/image-to-video.json`](../../../../../catalog/models/sync/lipsync/3.0/image-to-video.json) · Store page: https://www.sandbase.ai/model/sync/lipsync/3.0/image-to-video
