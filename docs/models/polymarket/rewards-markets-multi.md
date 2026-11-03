# Polymarket Get multiple markets with rewards API: pricing, parameters and code examples

`polymarket/rewards-markets-multi` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns multiple markets with rewards and supports filtering and sorting.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/rewards-markets-multi"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/rewards-markets-multi', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/rewards-markets-multi", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/rewards-markets-multi", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/rewards-markets-multi` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Text search on market question/description  |
| `event_id` | string |  | Filter by event ID. Can be repeated for multiple events (e.g., ?event_id=100&event_id=200)  |
| `order_by` | string |  | Field to sort results by one of: `market_id`, `created_at`, `volume_24hr`, `spread`, `competitiveness`, `max_spread`, `min_size`, `question`, `one_day_price_change`, `rate_per_day`, `price`, `end_date` … |
| `position` | string |  | Sort direction one of: `ASC`, `DESC` |
| `tag_slug` | string |  | Filter by tag slug. Can be repeated for OR logic (e.g., ?tag_slug=sports&tag_slug=politics)  |
| `max_price` | number |  | Maximum first token price filter  |
| `min_price` | number |  | Minimum first token price filter  |
| `page_size` | integer |  | Number of items per page (max 500, values above are capped) default `100`; range –500 |
| `max_spread` | number |  | Maximum spread filter  |
| `min_spread` | number |  | Minimum spread filter  |
| `event_title` | string |  | Search event titles using case-insensitive pattern matching  |
| `next_cursor` | string |  | Pagination cursor from previous response  |
| `max_volume_24hr` | number |  | Maximum 24-hour volume filter  |
| `min_volume_24hr` | number |  | Minimum 24-hour volume filter  |

## Details

Returns a page of Polymarket markets that have liquidity rewards, with prices, spread, 24-hour volume and reward settings for each market. No input is required. You can filter by event, tag, text, price, spread or volume, and sort the results.

### Use cases

- List markets in one event with a reward minimum size and maximum spread to find where to quote orders.
- Find reward markets with a wide `spread` and high `volume_24hr` to rank quoting opportunities.
- Pull `token_id` values for reward markets to feed into order book or price calls.
- Track which markets in a tag such as sports or politics currently offer rewards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/rewards-markets-multi" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `event_id` | string | No | Filter by event ID. Can be repeated for multiple events (e.g., ?event_id=100&event_id=200) |
| `event_title` | string | No | Search event titles using case-insensitive pattern matching |
| `max_price` | number | No | Maximum first token price filter |
| `max_spread` | number | No | Maximum spread filter |
| `max_volume_24hr` | number | No | Maximum 24-hour volume filter |
| `min_price` | number | No | Minimum first token price filter |
| `min_spread` | number | No | Minimum spread filter |
| `min_volume_24hr` | number | No | Minimum 24-hour volume filter |
| `next_cursor` | string | No | Pagination cursor from previous response |
| `order_by` | string | No | Field to sort results by |
| `page_size` | integer | No | Number of items per page (max 500, values above are capped) |
| `position` | string | No | Sort direction |
| `q` | string | No | Text search on market question/description |
| `tag_slug` | string | No | Filter by tag slug. Can be repeated for OR logic (e.g., ?tag_slug=sports&tag_slug=politics) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 100,
  "data": [
    {
      "condition_id": "0x2d3c4fc5cde6dfb43448402b912e41bd4453e3f030448ed026bff8f1a0bc072e",
      "created_at": "2025-07-08T19:05:57.129881Z",
      "end_date": "2028-11-08 04:59:00+00",
      "event_id": "31552",
      "event_slug": "presidential-election-winner-2028",
      "group_item_title": "Eric Trump",
      "image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/eric-trump-eb65c618d6.png",
      "market_competitiveness": 0,
      "market_id": "561263",
      "market_slug": "will-eric-trump-win-the-2028-us-presidential-election",
      "one_day_price_change": 0,
      "question": "Will Eric Trump win the 2028 US Presidential Election?"
    }
  ],
  "limit": 100,
  "next_cursor": "MTAw"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count / limit` | Number of markets in this page and the page size used. |
| `next_cursor` | Cursor for the next page. Send it back as `next_cursor`. |
| `data[].market_id / data[].condition_id` | Identifiers for the market. `market_id` is a numeric string and `condition_id` is a hex string. |
| `data[].question / data[].group_item_title` | The market question and the short label of the item inside its event, such as a candidate name. |
| `data[].event_id / data[].event_slug` | The event the market belongs to. |
| `data[].tokens[].outcome / data[].tokens[].price` | The outcome name (`Yes` or `No`) and its current price. |
| `data[].tokens[].token_id` | Token ID for each outcome. Use it in order book, price and spread calls. |
| `data[].spread / data[].volume_24hr` | Current spread of the market and its 24-hour volume. |
| `data[].rewards_max_spread / data[].rewards_min_size` | Reward settings for the market: the maximum spread and the minimum order size. |
| `data[].one_day_price_change / data[].market_competitiveness` | Price change over one day and the competitiveness score of the market. |

### Notes

- Send the `next_cursor` value from the response as the `next_cursor` parameter to get the next page.
- `page_size` defaults to 100 and is capped at 500.
- `order_by` accepts values such as `volume_24hr`, `spread`, `rate_per_day` and `reward_end_date`. Set `position` to `ASC` or `DESC`.
- To read the full details of one market, call [Polymarket Get market by id](/apis/polymarket/markets-by-id). To see its order book, call [Polymarket Get order book](/apis/polymarket/book) with a `token_id`.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/rewards-markets-multi.json`](../../../catalog/models/polymarket/rewards-markets-multi.json) · Store page: https://www.sandbase.ai/model/polymarket/rewards-markets-multi
