# Polymarket Get market by slug API: pricing, parameters and code examples

`polymarket/markets-slug` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get market by slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/markets-slug", "slug": "xi-jinping-out-before-2027"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/markets-slug', {'slug': 'xi-jinping-out-before-2027'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/markets-slug", {
  "slug": "xi-jinping-out-before-2027"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/markets-slug", sandbase.Params{
	"slug": "xi-jinping-out-before-2027",
})
```

Same call via the path form: `POST /v1/api/polymarket/markets-slug` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `include_tag` | boolean |  | include_tag  |

## Details

Returns one Polymarket market as a JSON object, looked up by its URL slug. The response includes current prices, order book status, dates, fee settings, and the parent event. The only required input is `slug`.

### Use cases

- Show the current best bid, best ask and last trade price for a single prediction market.
- Read the resolution rules in `description` and the `endDate` before you display or analyze a market.
- Get the `conditionId` and `clobTokenIds` of a market so you can query order book and price APIs.
- Pull the parent event's volume, liquidity and open interest to size up a market.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/markets-slug" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "xi-jinping-out-before-2027"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | slug |
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
| `id / conditionId` | The market's numeric ID and its condition ID (a hex string). Use `conditionId` to match the market in other Polymarket calls. |
| `clobTokenIds` | A JSON string holding the token IDs for the market's outcomes. Parse it before use. |
| `bestBid / bestAsk / lastTradePrice` | Current best buy price, best sell price and last trade price. In this example they are `0.02`, `0.021` and `0.02`. |
| `active / closed / archived / acceptingOrders` | Flags that show whether the market is live, finished or hidden, and whether it takes orders now. |
| `description` | The resolution rules in plain text. The response may cut long text. |
| `endDate / endDateIso` | When the market ends, as a full UTC timestamp and as a plain date. |
| `competitive` | A score between 0 and 1 for the market. The response gives no further definition. |
| `feesEnabled / feeType / feeSchedule` | Whether fees apply, the fee category, and the fee rates. `feeSchedule` has `rate`, `rebateRate`, `exponent` and `takerOnly`. |
| `clobRewards[].rewardsDailyRate` | The daily rewards rate set for this market, with `startDate` and `endDate` for the program. |
| `events[].title / volume / liquidity / openInterest` | The parent event's title and its trading volume, liquidity and open interest. `volume1wk` and `volume1mo` give recent volume. |

### Notes

- Take the `slug` from a Polymarket market URL, or from the `slug` field in results of [Polymarket List markets](/apis/polymarket/markets) or [Polymarket Search markets, events, and profiles](/apis/polymarket/public-search).
- Set `include_tag` to `true` to ask for tag data. The example request did not use it.
- To look up a market by its numeric `id` instead, call [Polymarket Get market by id](/apis/polymarket/markets-by-id).
- Timestamps use ISO 8601 format in UTC, for example `2025-07-03T20:36:33Z`.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/markets-slug.json`](../../../catalog/models/polymarket/markets-slug.json) · Store page: https://www.sandbase.ai/model/polymarket/markets-slug
