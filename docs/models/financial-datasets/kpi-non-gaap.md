# Financial Datasets Non-GAAP Metrics API: pricing, parameters and code examples

`financial-datasets/kpi-non-gaap` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get non-GAAP financial metrics with GAAP equivalents and key adjustments.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/kpi-non-gaap", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/kpi-non-gaap', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/kpi-non-gaap", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/kpi-non-gaap", sandbase.Params{
	"ticker": "AAPL",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/kpi-non-gaap` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of periods to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. default `4`; range –50 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `period` | string |  | Filter by period type: quarterly or annual. one of: `quarterly`, `annual`; default `"quarterly"` |
| `ticker` | string | yes | The ticker symbol.  |
| `metric_name` | string |  | Filter to a specific metric.  |
| `report_period_gte` | string |  | Only return metrics on or after this date (YYYY-MM-DD).  |
| `report_period_lte` | string |  | Only return metrics on or before this date (YYYY-MM-DD).  |

## Details

Returns non-GAAP financial metrics that a public company reports, such as adjusted diluted EPS and adjusted net income. Each row includes the matching GAAP line item, a note on the adjustments, and a link to the source document. It needs a `ticker`.

### Use cases

- Compare adjusted EPS with GAAP diluted EPS to see how much one-time items change reported earnings.
- Read the `key_adjustments` text to find which one-time charges a company excluded in a fiscal year.
- Trace each metric to the filing text that supports it using `source_url`.
- Build a history of a company's adjusted metrics by period with `period`, `report_period_gte` and `report_period_lte`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/kpi-non-gaap" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "limit": 2, "period": "annual"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | The ticker symbol. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `limit` | integer | No | Number of periods to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. |
| `metric_name` | string | No | Filter to a specific metric. |
| `period` | string | No | Filter by period type: quarterly or annual. |
| `report_period_gte` | string | No | Only return metrics on or after this date (YYYY-MM-DD). |
| `report_period_lte` | string | No | Only return metrics on or before this date (YYYY-MM-DD). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "kpi_non_gaap": [
    {
      "gaap_equivalent": "Diluted earnings per share",
      "key_adjustments": "Excludes per-share impact ($0.67) of one-time income tax charge related to rever…",
      "metric_name": "Adjusted Diluted EPS",
      "period": "FY 2024",
      "period_type": "annual",
      "source_text": "Diluted earnings per share",
      "source_url": "https://www.sec.gov/Archives/edgar/data/320193/000032019325000077/a8-kex991q4202…",
      "ticker": "AAPL",
      "unit": "USD",
      "value": 6.75
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `kpi_non_gaap[].metric_name` | Name of the non-GAAP metric, for example `Adjusted Diluted EPS` or `Adjusted Net Income`. |
| `kpi_non_gaap[].value` | Numeric value of the metric for the period. Read it together with `unit`. |
| `kpi_non_gaap[].unit` | Unit of `value`. In this response it is `USD`. |
| `kpi_non_gaap[].gaap_equivalent` | The GAAP line item that the non-GAAP metric corresponds to, for example `Net income`. |
| `kpi_non_gaap[].key_adjustments` | Plain text describing what the company excluded to get from the GAAP figure to the non-GAAP figure. |
| `kpi_non_gaap[].period / kpi_non_gaap[].period_type` | Label of the reporting period, such as `FY 2024`, and its type, such as `annual`. |
| `kpi_non_gaap[].source_url / kpi_non_gaap[].source_text` | Link to the SEC filing where the figure appears, and the text snippet used to match it. |
| `kpi_non_gaap[].ticker` | Ticker symbol of the company the metric belongs to. |

### Notes

- `limit` is the total number of periods across all pages. Each page holds up to 10 records, linked by `next_page_url`.
- To get the next page, pass the cursor from `next_page_url` as `cursor`. All other parameters are then ignored.
- Use `metric_name` to filter to one metric, and `period` set to `quarterly` or `annual` to choose the period type. `period` defaults to `quarterly`.
- For GAAP figures, call [Financial Datasets Get Income Statements](/apis/financial-datasets/financials-income-statements).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/kpi-non-gaap.json`](../../../catalog/models/financial-datasets/kpi-non-gaap.json) · Store page: https://www.sandbase.ai/model/financial-datasets/kpi-non-gaap
