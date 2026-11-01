# Financial Datasets Metrics

`financial-datasets/kpi-metrics` · api · Financial Datasets

Get sector-specific operational KPIs for a ticker. Includes metrics like load factor, CET1 ratio, same-store sales, FFO per share, and more. Sourced from SEC 8-K earnings releases.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/kpi-metrics", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/kpi-metrics', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/kpi-metrics", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/kpi-metrics", sandbase.Params{
	"ticker": "AAPL",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/kpi-metrics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of periods to return. Returns all metrics for the N most recent periods. This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. default `4`; range –50 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `period` | string |  | Filter by period type: quarterly or annual. one of: `quarterly`, `annual`; default `"quarterly"` |
| `ticker` | string | yes | The ticker symbol.  |
| `metric_name` | string |  | Filter to a specific metric (e.g., load_factor, cet1_ratio).  |
| `report_period_gte` | string |  | Only return metrics on or after this date (YYYY-MM-DD).  |
| `report_period_lte` | string |  | Only return metrics on or before this date (YYYY-MM-DD).  |

## Details

Get sector-specific operational KPIs for a ticker. Includes metrics like load factor, CET1 ratio, same-store sales, FFO per share, and more. Sourced from SEC 8-K earnings releases.

The response is the official Financial Datasets API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/kpi-metrics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "limit": 2, "period": "annual"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original reques |
| `limit` | integer | No | Number of periods to return. Returns all metrics for the N most recent periods. This is the total across all pages, not a page size: each page holds up to 10 re |
| `metric_name` | string | No | Filter to a specific metric (e.g., load_factor, cet1_ratio). |
| `period` | string | No | Filter by period type: quarterly or annual. |
| `report_period_gte` | string | No | Only return metrics on or after this date (YYYY-MM-DD). |
| `report_period_lte` | string | No | Only return metrics on or before this date (YYYY-MM-DD). |
| `ticker` | string | Yes | The ticker symbol. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/kpi-metrics.json`](../../../catalog/models/financial-datasets/kpi-metrics.json) · Store page: https://www.sandbase.ai/model/financial-datasets/kpi-metrics
