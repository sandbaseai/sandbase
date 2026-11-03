# Douyin General Search API: pricing, parameters and code examples

`douyin/search/general-search-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Search Douyin (Chinese TikTok) from the app's general search tab and get videos with descriptions, authors and play, like, comment and share counts. Filter by sort, publish time, duration and content type.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/general-search-v1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/general-search-v1', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/general-search-v1", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/general-search-v1", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/general-search-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) default `0` |
| `keyword` | string |  | Search keyword, e.g., "cat" default `"猫咪"` |
| `backtrace` | string |  | Backtrace identifier (empty for first request, obtained from previous response for pagination) default `""` |
| `search_id` | string |  | Search ID (empty for first request, obtained from previous response for pagination) default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Search Douyin's general (comprehensive) tab for a keyword. Results include videos with their description, author, statistics and share URL.

### Use cases

- Discover trending Douyin content for a keyword.
- Find creators and videos for influencer marketing.
- Monitor brand or product mentions on Douyin.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/general-search-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `keyword` | string | No | Search keyword, e.g., "cat" |
| `backtrace` | string | No | Backtrace identifier (empty for first request, obtained from previous response for pagination) |
| `search_id` | string | No | Search ID (empty for first request, obtained from previous response for pagination) |
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
  "backtrace": "<backtrace>",
  "data": [
    {
      "type": 1,
      "aweme_info": {
        "aweme_id": "7565738211130035491",
        "create_time": 1761818400,
        "duration": 94000,
        "desc": "猫咪离家出走千万不要去找它 #养猫人#猫咪#养猫日常#养猫经验分享#新手养猫#养猫百科#萌宠#养猫…",
        "author": {
          "nickname": "<user>",
          "sec_uid": "<sec_uid>"
        },
        "statistics": {
          "play_count": 0,
          "digg_count": 86129,
          "comment_count": 4957,
          "share_count": 5232,
          "collect_count": 61272
        },
        "share_url": "https://www.iesdouyin.com/share/video/7565738211130035491/?…"
      }
    }
  ]
}
```

### Notes

- For the next page, pass back `cursor`, `search_id` and `backtrace` from the previous response.
- Filters (`sort_type`, `publish_time`, `filter_duration`, `content_type`) use string codes; `"0"` means no filter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Video Search](/apis/douyin/search/video-search-v2): Search Douyin videos by keyword and get descriptions, authors and play, like, comment and share counts.
- [Fetch hashtag search V1](/apis/douyin/search/challenge-search-v1): Fetch hashtag/challenge search results from Douyin App.
- [Fetch hashtag search V2](/apis/douyin/search/challenge-search-v2): Fetch hashtag/challenge search results from Douyin App using V2 API.

---
Machine-readable: [`catalog/models/douyin/search/general-search-v1.json`](../../../../catalog/models/douyin/search/general-search-v1.json) · Store page: https://www.sandbase.ai/model/douyin/search/general-search-v1
