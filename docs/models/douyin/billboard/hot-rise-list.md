# Douyin Rising Hot Search List API: pricing, parameters and code examples

`douyin/billboard/hot-rise-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin rising hot search topics and billboard rankings. Results can be filtered by keyword, sorted by a specified order, and segmented by category tags.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-rise-list", "order": "test", "page": 0, "page_size": 10}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-rise-list', {'order': 'test', 'page': 0, 'page_size': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-rise-list", {
  "order": "test",
  "page": 0,
  "page_size": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-rise-list", sandbase.Params{
	"order": "test",
	"page": 0,
	"page_size": 10,
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-rise-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number  |
| `order` | string | yes | Sorting method  |
| `keyword` | string |  | Hot search term  |
| `page_size` | integer | yes | Number of items per page  |
| `sentence_tag` | string |  | Hot category tag, get from hot list category, multiple categories separated by commas, empty for all  |

## Details

Returns a page of Douyin rising hot search topics with rank, hot score, category tag and hourly trend points. It needs `order`, `page` and `page_size`, and can also filter by `keyword` or `sentence_tag`.

### Use cases

- Track which Douyin search topics climb the ranking and by how many places.
- Chart the hourly heat of a topic from its `trends` values.
- Pull rising topics for one category, such as sports or finance, with `sentence_tag`.
- Search for a specific hot term with `keyword` to see where it ranks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-rise-list" \
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
        "SnapshotSubType": "",
        "SnapshotType": 100,
        "allow_publish": false,
        "city_code": 0,
        "city_name": "",
        "create_at": 1793683374,
        "first_item_cover_url": "",
        "hot_score": 7795171,
        "index": 1,
        "is_favorite": false,
        "item_list": null
      }
    ],
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 1852
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
| `data.objs[].sentence` | The hot search topic text. |
| `data.objs[].sentence_id` | ID of the hot search topic. |
| `data.objs[].rank / data.objs[].index` | Position of the topic in the list. In the sample, both match the topic's place on the page. |
| `data.objs[].rank_diff` | Change in rank. A larger number means a bigger move. |
| `data.objs[].hot_score` | Current heat score of the topic. |
| `data.objs[].sentence_tag / data.objs[].sentence_tag_name` | Numeric category code and its name, for example `5000` and `体育`. |
| `data.objs[].trends[].datetime / data.objs[].trends[].hot_score` | Hour label such as `2026-11-03 13` and the heat score at that hour. |
| `data.objs[].video_count` | Number of videos linked to the topic. |
| `data.objs[].create_at` | Unix timestamp in seconds for the topic's creation. |
| `data.page.total` | Total number of items that match the request. |
| `data.last_update_time` | Time of the latest snapshot, written as `YYYYMMDDHHMMSS`. |

### Notes

- Set `page` and `page_size` to walk through the list. `data.page.total` shows how many items exist.
- Get `sentence_tag` values from [Douyin Billboard Hot Category List](/apis/douyin/billboard/hot-category-list). Separate several tags with commas, or leave it empty for all.
- In the sample request, `order` is `rank`.
- Fields such as `item_list` and `related_event` came back as `null` in the sample.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-rise-list.json`](../../../../catalog/models/douyin/billboard/hot-rise-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-rise-list
