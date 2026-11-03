# Polymarket Get market by id API: pricing, parameters and code examples

`polymarket/markets-by-id` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get market by id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/markets-by-id", "id": 559651}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/markets-by-id', {'id': 559651})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/markets-by-id", {
  "id": 559651
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/markets-by-id", sandbase.Params{
	"id": 559651,
})
```

Same call via the path form: `POST /v1/api/polymarket/markets-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `include_tag` | boolean |  | include_tag  |

## Details

Returns the full record for one Polymarket market, including its prices, order book settings, fees, dates and status flags. It needs the numeric market `id`. You can set `include_tag` to ask for tag data as well.

### Use cases

- Show the current best bid, best ask and last trade price for a single prediction market.
- Check whether a market is active, closed, archived or accepting orders before you place or display it.
- Read the `conditionId` and `clobTokenIds` of a market to query its order book or trades.
- Read the fee schedule and rewards settings for a market to estimate trading costs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/markets-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 559651}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |
| `include_tag` | boolean | No | include_tag |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "$schema": "https://gamma-api.polymarket.com/schemas/Market.json",
  "acceptingOrders": true,
  "acceptingOrdersTimestamp": "2025-07-03T20:36:33Z",
  "active": true,
  "approved": true,
  "archived": false,
  "automaticallyActive": true,
  "bestAsk": 0.021,
  "bestBid": 0.02,
  "clearBookOnStart": true,
  "clobRewards": [
    {
      "assetAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
      "conditionId": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7",
      "endDate": "2500-12-31",
      "id": "303430",
      "rewardsAmount": 0,
      "rewardsDailyRate": 5,
      "startDate": "2026-09-16"
    }
  ],
  "clobTokenIds": "[\"323382…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | The market id as a string. It matches the `id` you sent in the request. |
| `conditionId` | The condition id of the market, a 0x-prefixed hex string. The same value appears in `clobRewards[].conditionId`. |
| `clobTokenIds` | A JSON-encoded string that holds a list of token ids for the market outcomes. Parse it before use. |
| `bestBid / bestAsk / lastTradePrice` | The highest bid, the lowest ask and the last trade price for the market. Values are decimals such as `0.02`. |
| `liquidity` | Liquidity of the market, returned as a numeric string. |
| `active / closed / archived / acceptingOrders` | Status flags that show whether the market is live, finished, archived or taking orders right now. |
| `endDate / endDateIso` | The scheduled end of the market, as a full UTC timestamp and as a plain date. |
| `description` | The resolution rules of the market in plain text. |
| `feeSchedule.rate / feeSchedule.rebateRate / feeSchedule.takerOnly` | Fee settings for the market. `takerOnly` shows whether the fee applies only to takers. |
| `clobRewards[].rewardsDailyRate` | The daily rewards rate in a rewards entry for this market. Each entry also has `startDate` and `endDate`. |

### Notes

- Use [Polymarket List markets](/apis/polymarket/markets) to find market ids, or [Polymarket Get market by slug](/apis/polymarket/markets-slug) if you only have a slug.
- Timestamps such as `createdAt` use ISO 8601 UTC format. `endDateIso` is a date only.
- Pass the values from `clobTokenIds` to [Polymarket Get order book](/apis/polymarket/book) to see the live order book.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/markets-by-id.json`](../../../catalog/models/polymarket/markets-by-id.json) · Store page: https://www.sandbase.ai/model/polymarket/markets-by-id
