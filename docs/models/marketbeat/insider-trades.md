# MarketBeat Insider Trades API: pricing, parameters and code examples

`marketbeat/insider-trades` · data API · MarketBeat · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get recent insider transactions for a stock including transaction dates, insider names, buy/sell actions, share counts, average share prices, and total transaction values.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/insider-trades", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('marketbeat/insider-trades', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("marketbeat/insider-trades", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "marketbeat/insider-trades", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/marketbeat/insider-trades` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. 'AAPL').  |
| `exchange` | string |  | Stock exchange (e.g. 'NYSE', '').  |

## Details

Returns a list of recent insider transactions for a stock on MarketBeat. Each row has the insider, the buy or sell action, the share count, the average price, and the total value. You send a stock `ticker` and can add an optional `exchange`.

### Use cases

- Track whether executives at a company are mostly buying or selling shares.
- Flag large sales by a single insider, such as repeated sales of the same share count on different dates.
- Add recent insider activity to a stock research dashboard or alert feed.
- Compare insider sale prices with the current share price for a ticker.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/marketbeat/insider-trades" \
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
        "Average Share Price": "$343.36",
        "Buy/Sell": "Sell",
        "Details": "",
        "Insider": "Jennifer NewsteadSVP",
        "Number of Shares": "2,399",
        "Total Transaction": "$823,720.64",
        "Transaction Date": "10/27/2026"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[]` | One insider transaction per row. Each row holds the keys `Transaction Date`, `Insider`, `Buy/Sell`, `Number of Shares`, `Average Share Price`, `Total Transaction` and `Details`. |
| `data.items[].Insider` | Name of the insider, with their role attached to the end of the name, for example `Jennifer NewsteadSVP` or `Ben BordersInsider`. Split the name and role in your own code if you need them apart. |
| `data.items[].Details` | Extra detail text for the transaction. It is an empty string in the sample rows. |
| `status` | Shows `success` when the call worked. |

### Notes

- All values in each row are display strings, including dates, share counts and prices. Dates look like `10/27/2026`, prices like `$343.36`, and share counts like `2,399`. Remove `$` and `,` and parse them before you do math.
- `Buy/Sell` shows the direction of the trade. The sample rows show `Sell`, and `Total Transaction` holds the full dollar value, for example `$823,720.64`.
- The sample rows are listed with the newest `Transaction Date` first.
- To find a ticker first, use [MarketBeat Search Stocks](/apis/marketbeat/search-stocks). For a broader view of the company, call [MarketBeat Stock Overview](/apis/marketbeat/stock-overview).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/marketbeat/insider-trades.json`](../../../catalog/models/marketbeat/insider-trades.json) · Store page: https://www.sandbase.ai/model/marketbeat/insider-trades
