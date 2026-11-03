# Douyin Video Search (V1) API: pricing, parameters and code examples

`douyin/search/video-search-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync, async

Search Douyin videos by keyword: descriptions, authors and play, like, comment and share counts, with sort, publish-time, duration and content-type filters.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync, async (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/video-search-v1", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/video-search-v1', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/video-search-v1", {
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
run, err := c.Run(ctx, "douyin/search/video-search-v1", sandbase.Params{
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

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/douyin/search/video-search-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) default `0` |
| `keyword` | string |  | Search keyword, e.g., "Artificial Intelligence" default `"猫咪"` |
| `backtrace` | string |  | Backtrace identifier used for pagination(obtained from the last response) default `""` |
| `search_id` | string |  | Search ID used for pagination(obtained from the last response) default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Search Douyin's video results for a keyword, with the same filters as the app.

### Use cases

- Find videos about a product or topic.
- Discover creators for campaigns.
- Track video volume for a keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/video-search-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `keyword` | string | No | Search keyword, e.g., "Artificial Intelligence" |
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
  "cursor": 10,
  "has_more": 1,
  "search_id": "<search_id>",
  "data": [
    {
      "type": 1,
      "aweme_info": {
        "aweme_id": "7626222853277534707",
        "create_time": 1775618376,
        "desc": "据说这是猫咪无法抗拒的声音！你家猫听到会有什么反应？快试了来告诉我～  #猫咪男高音 #蓝金渐层#…",
        "author": {
          "nickname": "<user>",
          "sec_uid": "<sec_uid>"
        },
        "statistics": {
          "play_count": 0,
          "digg_count": 62040,
          "comment_count": 3678,
          "share_count": 21334,
          "collect_count": 12233
        }
      }
    }
  ]
}
```

### Notes

- For the next page, pass back `cursor`, `search_id` and `backtrace`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin General Search](/apis/douyin/search/general-search-v1): Search Douyin (Chinese TikTok) from the app's general search tab and get videos with descriptions, authors and play, like, comment and share counts.
- [Douyin Search Suggestions](/apis/douyin/search/search-suggest): Get Douyin search autocomplete suggestions for a keyword: the related queries users see while typing in the Douyin app.
- [Douyin Video Search](/apis/douyin/search/video-search-v2): Search Douyin videos by keyword and get descriptions, authors and play, like, comment and share counts.

---
Machine-readable: [`catalog/models/douyin/search/video-search-v1.json`](../../../../catalog/models/douyin/search/video-search-v1.json) · Store page: https://www.sandbase.ai/model/douyin/search/video-search-v1
