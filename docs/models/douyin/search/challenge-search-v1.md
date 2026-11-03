# Douyin Challenge Search API: pricing, parameters and code examples

`douyin/search/challenge-search-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns Douyin challenge and hashtag search results matching a query. Supports filtering by date, content type, duration, and sorting method.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/challenge-search-v1", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/challenge-search-v1', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/challenge-search-v1", {
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
run, err := c.Run(ctx, "douyin/search/challenge-search-v1", sandbase.Params{
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

Same call via the path form: `POST /v1/api/douyin/search/challenge-search-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first request) default `0` |
| `keyword` | string |  | Search keyword, e.g., "food" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Returns Douyin challenge (hashtag) search results that match a `keyword`. Each result holds the challenge name, its ID, and the creator's avatar images. You can filter by publish time, content type and duration, and you can set the sort order.

### Use cases

- Find Douyin hashtags that contain a topic word, such as `猫咪`, and compare their name variants.
- Collect challenge IDs (`cid`) to use in other hashtag lookups.
- Page through all challenges for a keyword to build a hashtag list for a topic.
- Check whether a challenge is active by reading `challenge_status`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/challenge-search-v1" \
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
| `keyword` | string | No | Search keyword, e.g., "food" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID for pagination |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {},
  "challenge_list": [
    {
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
    }
  ],
  "cursor": 20,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153215538D3B1418CA743E39F6",
    "now": 1793691135000,
    "scenes": null,
    "search_request_id": ""
  },
  "global_doodle_config": {
    "keyword": "猫咪"
  },
  "has_more": 1,
  "is_match": false,
  "keyword_disabled": 0,
  "log_pb": {
    "impr_id": "20261103153215538D3B1418CA743E39F6",
    "stab_extra": {
      "traffic_identification": "normal"
    }
  },
  "qc": "",
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `challenge_list[].challenge_info.cha_name` | The hashtag or challenge name, shown without the # sign. |
| `challenge_list[].challenge_info.cid` | The challenge ID as a string. Use it to identify the hashtag in other calls. |
| `challenge_list[].challenge_info.challenge_status` | Status code of the challenge. The value `1` appears on all sample results. |
| `challenge_list[].challenge_info.author.avatar_168x168 / challenge_list[].challenge_info.author.avatar_300x300` | Avatar images tied to the challenge author, at two sizes. Each has `uri`, `url_list`, `width` and `height`. |
| `challenge_list[].challenge_info.author.avatar_168x168.url_list` | Image URLs for the avatar in WebP and JPEG formats. |
| `challenge_list[].items` | Video items under the challenge. It is `null` in the sample results. |
| `cursor` | Offset to send as `cursor` for the next page. The sample shows `20`. |
| `has_more` | Shows whether more results exist. `1` means more pages are available. |
| `extra.logid / log_pb.impr_id` | Request log ID and impression ID for this response. |
| `status_code` | Status code of the response. `0` appears on this successful call. |

### Notes

- Send `cursor` as `0` on the first request. For the next page, send the `cursor` value from the response and keep `has_more` in mind to know when to stop.
- The parameters `backtrace` and `search_id` are meant for pagination. In this response `extra.search_request_id` is an empty string.
- To see details for a challenge you found, call [Douyin Hashtag Details](/apis/douyin/app-v3/hashtag-detail). To list its videos, call [Douyin Hashtag Video List](/apis/douyin/app-v3/hashtag-video-list).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.
- [Douyin Discussion Search](/apis/douyin/search/discuss-search): Returns discussion and question-and-answer search results from Douyin.

---
Machine-readable: [`catalog/models/douyin/search/challenge-search-v1.json`](../../../../catalog/models/douyin/search/challenge-search-v1.json) · Store page: https://www.sandbase.ai/model/douyin/search/challenge-search-v1
