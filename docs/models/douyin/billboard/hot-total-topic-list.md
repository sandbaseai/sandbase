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

Query Douyin trending topic rankings by passing optional filters such as `keyword`, `tags`, and `date_window`.

### Use cases

- Track trending topics across Douyin vertical categories.
- Monitor historical engagement trends for specific keywords.
- Analyze viral content themes over hourly or daily time windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-topic-list" \
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

- Use `date_window` to specify time aggregation (1 for hourly, 2 for daily).
- Pagination is controlled using `page` and `page_size`.
- Multiple vertical category tags can be passed to the `tags` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-topic-list.json`](../../../../catalog/models/douyin/billboard/hot-total-topic-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-topic-list
