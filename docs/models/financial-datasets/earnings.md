# Financial Datasets Get Earnings Data API: pricing, parameters and code examples

`financial-datasets/earnings` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get the most recent earnings snapshot for a ticker. Optional change fields are returned only when available.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/earnings", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/earnings', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/earnings", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/earnings", sandbase.Params{
	"ticker": "AAPL",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/earnings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of most-recent report periods worth of filings to return, sorted by `(report_period DESC, filing_date ASC)`. The number of entries returned may exceed `limit` when a recent period has both an 8-K and a 10-Q /… default `1`; range 1–40 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `ticker` | string | yes | The ticker symbol (e.g. `AAPL`).  |

## Details

Returns earnings filings for a US-listed ticker, newest report period first. Each entry holds quarterly and annual figures, EPS surprise versus estimate, and a list of signals taken from the filing. The call needs a `ticker`, such as `AAPL`.

### Use cases

- Check whether a company beat or missed its EPS estimate in the latest quarter.
- Build an earnings feed that shows signal headlines such as revenue beats or margin changes.
- Track year-over-year change in EPS and capital expenditure across recent quarters.
- Link each earnings result to the SEC filing page that reported it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/earnings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | The ticker symbol (e.g. `AAPL`). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `limit` | integer | No | Number of most-recent report periods worth of filings to return, sorted by `(report_period DESC, filing_date ASC)`. The number of entries returned may exceed `limit` when a recent period has both an 8-K and a 10-Q / 10-K |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "earnings": [
    {
      "accession_number": "0000320193-26-000024",
      "annual": {
        "capital_expenditure": -9041000000.0,
        "cash_and_equivalents": 36305000000.0,
        "change_in_cash_and_equivalents": 371000000.0,
        "earnings_per_share": 8.98,
        "eps_surprise": "BEAT",
        "eps_surprise_pct": 0.0565,
        "estimated_earnings_per_share": 8.5,
        "estimated_revenue": 468204283862
      },
      "currency": "USD",
      "filing_date": "2026-11-02",
      "filing_datetime": "2026-11-02T16:30:23-05:00",
      "filing_url": "https://www.sec.gov/Archives/edgar/data/320193/000032019326000024/0000320193-26-…",
      "filing_window": "AFTER_HOURS",
      "fiscal_period": "2026-Q4",
      "quarterly": {
        "capital_expenditure": null,
        "cash_and_equivalents": 36305000000.0,
        "change_in_cash_and_equivalents": null,
        "earnings_per_share": 2.1,
        "earnings_per_share_chg": 0.0396,
        "earnings_per_share_yoy_chg": 0.1328,
        "eps_surprise": "BEAT",
        "eps_surprise_pct": 0.05
      },
      "report_period": "2026-09-26",
      "signals": [
        {
          "details": {
            "actual": 2.1,
            "estimate": 2.0,
            "surprise_pct": 0.05
          },
          "headline": "EPS of $2.10 beat estimate of $2.00 by 5.00%",
          "metric": "earnings_per_share",
          "period": "2026-Q4",
          "type": "EPS_BEAT"
        }
      ],
      "source_type": "8-K"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `earnings[].ticker` | Ticker symbol the entry belongs to. |
| `earnings[].fiscal_period / earnings[].report_period` | `fiscal_period` is the fiscal quarter label, such as `2026-Q4`. `report_period` is the date the period ended. |
| `earnings[].filing_date / earnings[].filing_datetime / earnings[].filing_window` | When the filing was made. `filing_datetime` includes the time zone offset. `filing_window` shows the timing, such as `AFTER_HOURS` or `PRE_MARKET`. |
| `earnings[].source_type` | Type of SEC filing behind the entry, such as `8-K` or `10-Q`. |
| `earnings[].accession_number / earnings[].filing_url` | SEC accession number and the link to the filing index page. |
| `earnings[].quarterly.earnings_per_share` | Reported EPS for the quarter. |
| `earnings[].quarterly.eps_surprise / earnings[].quarterly.eps_surprise_pct` | Whether EPS beat the estimate (for example `BEAT`) and the size of the surprise as a fraction. `0.1543` means 15.43%. |
| `earnings[].quarterly.earnings_per_share_yoy_chg / earnings[].quarterly.capital_expenditure_yoy_chg` | Year-over-year change as a fraction. Present only when available. |
| `earnings[].annual.estimated_earnings_per_share / earnings[].annual.estimated_revenue` | Estimates for the full year. The `annual` object appears only on some entries, such as the fiscal Q4 filing. |
| `earnings[].signals[]` | Highlights from the filing. Each has a `type` (for example `EPS_BEAT`, `REVENUE_BEAT`, `GUIDANCE_INITIATED`), a `metric`, a `period`, a readable `headline`, and a `details` object whose keys vary by type. |

### Notes

- `limit` counts report periods, not entries. One period can return two entries, such as an `8-K` and a `10-Q`, so the list may be longer than `limit`. Values above 40 are clamped to 40.
- Entries are sorted by `report_period` descending, then `filing_date` ascending.
- For the next page, pass the cursor from the response's `next_page_url` as `cursor`. The cursor replaces all other parameters.
- For consensus forecasts, call [Financial Datasets Get Analyst Estimates](/apis/financial-datasets/analyst-estimates). For full statements, call [Financial Datasets Get Income Statements](/apis/financial-datasets/financials-income-statements).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/earnings.json`](../../../catalog/models/financial-datasets/earnings.json) · Store page: https://www.sandbase.ai/model/financial-datasets/earnings
