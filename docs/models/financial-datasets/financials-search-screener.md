# Financial Datasets Stock Screener API: pricing, parameters and code examples

`financial-datasets/financials-search-screener` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Screen US public companies by financial metrics such as revenue, net income or P/E, with gt/lt/eq filters and ticker lists.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/financials-search-screener", "filters": [{"field": "revenue", "value": 100000000000, "operator": "gt"}]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/financials-search-screener', {'filters': [{'field': 'revenue', 'value': 100000000000, 'operator': 'gt'}]})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/financials-search-screener", {
  "filters": [
    {
      "field": "revenue",
      "value": 100000000000,
      "operator": "gt"
    }
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/financials-search-screener", sandbase.Params{
	"filters": []any{map[string]any{
		"field": "revenue",
		"value": 100000000000,
		"operator": "gt",
	}},
})
```

Same call via the path form: `POST /v1/api/financial-datasets/financials-search-screener` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. default `10`; range 1– |
| `filters` | array | yes | An array of filter objects to apply to the search.  |

## Details

Returns US public companies that match a set of financial metric filters, such as `revenue` greater than a value. You send a `filters` array, and each filter has a `field`, an `operator` and a `value`. Each result row holds the ticker, sector, industry, reporting period and the filtered metric.

### Use cases

- List every company with annual revenue above $100 billion to build a large-cap watchlist.
- Narrow a set of tickers with the `in` operator to those that meet a revenue threshold.
- Group screened companies by `sector` or `industry` to compare how many large companies sit in each.
- Feed the returned tickers into a financial statements call to pull full details for each match.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/financials-search-screener" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"filters": [{"field": "revenue", "operator": "gt", "value": 100000000000}], "limit": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `filters` | array | Yes | An array of filter objects to apply to the search. |
| `limit` | integer | No | The maximum number of results to return. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "results": [
    {
      "currency": "USD",
      "industry": "Broadline Retail",
      "report_period": "2026-09-30",
      "revenue": 797455000000.0,
      "sector": "Consumer Discretionary",
      "ticker": "AMZN"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[]` | One company that passed all filters. The list has at most `limit` rows. |
| `results[].ticker` | Stock ticker of the company, such as `AMZN`. Use it as input to other Financial Datasets APIs. |
| `results[].revenue` | Revenue value for the company, in the currency given in `currency`. The row includes the metric you filtered on. |
| `results[].currency` | Currency code of the metric values, such as `USD`. |
| `results[].report_period` | Date of the reporting period the metric belongs to, in `YYYY-MM-DD` format. |
| `results[].sector / results[].industry` | Sector and industry classification of the company, such as `Consumer Discretionary` and `Broadline Retail`. |

### Notes

- The `limit` parameter caps the number of rows and defaults to 10.
- Use `gt`, `lt`, `gte`, `lte` or `eq` with a number for metric fields. Use `in` with an array of strings only for `ticker` or `cik`.
- Results are not sorted by revenue in the sample response, so sort them yourself if you need a ranking.
- Pass a returned `ticker` to [Financial Datasets Get Financial Metrics Snapshot](/apis/financial-datasets/financial-metrics-snapshot) or [Financial Datasets Get Company Facts](/apis/financial-datasets/company-facts) for more detail.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/financials-search-screener.json`](../../../catalog/models/financial-datasets/financials-search-screener.json) · Store page: https://www.sandbase.ai/model/financial-datasets/financials-search-screener
