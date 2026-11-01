# Douyin High Fan Rate Billboard

`douyin/billboard/hot-total-high-fan-list` · api · Douyin

Returns Douyin billboard rankings for content with high follower conversion rates, filterable by keyword, category tags, and time window.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-high-fan-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-high-fan-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-high-fan-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-high-fan-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-high-fan-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Access Douyin billboard rankings for videos with high follow conversion rates using `keyword`, `tags`, and `date_window`.

### Use cases

- Track top Douyin content that drives high follower conversion.
- Filter viral creator videos by category tags and search keywords.
- Analyze high-performing video topics across hourly or daily windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-fan-list" \
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
| `page_size` | integer | No | Number of items per page |
| `date_window` | integer | No | Time window, 1 by hour 2 by day |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "objs": [
      {
        "fans_cnt": 229,
        "favorite_id": 0,
        "follow_cnt": 8251,
        "follow_rate": 0.015585,
        "image_cnt": 1,
        "item_cover_url": "https://p3-sign.douyinpic.com/tos-cn-i-0813c000-ce/ooBeZ7IgOlALaIsyF17L2YeCAvGtJ…",
        "item_duration": 0,
        "item_id": "7688038203362429882",
        "item_title": "抖音推流的核心规则，看懂少踩坑 1.只有观众在推荐页刷到你的视频，自愿看完、点赞评论，才算有效互动，能助推继续推流。 2.自己刷完反复播放、进别人主页求点赞、互赞秒评，这类虚假互…",
        "item_url": "https://lf9-music-east.douyinstatic.com/obj/ies-music-hj/7677505695020780345.mp3"
      }
    ]
  }
}
```

### Notes

- `date_window` sets the evaluation time window, such as 1 for hourly or 2 for daily.
- Results can be paginated using `page` and `page_size`.
- `tags` accepts category tags to narrow rankings by vertical topics.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-fan-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-fan-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-fan-list
