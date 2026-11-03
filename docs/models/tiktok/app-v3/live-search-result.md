# TikTok Stream Search Results API: pricing, parameters and code examples

`tiktok/app-v3/live-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns search results for active broadcasts matching a specified keyword. Supports filtering by country code and paginating via offset and count limits.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/live-search-result", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/live-search-result', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/live-search-result", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/live-search-result", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/live-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, do not exceed 20 default `20` |
| `offset` | integer |  | Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. default `0` |
| `region` | string |  | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. default `"US"` |
| `keyword` | string | yes | Keyword  |

## Details

Returns TikTok LIVE search results for a keyword. Each result is a live stream entry with its host and a stream ID. The only required input is `keyword`, and you can add `region`, `count` and `offset`.

### Use cases

- Find live streams that mention a brand or product name, such as `openai`.
- Collect the hosts who are broadcasting about a topic right now.
- Compare which streams appear for the same keyword in different `region` values.
- Page through all live results for a keyword to build a list of current broadcasters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/live-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number, do not exceed 20 |
| `offset` | integer | No | Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request. |
| `region` | string | No | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": 20,
  "data": [
    {
      "anchor": {
        "extra": "{}",
        "live_info": {},
        "owner_user_info": {
          "accept_private_policy": false,
          "account_labels": null,
          "ad_cover_url": null,
          "advance_feature_item_order": null,
          "advanced_feature_info": null,
          "authority_status": 0,
          "avatar_168x168": {
            "data_size": 0,
            "height": 720,
            "uri": "tos-useast5-avt-0068-tx/d29bf4d0c36077c6aace74b1dd3c8204",
            "url_list": [
              "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d29bf4d0c36077c…"
            ],
            "url_prefix": null,
            "width": 720
          },
          "avatar_300x300": {
            "data_size": 0,
            "height": 720,
            "uri": "tos-useast5-avt-0068-tx/d29bf4d0c36077c6aace74b1dd3c8204",
            "url_list": [
              "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/d29bf4d0c36077c…"
            ],
            "url_prefix": null,
            "width": 720
          }
        }
      },
      "type": 2
    }
  ],
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": [],
    "logid": "2026110307435548FE9CFC4468F5032CA3",
    "now": 1793691836000,
    "search_request_id": "",
    "server_stream_time": 598
  },
  "extra_data": null,
  "feedback_type": "live",
  "global_doodle_config": {
    "feedback_survey": [
      {
        "feedback_type": "live",
        "long_stress_info": null,
        "multiple_choices": [
          {
            "key": "Dislike",
            "value": "Dislike"
          }
        ],
        "send_us_multiple_choices": null
      }
    ],
    "feel_good": {
      "extra": "has_logged=true&query_flag1=0&query_flag2=0&query_usability=0&user_id=7576090281…",
      "token": "eyJhbGci…",
      "token_type": "Bearer"
    },
    "hide_results": false,
    "hit_dolphin": false,
    "hit_shark": false,
    "keyword": "openai",
    "new_source": "switch_tab",
    "search_channel": "musically_live",
    "tns_search_result": "Pass"
  },
  "guide_search_words": null,
  "has_more": 0,
  "log_pb": {
    "impr_id": "2026110307435548FE9CFC4468F5032CA3"
  },
  "status_code": 0,
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One search result entry. Each entry holds either a `lives` object or an `anchor` object, depending on its `type`. |
| `data[].type` | Result type code. In this response `1` marks an entry with a `lives` object and `2` marks an entry with an `anchor` object. |
| `data[].lives.aweme_id` | ID of the live stream item, returned as a string. |
| `data[].lives.author.avatar_thumb.url_list` | Image URLs for the host's 100x100 avatar. Several formats of the same image are listed. |
| `data[].anchor.owner_user_info.avatar_168x168.url_list / data[].anchor.owner_user_info.avatar_300x300.url_list` | Avatar image URLs for the host in two sizes. |
| `cursor` | Value to pass as `offset` to fetch the next page. It is `20` in this response. |
| `has_more` | Shows whether more results exist. `0` means no further page in this response. |
| `feedback_type` | Label for the result tab. It is `live` here. |
| `global_doodle_config.keyword` | The keyword the search ran for, echoed back. |
| `status_code` | Status of the request. `0` in this response. |

### Notes

- For the next page, send the `cursor` value from the response as `offset`. Keep `count` at 20 or below.
- Check `data[].type` before reading an entry, because the `lives` and `anchor` objects do not appear together in the same entry.
- Avatar `url_list` values can be `null`, so check them before use.
- To check whether a room is still live, call [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online). For room details, use [TikTok Broadcast Room Information](/apis/tiktok/app-v3/live-room-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/live-search-result.json`](../../../../catalog/models/tiktok/app-v3/live-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/live-search-result
