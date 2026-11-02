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

Get non-GAAP financial metrics with GAAP equivalents and key adjustments.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/kpi-non-gaap" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "limit": 2, "period": "annual"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `limit` | integer | No | Number of periods to return. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. |
| `metric_name` | string | No | Filter to a specific metric. |
| `period` | string | No | Filter by period type: quarterly or annual. |
| `report_period_gte` | string | No | Only return metrics on or after this date (YYYY-MM-DD). |
| `report_period_lte` | string | No | Only return metrics on or before this date (YYYY-MM-DD). |
| `ticker` | string | Yes | The ticker symbol. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/kpi-non-gaap.json`](../../../catalog/models/financial-datasets/kpi-non-gaap.json) · Store page: https://www.sandbase.ai/model/financial-datasets/kpi-non-gaap
