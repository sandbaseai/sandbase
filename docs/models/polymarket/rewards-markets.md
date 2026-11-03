# Polymarket Get raw rewards for a specific market API: pricing, parameters and code examples

`polymarket/rewards-markets` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Get raw rewards for a specific market from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/rewards-markets", "condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/rewards-markets', {'condition_id': '0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/rewards-markets", {
  "condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/rewards-markets", sandbase.Params{
	"condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
})
```

Same call via the path form: `POST /v1/api/polymarket/rewards-markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sponsored` | boolean |  | If true, folds sponsored daily rates into each config's rate_per_day default `false` |
| `next_cursor` | string |  | Pagination cursor from previous response  |
| `condition_id` | string | yes | The condition ID of the market  |

## Details

Returns the liquidity rewards setup for one Polymarket market. You pass the market's `condition_id`, and the response lists its reward configs, reward spread and size limits, and the outcome tokens with current prices.

### Use cases

- Check how much a market pays per day in liquidity rewards before you quote on it.
- Read the maximum spread and minimum order size a quote must meet to count for rewards.
- Get the `token_id` of each outcome so you can query order books or prices for that market.
- Track when a market's reward program starts and ends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/rewards-markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition_id": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition_id` | string | Yes | The condition ID of the market |
| `next_cursor` | string | No | Pagination cursor from previous response |
| `sponsored` | boolean | No | If true, folds sponsored daily rates into each config's rate_per_day |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 1,
  "data": [
    {
      "condition_id": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7",
      "event_slug": "xi-jinping-out-before-2027",
      "image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/xi-jinping-out-in-2025-EjF4…",
      "market_competitiveness": 9239.334112,
      "market_slug": "xi-jinping-out-before-2027",
      "question": "Xi Jinping out before 2027?",
      "rewards_config": [
        {
          "asset_address": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
          "end_date": "2500-12-31",
          "id": 303430,
          "rate_per_day": 5,
          "start_date": "2026-09-16",
          "total_days": 173232,
          "total_rewards": 0
        }
      ],
      "rewards_max_spread": 3.5,
      "rewards_min_size": 200,
      "tokens": [
        {
          "outcome": "Yes",
          "price": 0.0205,
          "token_id": "32338220…"
        }
      ]
    }
  ],
  "limit": 100,
  "next_cursor": "LTE="
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].question` | The market question in plain text. |
| `data[].market_slug / data[].event_slug` | Slugs for the market and for the event it belongs to. |
| `data[].rewards_config[].rate_per_day` | Reward amount paid per day for this config. With `sponsored` set to `true`, sponsored daily rates are added into this value. |
| `data[].rewards_config[].start_date / data[].rewards_config[].end_date` | Dates between which this reward config runs, in `YYYY-MM-DD` format. |
| `data[].rewards_config[].total_days / data[].rewards_config[].total_rewards` | Length of the config in days and the total rewards value recorded for it. |
| `data[].rewards_config[].asset_address` | Address of the asset used for the reward config. |
| `data[].rewards_max_spread` | Maximum spread allowed for an order to qualify for rewards. |
| `data[].rewards_min_size` | Minimum order size needed to qualify for rewards. |
| `data[].market_competitiveness` | A numeric score for how competitive the market's reward quoting is. |
| `data[].tokens[].outcome / data[].tokens[].price / data[].tokens[].token_id` | Name of each outcome, its current price, and the token ID for that outcome. |

### Notes

- Get the `condition_id` from a market lookup such as [Polymarket Get market by slug](/apis/polymarket/markets-slug) or [Polymarket List markets](/apis/polymarket/markets).
- The response includes `count`, `limit` and `next_cursor`. Pass `next_cursor` back as the `next_cursor` parameter to fetch the next page.
- Use the `token_id` values with [Polymarket Get order book](/apis/polymarket/book) to see live bids and asks.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/rewards-markets.json`](../../../catalog/models/polymarket/rewards-markets.json) · Store page: https://www.sandbase.ai/model/polymarket/rewards-markets
