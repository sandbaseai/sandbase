# Sync 3 Lipsync

`sync/lipsync/3.0/video-to-video` · video · Sync Labs

Sync 3 by sync. re-animates the speaker's lips in an existing video to match new audio, with studio-grade identity preservation.

## Pricing

- Depends on parameters (`params.video`, `usage.duration`).

Formula: `(usage.duration ?? media_duration(params.video) ?? 5.0) * 0.135`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sync/lipsync/3.0/video-to-video", "audio": "https://static.sandbase.ai/examples/0041ca28-136b-4673-abf2-5f4b57e4650a/input/86f172e0-e9ae-4108-b088-b329646c8265.wav", "video": "https://static.sandbase.ai/examples/0041ca28-136b-4673-abf2-5f4b57e4650a/input/857176e7-45a6-438a-b4d6-2a6c1c317efe.mp4"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sync/lipsync/3.0/video-to-video', {'audio': 'https://static.sandbase.ai/examples/0041ca28-136b-4673-abf2-5f4b57e4650a/input/86f172e0-e9ae-4108-b088-b329646c8265.wav', 'video': 'https://static.sandbase.ai/examples/0041ca28-136b-4673-abf2-5f4b57e4650a/input/857176e7-45a6-438a-b4d6-2a6c1c317efe.mp4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sync/lipsync/3.0/video-to-video", {
  "audio": "https://static.sandbase.ai/examples/0041ca28-136b-4673-abf2-5f4b57e4650a/input/86f172e0-e9ae-4108-b088-b329646c8265.wav",
  "video": "https://static.sandbase.ai/examples/0041ca28-136b-4673-abf2-5f4b57e4650a/input/857176e7-45a6-438a-b4d6-2a6c1c317efe.mp4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sync/lipsync/3.0/video-to-video", sandbase.Params{
	"audio": "https://static.sandbase.ai/examples/0041ca28-136b-4673-abf2-5f4b57e4650a/input/86f172e0-e9ae-4108-b088-b329646c8265.wav",
	"video": "https://static.sandbase.ai/examples/0041ca28-136b-4673-abf2-5f4b57e4650a/input/857176e7-45a6-438a-b4d6-2a6c1c317efe.mp4",
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
| `sync_mode` | string |  | How to handle audio/video length mismatch. one of: `cut_off`, `loop`, `bounce`, `silence`, `remap`; default `"cut_off"` |

## Details

Sync 3 re-animates the speaker's lips in an existing video to match new audio, with strong identity preservation.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `video` | video URL, required | — | Video with the speaker. |
| `audio` | audio URL, required | — | Speech to sync. |
| `sync_mode` | `cut_off` / `loop` / `bounce` / `silence` / `remap` | `cut_off` | What to do when audio and video lengths differ. |

### Billing

$0.135 per output second. The quote before submission assumes 5 seconds; the final charge uses the measured length.

| Output | Price |
|---|---|
| 5s | $0.675 |
| 30s | $4.05 |
| 60s | $8.10 |

Failed runs are not charged.

### Also on SandBase

Related: `sync/lipsync/3.0/image-to-video`.

---
Machine-readable: [`catalog/models/sync/lipsync/3.0/video-to-video.json`](../../../../../catalog/models/sync/lipsync/3.0/video-to-video.json) · Store page: https://www.sandbase.ai/model/sync/lipsync/3.0/video-to-video
