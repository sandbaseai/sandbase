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

Retrieve trending Douyin topic rankings with rising heat metrics. Filter results using `keyword`, `tags`, and `date_window`, with pagination controlled via `page` and `page_size`.

### Use cases

- Identify fast-growing topics on Douyin for content planning.
- Track historical trend metrics for specific vertical category tags.
- Monitor rising keyword popularity over hourly or daily time windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-high-topic-list" \
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
        "trends": [
          {
            "date": "20260922",
            "value": 2289584
          }
        ]
      }
    ]
  }
}
```

### Notes

- Set `date_window` to 1 for hourly intervals or 2 for daily intervals.
- Pass vertical category values via `tags` or filter by search terms using `keyword`.
- Control pagination using `page` and `page_size`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-high-topic-list.json`](../../../../catalog/models/douyin/billboard/hot-total-high-topic-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-high-topic-list
