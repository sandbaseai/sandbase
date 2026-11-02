# Facebook Post Search API: pricing, parameters and code examples

`facebook/search-post` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search public Facebook posts by keyword with optional inclusive date-range filters and cursor pagination. Use it to find topic-related posts or continue a time-bounded public-content search.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/search-post", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/search-post', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/search-post", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/search-post", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/facebook/search-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor for fetching the next set of results.  |
| `endDate` | string |  | End date for the search range (inclusive), formatted as yyyy-MM-dd.  |
| `keyword` | string | yes | Keyword to search for in public posts. Supports basic text matching.  |
| `startDate` | string |  | Start date for the search range (inclusive), formatted as yyyy-MM-dd.  |

## Details

Search public Facebook posts by keyword with optional inclusive date-range filters and cursor pagination. Use it to find topic-related posts or continue a time-bounded public-content search.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/search-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword to search for in public posts. Supports basic text matching. |
| `startDate` | string | No | Start date for the search range (inclusive), formatted as yyyy-MM-dd. |
| `endDate` | string | No | End date for the search range (inclusive), formatted as yyyy-MM-dd. |
| `cursor` | string | No | Pagination cursor for fetching the next set of results. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/facebook/search-post.json`](../../../catalog/models/facebook/search-post.json) · Store page: https://www.sandbase.ai/model/facebook/search-post
