# Financial Datasets Guidance API: pricing, parameters and code examples

`financial-datasets/kpi-guidance` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get structured forward guidance from earnings releases. Returns ranges, point estimates, and directional signals.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/kpi-guidance", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/kpi-guidance', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/kpi-guidance", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/kpi-guidance", sandbase.Params{
	"ticker": "AAPL",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/kpi-guidance` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of periods to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. default `4`; range –50 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `period` | string |  | Filter by period type: quarterly or annual. one of: `quarterly`, `annual`; default `"quarterly"` |
| `ticker` | string | yes | The ticker symbol.  |
| `metric_name` | string |  | Filter to a specific metric.  |
| `report_period_gte` | string |  | Only return guidance on or after this date (YYYY-MM-DD).  |
| `report_period_lte` | string |  | Only return guidance on or before this date (YYYY-MM-DD).  |

## Details

Returns forward guidance that a company stated in its earnings releases, as structured records. Each record has a metric, a period, a value or direction, and the source text. You need a `ticker`, and you can filter by `metric_name`, `period` and report date.

### Use cases

- Track how much buyback authorization Apple announced in each fiscal year.
- Pull the exact sentence and filing link behind a guidance figure for research notes.
- Compare guidance for one `metric_name` across several fiscal years.
- Flag new guidance by filtering on records where `change_direction` is `initiated`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/kpi-guidance" \
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
| `report_period_gte` | string | No | Only return guidance on or after this date (YYYY-MM-DD). |
| `report_period_lte` | string | No | Only return guidance on or before this date (YYYY-MM-DD). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "kpi_guidance": [
    {
      "change_direction": "initiated",
      "metric_name": "share_repurchases",
      "period": "FY 2026",
      "period_type": "annual",
      "point_estimate": 100000000000.0,
      "raw_text": "The board of directors has also authorized an additional program to repurchase u…",
      "source_text": "additional program to repurchase up to $100 billion of the Company's common stoc…",
      "source_url": "https://www.sec.gov/Archives/edgar/data/320193/000032019326000011/a8-kex991q2202…",
      "ticker": "AAPL",
      "unit": "dollars"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `kpi_guidance[].metric_name` | The metric the guidance covers, such as `share_repurchases`. |
| `kpi_guidance[].period / kpi_guidance[].period_type` | The fiscal period the guidance applies to, such as `FY 2026`, and whether it is `annual` or quarterly. |
| `kpi_guidance[].point_estimate` | The guided value as a single number. In this example it is `100000000000.0`, which is $100 billion. |
| `kpi_guidance[].unit` | The unit of the value, such as `dollars`. |
| `kpi_guidance[].change_direction` | How the guidance changed versus before. `initiated` means the company gave it for the first time. |
| `kpi_guidance[].raw_text` | The full sentence from the earnings release that contains the guidance. |
| `kpi_guidance[].source_text` | The shorter excerpt of the text that the structured value comes from. |
| `kpi_guidance[].source_url` | Link to the SEC filing that contains the guidance. |
| `kpi_guidance[].ticker` | The ticker symbol the record belongs to. |

### Notes

- `limit` is the total number of periods across all pages, up to `50`. Each page holds up to 10 records, linked by `next_page_url`.
- To get the next page, send the `cursor` from `next_page_url`. The cursor carries the original filters, so all other parameters are ignored.
- `period` defaults to `quarterly`. Set it to `annual` for fiscal year guidance.
- For actual reported results, call [Financial Datasets Get Earnings Data](/apis/financial-datasets/earnings). For consensus forecasts, use [Financial Datasets Get Analyst Estimates](/apis/financial-datasets/analyst-estimates).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/kpi-guidance.json`](../../../catalog/models/financial-datasets/kpi-guidance.json) · Store page: https://www.sandbase.ai/model/financial-datasets/kpi-guidance
