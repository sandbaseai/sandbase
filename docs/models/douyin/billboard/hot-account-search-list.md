# Douyin Hot Account Search

`douyin/billboard/hot-account-search-list` · api · Douyin

Returns a list of Douyin accounts matching a username or Douyin ID keyword, including follower counts, like totals, and performance metrics.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-search-list", "cursor": 0, "keyword": "华为"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-search-list', {'cursor': 0, 'keyword': '华为'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-search-list", {
  "cursor": 0,
  "keyword": "华为"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-search-list", sandbase.Params{
	"cursor": 0,
	"keyword": "华为",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer | yes | Cursor, default empty  |
| `keyword` | string | yes | Search username or Douyin number  |

## Details

Look up Douyin accounts by providing a search term in `keyword` and navigate results using `cursor`. The response details follower counts, like totals, and account performance statistics.

### Use cases

- Search for Douyin creators by username or Douyin account ID.
- Inspect follower counts and total likes for matched creator profiles.
- Discover influencer accounts matching specific brand or topic keywords.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cursor": 0, "keyword": "华为"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | Yes | Cursor, default empty |
| `keyword` | string | Yes | Search username or Douyin number |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "user_list": [
      {
        "fans_cnt": 13964515,
        "fans_incr_rate": 0,
        "group_id": 0,
        "like_cnt": 225688863,
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

- Search by username or Douyin number using `keyword`.
- Paginate through matching account results using `cursor`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-search-list.json`](../../../../catalog/models/douyin/billboard/hot-account-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-search-list
