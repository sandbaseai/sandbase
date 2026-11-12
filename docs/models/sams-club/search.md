# Sam's Club Search API: pricing, parameters and code examples

`sams-club/search` · data API · Sam's Club · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00319 per call · **Modes:** sync

Search SamsClub.com by keyword with optional sort, price-range, and page filters and get title, member price, stock, and rating for each product in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00319**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sams-club/search", "query": "paper towels"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sams-club/search', {'query': 'paper towels'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sams-club/search", {
  "query": "paper towels"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sams-club/search", sandbase.Params{
	"query": "paper towels",
})
```

Same call via the path form: `POST /v1/api/sams-club/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based results page of about 40 to 50 products. Each page is billed as one request. default `1`; range 1– |
| `sort` | string |  | Result sort order; omit for Sam's Club's Best Match (e.g. price_low sorts by lowest price first). one of: `best_match`, `price_low`, `price_high` |
| `query` | string | yes | Search keywords, e.g. "paper towels" or "tv".  |
| `maxPrice` | number |  | Optional maximum member price in USD. range 0– |
| `minPrice` | number |  | Optional minimum member price in USD. range 0– |

## Details

Search SamsClub.com by keyword with optional sort, price-range, and page filters and get title, member price, stock, and rating for each product in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "sams-club/search", "query": "paper towels"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keywords, e.g. "paper towels" or "tv". |
| `maxPrice` | number | No | Optional maximum member price in USD. |
| `minPrice` | number | No | Optional minimum member price in USD. |
| `page` | integer | No | 1-based results page of about 40 to 50 products. Each page is billed as one request. Default `1`. |
| `sort` | string | No | Result sort order; omit for Sam's Club's Best Match (e.g. price_low sorts by lowest price first). One of: `best_match`, `price_low`, `price_high`. |

### Pricing

Billed at the actual cost of each call, about $0.00319 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/sams-club/search.json`](../../../catalog/models/sams-club/search.json) · Store page: https://www.sandbase.ai/model/sams-club/search
