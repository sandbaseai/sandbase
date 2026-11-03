# MarketBeat Institutional Ownership API: pricing, parameters and code examples

`marketbeat/institutional-ownership` · data API · MarketBeat · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get institutional ownership data including top institutional holders, their share positions, market value, portfolio percentage, quarterly change in shares, and ownership percentage in company.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/institutional-ownership", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('marketbeat/institutional-ownership', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("marketbeat/institutional-ownership", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "marketbeat/institutional-ownership", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/marketbeat/institutional-ownership` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. 'AAPL').  |
| `exchange` | string |  | Stock exchange (e.g. 'NYSE', '').  |

## Details

Returns a list of institutional holders for a stock, with each holder's share count, market value, and ownership stake. It needs a stock `ticker` such as `AAPL`, and accepts an optional `exchange`.

### Use cases

- Track which funds hold the largest positions in a stock.
- Spot institutions that are adding or cutting shares by checking the quarterly change.
- Compare how much of each holder's portfolio sits in one company.
- Build an ownership table for a stock research page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/marketbeat/institutional-ownership" \
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
        "% of Portfolio": "3.4%",
        "Details": "",
        "Major Shareholder Name": "Sanders Capital LLC",
        "Market Value": "$3.49B",
        "Ownership in Company": "0.072%",
        "Quarterly Change in Shares": "-0.4%",
        "Reporting Date": "11/3/2026",
        "Shares Held": "10,484,052"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items` | List of institutional holders. Each entry is one holder with a set of string values. |
| `data.items[]` | One holder. The keys `Major Shareholder Name`, `Shares Held` and `Market Value` give the holder's name, its share count, and the value of its position. |
| `data.items[]` | The keys `% of Portfolio` and `Ownership in Company` show how much of the holder's portfolio this stock makes up and what share of the company the holder owns. `Quarterly Change in Shares` shows the share change with a `+` or `-` sign. |
| `data.items[].Details` | Extra detail text for the row. It is an empty string in the sample response. |
| `status` | Shows `success` when the call worked. |

### Notes

- All values in each item are strings, including numbers and percentages. Parse them before you sort or sum.
- `Reporting Date` is the filing date of the position, in the format `11/3/2026`.
- To find a ticker first, call [MarketBeat Search Stocks](/apis/marketbeat/search-stocks).
- For insider activity on the same stock, call [MarketBeat Insider Trades](/apis/marketbeat/insider-trades).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/marketbeat/institutional-ownership.json`](../../../catalog/models/marketbeat/institutional-ownership.json) · Store page: https://www.sandbase.ai/model/marketbeat/institutional-ownership
