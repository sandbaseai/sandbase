# Polymarket Get simplified markets API: pricing, parameters and code examples

`polymarket/simplified-markets` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns simplified CLOB markets with token and reward summaries.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/simplified-markets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/simplified-markets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/simplified-markets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/simplified-markets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/simplified-markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `next_cursor` | string |  | next_cursor  |

## Details

Returns a page of simplified Polymarket CLOB markets. Each market has its status flags, its `condition_id`, a reward summary and the outcome tokens with their prices. The only input is an optional `next_cursor` for paging.

### Use cases

- Build a full list of Polymarket `condition_id` values by paging through all CLOB markets.
- Collect the `token_id` for each Yes and No outcome so you can query order books or prices.
- Filter for markets that are `active` and still `accepting_orders` to find ones you can trade.
- Check which markets have reward settings by reading `rewards.rates`, `rewards.min_size` and `rewards.max_spread`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/simplified-markets" \
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
      "accepting_orders": false,
      "active": true,
      "archived": false,
      "closed": true,
      "condition_id": "0xb62f71aef4c9972ddb75ec977b48156e1cc72e30f0e36b0f12c14de7fd94c777",
      "rewards": {
        "max_spread": 0,
        "min_size": 0,
        "rates": null
      },
      "tokens": [
        {
          "outcome": "Yes",
          "price": 0,
          "token_id": "47648429…",
          "winner": false
        }
      ],
      "version": "v1"
    }
  ],
  "limit": 1000,
  "next_cursor": "aWQ6MjQ5Mzk2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].condition_id` | Identifier of the market, a hex string starting with `0x`. |
| `data[].active / data[].closed / data[].archived` | Boolean flags for the market state. In the sample, markets are `active` and `closed` at the same time, so check both. |
| `data[].accepting_orders` | Whether the market currently takes new orders. It is `false` for the closed markets in the sample. |
| `data[].tokens[].outcome` | Name of the outcome, such as `Yes` or `No`. |
| `data[].tokens[].token_id` | Identifier of the outcome token. It is a long numeric string. |
| `data[].tokens[].price` | Current price of the outcome token. Resolved markets in the sample show `0` or `1`. |
| `data[].tokens[].winner` | Whether this outcome token won the market. |
| `data[].rewards.max_spread / data[].rewards.min_size / data[].rewards.rates` | Reward settings for the market. The sample shows `0` for the first two and `null` for `rates`, which means no reward rates are listed. |
| `count / limit` | Number of markets in this page and the page size. Both are `1000` in the sample. |
| `next_cursor` | Cursor string to pass as `next_cursor` to get the next page. |

### Notes

- Send an empty body `{}` to get the first page. Pass the returned `next_cursor` value in the next request to get the following page.
- Use `data[].tokens[].token_id` as input for [Polymarket Get order book](/apis/polymarket/book) or [Polymarket Get market price](/apis/polymarket/price).
- For full market details, use [Polymarket Get CLOB market info](/apis/polymarket/clob-markets) with a `condition_id`.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/simplified-markets.json`](../../../catalog/models/polymarket/simplified-markets.json) · Store page: https://www.sandbase.ai/model/polymarket/simplified-markets
