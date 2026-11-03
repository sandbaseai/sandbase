# Polymarket List markets API: pricing, parameters and code examples

`polymarket/markets` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

List markets from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/markets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/markets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/markets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/markets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | array |  | id  |
| `cyom` | boolean |  | cyom  |
| `slug` | array |  | slug  |
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `closed` | boolean |  | Filter by closed state. Omitted or false returns open markets; true returns closed markets. Use any (case-insensitive) to include both states in an identifier lookup. Requires at least one of id, slug, clob_token_ids,… one of: `any` |
| `offset` | integer |  | offset range 0– |
| `tag_id` | integer |  | tag_id  |
| `game_id` | string |  | game_id  |
| `ascending` | boolean |  | ascending  |
| `include_tag` | boolean |  | include_tag  |
| `end_date_max` | string |  | end_date_max  |
| `end_date_min` | string |  | end_date_min  |
| `question_ids` | array |  | question_ids  |
| `related_tags` | boolean |  | related_tags  |
| `condition_ids` | array |  | condition_ids  |
| `clob_token_ids` | array |  | clob_token_ids  |
| `start_date_max` | string |  | start_date_max  |
| `start_date_min` | string |  | start_date_min  |
| `volume_num_max` | number |  | volume_num_max  |
| `volume_num_min` | number |  | volume_num_min  |
| `rewards_min_size` | number |  | rewards_min_size  |
| `liquidity_num_max` | number |  | liquidity_num_max  |
| `liquidity_num_min` | number |  | liquidity_num_min  |
| `sports_market_types` | array |  | sports_market_types  |
| `uma_resolution_status` | string |  | uma_resolution_status  |

## Details

Returns a list of Polymarket prediction markets as an array of market objects. Each market includes prices, liquidity, dates, fee settings, and its parent event. All inputs are optional filters such as `limit`, `offset`, `slug`, `id`, `tag_id`, and date or volume ranges.

### Use cases

- Pull the open markets with the highest volume or liquidity to build a ranked list of active bets.
- Look up the `bestBid`, `bestAsk`, and `lastTradePrice` of a market to track the current odds.
- Find the CLOB token IDs and condition ID of a market so you can query its order book or price history.
- Filter markets by end date or tag to monitor a topic such as politics until it resolves.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 1, "active": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ascending` | boolean | No | ascending |
| `clob_token_ids` | array | No | clob_token_ids |
| `closed` | boolean | No | Filter by closed state. Omitted or false returns open markets; true returns closed markets. Use any (case-insensitive) to include both states in an identifier lookup. Requires at least one of id, slug, clob_token_ids, po |
| `condition_ids` | array | No | condition_ids |
| `cyom` | boolean | No | cyom |
| `end_date_max` | string | No | end_date_max |
| `end_date_min` | string | No | end_date_min |
| `game_id` | string | No | game_id |
| `id` | array | No | id |
| `include_tag` | boolean | No | include_tag |
| `limit` | integer | No | limit |
| `liquidity_num_max` | number | No | liquidity_num_max |
| `liquidity_num_min` | number | No | liquidity_num_min |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |
| `question_ids` | array | No | question_ids |
| `related_tags` | boolean | No | related_tags |
| `rewards_min_size` | number | No | rewards_min_size |
| `slug` | array | No | slug |
| `sports_market_types` | array | No | sports_market_types |
| `start_date_max` | string | No | start_date_max |
| `start_date_min` | string | No | start_date_min |
| `tag_id` | integer | No | tag_id |
| `uma_resolution_status` | string | No | uma_resolution_status |
| `volume_num_max` | number | No | volume_num_max |
| `volume_num_min` | number | No | volume_num_min |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
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
    "clobTokenIds": "[\"323382…",
    "closed": false
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Numeric ID of the market, returned as a string. |
| `conditionId` | Condition ID of the market, a hex string. It also appears in `clobRewards[].conditionId`. |
| `clobTokenIds` | JSON-encoded string holding a list of token IDs for the market's outcomes. Parse it before use. |
| `bestBid / bestAsk / lastTradePrice` | Current best bid, best ask, and the last trade price of the market. |
| `liquidity` | Liquidity of the market, returned as a string. |
| `active / closed / archived / acceptingOrders` | Flags that show whether the market is live, finished, archived, or taking orders. |
| `endDate / endDateIso` | End date of the market as a full timestamp and as a plain date. |
| `description` | Text of the market's resolution rules. |
| `feeSchedule.rate / feeSchedule.rebateRate` | Fee rate and rebate rate set for the market. `feeSchedule.takerOnly` shows whether the fee applies only to takers. |
| `clobRewards[].rewardsDailyRate` | Daily reward rate for the market, with `startDate` and `endDate` for the reward period. |
| `events[].title / events[].slug` | Title and slug of the event that contains the market. |
| `events[].volume / events[].volume1mo / events[].openInterest` | Total volume, 1-month volume, and open interest of the parent event. |

### Notes

- Pass `limit` and `offset` to page through results.
- Set `closed` to `any` together with an identifier such as `id`, `slug`, or `condition_ids` to include open and closed markets in a lookup.
- Timestamps are ISO 8601 strings in UTC, for example `2025-07-03T20:36:33Z`.
- To fetch a single market, call [Polymarket Get market by slug](/apis/polymarket/markets-slug) or [Polymarket Get market by id](/apis/polymarket/markets-by-id). For the order book, call [Polymarket Get order book](/apis/polymarket/book).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/markets.json`](../../../catalog/models/polymarket/markets.json) · Store page: https://www.sandbase.ai/model/polymarket/markets
