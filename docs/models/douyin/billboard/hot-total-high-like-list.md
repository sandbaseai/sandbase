# Douyin High Like Rate Billboard

`douyin/billboard/hot-total-high-like-list` · api · Douyin

Returns trending Douyin videos ranked by high like rates. Filter results by category tags, search keywords, time windows, and pagination parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-high-like-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-high-like-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-high-like-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-high-like-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-high-like-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number default `1` |
| `tags` | array |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in  |
| `keyword` | string |  | Search keyword to filter the billboard, empty for all default `""` |
| `page_size` | integer |  | Number of items per page default `10` |
| `date_window` | integer |  | Time window, 1 by hour 2 by day default `24` |

## Details

Retrieve rankings of Douyin videos with high like rates using optional filters such as `tags`, `keyword`, and `date_window`.

### Use cases

- Identify top-performing Douyin videos with exceptional engagement rates.
- Monitor viral video trends filtered by category tags or search keywords.
- Inspect engagement metrics including follower growth rates and view durations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-like-list" \
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
        "fans_cnt": 7287,
        "favorite_id": 0,
        "follow_cnt": 3774,
        "follow_rate": 0.00029,
        "image_cnt": 0,
        "item_cover_url": "https://p3-sign.douyinpic.com/tos-cn-i-0813/o0Akye3HDQGhAD9UAwFAGA7OhEfYVABIEeAE…",
        "item_duration": 13652,
        "item_id": "7692681489309628406",
        "item_title": "谁能翻译下😅#猫咪 #喵语 #猫咪的迷惑行为",
        "item_url": "https://v11-cold1.douyinvod.com/91dceb8bc953f41a1e93392f24bfd743/6ac4f9c5/video/…"
      }
    ]
  }
}
```

### Notes

- Use `date_window` to set the time frame (1 for hourly, 2 for daily).
- Supports pagination with `page` and `page_size`.
- Leave `keyword` or `tags` empty to return billboard rankings across all categories.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-like-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-like-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-like-list
