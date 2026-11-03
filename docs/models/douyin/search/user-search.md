# Douyin User Search (Search) API: pricing, parameters and code examples

`douyin/search/user-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a list of Douyin users matching search keywords. Supports filtering by fan count and user type with cursor-based pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/user-search", "cursor": 0, "douyin_user_fans": "", "douyin_user_type": "", "keyword": "猫咪", "search_id": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/user-search', {'cursor': 0, 'douyin_user_fans': '', 'douyin_user_type': '', 'keyword': '猫咪', 'search_id': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/user-search", {
  "cursor": 0,
  "douyin_user_fans": "",
  "douyin_user_type": "",
  "keyword": "猫咪",
  "search_id": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/user-search", sandbase.Params{
	"cursor": 0,
	"douyin_user_fans": "",
	"douyin_user_type": "",
	"keyword": "猫咪",
	"search_id": "",
})
```

Same call via the path form: `POST /v1/api/douyin/search/user-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first page) default `0` |
| `keyword` | string |  | Search keyword, e.g., "AI" default `"猫咪"` |
| `search_id` | string |  | Search session ID for pagination default `""` |
| `douyin_user_fans` | string |  | Fan count filter default `""` |
| `douyin_user_type` | string |  | User type filter default `""` |

## Details

Returns a page of Douyin accounts that match a search keyword. It needs a `keyword`, and you can add `douyin_user_fans` and `douyin_user_type` filters. The response also lists the available filter values.

### Use cases

- Find Douyin creators in a niche by searching a topic keyword.
- Narrow a creator search to accounts in a given fan count bracket such as `1k_1w`.
- Separate enterprise accounts from ordinary users with the `enterprise_user` and `common_user` filters.
- Collect account IDs from search results to look up full profiles later.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/user-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for first page) |
| `douyin_user_fans` | string | No | Fan count filter |
| `douyin_user_type` | string | No | User type filter |
| `keyword` | string | No | Search keyword, e.g., "AI" |
| `search_id` | string | No | Search session ID for pagination |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "challenge_list": null,
  "cursor": 10,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153222488FACFCB253505A7FC1",
    "now": 1793691142460,
    "scenes": null,
    "search_request_id": "",
    "start_ms": 1793691142071
  },
  "global_doodle_config": {
    "filter_settings": [
      {
        "default_index": 0,
        "items": [
          {
            "log_value": "fans_all",
            "title": "不限",
            "value": ""
          }
        ],
        "log_name": "by_user_fans",
        "name": "douyin_user_fans",
        "title": "粉丝数量"
      }
    ],
    "filter_show_dot": 1640995200,
    "keyword": "猫咪"
  },
  "has_more": 1,
  "input_keyword": "猫咪",
  "log_pb": {
    "impr_id": "20261103153222488FACFCB253505A7FC1",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "music_list": null,
  "myself_user_id": "0",
  "qc": "",
  "rid": "20261103153222488FACFCB253505A7FC1",
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_list[]` | One search result per entry. Each entry holds a `dynamic_patch` object. |
| `user_list[].dynamic_patch.raw_data` | A JSON string with the account details for the result. It includes `user_info` with the account `uid`, `nickname` and `gender`. Parse the string to read these values. |
| `user_list[].dynamic_patch.schema` | An `aweme://` deep link string for the result card template in the Douyin app. |
| `user_list[].dynamic_patch.origin_type / user_list[].dynamic_patch.height` | Display values for the result card. Both are numbers. |
| `has_more` | Shows `1` when more results exist after this page. |
| `cursor` | The cursor value to send for the next page. |
| `input_keyword` | The keyword the search used. |
| `global_doodle_config.filter_settings[].name` | The request parameter a filter maps to, such as `douyin_user_fans` or `douyin_user_type`. |
| `global_doodle_config.filter_settings[].items[].value` | The value to send for that filter. An empty string means no filter. The `title` field holds the Chinese label. |
| `status_code` | Status of the search. `0` appears in the sample response. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, send the `cursor` value from the response.
- Pass the same `keyword` and filters on every page. Use `search_id` to keep the search session across pages.
- Filter values come from `global_doodle_config.filter_settings[].items[].value`, for example `0_1k`, `1k_1w`, `common_user` and `enterprise_user`.
- The `uid` inside `dynamic_patch.raw_data` is a numeric ID string. For a newer version of this search, see [Douyin User Search (V2)](/apis/douyin/search/user-search-v2).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/user-search.json`](../../../../catalog/models/douyin/search/user-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/user-search
