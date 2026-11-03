# TikTok User Search Results API: pricing, parameters and code examples

`tiktok/app-v3/user-search-result` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of user profiles matching specified keywords, with options to filter by account type, follower count, and preferences.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-search-result", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-search-result', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-search-result", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-search-result", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `keyword` | string | yes | Keyword  |
| `user_search_other_pref` | string |  | Sort by other preferences default `""` |
| `user_search_profile_type` | string |  | Sort by account type default `""` |
| `user_search_follower_count` | string |  | Sort by number of followers default `""` |

## Details

Returns a list of TikTok user profiles that match a search `keyword`. The only required input is `keyword`, and you can add paging and filter parameters.

### Use cases

- Find TikTok accounts that match a brand name such as `openai`.
- Collect avatar image URLs for accounts that match a search term.
- Page through all accounts that match a keyword with `count` and `offset`.
- Narrow a creator search with the follower count and profile type filters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-search-result" \
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
| `user_search_follower_count` | string | No | Sort by number of followers |
| `user_search_other_pref` | string | No | Sort by other preferences |
| `user_search_profile_type` | string | No | Sort by account type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "challenge_list": null,
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": [],
    "logid": "20261103074408EF1DF108C79A43821A2A",
    "now": 1793691849000,
    "search_request_id": "",
    "server_stream_time": 612
  },
  "feedback_type": "user",
  "global_doodle_config": {
    "ab_params": {
      "user_relation_ship": "1"
    },
    "display_filter_bar": 1,
    "feedback_survey": [
      {
        "feedback_type": "user",
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
    "hide_results": false,
    "hit_dolphin": false,
    "hit_shark": false,
    "keyword": "openai",
    "new_source": "switch_tab",
    "search_channel": "musically_user",
    "tns_search_result": "Pass"
  },
  "has_more": 1,
  "input_keyword": "openai",
  "log_pb": {
    "impr_id": "20261103074408EF1DF108C79A43821A2A"
  },
  "music_list": null,
  "qc": "",
  "rid": "20261103074408EF1DF108C79A43821A2A",
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_list[]` | One matching account per item. Each item holds the account details under `user_info`. |
| `user_list[].user_info` | Profile data for the matched account. |
| `user_list[].user_info.avatar_168x168 / user_list[].user_info.avatar_300x300` | Avatar images at two sizes. Each has a `uri`, `width`, `height` and a `url_list` with several image links. |
| `user_list[].user_info.avatar_168x168.url_list` | Direct image URLs for the small avatar, in HEIC and JPEG formats. |
| `user_list[].user_info.authority_status` | Account authority flag. It is `0` in the sample response. |
| `has_more` | Shows whether more results remain. It is `1` in the sample response. |
| `cursor` | Position value for the next page. It is `20` in the sample response. |
| `input_keyword` | The search keyword that the request used. |
| `status_code` | Result status of the call. `0` in the sample response. |

### Notes

- Page through results with `count` and `offset`. The sample response returns `cursor` as `20` and `has_more` as `1`, so use the `cursor` value as the next `offset`.
- Several `user_list[]` fields, such as `items`, `musics` and `challenges`, are `null` for user search results.
- The filter parameters `user_search_follower_count`, `user_search_profile_type` and `user_search_other_pref` are strings and default to an empty string.
- To get more details on a matched account, call [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-search-result.json`](../../../../catalog/models/tiktok/app-v3/user-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-search-result
