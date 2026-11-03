# Douyin Hot Content Words API: pricing, parameters and code examples

`douyin/billboard/hot-total-hot-word-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending content words and popularity scores from Douyin billboards. Supports filtering by search keyword, time window, and pagination parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-hot-word-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-hot-word-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-hot-word-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-hot-word-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-hot-word-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search keyword default `"抖音"` |
| `page_num` | integer |  | Page number default `1` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of Douyin billboard content words that match a search keyword. Each word has a popularity `score` and a daily trend series. The request takes optional `keyword`, `date_window`, `page_num` and `page_size` values.

### Use cases

- Check how popular a phrase such as `人工智能` is on Douyin compared with similar words.
- Chart the daily trend values of a content word to see when interest peaked.
- Build a list of related content words around a brand or topic keyword.
- Page through all matching words to export a full keyword set for research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-hot-word-list" \
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
        "favorite_id": 0,
        "id": "NRsKn6EBoYl6zwhYLhSC",
        "is_favorite": false,
        "query_day": "20261102",
        "rising_ratio": 0,
        "rising_speed": "",
        "score": 112,
        "title": "抖音音乐",
        "trends": [
          {
            "date": "20260928",
            "value": 9177.417093277045
          }
        ]
      }
    ],
    "total_count": 1268,
    "word_list": [
      {
        "favorite_id": 0,
        "id": "NRsKn6EBoYl6zwhYLhSC",
        "is_favorite": false,
        "query_day": "20261102",
        "rising_ratio": 0,
        "rising_speed": "",
        "score": 112,
        "title": "抖音音乐",
        "trends": [
          {
            "date": "20260928",
            "value": 9177.417093277045
          }
        ]
      }
    ]
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
| `data.word_list[].title` | The content word text. |
| `data.word_list[].score` | Popularity score of the word. Higher values mean a more popular word. |
| `data.word_list[].id` | Identifier of the word entry. |
| `data.word_list[].query_day` | Day of the query, as a `YYYYMMDD` string. |
| `data.word_list[].trends[].date / data.word_list[].trends[].value` | One point of the trend series. `date` is a `YYYYMMDD` string and `value` is the metric number for that day. |
| `data.word_list[].rising_ratio / data.word_list[].rising_speed` | Rise indicators for the word. They were `0` and an empty string in this sample. |
| `data.word_list[].is_favorite / data.word_list[].favorite_id` | Favorite state of the word for the account. They were `false` and `0` in this sample. |
| `data.total_count` | Total number of words that match the request. Use it to work out how many pages exist. |
| `data.objs[]` | Holds the same items as `data.word_list[]`. |

### Notes

- Set `date_window` to `1` for hourly data or `2` for daily data.
- Page through results with `page_num` and `page_size`. Compare `data.total_count` with the number of items you have fetched.
- Dates in `query_day` and `trends[].date` use the `YYYYMMDD` format.
- For details on a single word, try [Douyin Billboard Hot Word Details](/apis/douyin/billboard/hot-total-hot-word-detail-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-hot-word-list.json`](../../../../catalog/models/douyin/billboard/hot-total-hot-word-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-hot-word-list
