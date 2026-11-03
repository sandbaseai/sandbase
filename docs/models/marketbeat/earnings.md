# MarketBeat Earnings API: pricing, parameters and code examples

`marketbeat/earnings` · data API · MarketBeat · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get earnings estimates and historical earnings data including EPS estimates (low, high, average), number of analyst estimates, revenue estimates, and company revenue guidance. Covers both quarterly and fiscal year.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/earnings", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('marketbeat/earnings', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("marketbeat/earnings", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "marketbeat/earnings", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/marketbeat/earnings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. 'AAPL').  |
| `exchange` | string |  | Stock exchange (e.g. 'NYSE', '').  |

## Details

Returns analyst earnings estimates per fiscal quarter for a stock, including low, high and average EPS, the number of estimates, and company revenue guidance. It needs a stock `ticker` such as `AAPL`, with an optional `exchange`.

### Use cases

- Compare the low and high EPS estimates for the next quarter to see how far analysts disagree.
- Track the revenue guidance range a company gave for upcoming quarters.
- Build an earnings calendar view that lists each upcoming quarter with its consensus EPS.
- Check how many analysts cover a stock before relying on its average estimate.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/marketbeat/earnings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Stock ticker symbol (e.g. 'AAPL'). |
| `exchange` | string | No | Stock exchange (e.g. 'NYSE', ''). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "history": [
      {
        "Average Estimate": "$2.53",
        "Company Revenue Guidance": "",
        "High Estimate": "$2.64",
        "Low Estimate": "$2.28",
        "Number of Estimates": "4",
        "Quarter": "Q1 2026",
        "Revenue Estimate at Guidance": ""
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.history[]` | One object per fiscal quarter. Each object holds the keys `Average Estimate`, `High Estimate` and `Low Estimate` (EPS as dollar strings such as `$2.53`), and `Number of Estimates` (the count of analyst estimates). |
| `data.history[].Quarter` | The fiscal quarter the estimates apply to, for example `Q1 2026`. |
| `data` | Wraps the `history` list of quarterly estimate objects. Each object also holds `Company Revenue Guidance` (a range such as `$107.8 B - $110.6 B`) and `Revenue Estimate at Guidance` (such as `$105.1 B`). Both are empty strings when no guidance exists. |
| `status` | Shows `success` when the call worked. |

### Notes

- Every value inside `data.history[]` is a string, including numbers and dollar amounts. Parse them before doing math.
- Empty strings in the revenue guidance keys mean no value was returned for that quarter.
- Use [MarketBeat Search Stocks](/apis/marketbeat/search-stocks) to find a ticker, and [MarketBeat Analyst Ratings](/apis/marketbeat/analyst-ratings) for rating changes on the same stock.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/marketbeat/earnings.json`](../../../catalog/models/marketbeat/earnings.json) · Store page: https://www.sandbase.ai/model/marketbeat/earnings
