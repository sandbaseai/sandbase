# Douyin Hot Total Search List API: pricing, parameters and code examples

`douyin/billboard/hot-total-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin billboard search hot list rankings and search trend metrics. Supports filtering by keyword, date window timeframe, and pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-search-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-search-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-search-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-search-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search keyword default `"抖音"` |
| `page_num` | integer |  | Page number default `1` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of Douyin search keywords from the billboard, each with a search score and a short daily trend. It takes an optional `keyword`, a `date_window` mode, and pagination parameters. The default `keyword` is `抖音`.

### Use cases

- Compare the search score of related queries such as `抖音客服` and `抖音热门` in one call.
- Chart the daily search volume of a keyword over the returned date range.
- Page through all matching keywords to build a list of search terms around a topic.
- Switch `date_window` between hourly and daily mode to compare short-term and longer-term search interest.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_window` | integer | No | Time window, 1 by hour 2 by day |
| `keyword` | string | No | Search keyword |
| `page_num` | integer | No | Page number |
| `page_size` | integer | No | Number of items per page |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "objs": [
      {
        "key_word": "抖音",
        "search_score": 3542056,
        "trends": [
          {
            "date": "20261020",
            "value": 3322408
          }
        ]
      }
    ],
    "page_num": 1,
    "page_size": 10,
    "search_list": [
      {
        "key_word": "抖音",
        "search_score": 3542056,
        "trends": [
          {
            "date": "20261020",
            "value": 3322408
          }
        ]
      }
    ],
    "total_count": 820
  },
  "extra": {
    "now": 1793691110000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.search_list[].key_word` | The search keyword for this ranking row. |
| `data.search_list[].search_score` | The search score of the keyword. Higher values mean more search interest. Rows come ordered from highest to lowest score. |
| `data.search_list[].trends[].date` | The date of the trend point as a `YYYYMMDD` string, for example `20261022`. |
| `data.search_list[].trends[].value` | The search value for the keyword on that date. |
| `data.objs[]` | Holds the same rows as `data.search_list[]`, with the same `key_word`, `search_score` and `trends` fields. |
| `data.total_count` | The total number of keywords that match the request, across all pages. |
| `data.page_num / data.page_size` | The page number and page size that the response used. |
| `extra.now` | A millisecond timestamp attached to the response. |

### Notes

- Set `page_num` and `page_size` to walk through the list. Compare `data.total_count` with the number of rows you have read to know when to stop.
- `date_window` takes `1` for hourly mode or `2` for daily mode.
- `data.objs` and `data.search_list` hold the same rows, so read only one of them.
- For a list of rising search terms, call [Douyin Billboard Rising Search List](/apis/douyin/billboard/hot-total-high-search-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-search-list.json`](../../../../catalog/models/douyin/billboard/hot-total-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-search-list
