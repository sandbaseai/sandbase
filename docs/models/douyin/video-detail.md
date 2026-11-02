# Douyin Video Details API: pricing, parameters and code examples

`douyin/video-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get details for a Douyin (TikTok China) video by video ID. Use it to look up a known video before content review, archiving, or related analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/video-detail", "videoId": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/video-detail', {'videoId': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/video-detail", {
  "videoId": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/video-detail", sandbase.Params{
	"videoId": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `videoId` | string | yes | The unique video identifier (aweme_id or model_id).  |

## Details

Get details for a Douyin (TikTok China) video by video ID. Use it to look up a known video before content review, archiving, or related analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "7372484719365098803"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique video identifier (aweme_id or model_id). |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/video-detail.json`](../../../catalog/models/douyin/video-detail.json) · Store page: https://www.sandbase.ai/model/douyin/video-detail
