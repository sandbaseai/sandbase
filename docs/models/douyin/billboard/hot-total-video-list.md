# Douyin Hot Video Ranking API: pricing, parameters and code examples

`douyin/billboard/hot-total-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Get Douyin hot video rankings: overall hot videos, low-follower breakouts, high completion, follower growth and like-rate lists, with play, like and follower stats, filters by category and time window.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-video-list", "keyword": "", "page": 20, "page_size": 50, "sub_type": 1001, "tags": []}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-video-list', {'keyword': '', 'page': 20, 'page_size': 50, 'sub_type': 1001, 'tags': []})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-video-list", {
  "keyword": "",
  "page": 20,
  "page_size": 50,
  "sub_type": 1001,
  "tags": []
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-video-list", sandbase.Params{
	"keyword": "",
	"page": 20,
	"page_size": 50,
	"sub_type": 1001,
	"tags": []any{},
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `sub_type` | integer |  | List category, 1001 Video total list 1002 Low fan explosion 1003 High completion rate 1004 High fan growth rate 1005 High like rate default `1001` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Fetch the Douyin (Juliang Suanshu) hot video billboard. Choose a list type with `sub_type`, filter by keyword or vertical tags, and get ranked videos with play, like and follower metrics.

### Use cases

- Spot trending videos and formats before they peak.
- Find low-follower creators with breakout videos.
- Benchmark like rate and completion for a category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number |
| `tags` | array | No | Sub-level vertical category tag, empty for all, multiple tags need to be passed in |
| `keyword` | string | No | Search keyword to filter the billboard, empty for all |
| `sub_type` | integer | No | List category, 1001 Video total list 1002 Low fan explosion 1003 High completion rate 1004 High fan growth rate 1005 Hi… |
| `page_size` | integer | No | Number of items per page |
| `date_window` | integer | No | Time window, 1 by hour 2 by day |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "code": 0,
  "data": {
    "page": {
      "page": 1,
      "page_size": 10,
      "total": 1000
    },
    "objs": [
      {
        "item_id": "7692681489309628406",
        "publish_time": 1791091983,
        "item_duration": 13652,
        "play_cnt": 13545023,
        "like_cnt": 1218230,
        "like_rate": 0.089939,
        "follow_rate": 0.00029,
        "fans_cnt": 6604,
        "score": 1215906,
        "item_title": "谁能翻译下😅#猫咪 #喵语 #猫咪的迷惑行为",
        "nick_name": "<user>"
      }
    ]
  }
}
```

### Notes

- `sub_type`: 1001 overall, 1002 low-follower breakouts, 1003 high completion, 1004 follower growth, 1005 like rate.
- `date_window`: 1 = by hour, 2 = by day (default 24).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Fetch Chinese city list](/model/douyin/billboard/city-list): Get city list.
- [Fetch vertical content tags](/model/douyin/billboard/content-tag): Get vertical content tags.
- [Fetch fan interest author 20 users](/model/douyin/billboard/hot-account-fans-interest-account-list): Get the fan interest author 20 users.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-video-list.json`](../../../../catalog/models/douyin/billboard/hot-total-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-video-list
