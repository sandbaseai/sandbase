# Slickdeals Search API: pricing, parameters and code examples

`slickdeals/search` · data API · Slickdeals · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00213 per call · **Modes:** sync

Search Slickdeals deals by keyword with optional sort, price, discount, and page filters and get title, price, list price, store, score, and comment count for each deal in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00213**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "slickdeals/search", "query": "airpods"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('slickdeals/search', {'query': 'airpods'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("slickdeals/search", {
  "query": "airpods"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "slickdeals/search", sandbase.Params{
	"query": "airpods",
})
```

Same call via the path form: `POST /v1/api/slickdeals/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based page of 40 deals; Slickdeals stops at page 25. Each page is billed as one request. default `1`; range 1–25 |
| `sort` | string |  | Result order; omit for Slickdeals' relevance order (e.g. new for the most recently posted deals first). one of: `best_match`, `new`, `popular`, `price_low`, `price_high` |
| `query` | string | yes | Search keywords, e.g. "airpods" or "laptop".  |
| `maxPrice` | number |  | Optional maximum deal price in USD; deals without a numeric price are left out. range 0– |
| `minPrice` | number |  | Optional minimum deal price in USD; deals without a numeric price are left out. range 0– |
| `hideExpired` | boolean |  | Optional; true leaves out deals the community marked expired.  |
| `minDiscount` | integer |  | Optional; keep only deals at least this many percent off the list price, e.g. 50. range 1–99 |

## Details

Search Slickdeals deals by keyword with optional sort, price, discount, and page filters and get title, price, list price, store, score, and comment count for each deal in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "slickdeals/search", "query": "airpods"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keywords, e.g. "airpods" or "laptop". |
| `hideExpired` | boolean | No | Optional; true leaves out deals the community marked expired. |
| `maxPrice` | number | No | Optional maximum deal price in USD; deals without a numeric price are left out. |
| `minDiscount` | integer | No | Optional; keep only deals at least this many percent off the list price, e.g. 50. |
| `minPrice` | number | No | Optional minimum deal price in USD; deals without a numeric price are left out. |
| `page` | integer | No | 1-based page of 40 deals; Slickdeals stops at page 25. Each page is billed as one request. Default `1`. |
| `sort` | string | No | Result order; omit for Slickdeals' relevance order (e.g. new for the most recently posted deals first). One of: `best_match`, `new`, `popular`, `price_low`, `price_high`. |

### Pricing

Billed at the actual cost of each call, about $0.00213 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/slickdeals/search.json`](../../../catalog/models/slickdeals/search.json) · Store page: https://www.sandbase.ai/model/slickdeals/search
