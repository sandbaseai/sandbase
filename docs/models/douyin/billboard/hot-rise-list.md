# Douyin Rising Hot Search List API: pricing, parameters and code examples

`douyin/billboard/hot-rise-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin rising hot search topics and billboard rankings. Results can be filtered by keyword, sorted by a specified order, and segmented by category tags.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-rise-list", "order": "test", "page": 0, "page_size": 10}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-rise-list', {'order': 'test', 'page': 0, 'page_size': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-rise-list", {
  "order": "test",
  "page": 0,
  "page_size": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-rise-list", sandbase.Params{
	"order": "test",
	"page": 0,
	"page_size": 10,
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-rise-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number  |
| `order` | string | yes | Sorting method  |
| `keyword` | string |  | Hot search term  |
| `page_size` | integer | yes | Number of items per page  |
| `sentence_tag` | string |  | Hot category tag, get from hot list category, multiple categories separated by commas, empty for all  |

## Details

Access the Douyin rising hot search ranking with pagination using `page` and `page_size`, ordered via `order`.

### Use cases

- Track rapidly climbing search terms on Douyin.
- Filter trending search queries by category tags.
- Monitor breakout topics matching specific search keywords.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-rise-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"order": "rank", "page": 1, "page_size": 10}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | Yes | Page number |
| `order` | string | Yes | Sorting method |
| `page_size` | integer | Yes | Number of items per page |
| `keyword` | string | No | Hot search term |
| `sentence_tag` | string | No | Hot category tag, get from hot list category, multiple categories separated by commas, empty for all |

### Notes

- Pass multiple category values into `sentence_tag` separated by commas, or leave it empty for all categories.
- Both `page` and `page_size` are required for pagination control.
- The `order` parameter specifies the sorting method for the rising list.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-rise-list.json`](../../../../catalog/models/douyin/billboard/hot-rise-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-rise-list
