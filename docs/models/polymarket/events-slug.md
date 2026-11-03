# Polymarket Get event by slug API: pricing, parameters and code examples

`polymarket/events-slug` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get event by slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/events-slug", "slug": "nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/events-slug', {'slug': 'nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/events-slug", {
  "slug": "nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/events-slug", sandbase.Params{
	"slug": "nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup",
})
```

Same call via the path form: `POST /v1/api/polymarket/events-slug` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `include_chat` | boolean |  | include_chat  |
| `include_template` | boolean |  | include_template  |

## Details

Returns one Polymarket event for a given `slug`. The response includes the event's dates, status flags, tags, series, and the list of markets inside it. Optional flags `include_chat` and `include_template` add extra data to the call.

### Use cases

- Load the full record of a known Polymarket event page from the slug in its URL.
- Read the markets inside an event, with their condition IDs and token IDs, before you query prices or order books.
- Check whether an event is `active`, `closed`, or `archived` before you show it in an app.
- Group events by series or tag, such as the NBA series, for sports dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/events-slug" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | slug |
| `include_chat` | boolean | No | include_chat |
| `include_template` | boolean | No | include_template |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "$schema": "https://gamma-api.polymarket.com/schemas/Event.json",
  "active": true,
  "archived": false,
  "category": "Sports",
  "closed": true,
  "closedTime": "2022-07-27T14:40:02.074Z",
  "commentCount": 8128,
  "competitive": 0,
  "createdAt": "2022-07-27T14:40:02.074Z",
  "creationDate": "2021-12-04T00:00:00Z",
  "cyom": false,
  "deploying": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id / slug / ticker` | Identifiers of the event. `id` is a numeric string, and `slug` and `ticker` hold the URL-style name. |
| `active / closed / archived` | Status flags for the event. `closedTime` shows when the event was closed. |
| `startDate / endDate / creationDate` | Dates of the event in ISO 8601 format. |
| `description / resolutionSource` | The resolution rules in text, and the URL of the source used to settle the event. |
| `commentCount` | Number of comments on the event. |
| `liquidity / openInterest` | Numeric liquidity and open interest of the event. Both are `0` in this example. |
| `markets[].id / markets[].conditionId` | ID of each market in the event, and its `0x` condition ID. |
| `markets[].clobTokenIds` | JSON string that holds the token IDs of the market, one for each outcome. |
| `markets[].bestBid / markets[].bestAsk / markets[].lastTradePrice` | Best bid, best ask, and last trade price of the market. |
| `series[].title / series[].slug / series[].recurrence` | Name, slug, and recurrence of the series the event belongs to, such as `NBA` and `daily`. |
| `tags[].label / tags[].slug` | Label and slug of each tag on the event. |

### Notes

- Take the `slug` from the end of a Polymarket event URL, or find it with [Polymarket List events](/apis/polymarket/events) or [Polymarket Search markets, events, and profiles](/apis/polymarket/public-search).
- To look up an event by its numeric `id` instead, use [Polymarket Get event by id](/apis/polymarket/events-by-id).
- `markets[].clobTokenIds` is a JSON string, so parse it before you use the token IDs.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/events-slug.json`](../../../catalog/models/polymarket/events-slug.json) · Store page: https://www.sandbase.ai/model/polymarket/events-slug
