# Kuaishou Comprehensive Search API: pricing, parameters and code examples

`kuaishou/app/search-comprehensive` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Returns aggregated search feeds across videos and users on Kuaishou, with filtering options for duration, sort order, and release timeframe.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-comprehensive", "keyword": "汽车之家"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-comprehensive', {'keyword': '汽车之家'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-comprehensive", {
  "keyword": "汽车之家"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-comprehensive", sandbase.Params{
	"keyword": "汽车之家",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-comprehensive` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | 分页游标/Pagination cursor  |
| `duration` | string |  | Duration filter one of: `all`, `under_1_min`, `1_to_5_min`, `over_5_min`; default `"all"` |
| `sort_type` | string |  | Sort type one of: `all`, `newest`, `most_likes`; default `"all"` |
| `publish_time` | string |  | Publish time filter one of: `all`, `one_day`, `one_week`, `one_month`; default `"all"` |

## Details

Search across Kuaishou feeds using a target `keyword` with optional filters for sorting, video duration, and upload date.

### Use cases

- Discover trending videos and posts matching a specific search query.
- Filter search results by duration and engagement metrics.
- Track recent platform discussions across custom time ranges.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-comprehensive" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | — |
| `pcursor` | string | No | — |
| `duration` | string | No | Duration filter |
| `sort_type` | string | No | Sort type |
| `publish_time` | string | No | Publish time filter |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "mixFeeds": [
    {
      "atmosphereType": 0,
      "itemType": 5,
      "rank": 0,
      "extInfo": {
        "recoType": 101
      },
      "feed": {
        "caption": "世界上最强大的AI排名，2026年\r #世界之最  #AI  #大模型  #deepseek",
        "captionSpliceAnnotation": "(来源：其他平台)",
        "captionToComment": "世界上最强大的AI排名，2026年  #世界之最 #AI #大模型 #deepseek",
        "clearScreenSameAuthorCount": 938,
        "collect_count": 5245,
        "comment_count": 3450
      },
      "searchTitleInfo": {
        "actionType": 1,
        "searchFeedTitle": "热评 Gemini和ChatGPT我都有，但是个人感觉Gemini的生态更好一点",
        "titlePosition": 1,
        "titleType": "COMMENT"
      }
    }
  ]
}
```

### Notes

- Pass `pcursor` to navigate through paginated search results.
- Filter by `duration` with options such as `under_1_min`, `1_to_5_min`, and `over_5_min`.
- Sort results using `sort_type` options such as `newest` or `most_likes`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-comprehensive.json`](../../../../catalog/models/kuaishou/app/search-comprehensive.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-comprehensive
