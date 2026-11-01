# Youku Video Details

`youku/video-detail` · api · Youku

Get details for a Youku video identified by video ID. Use it to look up a known video for content review, cataloging, or subsequent video analysis.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youku/video-detail", "videoId": "XNjU1ODM3MjI4NA=="}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youku/video-detail', {'videoId': 'XNjU1ODM3MjI4NA=='})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youku/video-detail", {
  "videoId": "XNjU1ODM3MjI4NA=="
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youku/video-detail", sandbase.Params{
	"videoId": "XNjU1ODM3MjI4NA==",
})
```

Same call via the path form: `POST /v1/api/youku/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `videoId` | string | yes | The unique identifier for the video.  |

## Details

Get details for a Youku video identified by video ID. Use it to look up a known video for content review, cataloging, or subsequent video analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youku/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "XNjU1ODM3MjI4NA=="}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique identifier for the video. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/youku/video-detail.json`](../../../catalog/models/youku/video-detail.json) · Store page: https://www.sandbase.ai/model/youku/video-detail
