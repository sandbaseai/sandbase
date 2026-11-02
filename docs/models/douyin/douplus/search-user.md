# Douyin DOU+ User Search API: pricing, parameters and code examples

`douyin/douplus/search-user` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname. Returns matching user profiles with support for cursor-based pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/search-user", "count": 20, "cursor": 0, "keyword": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/search-user', {'count': 20, 'cursor': 0, 'keyword': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/search-user", {
  "count": 20,
  "cursor": 0,
  "keyword": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/search-user", sandbase.Params{
	"count": 20,
	"cursor": 0,
	"keyword": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/search-user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` |  |  | Number of results per page, default 20  |
| `cursor` |  |  | Pagination cursor, 0 for first page, then pass the cursor from the previous response  |
| `keyword` | string | yes | Search keyword (Douyin ID / nickname) (required)  |

## Details

Query Douyin users eligible for DOU+ delivery using the required `keyword` parameter. Supports stepping through results via `cursor` and custom page sizes via `count`.

### Use cases

- Find Douyin accounts by nickname for DOU+ promotion targeting.
- Look up specific Douyin IDs to confirm account identity in delivery workflows.
- Browse through user search results using pagination tokens.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/search-user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (Douyin ID / nickname) (required) |
| `count` | string | No | Number of results per page, default 20 |
| `cursor` | string | No | Pagination cursor, 0 for first page, then pass the cursor from the previous response |

### Notes

- The `keyword` parameter is required and accepts either a Douyin ID or account nickname.
- Set `cursor` to 0 for the first page, then use the cursor value returned by the prior response.
- The `count` parameter defaults to 20 results per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin DOU+ Promotable Items](/model/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ Talent Categories](/model/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.
- [Douyin DOU+ Talents by Category](/model/douyin/douplus/talents-by-category): Returns a list of DOU+ talents filtered by category name or keyword.

---
Machine-readable: [`catalog/models/douyin/douplus/search-user.json`](../../../../catalog/models/douyin/douplus/search-user.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/search-user
