# Douyin DOU+ Video Ranking API: pricing, parameters and code examples

`douyin/douplus/video-ranking` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves DOU+ video leaderboard metrics filterable by category, ranking dimension, and time range. Returns video titles, author details, and engagement statistics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/video-ranking"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/video-ranking', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/video-ranking", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/video-ranking", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/douplus/video-ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `adv_id` |  |  | Advertiser id, optional  |
| `tag_id` |  |  | Category id, default 634 (Entertainment). Full map: 601 Plot, 602 Star, 606 Music, 607 ACGN,  |
| `dim_type` |  |  | Ranking dimension, default 5. 1=low-fan hits, 2=high completion, 3=high like-rate, 4=high follower-growth, 5=hotness index  |
| `time_range` |  |  | Time range, 1 / 2 / 3, default 2  |

## Details

Queries the DOU+ video leaderboard using optional filters such as `dim_type`, `tag_id`, and `time_range`. It returns video engagement metrics, author follower counts, and post titles.

### Use cases

- Track top-performing DOU+ promotional videos across specific content categories.
- Compare video completion rates, like ratios, and follower growth across leaderboard metrics.
- Identify trending Douyin short videos ranked by the platform hotness index.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/video-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `adv_id` | string | No | Advertiser id, optional |
| `tag_id` | string | No | Category id, default 634 (Entertainment). |
| `dim_type` | string | No | Ranking dimension, default 5. 1=low-fan hits, 2=high completion, 3=high like-rate, 4=high follower-growth, 5=hotness index |
| `time_range` | string | No | Time range, 1 / 2 / 3, default 2 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "createTime": "1790162085",
      "title": "我宣布这是新的上海落地签#无畏契约 #巴黎世家 #上海 #网吧  #万万没想到",
      "author": {
        "followerCount": 3525257,
        "nickname": "<user>"
      },
      "statistics": {
        "FinishPlayRate": 0.19741609101658283,
        "LikeRate": 0.04709622998026867,
        "NewFansRate": 0.0001355522866117548
      }
    }
  ]
}
```

### Notes

- `dim_type` sets the ranking dimension: 1 for low-fan hits, 2 for high completion, 3 for like rate, 4 for follower growth, and 5 for hotness index.
- `tag_id` filters by category ID, defaulting to 634 (Entertainment) with options such as 601 (Plot), 602 (Star), 606 (Music), and 607 (ACGN).
- `time_range` specifies the period using values 1, 2, or 3, with 2 as the default.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin DOU+ Promotable Items](/model/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/model/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/model/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.

---
Machine-readable: [`catalog/models/douyin/douplus/video-ranking.json`](../../../../catalog/models/douyin/douplus/video-ranking.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/video-ranking
