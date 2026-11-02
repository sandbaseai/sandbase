# Douyin DOU+ Talents by Category API: pricing, parameters and code examples

`douyin/douplus/talents-by-category` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of DOU+ talents filtered by category name or keyword. Supports pagination through page index and page size parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/talents-by-category", "limit": 20, "page": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/talents-by-category', {'limit': 20, 'page': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/talents-by-category", {
  "limit": 20,
  "page": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/talents-by-category", sandbase.Params{
	"limit": 20,
	"page": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/talents-by-category` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` |  |  | Category name or keyword (from the talent category endpoint); empty for all  |
| `page` |  |  | Page index from 0, default 0  |
| `limit` |  |  | Page size, default 20  |

## Details

Fetch Douyin DOU+ talents by specifying category criteria with `name`. You can paginate through results using `page` and `limit`.

### Use cases

- Find Douyin influencers within a specific content niche.
- Browse DOU+ promotional creators by category keyword.
- Paginate through talent directories for partnership screening.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/talents-by-category" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | string | No | Category name or keyword (from the talent category endpoint); empty for all |
| `page` | string | No | Page index from 0, default 0 |
| `limit` | string | No | Page size, default 20 |

### Notes

- Leave `name` empty to return all talent categories.
- Obtain category values from the talent category endpoint.
- `page` starts at index 0 and defaults to 0, while `limit` defaults to 20.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin DOU+ Promotable Items](/model/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/model/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/model/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.

---
Machine-readable: [`catalog/models/douyin/douplus/talents-by-category.json`](../../../../catalog/models/douyin/douplus/talents-by-category.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/talents-by-category
