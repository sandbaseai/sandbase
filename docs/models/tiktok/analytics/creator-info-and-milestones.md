# TikTok Creator Info and Milestones API: pricing, parameters and code examples

`tiktok/analytics/creator-info-and-milestones` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns creator details and milestone history for a specified TikTok account. Looks up account growth events and metrics using the creator's user ID.

## Pricing

- **$0.001 per call** (USD)
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

Returns basic profile data and a list of follower milestones for one TikTok creator. It needs the creator's numeric `user_id`.

### Use cases

- Show when a creator passed 100K, 500K and 1M followers.
- Compare how fast different creators reached their first follower milestones.
- Pull a creator's current follower and like totals next to their growth history for a vetting report.
- Map a numeric `user_id` to the creator's `unique_id` and `sec_user_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/analytics/creator-info-and-milestones" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "107955"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Creator user ID, required parameter, can be obtained from user profile URL or TikTok backend |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "creator_info": {
    "avatar_url": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/ba67b11de451691…",
    "follower_count": 96532195,
    "like_count": 466681716,
    "message": {
      "data_source": 1,
      "status": 1,
      "timestamp": 1793691831
    },
    "nickname": "TikTok",
    "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
    "unique_id": "tiktok"
  },
  "milestones": [
    {
      "creator_summary": {
        "message": {
          "data_source": 1,
          "status": 1,
          "timestamp": 1793691831
        },
        "value": "No public data to display"
      },
      "milestone": 6,
      "milestone_month_day": {
        "message": {
          "data_source": 1,
          "status": 1,
          "timestamp": 1793691831
        },
        "value": "10/4"
      },
      "milestone_title": {
        "message": {
          "data_source": 1,
          "status": 1,
          "timestamp": 1793691831
        },
        "value": "Reached 1M followers"
      },
      "milestone_year": {
        "message": {
          "data_source": 1,
          "status": 1,
          "timestamp": 1793691831
        },
        "value": "2015"
      }
    }
  ],
  "user_id": "107955"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `creator_info.unique_id / creator_info.nickname` | The creator's handle and display name. |
| `creator_info.follower_count / creator_info.like_count` | Total followers and total likes for the account. |
| `creator_info.sec_user_id` | The creator's `sec_user_id`, a longer string ID for the same account. |
| `creator_info.avatar_url` | Link to the creator's profile picture image. |
| `milestones[].milestone` | Number for the milestone step. Higher numbers appear for larger follower targets (6 is 1M, 5 is 500K, 4 is 100K). |
| `milestones[].milestone_title.value` | Text label for the milestone, such as `Reached 1M followers`. |
| `milestones[].milestone_month_day.value / milestones[].milestone_year.value` | The month/day and the year of the milestone, as strings. |
| `milestones[].creator_summary.value` | A summary text for the milestone. It can read `No public data to display`. |
| `user_id` | The `user_id` you sent, echoed back. |

### Notes

- Each milestone value sits inside an object with a `value` and a `message` block. The `message` block holds `data_source`, `status` and `timestamp`.
- `milestone_month_day.value` uses a month/day format without leading zeros, such as `10/4`.
- Milestones come back newest first in the sample response.
- To find videos from this account's era or check view quality, try [TikTok Video Metrics](/apis/tiktok/analytics/video-metrics) or [Detect fake views in video](/apis/tiktok/analytics/detect-fake-views).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video Comment Keywords](/apis/tiktok/analytics/comment-keywords): Returns extracted keywords and topics from user comments on a TikTok video.
- [Detect fake views in video](/apis/tiktok/analytics/detect-fake-views): Check whether a TikTok video has fake views.
- [TikTok Video Metrics](/apis/tiktok/analytics/video-metrics): Retrieve detailed analytics for TikTok videos, including total views, likes, comments, favorites, and 14-day daily performance trends using a video identifier.

---
Machine-readable: [`catalog/models/tiktok/analytics/creator-info-and-milestones.json`](../../../../catalog/models/tiktok/analytics/creator-info-and-milestones.json) · Store page: https://www.sandbase.ai/model/tiktok/analytics/creator-info-and-milestones
