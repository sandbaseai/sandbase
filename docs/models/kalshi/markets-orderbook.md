# Kalshi Get Kalshi Market OrderBook API: pricing, parameters and code examples

`kalshi/markets-orderbook` · data API · Kalshi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Kalshi Market OrderBook from Kalshi. Returns the official Kalshi API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/markets-orderbook", "ticker": "KXHIGHNY-26OCT31-B60.5"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kalshi/markets-orderbook', {'ticker': 'KXHIGHNY-26OCT31-B60.5'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kalshi/markets-orderbook", {
  "ticker": "KXHIGHNY-26OCT31-B60.5"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kalshi/markets-orderbook", sandbase.Params{
	"ticker": "KXHIGHNY-26OCT31-B60.5",
})
```

Same call via the path form: `POST /v1/api/kalshi/markets-orderbook` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `depth` | integer |  | Depth of the orderbook to retrieve (0 or negative means all levels, 1-100 for specific depth) default `0`; range 0–100 |
| `ticker` | string | yes | Market ticker  |

## Details

Returns the current order book for one Kalshi market. You pass the market `ticker`, and you can limit the number of price levels with `depth`.

### Use cases

- Check the bid side of a Kalshi market before placing an order.
- Track how the `yes_dollars` and `no_dollars` books change over time for a single market.
- Detect markets with no resting orders by checking for empty lists.
- Chart order book depth for a weather market such as a New York daily high temperature.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kalshi/markets-orderbook" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "KXHIGHNY-26OCT31-B60.5"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Market ticker |
| `depth` | integer | No | Depth of the orderbook to retrieve (0 or negative means all levels, 1-100 for specific depth) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "orderbook_fp": {
    "no_dollars": [],
    "yes_dollars": []
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `orderbook_fp` | Top-level object that holds the order book for the requested market. |
| `orderbook_fp.yes_dollars` | List of price levels on the yes side of the book. The list is empty in the sample response, which means no yes orders were listed. |
| `orderbook_fp.no_dollars` | List of price levels on the no side of the book. The list is empty in the sample response, which means no no orders were listed. |

### Notes

- Get the `ticker` value from [Kalshi Get Kalshi Markets](/apis/kalshi/markets). Use the market's ticker, not the event ticker.
- Set `depth` from 1 to 100 to limit the number of levels. The default `0` returns all levels.
- Both lists can come back empty, as in the example for `KXHIGHNY-26OCT31-B60.5`.
- For the last price of a market, call [Kalshi Get Market Price](/apis/kalshi/markets-by-ticker).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/kalshi/markets-orderbook.json`](../../../catalog/models/kalshi/markets-orderbook.json) · Store page: https://www.sandbase.ai/model/kalshi/markets-orderbook
