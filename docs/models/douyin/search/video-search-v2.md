# Douyin Video Search API: pricing, parameters and code examples

`douyin/search/video-search-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Search Douyin videos by keyword and get descriptions, authors and play, like, comment and share counts. Filter by sort order, publish time, duration and content type, with cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/video-search-v2", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/video-search-v2', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/video-search-v2", {
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
run, err := c.Run(ctx, "douyin/search/video-search-v2", sandbase.Params{
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

Same call via the path form: `POST /v1/api/douyin/search/video-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) default `0` |
| `keyword` | string |  | Search keyword, e.g., "robot" default `"猫咪"` |
| `backtrace` | string |  | Backtrace identifier used for pagination(obtained from the last response) default `""` |
| `search_id` | string |  | Search ID used for pagination(obtained from the last response) default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Search Douyin videos by keyword with sort, publish-time and content-type filters. Each result carries the full video object: caption, stats, author and play URLs.

### Use cases

- Find popular videos about a product, brand or topic.
- Collect video IDs for comment or trend analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/video-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `backtrace` | string | No | Backtrace identifier used for pagination(obtained from the last response) |
| `content_type` | string | No | Content type filter |
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `filter_duration` | string | No | Video duration filter |
| `keyword` | string | No | Search keyword, e.g., "robot" |
| `publish_time` | string | No | Publish time filter |
| `search_id` | string | No | Search ID used for pagination(obtained from the last response) |
| `sort_type` | string | No | Sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "business_data": [
    {
      "data": {
        "aweme_info": {
          "aweme_id": "7647874180994472809",
          "desc": "窝酱紫可爱吗#金白米努特 #米努特矮脚猫 #萌宠小猫 #软萌小猫",
          "create_time": 1780659469,
          "statistics": {
            "digg_count": 44274,
            "comment_count": 3408,
            "collect_count": 7609,
            "share_count": 40029
          },
          "author": {
            "nickname": "小心米努特矮脚猫舍",
            "uid": "152191991817676",
            "sec_uid": "MS4wLjABAAAATyiM0d18Q9CLp0BXGm…",
            "unique_id": "51547535777"
          },
          "video": {
            "duration": 5549,
            "width": 576,
            "height": 1024,
            "play_addr": {
              "url_list": [
                "https://v3-search.douyinvod.com/f647cae6595842a683dc8f01c823…"
              ]
            }
          }
        }
      }
    }
  ],
  "business_config": {
    "has_more": 1,
    "next_page": {
      "cursor": 8,
      "search_id": "20261103113733421D26B2FB79B528103F"
    },
    "backtrace": "J6aGE6HAjYfQrWVjdpCA4koXHeq2D+…"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `business_data[].data.aweme_info` | One video per result, same fields as the video detail APIs (`aweme_id`, `desc`, `statistics`, `author`, `video`). |
| `business_config.has_more` | 1 when more pages exist. |
| `business_config.next_page` | `cursor` and `search_id` for the next page. |
| `business_config.backtrace` | Send back as `backtrace` for the next page. |

### Notes

- For the next page pass `next_page.cursor`, `next_page.search_id` and `backtrace` from the previous response.
- `sort_type`, `publish_time` and `content_type` follow the Douyin app's filter options.

### Pricing

$0.01 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin General Search](/apis/douyin/search/general-search-v1): Search Douyin (Chinese TikTok) from the app's general search tab and get videos with descriptions, authors and play, like, comment and share counts.
- [Fetch hashtag search V1](/apis/douyin/search/challenge-search-v1): Fetch hashtag/challenge search results from Douyin App.
- [Fetch hashtag search V2](/apis/douyin/search/challenge-search-v2): Fetch hashtag/challenge search results from Douyin App using V2 API.

---
Machine-readable: [`catalog/models/douyin/search/video-search-v2.json`](../../../../catalog/models/douyin/search/video-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/video-search-v2
