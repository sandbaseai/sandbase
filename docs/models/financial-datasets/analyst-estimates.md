# Financial Datasets Get Analyst Estimates API: pricing, parameters and code examples

`financial-datasets/analyst-estimates` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Analyst Estimates from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/analyst-estimates"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/analyst-estimates', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/analyst-estimates", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/analyst-estimates", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/analyst-estimates` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | limit  |
| `period` | string |  | period  |
| `ticker` | string |  | ticker  |

## Details

Returns analyst consensus estimates for a public company. Each row has an estimated earnings per share and revenue for one future fiscal period. You pass a stock `ticker`, and you can set `period` and `limit`.

### Use cases

- Compare the forecast `earnings_per_share` for the next two fiscal years of a stock such as `AAPL`.
- Build a revenue growth projection from the estimated `revenue` values across fiscal periods.
- Check expected earnings against reported results by pairing estimates with earnings data.
- Feed forward-looking numbers into a valuation model or a stock research dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/analyst-estimates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": "2", "period": "annual", "ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | string | No | limit |
| `period` | string | No | period |
| `ticker` | string | No | ticker |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "analyst_estimates": [
    {
      "earnings_per_share": 9.3,
      "fiscal_period": "2027-09-30",
      "period": "annual",
      "revenue": 499734519018
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `analyst_estimates[]` | List of estimate rows, one per fiscal period. The request used `limit` set to `2`, and the response holds two rows. |
| `analyst_estimates[].fiscal_period` | End date of the fiscal period the estimate covers, in `YYYY-MM-DD` format, for example `2027-09-30`. |
| `analyst_estimates[].period` | Length of the period. The value is `annual` in this response, which matches the `period` request value. |
| `analyst_estimates[].earnings_per_share` | Estimated earnings per share for that fiscal period, for example `9.3`. |
| `analyst_estimates[].revenue` | Estimated revenue for that fiscal period, given as a plain number, for example `499734519018`. |

### Notes

- Pass the stock symbol in `ticker`, for example `AAPL`.
- The sample request used `period` set to `annual`. Rows are ordered by `fiscal_period`, earliest first.
- Use `limit` to cap the number of rows returned. It is sent as a string, such as `"2"`.
- For reported results to compare with these estimates, call [Financial Datasets Get Earnings Data](/apis/financial-datasets/earnings) or [Financial Datasets Get Income Statements](/apis/financial-datasets/financials-income-statements).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/analyst-estimates.json`](../../../catalog/models/financial-datasets/analyst-estimates.json) · Store page: https://www.sandbase.ai/model/financial-datasets/analyst-estimates
