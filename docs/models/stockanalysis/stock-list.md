# StockAnalysis Stock List API: pricing, parameters and code examples

`stockanalysis/stock-list` · data API · StockAnalysis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Stocks from a curated stock list by URL slug. Returns the list title, description, stock count, and an array of stock entries with symbol, name, market cap, price, change, and revenue.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stockanalysis/stock-list", "slug": "biggest-companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('stockanalysis/stock-list', {'slug': 'biggest-companies'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("stockanalysis/stock-list", {
  "slug": "biggest-companies"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "stockanalysis/stock-list", sandbase.Params{
	"slug": "biggest-companies",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/stockanalysis/stock-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | List slug from the site URL path.  |

## Details

Returns a list of stocks from a StockAnalysis list page, plus the list's total stock count. It needs one input: the list `slug` from the site URL, such as `biggest-companies`.

### Use cases

- Pull the largest companies by market cap into a ranked table.
- Build a watchlist with ticker symbols, prices, and daily change from a named list.
- Draw small one-year price charts from `spark1y` next to each company name.
- Group listed companies by country or state to see where the biggest names are based.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/stockanalysis/stock-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "biggest-companies"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | List slug from the site URL path. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 53518,
    "description": null,
    "slug": "biggest-companies",
    "stocks": [
      {
        "change": -1.83,
        "country": "United States",
        "isPrimaryListing": true,
        "logo": "https://logos.stockanalysis.com/aapl.svg",
        "logoDark": "https://logos.stockanalysis.com/aapl-dark.svg",
        "marketCapUSD": 4937502977600,
        "n": "Apple Inc.",
        "no": 1,
        "price": 338.32,
        "priceCurrency": "USD",
        "priceUSD": 338.32,
        "s": "AAPL"
      }
    ],
    "title": null
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Total number of stocks in the list. The response shows only part of them in `data.stocks`. |
| `data.slug` | The list slug that was requested. |
| `data.title / data.description` | List title and description. Both can be `null`. |
| `data.stocks[].s / data.stocks[].n` | Ticker symbol (such as `AAPL`) and company name. |
| `data.stocks[].no` | Rank of the stock within the list, starting at `1`. |
| `data.stocks[].price / data.stocks[].priceCurrency` | Latest price and the currency it is quoted in. |
| `data.stocks[].priceUSD / data.stocks[].marketCapUSD` | Price and market cap converted to US dollars. Use these to compare stocks across currencies. |
| `data.stocks[].change` | Price change value for the stock, for example `-1.83`. |
| `data.stocks[].spark1y` | Array of prices for a one-year sparkline chart. |
| `data.stocks[].country / data.stocks[].state` | Country and state or region of the company. |

### Notes

- Take the `slug` from the list page URL path on StockAnalysis, for example `biggest-companies`.
- Each entry has `isPrimaryListing` and `subtype`, which you can use to filter results.
- To look up a ticker from this list, call [StockAnalysis Stock Overview](/apis/stockanalysis/stock-overview) or [StockAnalysis Stock Statistics](/apis/stockanalysis/stock-statistics).
- To find a stock by name, use [StockAnalysis Search Stocks](/apis/stockanalysis/search-stocks).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/stockanalysis/stock-list.json`](../../../catalog/models/stockanalysis/stock-list.json) · Store page: https://www.sandbase.ai/model/stockanalysis/stock-list
