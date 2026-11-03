# Polymarket Get sampling markets API: pricing, parameters and code examples

`polymarket/sampling-markets` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns sampling markets with richer descriptive metadata, token summaries, and tags.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/sampling-markets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/sampling-markets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/sampling-markets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/sampling-markets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/sampling-markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `next_cursor` | string |  | next_cursor  |

## Details

Returns a page of Polymarket sampling markets with the question, description, tags, outcome tokens with prices, order settings and reward settings. It needs no input for the first page. Pass `next_cursor` to get the next page.

### Use cases

- Pull the current `Yes` and `No` prices for a set of sampled markets to track how the market rates an outcome.
- Filter markets by `tags` to build a list of politics or geopolitics questions.
- Collect `token_id` values to feed into price, order book or midpoint calls.
- Compare `rewards` settings across markets to find where liquidity rewards are offered.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/sampling-markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `next_cursor` | string | No | next_cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 1000,
  "data": [
    {
      "accepting_order_timestamp": "2025-07-03T20:36:33Z",
      "accepting_orders": true,
      "active": true,
      "archived": false,
      "closed": false,
      "condition_id": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7",
      "description": "This market will resolve to \"Yes\" if China's General Secretary of the Communist …",
      "enable_order_book": true,
      "end_date_iso": "2027-01-01T00:00:00Z",
      "fpmm": "",
      "game_start_time": null,
      "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/xi-jinping-out-in-2025-EjF4…"
    }
  ],
  "limit": 1000,
  "next_cursor": "aWQ6MTMyODAxOQ=="
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].question / data[].description` | The market question and the text that explains how the market resolves. |
| `data[].market_slug` | URL slug for the market. Use it to look up the market by slug. |
| `data[].condition_id / data[].question_id` | Hex IDs for the market condition and its question. |
| `data[].tokens[].outcome / data[].tokens[].price` | Name of each outcome, such as `Yes` or `No`, and its current price as a decimal between 0 and 1. |
| `data[].tokens[].token_id / data[].tokens[].winner` | ID of the outcome token and a flag that shows whether that outcome won. |
| `data[].tags` | List of topic labels for the market, such as `Politics` or `Geopolitics`. |
| `data[].active / data[].closed / data[].archived / data[].accepting_orders` | Flags for the market state and whether it takes orders now. |
| `data[].end_date_iso` | End date of the market as an ISO 8601 UTC timestamp. |
| `data[].neg_risk / data[].neg_risk_market_id` | Shows whether the market is part of a negative risk group. The market ID links markets in the same group. |
| `data[].rewards.max_spread / data[].rewards.min_size / data[].rewards.rates[].rewards_daily_rate` | Reward settings for the market: the maximum spread, the minimum size, and the daily reward rate for each asset. |

### Notes

- Send `{}` to get the first page. The response has `count`, `limit` and `next_cursor`.
- To get the next page, copy `next_cursor` from the response into the `next_cursor` request parameter.
- Use `token_id` with [Polymarket Get order book](/apis/polymarket/book) or [Polymarket Get midpoint price](/apis/polymarket/midpoint) to get live market data for one outcome.
- For a shorter response per market, use [Polymarket Get sampling simplified markets](/apis/polymarket/sampling-simplified-markets).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/sampling-markets.json`](../../../catalog/models/polymarket/sampling-markets.json) · Store page: https://www.sandbase.ai/model/polymarket/sampling-markets
