# TikTok Video Keyword Search

`tiktok/app-v3/video-search-result` · api · TikTok

Returns a list of TikTok videos matching a search query. Supports filtering by target region, time range, and relevance or like count sorting.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/video-search-result", "count": 3, "keyword": "AI", "publish_time": 7, "region": "US", "sort_type": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/video-search-result', {'count': 3, 'keyword': 'AI', 'publish_time': 7, 'region': 'US', 'sort_type': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/video-search-result", {
  "count": 3,
  "keyword": "AI",
  "publish_time": 7,
  "region": "US",
  "sort_type": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/video-search-result", sandbase.Params{
	"count": 3,
	"keyword": "AI",
	"publish_time": 7,
	"region": "US",
	"sort_type": 0,
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/video-search-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `region` | string |  | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. default `"US"` |
| `keyword` | string | yes | Keyword  |
| `sort_type` | integer |  | 0-Relatedness, 1-Most likes default `0` |
| `publish_time` | integer |  | 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year default `0` |

## Details

Search for TikTok videos matching a query by providing a `keyword`. You can also filter results by `region`, `sort_type`, and `publish_time`.

### Use cases

- Find relevant TikTok videos based on specific search keywords.
- Track popular content filtered by region and like count.
- Monitor recent video trends within specific date intervals.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/video-search-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |
| `region` | string | No | Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes. |
| `sort_type` | integer | No | 0-Relatedness, 1-Most likes |
| `publish_time` | integer | No | 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "search_item_list": [
    {
      "aweme_info": {
        "author_user_id": 6839011172614194182,
        "aweme_id": "7692923759547682078",
        "aweme_type": 0,
        "bodydance_score": 0,
        "content_level": 1,
        "content_original_type": 2
      }
    }
  ]
}
```

### Notes

- Set `sort_type` to 0 for relatedness or 1 for most likes.
- Filter by date with `publish_time` using 0 (unlimited), 1 (last day), 7 (last week), 30 (last month), 90 (last 3 months), or 180 (last half year).
- Specify `region` using ISO 3166-1 alpha-2 country codes, with US as the default.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/video-search-result.json`](../../../../catalog/models/tiktok/app-v3/video-search-result.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/video-search-result
