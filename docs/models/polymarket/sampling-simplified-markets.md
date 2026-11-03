# Polymarket Get sampling simplified markets API: pricing, parameters and code examples

`polymarket/sampling-simplified-markets` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns sampling simplified markets with reward and token summaries.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/sampling-simplified-markets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/sampling-simplified-markets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/sampling-simplified-markets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/sampling-simplified-markets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/sampling-simplified-markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `next_cursor` | string |  | next_cursor  |

## Details

Returns a page of Polymarket markets that have reward programs, with each market's reward settings and its outcome tokens with prices. The call needs no input for the first page, and takes an optional `next_cursor` to fetch later pages.

### Use cases

- List markets that pay liquidity rewards and compare their `rewards_daily_rate` values.
- Find the `token_id` for each Yes and No outcome to use in order book or price calls.
- Track current outcome prices for reward-eligible markets.
- Filter for markets that are active and still accepting orders before quoting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/sampling-simplified-markets" \
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
      "accepting_orders": true,
      "active": true,
      "archived": false,
      "closed": false,
      "condition_id": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7",
      "rewards": {
        "max_spread": 3.5,
        "min_size": 200,
        "rates": [
          {
            "asset_address": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
            "rewards_daily_rate": 5
          }
        ]
      },
      "tokens": [
        {
          "outcome": "Yes",
          "price": 0.0205,
          "token_id": "32338220…",
          "winner": false
        }
      ],
      "version": "v1"
    }
  ],
  "limit": 1000,
  "next_cursor": "aWQ6MTMyODAxOQ=="
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Number of markets in this response page. |
| `limit` | Page size limit for the response. The sample shows `1000`. |
| `next_cursor` | Cursor string to pass as `next_cursor` to get the next page. |
| `data[].condition_id` | Hex ID of the market condition. Use it to identify the market in other calls. |
| `data[].active / data[].closed / data[].archived / data[].accepting_orders` | Boolean flags for market state. They show whether the market is live, finished, archived, or taking orders. |
| `data[].rewards.max_spread` | Maximum spread value allowed for an order to count toward rewards. |
| `data[].rewards.min_size` | Minimum order size value for an order to count toward rewards. |
| `data[].rewards.rates[].rewards_daily_rate` | Daily reward rate for the asset listed in `asset_address`. |
| `data[].tokens[].outcome / data[].tokens[].price` | Outcome label such as `Yes` or `No`, and its current price. Prices of the two outcomes add up to about 1. |
| `data[].tokens[].token_id / data[].tokens[].winner` | Long numeric ID of the outcome token, and a flag that shows whether that outcome won. |

### Notes

- Leave `next_cursor` out for the first page. Pass the `next_cursor` value from the response to get the next page.
- Use `token_id` as the input for token-based calls such as [Polymarket Get order book](/apis/polymarket/book) and [Polymarket Get midpoint price](/apis/polymarket/midpoint).
- Use `condition_id` with [Polymarket Get CLOB market info](/apis/polymarket/clob-markets) to get more detail on a single market.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/sampling-simplified-markets.json`](../../../catalog/models/polymarket/sampling-simplified-markets.json) · Store page: https://www.sandbase.ai/model/polymarket/sampling-simplified-markets
