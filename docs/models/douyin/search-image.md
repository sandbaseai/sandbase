# Douyin Image Post Search API: pricing, parameters and code examples

`douyin/search-image` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search Douyin (TikTok China) image posts by keyword with search-session pagination. Omit searchId for the first page, then use the search ID from the previous response to continue.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search-image", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search-image', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search-image", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search-image", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/douyin/search-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | The search keyword.  |
| `searchId` | string |  | Search ID returned by the previous response. Leave it empty for the first page.  |

## Details

Returns a page of Douyin image post search results for a keyword. Each result includes the post's author info and a rank within the search session. The only required input is `keyword`.

### Use cases

- Collect image posts about a topic such as `美食` to study what content ranks for it.
- Find creators who publish image posts for a keyword by reading each result's author fields.
- Page through a full search session by passing the returned search ID back as `searchId`.
- Build a list of post IDs to look up in more detail with a video or post detail API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword. |
| `searchId` | string | No | Search ID returned by the previous response. Leave it empty for the first page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_config": {
    "ad_info": null,
    "card_count": 7,
    "extra_fresh_struct": null,
    "feedback": null,
    "feelgood_msg": {},
    "filter_bar": null,
    "general_search_config": {
      "double_column_layout_type": 3
    },
    "has_more": 1,
    "is_filter_search": 0,
    "keyword": "美食",
    "next_page": {
      "cursor": 8,
      "keyword": "美食",
      "origin_query": "美食",
      "poi_search_info": "",
      "search_id": "202611031532144CDF780CB96549D598A8",
      "search_request_id": "202611031532144CDF780CB96549D598A8"
    },
    "poi_search_info": ""
  },
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_image",
      "data": {
        "aweme_info": {
          "activity_video_type": -1,
          "ai_follow_images": null,
          "ai_search_struct": {
            "show_ai_entrance": true
          },
          "anchors": null,
          "authentication_token": "MS4wLjAA…",
          "author": {
            "accept_private_policy": false,
            "account_cert_info": "{}",
            "account_region": "",
            "ad_cover_url": null,
            "allow_story_normal_like": false,
            "apple_account": 0,
            "authority_status": 0,
            "avatar_168x168": {
              "height": 720,
              "uri": "168x168/aweme-avatar/tos-cn-i-0813c000-ce_owdMnECAvA9xYL8XAalAXPnpiA53iir6IQB1x",
              "url_list": [
                "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813c000-ce_owdMnECAvA9xYL8XA…"
              ],
              "width": 720
            }
          },
          "author_mask_tag": 0,
          "author_user_id": 73592891627
        },
        "aweme_list": null,
        "card_id": "douyin.doctype_aweme_image",
        "card_style_type": 1,
        "card_type": 1,
        "debug_data": {
          "filter_debug_info_list": null
        },
        "debug_diff_info": {},
        "doc_type": 303
      },
      "data_id": "0_7701644345287494948",
      "log": {
        "dcm": "search.natural.aweme_image.7701644345287494948.202611031532144CDF780CB96549D598A…",
        "rank": "1",
        "search_id": "202611031532144CDF780CB96549D598A8"
      },
      "type": 12
    }
  ],
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031532144CDF780CB96549D598A8",
    "now": 1793691135000,
    "scenes": null,
    "search_request_id": "20261102EC5DDC68B137D03B"
  },
  "global_config": {},
  "log": {
    "impr_id": "202611031532144CDF780CB96549D598A8",
    "search_id": "202611031532144CDF780CB96549D598A8",
    "search_keyword": "美食"
  },
  "log_pb": {
    "impr_id": "202611031532144CDF780CB96549D598A8"
  },
  "status_code": 0,
  "time_cost": {
    "stream_inner": 1055
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[]` | One search result card. Each card is an image post (`card_id` is `douyin.doctype_aweme_image`). |
| `business_data[].data_id` | Result ID in the form `<position>_<post ID>`, for example `0_7701644345287494948`. The number after the underscore matches the post ID in `log.dcm`. |
| `business_data[].log.rank` | Position of the result in the search, starting at `1`. |
| `business_data[].log.dcm` | Tracking string for the result. It contains the post ID and the search ID. |
| `business_data[].data.aweme_info.author_user_id` | Numeric ID of the user who published the post. |
| `business_data[].data.aweme_info.author.avatar_168x168.url_list` | Avatar image URLs of the author at 168x168, in `webp` and `jpeg` formats. |
| `business_config.has_more` | Shows whether more results exist. `1` in this response. |
| `business_config.next_page.search_id / business_config.next_page.search_request_id` | Search session ID to send as `searchId` to get the next page. |
| `business_config.next_page.cursor` | Cursor position for the next page. It is `8` in this response. |
| `status_code` | Status of the call. `0` in this response. |

### Notes

- Leave `searchId` out on the first call. For later pages, send the value from `business_config.next_page.search_id` along with the same `keyword`.
- Keep requesting pages while `business_config.has_more` is `1`.
- Fields such as `aweme_info.author` hold many more profile values than the ones listed here. Many of them are `null` or empty in image post results.
- To get details for a single post, use the post ID from `data_id` with [Douyin Single Video Details](/apis/douyin/app-v3/one-video) or [Douyin Video Detail](/apis/douyin/app-v3/one-video-v3).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/search-image.json`](../../../catalog/models/douyin/search-image.json) · Store page: https://www.sandbase.ai/model/douyin/search-image
