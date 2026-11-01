# HeyGen Lipsync Precision

`heygen/lipsync/precision` · video · HeyGen

HeyGen v3 Lipsync (precision) replaces the speech in a video and re-syncs the speaker's lips to the new audio.

## Pricing

- Depends on parameters (`params.audio`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.audio) ?? 5.0) * 0.1`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/lipsync/precision", "audio": "https://static.sandbase.ai/examples/3c0d2094-8315-4f9f-bfbd-1a209d8ab9e0/input/733399b2-2dc9-4da1-93ed-5b156997b3c6.mp3", "video": "https://static.sandbase.ai/examples/3c0d2094-8315-4f9f-bfbd-1a209d8ab9e0/input/c517493c-b3d5-4f92-be2f-684336862d50.mp4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/lipsync/precision', {'audio': 'https://static.sandbase.ai/examples/3c0d2094-8315-4f9f-bfbd-1a209d8ab9e0/input/733399b2-2dc9-4da1-93ed-5b156997b3c6.mp3', 'video': 'https://static.sandbase.ai/examples/3c0d2094-8315-4f9f-bfbd-1a209d8ab9e0/input/c517493c-b3d5-4f92-be2f-684336862d50.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/lipsync/precision", {
  "audio": "https://static.sandbase.ai/examples/3c0d2094-8315-4f9f-bfbd-1a209d8ab9e0/input/733399b2-2dc9-4da1-93ed-5b156997b3c6.mp3",
  "video": "https://static.sandbase.ai/examples/3c0d2094-8315-4f9f-bfbd-1a209d8ab9e0/input/c517493c-b3d5-4f92-be2f-684336862d50.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/lipsync/precision", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/3c0d2094-8315-4f9f-bfbd-1a209d8ab9e0/input/733399b2-2dc9-4da1-93ed-5b156997b3c6.mp3",
	"video": "https://static.sandbase.ai/examples/3c0d2094-8315-4f9f-bfbd-1a209d8ab9e0/input/c517493c-b3d5-4f92-be2f-684336862d50.mp4",
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
| `video` | string | yes | Input video URL.  |
| `end_time` | number |  | End time (seconds) for partial lipsync. range 0– |
| `start_time` | number |  | Start time (seconds) for partial lipsync. range 0– |
| `enable_caption` | boolean |  | Burn in captions. default `false` |
| `disable_music_track` | boolean |  | Remove background music from the source video. default `false` |
| `enable_dynamic_duration` | boolean |  | Allow the video length to follow the new audio. default `true` |
| `enable_speech_enhancement` | boolean |  | Enhance the replacement audio. default `false` |

## Details

HeyGen Lipsync (precision) replaces the speech in a video and re-syncs the speaker's lips to new audio. Precision gives the best sync.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `video` | video URL, required | — | Video with the speaker. |
| `audio` | audio URL, required | — | New speech. |
| `disable_music_track` | boolean | false | Drop background music. |
| `enable_caption` | boolean | false | Burn in captions. |
| `enable_dynamic_duration` | boolean | true | Adjust video length to the new audio. |
| `enable_speech_enhancement` | boolean | false | Clean up the new speech. |
| `end_time` | number | — | Optional end of the section. |
| `start_time` | number | — | Optional start of the section to sync (seconds). |

### Billing

$0.10 per output second. The quote before submission assumes 5 seconds.

| Output | Price |
|---|---|
| 5s | $0.50 |
| 30s | $3.00 |
| 60s | $6.00 |

Failed runs are not charged.

### Also on SandBase

Related: `heygen/lipsync/speed`, `sync/lipsync/3.0/video-to-video`.

---
Machine-readable: [`catalog/models/heygen/lipsync/precision.json`](../../../../catalog/models/heygen/lipsync/precision.json) · Store page: https://www.sandbase.ai/model/heygen/lipsync/precision
