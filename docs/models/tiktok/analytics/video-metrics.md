# TikTok Video Metrics API: pricing, parameters and code examples

`tiktok/analytics/video-metrics` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieve detailed analytics for TikTok videos, including total views, likes, comments, favorites, and 14-day daily performance trends using a video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/analytics/video-metrics", "item_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/analytics/video-metrics', {'item_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/analytics/video-metrics", {
  "item_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/analytics/video-metrics", sandbase.Params{
	"item_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/analytics/video-metrics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video ID, required parameter, can be obtained from video sharing links or TikTok Studio  |

## Details

Retrieve detailed video performance metrics and 14-day daily trends on TikTok by supplying an `item_id`.

### Use cases

- Review engagement metrics such as views, likes, comments, and favorites for individual clips.
- Analyze 14-day daily performance trends to evaluate content effectiveness over time.
- Optimize content strategies based on audience interaction and reach statistics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/analytics/video-metrics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7350810998023949599"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video ID, required parameter, can be obtained from video sharing links or TikTok Studio |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "item_id": "7350810998023949599"
}
```

### Notes

- `item_id` is required and can be obtained from video sharing links or TikTok Studio.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video Comment Keywords](/model/tiktok/analytics/comment-keywords): Returns extracted keywords and topics from user comments on a TikTok video.
- [TikTok Creator Info and Milestones](/model/tiktok/analytics/creator-info-and-milestones): Returns creator details and milestone history for a specified TikTok account.
- [Detect fake views in video](/model/tiktok/analytics/detect-fake-views): Check whether a TikTok video has fake views.

---
Machine-readable: [`catalog/models/tiktok/analytics/video-metrics.json`](../../../../catalog/models/tiktok/analytics/video-metrics.json) · Store page: https://www.sandbase.ai/model/tiktok/analytics/video-metrics
