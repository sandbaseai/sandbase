# TikTok Hashtag Search Results API: pricing, parameters and code examples

`tiktok/app-v3/hashtag-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns TikTok hashtag search results matching a specified search keyword. Includes challenge details such as hashtag name, use count, and user count.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/hashtag-search-result", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/hashtag-search-result', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/hashtag-search-result", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/hashtag-search-result", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/hashtag-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `keyword` | string | yes | Keyword  |

## Details

Returns a list of TikTok hashtags (challenges) that match a search keyword. It needs one input, `keyword`, and accepts `count` and `offset` for paging.

### Use cases

- Find hashtag variants of a brand name, such as `openai` and `open_ai`, before you start tracking them.
- Collect hashtag IDs (`cid`) to pass to other hashtag APIs.
- Check whether a keyword has a matching hashtag on TikTok.
- Page through all hashtags related to a topic to build a list of tags to monitor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/hashtag-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {},
  "challenge_list": [
    {
      "challenge_info": {
        "banner_list": null,
        "cha_attrs": null,
        "cha_name": "openai",
        "cid": "72988465",
        "collect_stat": 0,
        "connect_music": [],
        "desc": "",
        "extra_attr": {
          "is_live": false
        }
      },
      "items": null,
      "position": null
    }
  ],
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": [],
    "logid": "20261103074353B6A0EB0AB2CEEC6C9841",
    "now": 1793691833000,
    "search_request_id": "",
    "server_stream_time": 430
  },
  "feedback_type": "challenge",
  "global_doodle_config": {
    "feedback_survey": [
      {
        "feedback_type": "challenge",
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
      "extra": "has_logged=true&query_flag1=0&query_flag2=0&query_usability=0&user_id=7563412318…",
      "token": "eyJhbGci…",
      "token_type": "Bearer"
    },
    "hashtag_vertical_style_type": 1,
    "hide_results": false,
    "hit_dolphin": false,
    "hit_shark": false,
    "keyword": "openai",
    "new_source": "normal_search",
    "search_channel": "musically_challenge",
    "tns_search_result": "Pass"
  },
  "has_more": 1,
  "is_match": false,
  "keyword_disabled": 0,
  "log_pb": {
    "impr_id": "20261103074353B6A0EB0AB2CEEC6C9841"
  },
  "qc": "",
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `challenge_list[]` | One matching hashtag per item. Results follow the order that TikTok returns. |
| `challenge_list[].challenge_info.cha_name` | Name of the hashtag, without the leading `#`. |
| `challenge_list[].challenge_info.cid` | ID of the hashtag, returned as a string. |
| `challenge_list[].challenge_info.desc` | Description text of the hashtag. It is often an empty string. |
| `challenge_list[].challenge_info.extra_attr.is_live` | Boolean flag in the hashtag's extra attributes. It is `false` for all hashtags in this example. |
| `has_more` | Shows whether more results exist. `1` means you can request another page. |
| `cursor` | Cursor value returned with the page. It is `20` here, which matches the default `count`. |
| `status_code` | Status of the request. `0` is returned for this successful call. |
| `global_doodle_config.keyword` | The keyword that TikTok used for the search. |

### Notes

- Pass the search term in `keyword`. Set `count` for the page size (default `20`) and `offset` for the starting position (default `0`).
- When `has_more` is `1`, call again with `offset` set to the returned `cursor` value to get the next page.
- `items` and `position` are `null` in each result, and `use_count` and `user_count` are not present in this response. Use [TikTok Hashtag Detail](/apis/tiktok/app-v3/hashtag-detail) with the `cid` for more on one hashtag.
- To see videos under a hashtag, call [TikTok Hashtag Video List](/apis/tiktok/app-v3/hashtag-video-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/hashtag-search-result.json`](../../../../catalog/models/tiktok/app-v3/hashtag-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/hashtag-search-result
