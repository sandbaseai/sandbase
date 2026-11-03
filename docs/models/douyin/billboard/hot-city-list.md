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

Returns Douyin trending topics for a city, one ranked entry per topic with its hot score, category tag and recent score history. It needs `order`, `page` and `page_size`. You can narrow results with `city_code`, `sentence_tag` and `keyword`.

### Use cases

- Track which topics rank highest in a single city such as Beijing.
- Filter a city's hot topics by category, for example travel or food, to find local content ideas.
- Sort by `rank_diff` to find topics that moved the most in the ranking.
- Chart the `trends` history of a topic to see how its hot score changed over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-city-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"order": "rank", "page": 1, "page_size": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `order` | string | Yes | Sorting method |
| `page` | integer | Yes | Page number |
| `page_size` | integer | Yes | Number of items per page |
| `city_code` | string | No | City code, get from city list, empty for all |
| `keyword` | string | No | Hot search term |
| `sentence_tag` | string | No | Hot category tag, get from hot list category, multiple categories separated by commas, empty for all |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "last_update_time": "20261103152500",
    "objs": [
      {
        "SnapshotID": 20261103152500,
        "SnapshotSubType": "110000",
        "SnapshotType": 1,
        "allow_publish": false,
        "city_code": 0,
        "city_name": "北京",
        "create_at": 1793515244,
        "first_item_cover_url": "",
        "hot_score": 8223985,
        "index": 1,
        "is_favorite": false,
        "item_list": null
      }
    ],
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 8017
    }
  },
  "extra": {
    "now": 1793691107000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.objs[].sentence` | The hot topic text as shown on the billboard. |
| `data.objs[].rank / data.objs[].index` | Position of the topic in the list. Both are 1 for the first item. |
| `data.objs[].rank_diff` | Change value for the rank. Use it with `order` set to `rank_diff` to sort by this value. |
| `data.objs[].hot_score` | Current hot score of the topic. |
| `data.objs[].city_name / data.objs[].city_code` | Name and code of the city the topic belongs to. A `city_code` of `0` appears on a row whose `city_name` is still the city name, so rely on `city_name` too. |
| `data.objs[].sentence_tag / data.objs[].sentence_tag_name` | Numeric category tag and its name, such as `旅行` (travel), `娱乐` (entertainment) or `美食` (food). |
| `data.objs[].sentence_id` | Numeric ID of the hot topic. |
| `data.objs[].video_count` | Number of videos linked to the topic. |
| `data.objs[].trends[]` | Score history for the topic. Each entry has a `datetime` and a `hot_score`. |
| `data.page.total` | Total number of matching topics across all pages. |
| `data.last_update_time` | Time of the latest snapshot, written as `YYYYMMDDHHMMSS`. |

### Notes

- Get `city_code` from [Douyin Billboard City List](/apis/douyin/billboard/city-list).
- Get `sentence_tag` values from [Douyin Billboard Hot Category List](/apis/douyin/billboard/hot-category-list). Separate several tags with commas.
- Page through results with `page` and `page_size`. Compare `data.page.total` with the number of rows you have read.
- `datetime` values in `trends` use the format `YYYYMMDDHHMMSS`. `create_at` is a Unix timestamp in seconds.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-city-list.json`](../../../../catalog/models/douyin/billboard/hot-city-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-city-list
