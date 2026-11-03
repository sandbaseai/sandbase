# StockAnalysis Stock Financials Income API: pricing, parameters and code examples

`stockanalysis/stock-financials-income` · data API · StockAnalysis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Detailed income statement for a stock. Returns annual financial data including revenue, gross profit, operating income, net income, EPS, margins, and growth rates organized in a financialData object with arrays per.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stockanalysis/stock-financials-income", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('stockanalysis/stock-financials-income', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("stockanalysis/stock-financials-income", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "stockanalysis/stock-financials-income", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/stockanalysis/stock-financials-income` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Stock ticker symbol (e.g. 'AAPL', 'MSFT', 'NVDA').  |

## Details

Returns the annual income statement for a stock, including revenue, gross profit, operating income, net income, EPS, margins and cash flow figures. It needs one input, the ticker `symbol`, such as `AAPL`.

### Use cases

- Compare revenue, gross profit and net income for a company over several fiscal years.
- Track gross, operating and profit margins to see how profitability changes.
- Calculate per-share trends from diluted EPS, dividends per share and share counts.
- Build a valuation model that starts from trailing twelve month revenue, EBITDA and free cash flow.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/stockanalysis/stock-financials-income" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock ticker symbol (e.g. 'AAPL', 'MSFT', 'NVDA'). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "availableSources": [
      "spg"
    ],
    "classicStatementLayout": false,
    "defaultSource": "spg",
    "details": {
      "fiscalYear": "October - September",
      "fiscalYearShort": "Oct - Sep",
      "lastTradingDay": "Nov 2, 2026",
      "lastTrailingDate": "Sep 26, 2026",
      "reportingFrequency": null,
      "source": "spg"
    },
    "financialData": {
      "cor": [
        245232000000
      ],
      "datekey": [
        "TTM"
      ],
      "depAmorEbitda": [
        13423000000
      ],
      "dps": [
        null
      ],
      "ebit": [
        158063000000
      ],
      "ebitMargin": [
        0.3301
      ],
      "ebitda": [
        171486000000
      ],
      "ebitdaMargin": [
        0.35813
      ],
      "epsBasic": [
        9.01484
      ],
      "epsdil": [
        8.98
      ],
      "fcf": [
        136056000000
      ],
      "fcfMargin": [
        0.28414
      ]
    },
    "financialState": null,
    "fullWidthFinancials": false,
    "full_count": 10,
    "head": {
      "description": "Detailed annual and quarterly income statement for Apple (AAPL). See many years …",
      "heading": "Income Statement",
      "title": "Apple (AAPL) Income Statement",
      "url": "/stocks/aapl/financials/income-statement/"
    },
    "map": [
      {
        "id": "operatingRevenue",
        "title": "Operating Revenue"
      }
    ],
    "overrideSource": null,
    "overviewLeftToRight": false
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.financialData.datekey[]` | Period label for each position in the arrays. The first value is `TTM` for trailing twelve months, and the others are period end dates such as `2025-09-27`. |
| `data.financialData.revenue[]` | Revenue for each period, in the same order as `datekey`. |
| `data.financialData.gp[] / data.financialData.opinc[] / data.financialData.netinc[]` | Gross profit, operating income and net income for each period. |
| `data.financialData.grossMargin[] / data.financialData.operatingMargin[] / data.financialData.profitMargin[]` | Margins as decimal ratios. For example, `0.48786` is a gross margin of about 48.8%. |
| `data.financialData.epsdil[] / data.financialData.epsBasic[]` | Diluted and basic earnings per share for each period. |
| `data.financialData.ebitda[] / data.financialData.fcf[]` | EBITDA and free cash flow for each period. |
| `data.financialData.rnd[] / data.financialData.sgna[] / data.financialData.opex[]` | Research and development, selling, general and administrative, and total operating expenses. |
| `data.financialData.sharesDiluted[] / data.financialData.sharesBasic[]` | Diluted and basic weighted share counts for each period. |
| `data.financialData.fiscalYear[] / data.financialData.fiscalQuarter[]` | Fiscal year and fiscal quarter that each period belongs to. |
| `data.prior` | Same income statement fields for an older period (fiscal year `2021` in this response), held in single-item arrays. |

### Notes

- Every array in `data.financialData` lines up by index with `data.financialData.datekey`. Read the same index across arrays to get one period.
- Some values can be `null`, for example `interestExpense` and `interestIncome` in the current periods.
- The `period` field is `annual` in this response. `data.details.fiscalYear` gives the company fiscal year range, such as `October - September`.
- To find a valid ticker, use [StockAnalysis Search Stocks](/apis/stockanalysis/search-stocks) or [StockAnalysis Stock List](/apis/stockanalysis/stock-list).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/stockanalysis/stock-financials-income.json`](../../../catalog/models/stockanalysis/stock-financials-income.json) · Store page: https://www.sandbase.ai/model/stockanalysis/stock-financials-income
