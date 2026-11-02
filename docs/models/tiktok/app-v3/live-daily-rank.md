# TikTok LIVE Ranking API: pricing, parameters and code examples

`tiktok/app-v3/live-daily-rank` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get TikTok LIVE rankings: hourly, weekly, rookie and other leaderboards with rank, score and creator.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/live-daily-rank"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/live-daily-rank', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/live-daily-rank", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/live-daily-rank", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/live-daily-rank` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string |  | Live room id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different room ids of different live rooms.  |
| `anchor_id` | string |  | Anchor id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different anchor ids of different live rooms.  |
| `rank_type` | integer |  | Rank type: 0: hourly_rank (Hourly Rank); 1: weekly_rank (Weekly Rank); 5: rookie_star_rank (Rookie Star Rank); 6: sale_rank (Sale Rank); 8: daily_rank (Daily Rank); 10: weekly_game_rank (Weekly Game Rank); 11:…  |
| `region_type` | integer |  | Region type, use the default value, the specific meaning is unknown.  |
| `gap_interval` | integer |  | Time interval, use the default value to represent the current day, use -1 to represent the ranking record.  |

## Details

Fetch TikTok LIVE leaderboards. Choose the board with `rank_type` (hourly, weekly, rookie star and more).

### Use cases

- Track top live streamers.
- Find rising live creators for partnerships.
- Monitor live competition in a market.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/live-daily-rank" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | No | Live room id, which can be obtained from the live room information interface, use the default value, this parameter wil… |
| `anchor_id` | string | No | Anchor id, which can be obtained from the live room information interface, use the default value, this parameter will a… |
| `rank_type` | integer | No | Rank type: 0: hourly_rank (Hourly Rank); 1: weekly_rank (Weekly Rank); 5: rookie_star_rank (Rookie Star Rank); 6: sale_… |
| `region_type` | integer | No | Region type, use the default value, the specific meaning is unknown. |
| `gap_interval` | integer | No | Time interval, use the default value to represent the current day, use -1 to represent the ranking record. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "rank_view": {
      "ranks": [
        {
          "rank": 1,
          "score": 1014521,
          "score_description": "1.0M",
          "rank_user": {
            "id": "<user id>",
            "nickname": "<user>"
          }
        }
      ]
    }
  }
}
```

### Notes

- `rank_type`: 0 hourly, 1 weekly, 5 rookie star.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Creator Search Insights](/model/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…
- [TikTok Creator Search Insights Detail](/model/tiktok/app-v3/creator-search-insights-detail): Get detailed statistics for a TikTok Creator Search Insights query: popularity over time and audience breakdown by age, gender and country.

---
Machine-readable: [`catalog/models/tiktok/app-v3/live-daily-rank.json`](../../../../catalog/models/tiktok/app-v3/live-daily-rank.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/live-daily-rank
