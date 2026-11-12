# Best Buy Search API: pricing, parameters and code examples

`best-buy/search` · data API · Best Buy · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0009 per call · **Modes:** sync

Search BestBuy.com by keyword with optional sort, price-range, and page filters and get title, price, rating, and brand for each product in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0009**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "best-buy/search", "query": "airpods"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('best-buy/search', {'query': 'airpods'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("best-buy/search", {
  "query": "airpods"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "best-buy/search", sandbase.Params{
	"query": "airpods",
})
```

Same call via the path form: `POST /v1/api/best-buy/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based results page of about 18 to 24 products; Best Buy serves no products past page 100. Each page is billed as one request. Page sizes differ between sources, so deduplicate on sku. default `1`; range 1–100 |
| `sort` | string |  | Result sort order; omit for Best Buy's own relevance order (e.g. price_low sorts by lowest price first). one of: `best_match`, `best_seller`, `price_low`, `price_high`, `rating_high`, `new` |
| `query` | string | yes | Search keywords, e.g. "airpods" or "65 inch tv".  |
| `maxPrice` | number |  | Optional maximum product price in USD. range 0– |
| `minPrice` | number |  | Optional minimum product price in USD. range 0– |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `totalResults`, and it is served only by a source that returns every…  |

## Details

Search BestBuy.com by keyword with optional sort, price-range, and page filters and get title, price, rating, and brand for each product in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "best-buy/search", "query": "airpods"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keywords, e.g. "airpods" or "65 inch tv". |
| `maxPrice` | number | No | Optional maximum product price in USD. |
| `minPrice` | number | No | Optional minimum product price in USD. |
| `page` | integer | No | 1-based results page of about 18 to 24 products; Best Buy serves no products past page 100. Each page is billed as one request. Page sizes differ between sources, so deduplicate on sku. Default `1`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `totalResults`, and it is served only by a source that returns every o |
| `sort` | string | No | Result sort order; omit for Best Buy's own relevance order (e.g. price_low sorts by lowest price first). One of: `best_match`, `best_seller`, `price_low`, `price_high`, `rating_high`, `new`. |

### Pricing

Billed at the actual cost of each call, about $0.0009 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/best-buy/search.json`](../../../catalog/models/best-buy/search.json) · Store page: https://www.sandbase.ai/model/best-buy/search
