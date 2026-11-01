# FlashVSR

`alibaba/flashvsr` · video · Alibaba

FlashVSR is a video super-resolution model that upscales videos to higher resolutions (720p / 1080p / 2K / 4K) with fast inference.

## Pricing

- Depends on parameters (`params.resolution`, `usage.duration`).

Formula: `(usage.duration ?? 5.0) * ((params.resolution ?? "1080p") == "4k" ? 0.124 : (params.resolution ?? "1080p") == "2k" ? 0.055 : (params.resolution ?? "1080p") == "1080p" ? 0.031 : 0.014)`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/flashvsr", "video": "<video>", "resolution": "1080p"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/flashvsr', {'video': '<video>', 'resolution': '1080p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/flashvsr", {
  "video": "<video>",
  "resolution": "1080p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/flashvsr", sandbase.Params{
	"video": "<video>",
	"resolution": "1080p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video` | string | yes | Input video URL (HTTPS, publicly accessible).  |
| `resolution` | string | yes | Target output resolution. one of: `720p`, `1080p`, `2k`, `4k`; default `"1080p"` |

## Details

Upscale an existing video to 720p, 1080p, 2K, or 4K with FlashVSR's fast video super-resolution, which restores detail while keeping motion stable.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `video` | video URL, required | — | Video to upscale. |
| `resolution` | `720p` / `1080p` / `2k` / `4k`, required | `1080p` | Target resolution; sets the per-second rate. |

### Billing

You pay per second of output video: $0.014 at 720p, $0.031 at 1080p, $0.055 at 2K, and $0.124 at 4K. The quote before submission assumes 5 seconds; the final charge uses the measured length.

| Video length | 720p | 1080p | 2k | 4k |
|---|---|---|---|---|
| 5s | $0.07 | $0.155 | $0.275 | $0.62 |
| 10s | $0.14 | $0.31 | $0.55 | $1.24 |
| 30s | $0.42 | $0.93 | $1.65 | $3.72 |

Failed runs are not charged.

### Limits

- Upscaling restores detail but cannot fix heavy blur or compression artifacts completely.

### Also on SandBase

Related: `bytedance/upscaler/video` (ByteDance video upscaler).

---
Machine-readable: [`catalog/models/alibaba/flashvsr.json`](../../../catalog/models/alibaba/flashvsr.json) · Store page: https://www.sandbase.ai/model/alibaba/flashvsr
