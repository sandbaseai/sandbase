# TikTok Creator Search Insights Videos API: pricing, parameters and code examples

`tiktok/app-v3/creator-search-insights-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns popular videos related to a specific search term from creator search insights. Results support pagination using offset and count parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/creator-search-insights-videos", "count": 1, "keyword": "app that", "offset": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/creator-search-insights-videos', {'count': 1, 'keyword': 'app that', 'offset': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/creator-search-insights-videos", {
  "count": 1,
  "keyword": "app that",
  "offset": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/creator-search-insights-videos", sandbase.Params{
	"count": 1,
	"keyword": "app that",
	"offset": 0,
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/creator-search-insights-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, default 20 default `20` |
| `offset` | integer |  | Pagination offset, default 0 default `0` |
| `keyword` | string | yes | Search keyword, obtained from fetch_creator_search_insights or fetch_creator_search_insights_trend  |

## Details

Query popular videos related to search topics by providing a `keyword` parameter. Control response volume and pagination using `count` and `offset`.

### Use cases

- Discover trending videos tied to specific search queries.
- Analyze high-performing content formats for target keywords.
- Track top video results from search insights topic lists.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/creator-search-insights-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword, obtained from fetch_creator_search_insights or fetch_creator_search_insights_trend |
| `count` | integer | No | Number per page, default 20 |
| `offset` | integer | No | Pagination offset, default 0 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "search_item_list": [
    {
      "aweme_info": {
        "author_user_id": 7648715379941901319,
        "aweme_id": "7691716847925824776",
        "aweme_type": 0,
        "bodydance_score": 0,
        "content_desc": "[\"in 2008 paul graham said you could parachute sam altman onto an island of cannibals and…",
        "content_level": 1
      }
    }
  ]
}
```

### Notes

- `keyword` can be obtained from creator search insights or search insights trend endpoints.
- `count` defaults to 20 items per page.
- `offset` defaults to 0 for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/creator-search-insights-videos.json`](../../../../catalog/models/tiktok/app-v3/creator-search-insights-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/creator-search-insights-videos
