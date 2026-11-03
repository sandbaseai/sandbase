# Douyin Hashtag Challenge Search (V2) API: pricing, parameters and code examples

`douyin/search/challenge-search-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns Douyin hashtag and challenge search results matching a query keyword. Supports filtering by sort type, content type, post date, and duration with cursor-based pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/challenge-search-v2", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/challenge-search-v2', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/challenge-search-v2", {
  "backtrace": "",
  "content_type": "0",
  "cursor": 0,
  "filter_duration": "0",
  "keyword": "猫咪",
  "publish_time": "0",
  "search_id": "",
  "sort_type": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/challenge-search-v2", sandbase.Params{
	"backtrace": "",
	"content_type": "0",
	"cursor": 0,
	"filter_duration": "0",
	"keyword": "猫咪",
	"publish_time": "0",
	"search_id": "",
	"sort_type": "0",
})
```

Same call via the path form: `POST /v1/api/douyin/search/challenge-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first request) default `0` |
| `keyword` | string |  | Search keyword, e.g., "game" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Returns Douyin hashtag and challenge search results for a `keyword`. Each result card holds the hashtag name, its challenge ID and the account linked to it. The API also returns the values needed to request the next page.

### Use cases

- Find Douyin hashtags that match a topic keyword, such as a pet or product term.
- Collect `cid` values for hashtags to use in other Douyin hashtag lookups.
- Compare spelling variants of one topic, such as simplified and traditional Chinese hashtag names.
- Page through all hashtag matches for a campaign keyword and store the names.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/challenge-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `content_type` | string | No | Content type filter |
| `cursor` | integer | No | Pagination cursor (0 for first request) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "game" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID for pagination |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": null,
    "card_count": 19,
    "extra": {
      "is_filter_search": 0,
      "req_start_ts": 1793691135037
    },
    "extra_fresh_struct": null,
    "feedback": null,
    "feelgood_msg": {},
    "filter_bar": null,
    "has_more": 1,
    "is_filter_search": 0,
    "keyword": "猫咪",
    "next_page": {
      "cursor": 20,
      "keyword": "猫咪",
      "poi_search_info": "",
      "search_id": "202611031532142BE6991D1648F635C376",
      "search_request_id": "202611031532142BE6991D1648F635C376"
    },
    "poi_search_info": ""
  },
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_hashtag",
      "data": {
        "challenge_info": {
          "author": {
            "accept_private_policy": false,
            "account_region": "",
            "ad_cover_url": null,
            "allow_story_normal_like": false,
            "apple_account": 0,
            "authority_status": 0,
            "avatar_168x168": {
              "height": 720,
              "uri": "168x168/aweme-avatar/tos-cn-avt-0015_8f9c89c85921da89d4026411d3fd5864",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_8f9c89c85921da89d40264…"
              ],
              "width": 720
            },
            "avatar_300x300": {
              "height": 720,
              "uri": "300x300/aweme-avatar/tos-cn-avt-0015_8f9c89c85921da89d4026411d3fd5864",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_8f9c89c85921da89d40264…"
              ],
              "width": 720
            }
          },
          "banner_list": null,
          "cha_attrs": null,
          "cha_name": "猫咪",
          "challenge_status": 1,
          "cid": "1562727459956738",
          "collect_stat": 0,
          "connect_music": []
        },
        "items": null,
        "position": null
      },
      "data_id": "0",
      "log": {},
      "type": 2
    }
  ],
  "extra": {
    "device_score": 0,
    "fatal_item_ids": [],
    "logid": "202611031532142BE6991D1648F635C376",
    "now": 1793691135000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_config": {
    "hidden_filter": false
  },
  "log": {
    "impr_id": "202611031532142BE6991D1648F635C376",
    "search_id": "202611031532142BE6991D1648F635C376",
    "search_keyword": "猫咪"
  },
  "log_pb": {
    "impr_id": "202611031532142BE6991D1648F635C376",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "status_code": 0,
  "time_cost": {
    "stream_inner": 308
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[].data.challenge_info.cha_name` | Name of the hashtag or challenge, without the leading # symbol. |
| `business_data[].data.challenge_info.cid` | Challenge ID of the hashtag, returned as a string. |
| `business_data[].data.challenge_info.challenge_status` | Status code of the challenge. The value is `1` for every result in this sample. |
| `business_data[].data.challenge_info.author.avatar_168x168 / business_data[].data.challenge_info.author.avatar_300x300` | Avatar images of the account linked to the challenge. Each has `url_list` with image URLs, plus `width` and `height`. |
| `business_data[].card_id` | Card type label. Hashtag results use `douyin.doctype_aweme_hashtag`. |
| `business_data[].data_id` | Position index of the card in the result list, returned as a string. |
| `business_config.has_more` | Shows whether more results exist. The value `1` means another page is available. |
| `business_config.next_page.cursor` | Cursor value to send as `cursor` in the next request. |
| `business_config.next_page.search_id / log.search_id` | ID of this search. Send it as `search_id` when you request the next page. |
| `status_code` | Status of the response. `0` appears on a successful call. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, send the `cursor` and `search_id` from `business_config.next_page`.
- No `backtrace` value appears in this response. Leave it empty unless a response returns one.
- Use the `cid` of a result to look up a hashtag with [Douyin Hashtag Details](/apis/douyin/app-v3/hashtag-detail) or list its videos with [Douyin Hashtag Video List](/apis/douyin/app-v3/hashtag-video-list).
- `business_data[].data.items` was `null` in this sample, so the cards carry no videos.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.
- [Douyin Discussion Search](/apis/douyin/search/discuss-search): Returns discussion and question-and-answer search results from Douyin.

---
Machine-readable: [`catalog/models/douyin/search/challenge-search-v2.json`](../../../../catalog/models/douyin/search/challenge-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/challenge-search-v2
