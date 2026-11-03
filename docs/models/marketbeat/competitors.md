# MarketBeat Competitors API: pricing, parameters and code examples

`marketbeat/competitors` · data API · MarketBeat · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get competitor comparison data for a stock. Returns multiple comparison tables covering earnings/valuation, profitability, and analyst sentiment.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/competitors", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('marketbeat/competitors', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("marketbeat/competitors", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "marketbeat/competitors", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/marketbeat/competitors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. 'AAPL').  |
| `exchange` | string |  | Stock exchange (e.g. 'NYSE', '').  |

## Details

Returns side-by-side comparison tables between a stock and one of its competitors. The tables cover earnings and valuation, profitability, and analyst ratings. It needs a stock `ticker`, with an optional `exchange`.

### Use cases

- Compare the price to earnings and price to sales ratios of a stock against a rival to check relative valuation.
- Rank two companies by net margin, return on assets, and return on equity in a screening tool.
- Show analyst buy, hold, and sell counts for two companies in one research dashboard.
- Build a competitor summary card for a stock page from the question-style table titles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/marketbeat/competitors" \
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
    "items": [
      {
        "category": "Which has stronger earnings & valuation, AMZN or AAPL?",
        "data": [
          {
            "Company": "Amazon.com",
            "Earnings Per Share": "$12.37",
            "Gross Revenue": "$797.46B",
            "Net Income": "$77.67B",
            "Price/Earnings Ratio": "19.86",
            "Price/Sales Ratio": "3.32"
          }
        ]
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status` | Shows `success` when the call worked. |
| `data.items[].category` | Question that titles each comparison table, such as which company has stronger earnings and valuation. It names the two tickers being compared. |
| `data.items[].data[]` | One row per compared company in that table. The first table holds earnings per share, gross revenue, net income, price to earnings ratio, and price to sales ratio. The second holds net margins, return on assets, and return on equity. The third holds the rating score and the strong buy, buy, hold, and sell counts. |
| `data.items[].data[].Company` | Company name for the row, such as `Apple` or `Amazon.com`. Each table has one row per compared company. |

### Notes

- Each item in `data.items` has its own columns, so read the keys of each row per table instead of assuming one shape.
- All values are strings with units attached, such as `$` and `%` signs or a `B` suffix. Strip them before doing math.
- The rating count values join the number and the label with no space, for example `56Buy rating(s)`. Parse the leading digits to get the count.
- For the analyst ratings behind the sentiment table, call [MarketBeat Analyst Ratings](/apis/marketbeat/analyst-ratings).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/marketbeat/competitors.json`](../../../catalog/models/marketbeat/competitors.json) · Store page: https://www.sandbase.ai/model/marketbeat/competitors
