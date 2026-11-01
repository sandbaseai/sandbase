# Douyin Video Search

`douyin/search/video-search-v2` · api · Douyin

Search Douyin videos by keyword and get descriptions, authors and play, like, comment and share counts. Filter by sort order, publish time, duration and content type, with cursor pagination.

## Pricing

- **$0.015 per call** (USD)
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

Search Douyin's video tab for a keyword. Each result includes the video description, author and statistics.

### Use cases

- Find videos about a product or topic.
- Discover creators for influencer campaigns.
- Track video volume and engagement for a keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/video-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `keyword` | string | No | Search keyword, e.g., "robot" |
| `backtrace` | string | No | Backtrace identifier used for pagination(obtained from the last response) |
| `search_id` | string | No | Search ID used for pagination(obtained from the last response) |
| `sort_type` | string | No | Sorting method |
| `content_type` | string | No | Content type filter |
| `publish_time` | string | No | Publish time filter |
| `filter_duration` | string | No | Video duration filter |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "business_data": [
    {
      "type": 1,
      "data": {
        "aweme_info": {
          "aweme_id": "7581331706625500153",
          "create_time": 1765166347,
          "duration": 289767,
          "desc": "科普分享一些猫的种类，你看你认识几种！#盘点#科普#分享#猫",
          "author": {
            "nickname": "<user>",
            "sec_uid": "<sec_uid>"
          },
          "statistics": {
            "play_count": 0,
            "digg_count": 55214,
            "comment_count": 3720,
            "share_count": 10943,
            "collect_count": 21141
          },
          "share_url": "https://www.iesdouyin.com/share/video/7581331706625500153/?…"
        }
      }
    }
  ],
  "business_config": {
    "has_more": 1,
    "next_page": {
      "cursor": 10,
      "search_id": "<search_id>"
    }
  }
}
```

### Notes

- For the next page, pass back `cursor`, `search_id` and `backtrace` from the previous response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin General Search](/model/douyin/search/general-search-v1): Search Douyin (Chinese TikTok) from the app's general search tab and get videos with descriptions, authors and play, like, comment and share counts.
- [Fetch hashtag search V1](/model/douyin/search/challenge-search-v1): Fetch hashtag/challenge search results from Douyin App.
- [Fetch hashtag search V2](/model/douyin/search/challenge-search-v2): Fetch hashtag/challenge search results from Douyin App using V2 API.

---
Machine-readable: [`catalog/models/douyin/search/video-search-v2.json`](../../../../catalog/models/douyin/search/video-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/video-search-v2
