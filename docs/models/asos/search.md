# ASOS Search API: pricing, parameters and code examples

`asos/search` · data API · ASOS · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Search ASOS by keyword in any of its 11 country stores with optional sort, price-range, and page filters and get title, price, brand, and colour for each product in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "asos/search", "query": "white sneakers"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('asos/search', {'query': 'white sneakers'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("asos/search", {
  "query": "white sneakers"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "asos/search", sandbase.Params{
	"query": "white sneakers",
})
```

Same call via the path form: `POST /v1/api/asos/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | 1-based results page of 48 products. Each page is billed as one request. default `1`; range 1–200 |
| `sort` | string |  | Result sort order; omit for ASOS's recommended order (e.g. new for newest arrivals first). one of: `best_match`, `new`, `price_low`, `price_high` |
| `query` | string | yes | Search keywords, e.g. "white sneakers" or "summer dress".  |
| `country` | string |  | ASOS country store to search, which also sets the price currency (gb GBP, us USD, au AUD, de/fr/it/es/nl EUR, se SEK, dk DKK, pl PLN); defaults to gb, the UK store. Product ids and URLs are store-specific. one of: `gb`, `us`, `au`, `de`, `fr`, `it`, `es`, `nl`, `se`, `dk`, `pl`; default `"gb"` |
| `maxPrice` | number |  | Optional maximum product price, in the store's currency. range 0– |
| `minPrice` | number |  | Optional minimum product price, in the store's currency. range 0– |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `inStock`, and it is served only by a source that returns every one…  |

## Details

Search ASOS by keyword in any of its 11 country stores with optional sort, price-range, and page filters and get title, price, brand, and colour for each product in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "asos/search", "query": "white sneakers", "country": "us"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keywords, e.g. "white sneakers" or "summer dress". |
| `country` | string | No | ASOS country store to search, which also sets the price currency (gb GBP, us USD, au AUD, de/fr/it/es/nl EUR, se SEK, dk DKK, pl PLN); defaults to gb, the UK store. Product ids and URLs are store-specific. One of: `gb`,  |
| `maxPrice` | number | No | Optional maximum product price, in the store's currency. |
| `minPrice` | number | No | Optional minimum product price, in the store's currency. |
| `page` | integer | No | 1-based results page of 48 products. Each page is billed as one request. Default `1`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `inStock`, and it is served only by a source that returns every one of |
| `sort` | string | No | Result sort order; omit for ASOS's recommended order (e.g. new for newest arrivals first). One of: `best_match`, `new`, `price_low`, `price_high`. |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/asos/search.json`](../../../catalog/models/asos/search.json) · Store page: https://www.sandbase.ai/model/asos/search
