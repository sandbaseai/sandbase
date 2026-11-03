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

Returns a page of Douyin users whose names match a search keyword. Each result includes the user's `user_id`, `nick_name`, avatar, follower count, like count and number of published videos. The API takes a `keyword` and an optional `cursor`.

### Use cases

- Find Douyin creators in a niche by searching a topic word such as a pet or fitness term.
- Rank matching accounts by `fans_cnt` to build a shortlist of influencers.
- Collect `user_id` values to look up full profiles or videos for each account.
- Compare `publish_cnt` and `like_cnt` across accounts that share the same name.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/user-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for first page) |
| `keyword` | string | No | Search keyword, e.g., "AI" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor": 30,
    "has_more": true,
    "user_list": [
      {
        "avatar_url": "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_a53d8c295078…",
        "fans_cnt": 220255,
        "fans_incr_rate": 0,
        "fans_trends": null,
        "group_id": 0,
        "group_name": "",
        "like_cnt": 5689499,
        "monitor_id": 0,
        "monitor_period": 0,
        "monitor_status": 0,
        "new_fans_cnt": 0,
        "new_item_monitor": 0
      }
    ]
  },
  "extra": {
    "now": 1793691142000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user_list[].user_id` | Unique ID of the Douyin user. It is a long string that starts with `MS4w`. |
| `data.user_list[].nick_name` | Display name of the account. |
| `data.user_list[].avatar_url` | URL of the 100x100 avatar image. |
| `data.user_list[].fans_cnt` | Follower count of the account. |
| `data.user_list[].like_cnt` | Total likes the account has received. |
| `data.user_list[].publish_cnt` | Number of videos the account has published. |
| `data.cursor` | Cursor value to send in the next request to get the following page. |
| `data.has_more` | `true` when more results are available after this page. |
| `data.user_list[].fans_incr_rate / new_fans_cnt / new_like_cnt` | Follower and like growth fields. They are `0` in this response, so do not rely on them. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, pass the `data.cursor` value from the previous response (`30` in the sample) and stop when `has_more` is `false`.
- `keyword` is the search text. Many accounts can share one `nick_name`, so use `user_id` to tell them apart.
- Fields such as `monitor_id`, `group_id` and `target_cnt` were `0` and `fans_trends` was `null` in the sample response.
- For a similar user search with a different response layout, see [Douyin User Search (Search)](/apis/douyin/search/user-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/user-search-v2.json`](../../../../catalog/models/douyin/search/user-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/user-search-v2
