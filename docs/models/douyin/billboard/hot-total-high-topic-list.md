# Douyin Rising Popularity Topic List API: pricing, parameters and code examples

`douyin/billboard/hot-total-high-topic-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending Douyin topics with rising popularity and historical trend metrics. Supports filtering by keyword, vertical category tags, time window, and pagination parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-high-topic-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-high-topic-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-high-topic-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-high-topic-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-high-topic-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Returns a ranked list of Douyin topics (challenges) whose popularity is rising, with play counts, post counts and daily trend values. All inputs are optional. You can filter by `keyword`, `tags` and `date_window`, and page through results with `page` and `page_size`.

### Use cases

- Spot Douyin topics that are gaining plays so you can plan content around them.
- Chart the daily trend values of a topic to see when it peaked.
- Compare `publish_cnt` and `avg_play_cnt` across topics to find ones with high reach per post.
- Pull a keyword-filtered topic list to check whether a theme is currently rising.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-topic-list" \
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
        "avg_play_cnt": 19064,
        "challenge_id": "1730102465878094",
        "challenge_name": "纯稚",
        "challenge_type": 1,
        "cover_url": "https://p11-sign.douyinpic.com/aweme/200x200/image-cut-tos/798fb02bb4e6ac27b2363…",
        "create_time": 1649956392,
        "is_favorite": false,
        "is_recommend": false,
        "item_list": null,
        "origin_rank": 1,
        "origin_trend_str": "20261020:29349.0,20261030:3224149.0,20261028:1157806.0,20261022:20401.0,20261027…",
        "play_cnt": 1323482617
      }
    ],
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 1000
    }
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
| `data.objs[].challenge_id / challenge_name` | ID and display name of the topic (challenge). |
| `data.objs[].real_rank / show_rank / origin_rank` | Rank positions of the topic in the list. They are all `1` for the top item in this response. |
| `data.objs[].score` | Popularity score of the topic used for the ranking. |
| `data.objs[].play_cnt` | Total plays recorded for the topic. |
| `data.objs[].publish_cnt` | Number of videos published under the topic. |
| `data.objs[].avg_play_cnt` | Average plays per video for the topic. |
| `data.objs[].trends[].date / value` | Daily trend points. `date` is a `YYYYMMDD` string and `value` is the metric for that day. |
| `data.objs[].origin_trend_str` | The same trend data as one string of `date:value` pairs separated by commas. |
| `data.objs[].create_time` | Creation time of the topic as a Unix timestamp in seconds. |
| `data.objs[].cover_url` | Link to a cover image for the topic. |
| `data.page.page / page_size / total` | Current page number, items per page, and total number of matching topics. |

### Notes

- Send `date_window` as `1` for hourly or `2` for daily, as described in the parameter schema.
- Page through results with `page` and `page_size`. The `data.page.total` value shows how many topics match.
- To fill `tags`, get category values from [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag).
- `item_list` and `related_event` were `null` in the sample response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-topic-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-topic-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-topic-list
