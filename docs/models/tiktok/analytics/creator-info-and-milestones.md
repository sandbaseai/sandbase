# TikTok Creator Info and Milestones API: pricing, parameters and code examples

`tiktok/analytics/creator-info-and-milestones` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns creator details and milestone history for a specified TikTok account. Looks up account growth events and metrics using the creator's user ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/analytics/creator-info-and-milestones", "user_id": "107955"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/analytics/creator-info-and-milestones', {'user_id': '107955'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/analytics/creator-info-and-milestones", {
  "user_id": "107955"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/analytics/creator-info-and-milestones", sandbase.Params{
	"user_id": "107955",
})
```

Same call via the path form: `POST /v1/api/tiktok/analytics/creator-info-and-milestones` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Creator user ID, required parameter, can be obtained from user profile URL or TikTok backend  |

## Details

Retrieve creator profile metrics and achievement milestones using the required `user_id`. This endpoint outlines account growth trajectory and historical events.

### Use cases

- Review historical follower milestones for specific TikTok creators.
- Analyze creator growth timelines and major achievement dates.
- Track account development trajectories for influencer performance evaluations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/analytics/creator-info-and-milestones" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "107955"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Creator user ID, required parameter, can be obtained from user profile URL or TikTok backend |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "milestones": [
    {
      "creator_summary": {
        "value": "No public data to display"
      },
      "milestone_month_day": {
        "value": "10/4"
      },
      "milestone_title": {
        "value": "Reached 1M followers"
      },
      "milestone_year": {
        "value": "2015"
      }
    }
  ]
}
```

### Notes

- `user_id` is required and can be found in the creator profile URL or TikTok backend.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video Comment Keywords](/model/tiktok/analytics/comment-keywords): Returns extracted keywords and topics from user comments on a TikTok video.
- [Detect fake views in video](/model/tiktok/analytics/detect-fake-views): Check whether a TikTok video has fake views.
- [TikTok Video Metrics](/model/tiktok/analytics/video-metrics): Retrieve detailed analytics for TikTok videos, including total views, likes, comments, favorites, and 14-day daily performance trends using a video identifier.

---
Machine-readable: [`catalog/models/tiktok/analytics/creator-info-and-milestones.json`](../../../../catalog/models/tiktok/analytics/creator-info-and-milestones.json) · Store page: https://www.sandbase.ai/model/tiktok/analytics/creator-info-and-milestones
