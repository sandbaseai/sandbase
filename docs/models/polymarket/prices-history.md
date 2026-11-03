# Polymarket Get prices history API: pricing, parameters and code examples

`polymarket/prices-history` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Get prices history from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/prices-history", "market": "32338220190071351435772801779725302244575775216413325951443816017994629993401"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/prices-history', {'market': '32338220190071351435772801779725302244575775216413325951443816017994629993401'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/prices-history", {
  "market": "32338220190071351435772801779725302244575775216413325951443816017994629993401"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/prices-history", sandbase.Params{
	"market": "32338220190071351435772801779725302244575775216413325951443816017994629993401",
})
```

Same call via the path form: `POST /v1/api/polymarket/prices-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `endTs` | number |  | Filter by items before this unix timestamp.  |
| `market` | string | yes | The market (asset id) to query.  |
| `startTs` | number |  | Filter by items after this unix timestamp.  |
| `fidelity` | integer |  | Accuracy of the data expressed in minutes. Default is 1 minute.  |
| `interval` | string |  | Time interval for data aggregation. one of: `max`, `all`, `1m`, `1w`, `1d`, `6h`, `1h` |

## Details

Returns the price history of one Polymarket outcome token as a list of timestamped prices. It needs a `market` value, which is the asset (token) id, and accepts optional `interval`, `fidelity`, `startTs` and `endTs` parameters.

### Use cases

- Plot how the market's implied probability for one outcome changed over the past week.
- Backtest a trading rule against hourly prices for a single outcome token.
- Find the time when a price jumped by comparing consecutive points in the series.
- Export a fixed time window of prices by setting `startTs` and `endTs`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/prices-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"market": "32338220190071351435772801779725302244575775216413325951443816017994629993401", "interval": "1w", "fidelity": 60}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `market` | string | Yes | The market (asset id) to query. |
| `endTs` | number | No | Filter by items before this unix timestamp. |
| `fidelity` | integer | No | Accuracy of the data expressed in minutes. Default is 1 minute. |
| `interval` | string | No | Time interval for data aggregation. |
| `startTs` | number | No | Filter by items after this unix timestamp. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "history": [
    {
      "p": 0.0375,
      "t": 1793088028
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `history` | List of price points for the requested market, in time order. |
| `history[].p` | Price of the outcome token at that point. The values in this response sit between 0 and 1, such as `0.0375`. |
| `history[].t` | Unix timestamp in seconds for the price point. |

### Notes

- `market` is the asset (token) id, a long numeric string. Use [Polymarket Get market by slug](/apis/polymarket/markets-slug) to look up a market and find its token ids.
- In the example request, `fidelity` is `60` and the points are about 3,600 seconds apart, which matches one point per hour.
- To get the current price instead of a series, call [Polymarket Get market price](/apis/polymarket/price).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/prices-history.json`](../../../catalog/models/polymarket/prices-history.json) · Store page: https://www.sandbase.ai/model/polymarket/prices-history
