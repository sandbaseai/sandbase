# Douyin User Search (V2) API: pricing, parameters and code examples

`douyin/search/user-search-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches for Douyin users matching specified search keywords and returns user metrics such as follower and like counts. Supports cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/user-search-v2", "cursor": 0, "keyword": "猫咪"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/user-search-v2', {'cursor': 0, 'keyword': '猫咪'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/user-search-v2", {
  "cursor": 0,
  "keyword": "猫咪"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/user-search-v2", sandbase.Params{
	"cursor": 0,
	"keyword": "猫咪",
})
```

Same call via the path form: `POST /v1/api/douyin/search/user-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first page) default `0` |
| `keyword` | string |  | Search keyword, e.g., "AI" default `"猫咪"` |

## Details

Search Douyin users matching a given `keyword` string. Results can be paged using the `cursor` parameter.

### Use cases

- Discover Douyin accounts matching targeted search topics.
- Inspect follower and like engagement counts for searched creators.
- Automate influencer identification workflows across search queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/user-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for first page) |
| `keyword` | string | No | Search keyword, e.g., "AI" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "user_list": [
      {
        "fans_cnt": 223954,
        "fans_incr_rate": 0,
        "group_id": 0,
        "like_cnt": 5588658,
        "monitor_id": 0,
        "monitor_status": 0,
        "new_fans_cnt": 0,
        "new_item_target_cnt": 0,
        "new_item_target_type": 0,
        "new_like_cnt": 0
      }
    ]
  }
}
```

### Notes

- Set `cursor` to 0 to retrieve the first page of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/user-search-v2.json`](../../../../catalog/models/douyin/search/user-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/user-search-v2
