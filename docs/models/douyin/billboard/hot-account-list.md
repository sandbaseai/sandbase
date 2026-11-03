# Douyin Hot Account List API: pricing, parameters and code examples

`douyin/billboard/hot-account-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending Douyin accounts from the billboard ranking with engagement metrics. Supports filtering by category tag via query_tag and time window via date_window.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page_num` | integer |  | Page number, default 1 default `1` |
| `page_size` | integer |  | Number of items per page, default 20 default `10` |
| `query_tag` | object |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in default `{}` |
| `date_window` | integer |  | Time window, format hour, default 24 hours default `24` |

## Details

Retrieve trending Douyin accounts and their follower growth metrics using optional filters like `query_tag` and `date_window`.

### Use cases

- Track rapidly growing Douyin creator accounts across specific vertical categories.
- Analyze trending influencer performance and follower growth rates over selected hourly time windows.
- Benchmark creator engagement metrics including total likes and new follower counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page_num` | integer | No | Page number, default 1 |
| `page_size` | integer | No | Number of items per page, default 20 |
| `query_tag` | object | No | Sub-level vertical category tag, empty for all, multiple tags need to be passed in |
| `date_window` | integer | No | Time window, format hour, default 24 hours |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "user_list": [
      {
        "fans_cnt": 203292169,
        "fans_incr_rate": 2.3198677195291536e-05,
        "group_id": 0,
        "like_cnt": 19091626159,
        "monitor_id": 0,
        "monitor_status": 0,
        "new_fans_cnt": 4716,
        "new_item_target_cnt": 0,
        "new_item_target_type": 0,
        "new_like_cnt": 5275329
      }
    ]
  }
}
```

### Notes

- Specify the time window in hours using `date_window`, which defaults to 24.
- Paginate through results using `page_num` and `page_size` (default 20).
- Filter across vertical categories by providing tags in `query_tag`, or leave it empty for all categories.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-list.json`](../../../../catalog/models/douyin/billboard/hot-account-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-list
