# Nasdaq Retail Trading Activity API: pricing, parameters and code examples

`nasdaq/retail-trading-activity` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retail Trading Activity Tracker (RTAT) showing the top 5 stocks by percent of retail equity flow, with activity percentage change and buy/sell sentiment.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/retail-trading-activity"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/retail-trading-activity', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/retail-trading-activity", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/retail-trading-activity", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/retail-trading-activity` with the body above minus `model`.

## Details

Returns the Nasdaq Retail Trading Activity Tracker (RTAT) table, which lists the top 5 stocks by percent of retail equity flow. Each row shows the ticker, company name, activity percentage, and a buy/sell sentiment label. The API takes no input.

### Use cases

- Show a daily list of the stocks with the highest share of retail equity flow on a market dashboard.
- Flag tickers with a rising activity share, such as rows where `deltaIndicator` is `up`, for further research.
- Compare retail buy/sell sentiment across the top 5 names in a daily market summary.
- Feed the ticker list into a watchlist or alert tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/retail-trading-activity" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": {
      "date": "Data as of Oct 29, 2026",
      "subtitle": "Top 5 by Percent of Retail Equity Flow",
      "table": {
        "asOf": null,
        "headers": {
          "activity": "ACTIVITY",
          "sentiment": "SENTIMENT",
          "ticker": "SYMBOL"
        },
        "rows": [
          {
            "activity": "+26.15%",
            "deltaIndicator": "up",
            "sentiment": "BUY +3",
            "ticker": [
              "AMC"
            ],
            "url": "/market-activity/stocks/amc"
          }
        ]
      },
      "title": "Retail Trading Activity Tracker"
    },
    "message": null,
    "status": {
      "bCodeMessage": null,
      "developerMessage": null,
      "rCode": 200
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data.title / data.data.subtitle` | Name of the tracker and the ranking rule, here `Top 5 by Percent of Retail Equity Flow`. |
| `data.data.date` | Text label with the as-of date for the data, for example `Data as of Oct 29, 2026`. |
| `data.data.table.rows[].ticker` | A list with two items: the stock symbol first, then the full company name. |
| `data.data.table.rows[].activity` | Activity for the stock as a percent string. Some values carry a sign, such as `+26.15%`, and some do not, such as `20.6%`. |
| `data.data.table.rows[].deltaIndicator` | Direction of the change in activity. Values seen are `up` and `unch`. |
| `data.data.table.rows[].sentiment` | Buy/sell sentiment label, such as `BUY +3` or `EVEN`. |
| `data.data.table.rows[].url` | Relative path to the stock page on Nasdaq, for example `/market-activity/stocks/amc`. |
| `data.data.table.headers` | Display labels for the table columns, with keys `activity`, `sentiment` and `ticker`. |
| `data.data.status.rCode / status` | Status codes for the call. `rCode` is `200` and the top-level `status` is `success` when the call works. |

### Notes

- The request body is empty (`{}`). There is nothing to filter or page through.
- The `date` field is a display string, not an ISO timestamp. `table.asOf` was `null` in this response.
- Pass a symbol from `ticker[0]` to [Nasdaq Stock Quote](/apis/nasdaq/stock-quote) to get quote data for that stock.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/nasdaq/retail-trading-activity.json`](../../../catalog/models/nasdaq/retail-trading-activity.json) · Store page: https://www.sandbase.ai/model/nasdaq/retail-trading-activity
