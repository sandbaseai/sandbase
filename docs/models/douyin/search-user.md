# Douyin User Search API: pricing, parameters and code examples

`douyin/search-user` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search Douyin (TikTok China) users by keyword with page-based pagination and optional account-type filtering. Use it to discover creators, brands, or verified accounts for research.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search-user", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search-user', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search-user", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search-user", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/douyin/search-user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). default `1` |
| `keyword` | string | yes | The search keyword.  |
| `userType` | string |  | Filter by user type. one of: `common_user`, `enterprise_user`, `personal_user` |

## Details

Returns a page of Douyin user search results for a keyword. The only required input is `keyword`. You can add `page` to move through results and `userType` to filter by account type.

### Use cases

- Find creator and brand accounts that match a niche keyword such as `美食` (food).
- Page through results to build a list of candidate accounts for market research.
- Filter by `userType` to compare enterprise accounts with personal accounts for a topic.
- Log the `search_id` of a query so you can trace which search produced a given result set.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search-user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword. |
| `page` | integer | No | Page number (starting from 1). |
| `userType` | string | No | Filter by user type. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": null,
    "card_count": 19,
    "extra": {
      "hidden_filter": false,
      "is_filter_search": 0,
      "req_start_ts": 1793691135691
    },
    "extra_fresh_struct": null,
    "feedback": {
      "text_first": "找不到想找的帐号？",
      "text_second": "告诉我们",
      "url": "aweme://webview/?url=https%3A%2F%2Faweme.snssdk.com%2Ffalcon%2Ffe_app_react%2Fqu…"
    },
    "filter_bar": null,
    "has_more": 1,
    "is_filter_search": 0,
    "keyword": "美食",
    "next_page": {
      "cursor": 20,
      "keyword": "美食",
      "poi_search_info": "",
      "search_id": "2026110315321535AE25B844FEC0561826",
      "search_request_id": "2026110315321535AE25B844FEC0561826"
    },
    "poi_search_info": "",
    "pre_loadmore_config": null
  },
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_user",
      "data": {
        "aweme_list": null,
        "card_id": "douyin.doctype_aweme_user",
        "card_protocal_struct": {
          "render_extra": {
            "card_type_name": "channel_user",
            "height": 80,
            "schema": "aweme://lynxview/?channel=morphling_high&bundle=channel_user%2Findex%2Ftemplate.…",
            "type": 999
          },
          "render_type": 1
        },
        "card_style_type": 4,
        "card_type": 4,
        "card_type_name": "channel_user",
        "debug_data": {
          "filter_debug_info_list": null
        },
        "debug_diff_info": {}
      },
      "data_id": "0",
      "log": {
        "dcm": "search.natural.discover.3971034404880483.2026110315321535AE25B844FEC0561826"
      },
      "type": 999
    }
  ],
  "extra": {
    "device_score": 0,
    "fatal_item_ids": [],
    "logid": "2026110315321535AE25B844FEC0561826",
    "now": 1793691136000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_config": {
    "hidden_filter": false
  },
  "log": {
    "impr_id": "2026110315321535AE25B844FEC0561826",
    "search_id": "2026110315321535AE25B844FEC0561826",
    "search_keyword": "美食"
  },
  "log_pb": {
    "impr_id": "2026110315321535AE25B844FEC0561826"
  },
  "mock_recall_path": "/aweme/v2/search/discover/",
  "path": "/aweme/v2/search/discover/",
  "render_info": [
    {
      "render_extra": {
        "card_type_name": "channel_user",
        "height": 80,
        "schema": "aweme://lynxview/?channel=morphling_high&bundle=channel_user%2Findex%2Ftemplate.…",
        "type": 999
      },
      "render_id": "0",
      "render_type": 1,
      "ui_info": null
    }
  ],
  "status_code": 0,
  "struct": {
    "children": [
      {
        "data_id": "0",
        "fp": "",
        "id": "0",
        "render_id": "0"
      }
    ],
    "fp": "",
    "id": "00",
    "layout_type": 1
  },
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[]` | One search result card per entry. Each card in this response has `card_type_name` set to `channel_user`, which marks it as a user result. |
| `business_data[].data_id` | Position of the card in the result list, as a string starting at `0`. |
| `business_data[].log.dcm` | Tracking string for the card. It ends with the search ID, and the number before that appears to identify the matched account. |
| `business_config.has_more` | Shows whether more results exist. The value `1` means there is another page. |
| `business_config.next_page.cursor` | Offset for the next page of results. It is `20` in this response. |
| `business_config.card_count` | Number of cards the search reports for this page. |
| `business_config.keyword / log.search_keyword` | The keyword the search ran with. |
| `business_config.next_page.search_id / log.search_id / log.impr_id` | Identifier for this search request. All three carry the same value in this response. |
| `status_code / success` | `status_code` of `0` and `success` of `true` mean the call worked. |

### Notes

- The `business_data[]` cards in this response show only card metadata, such as `card_id` and `data_id`. They do not show account names or follower counts, so check the card contents before you rely on them.
- Send `page` starting from `1` to get later pages. Check `business_config.has_more` to see whether another page exists.
- `userType` accepts `common_user`, `enterprise_user` or `personal_user`.
- To look up one account in detail, use [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douyin/search-user.json`](../../../catalog/models/douyin/search-user.json) · Store page: https://www.sandbase.ai/model/douyin/search-user
