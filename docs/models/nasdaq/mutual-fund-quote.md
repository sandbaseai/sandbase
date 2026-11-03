# Nasdaq Mutual Fund Quote API: pricing, parameters and code examples

`nasdaq/mutual-fund-quote` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Quote and details for a mutual fund including NAV and daily change. Mutual funds show isRealTime=false and have no bid/ask/volume data.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/mutual-fund-quote", "symbol": "VFIAX"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/mutual-fund-quote', {'symbol': 'VFIAX'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/mutual-fund-quote", {
  "symbol": "VFIAX"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/mutual-fund-quote", sandbase.Params{
	"symbol": "VFIAX",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/mutual-fund-quote` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string | yes | Mutual fund symbol (e.g. VFIAX).  |

## Details

Returns the current quote and basic details for one mutual fund listed on Nasdaq, including the last price, currency and fund type. It needs a fund ticker in `symbol`, such as `VFIAX`.

### Use cases

- Show the latest price of a Vanguard or other fund in a portfolio tracker.
- Check whether a fund moved up or down since the previous price using `deltaIndicator`.
- Confirm a ticker is a managed fund and read its full company name before adding it to a watchlist.
- Fill a fund detail page with the fund name, exchange and currency.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/mutual-fund-quote" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "VFIAX"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Mutual fund symbol (e.g. VFIAX). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": {
      "assetClass": "MUTUALFUNDS",
      "companyName": "Vanguard 500 Index Fd Admiral Shs",
      "exchange": "Nasdaq Fund Network",
      "isHeld": false,
      "isNasdaq100": false,
      "isNasdaqListed": false,
      "keyStats": null,
      "marketStatus": null,
      "notifications": null,
      "primaryData": {
        "askPrice": "",
        "askSize": "",
        "bidPrice": "",
        "bidSize": "",
        "currency": "USD",
        "deltaIndicator": "down",
        "isRealTime": false,
        "lastSalePrice": "$699.87"
      },
      "secondaryData": null,
      "stockType": "Managed Fund"
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
| `data.data.symbol` | The fund ticker that was requested, for example `VFIAX`. |
| `data.data.companyName` | Full name of the fund, for example `Vanguard 500 Index Fd Admiral Shs`. |
| `data.data.assetClass / data.data.stockType` | Asset class (`MUTUALFUNDS`) and fund type (`Managed Fund`). |
| `data.data.exchange` | Where the fund is listed. Mutual funds show `Nasdaq Fund Network`. |
| `data.data.primaryData.lastSalePrice` | Latest price of the fund as a formatted string with a dollar sign, for example `$699.87`. |
| `data.data.primaryData.deltaIndicator` | Direction of the latest change, such as `down`. |
| `data.data.primaryData.currency` | Currency of the price, for example `USD`. |
| `data.data.primaryData.isRealTime` | Whether the price is real time. It is `false` for mutual funds. |
| `data.data.primaryData.askPrice / bidPrice / askSize / bidSize` | Bid and ask values. They are empty strings for mutual funds. |
| `data.status.rCode` | Status code of the quote lookup. `200` means the lookup worked. |

### Notes

- `lastSalePrice` is a string with a `$` sign. Strip the symbol before you do math.
- `keyStats`, `marketStatus`, `notifications` and `secondaryData` are `null` in this response.
- If you do not know the ticker, find it first with [Nasdaq Search Symbols](/apis/nasdaq/search-symbols).
- For exchange-traded funds, use [Nasdaq Etf Quote](/apis/nasdaq/etf-quote) instead.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/nasdaq/mutual-fund-quote.json`](../../../catalog/models/nasdaq/mutual-fund-quote.json) · Store page: https://www.sandbase.ai/model/nasdaq/mutual-fund-quote
