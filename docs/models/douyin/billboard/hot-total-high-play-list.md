# Douyin High Completion Rate Billboard API: pricing, parameters and code examples

`douyin/billboard/hot-total-high-play-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin billboard rankings for videos with high completion rates. Filter results by search keyword, category tags, time window, and pagination settings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-high-play-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-high-play-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-high-play-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-high-play-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-high-play-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Retrieve top-performing Douyin videos with high completion rates. Filter rankings using `keyword`, category `tags`, and `date_window`.

### Use cases

- Discover high-retention Douyin videos across specific categories.
- Monitor top viral content trends within hourly or daily time windows.
- Track audience engagement metrics and follow rates for benchmark analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-play-list" \
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
        "fans_cnt": 1597,
        "favorite_id": 0,
        "follow_cnt": 2072,
        "follow_rate": 0.000136,
        "image_cnt": 0,
        "item_cover_url": "https://p26-sign.douyinpic.com/tos-cn-p-0015c000-ce/ooeXGE3JA1yInDW1HQnii2FYEBlf…",
        "item_duration": 9000,
        "item_id": "7692743433555444923",
        "item_title": "小孩哥你认错人了#牵错人的尴尬",
        "item_url": "https://v26-cold.douyinvod.com/dc00f5f449521a9a0c4973b396e08ae3/6ac4fa14/video/t…"
      }
    ]
  }
}
```

### Notes

- Use `date_window` to set the time window (1 for hourly, 2 for daily).
- Filter rankings by category with `tags` or by search term using `keyword`.
- Control pagination with `page` and `page_size`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-play-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-play-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-play-list
