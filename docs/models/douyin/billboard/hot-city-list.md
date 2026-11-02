# Douyin City Hot List API: pricing, parameters and code examples

`douyin/billboard/hot-city-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin trending topics filtered by city location. Allows sorting and filtering by city code, category tags, and search keywords.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-city-list", "order": "rank", "page": 1, "page_size": 10}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-city-list', {'order': 'rank', 'page': 1, 'page_size': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-city-list", {
  "order": "rank",
  "page": 1,
  "page_size": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-city-list", sandbase.Params{
	"order": "rank",
	"page": 1,
	"page_size": 10,
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-city-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number  |
| `order` | string | yes | Sorting method  |
| `keyword` | string |  | Hot search term default `""` |
| `city_code` | string |  | City code, get from city list, empty for all default `""` |
| `page_size` | integer | yes | Number of items per page  |
| `sentence_tag` | string |  | Hot category tag, get from hot list category, multiple categories separated by commas, empty for all default `""` |

## Details

Query Douyin regional trending lists using `city_code` and `sentence_tag` to track location-specific topics and their trend scores.

### Use cases

- Track trending local topics across specific cities on Douyin.
- Filter regional billboard rankings by category tags or keywords.
- Monitor historical hot score trends for location-based search terms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-city-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"order": "rank", "page": 1, "page_size": 10}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | Yes | Page number |
| `order` | string | Yes | Sorting method |
| `page_size` | integer | Yes | Number of items per page |
| `keyword` | string | No | Hot search term |
| `city_code` | string | No | City code, get from city list, empty for all |
| `sentence_tag` | string | No | Hot category tag, get from hot list category, multiple categories separated by commas, empty for all |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "objs": [
      {
        "trends": [
          {
            "datetime": "20261006092500",
            "hot_score": 4026339
          }
        ]
      }
    ]
  }
}
```

### Notes

- Leave `city_code` empty to retrieve trending topics across all cities.
- Multiple tags in `sentence_tag` can be separated by commas, or left empty for all categories.
- Pagination is controlled using the required `page` and `page_size` parameters.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-city-list.json`](../../../../catalog/models/douyin/billboard/hot-city-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-city-list
