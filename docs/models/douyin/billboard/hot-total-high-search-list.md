# Douyin Billboard Rising Search List API: pricing, parameters and code examples

`douyin/billboard/hot-total-high-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns rising search queries and trend data from the Douyin billboard. Supports filtering by search keyword, time window, and standard pagination options.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-high-search-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-high-search-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-high-search-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-high-search-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-high-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search keyword default `"抖音"` |
| `page_num` | integer |  | Page number default `1` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a list of rising search queries from the Douyin billboard. Each item has a search score and a daily trend series. All inputs are optional: `keyword`, `date_window`, `page_num` and `page_size`.

### Use cases

- Find search terms on Douyin that are gaining volume around a topic such as a brand or product name.
- Chart the daily `value` series of a rising query to see whether interest is still climbing or fading.
- Rank related queries by `search_score` to pick keywords for Douyin content or ad planning.
- Page through the full result set with `total_count` to build a keyword list for a topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-search-list" \
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
        "key_word": "抖音来客",
        "search_score": 1933570,
        "trends": [
          {
            "date": "20261020",
            "value": 1771342
          }
        ]
      }
    ],
    "page_num": 1,
    "page_size": 10,
    "search_list": [
      {
        "key_word": "抖音来客",
        "search_score": 1933570,
        "trends": [
          {
            "date": "20261020",
            "value": 1771342
          }
        ]
      }
    ],
    "total_count": 74
  },
  "extra": {
    "now": 1793691109000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.search_list[].key_word` | The rising search query text. |
| `data.search_list[].search_score` | A single score for the query. Use it to compare queries within the same response. |
| `data.search_list[].trends[].date` | Date of the trend point as a `YYYYMMDD` string, for example `20261022`. |
| `data.search_list[].trends[].value` | Trend value for that date. Read the points in order to see the direction of the query. |
| `data.objs[]` | Holds the same items as `data.search_list[]`, with the same `key_word`, `search_score` and `trends` fields. |
| `data.total_count` | Total number of matching queries across all pages. |
| `data.page_num / data.page_size` | The page number and page size that the response used. |
| `extra.now` | A timestamp in the `extra` block, shown as a 13-digit number that looks like Unix time in milliseconds. |

### Notes

- All parameters are optional. The response shows `page_num` as `1` and `page_size` as `10` when you send an empty body.
- Raise `page_num` and compare against `total_count` to read every page.
- Set `date_window` to `1` for hourly data or `2` for daily data. The example response contains daily `YYYYMMDD` dates.
- For other Douyin search rankings, see [Douyin Hot Total Search List](/apis/douyin/billboard/hot-total-search-list) and [Douyin Rising Hot Search List](/apis/douyin/billboard/hot-rise-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-search-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-search-list
