# Douyin Hot Topic Billboard API: pricing, parameters and code examples

`douyin/billboard/hot-total-topic-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending topic rankings and historical trend metrics from Douyin. Results can be filtered by keyword, vertical category tags, and time window.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-topic-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-topic-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-topic-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-topic-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-topic-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of trending Douyin topics (challenges) with play counts, post counts, and daily trend values. All inputs are optional: you can filter by `keyword`, vertical category `tags`, and a time window set with `date_window`.

### Use cases

- Pull the current top Douyin topics and rank them by `score` for a daily trend report.
- Chart the daily `trends` values of a topic to see when it started to rise.
- Compare `play_cnt` and `publish_cnt` across topics to find topics with many views but few posts.
- Search a `keyword` to check whether a brand or event name appears on the topic billboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-topic-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_window` | integer | No | Time window, 1 by hour 2 by day |
| `keyword` | string | No | Search keyword to filter the billboard, empty for all |
| `page` | integer | No | Page number |
| `page_size` | integer | No | Number of items per page |
| `tags` | array | No | Sub-level vertical category tag, empty for all, multiple tags need to be passed in |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "objs": [
      {
        "avg_play_cnt": 38079,
        "challenge_id": "1595429526316039",
        "challenge_name": "灭霸",
        "challenge_type": 0,
        "cover_url": "https://p26-sign.douyinpic.com/aweme/200x200/image-cut-tos/b2179d18e9b91ba0d9221…",
        "create_time": 1521520163,
        "is_favorite": false,
        "is_recommend": false,
        "item_list": null,
        "origin_rank": 1,
        "origin_trend_str": "20261020:3370532.0,20261028:1.7237847E7,20261021:5037043.0,20261022:4111507.0,20…",
        "play_cnt": 5227547011
      }
    ],
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 1000
    }
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
| `data.objs[].challenge_name` | Name of the topic (challenge), as shown on Douyin. |
| `data.objs[].challenge_id` | ID of the topic, returned as a string. |
| `data.objs[].real_rank / show_rank / origin_rank` | Rank values of the topic on the billboard. In this response all three are equal for each item. |
| `data.objs[].score` | Hotness score for the topic in the selected window. Items are listed in descending order of this score. |
| `data.objs[].play_cnt` | Total play count for the topic. |
| `data.objs[].publish_cnt` | Number of posts published under the topic. |
| `data.objs[].avg_play_cnt` | Average play count per post for the topic. |
| `data.objs[].trends[].date / trends[].value` | Daily trend points for the topic. `date` is formatted as `YYYYMMDD` and `value` is the metric for that day. |
| `data.objs[].create_time` | Creation time of the topic as a Unix timestamp in seconds. |
| `data.page.total` | Total number of items available for the query, along with the current `page` and `page_size`. |

### Notes

- `data.objs[].origin_trend_str` repeats the trend data as one string of `date:value` pairs separated by commas. Use `trends` for easier parsing.
- Page through results with `page` and `page_size`. The response returns the current values in `data.page`.
- Get valid `tags` values from [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag).
- `data.objs[].cover_url` is a signed image link that contains an `x-expires` parameter, so download the image soon after you fetch it.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-topic-list.json`](../../../../catalog/models/douyin/billboard/hot-total-topic-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-topic-list
