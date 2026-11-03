# Polymarket Get event by id API: pricing, parameters and code examples

`polymarket/events-by-id` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get event by id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/events-by-id", "id": 2890}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/events-by-id', {'id': 2890})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/events-by-id", {
  "id": 2890
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/events-by-id", sandbase.Params{
	"id": 2890,
})
```

Same call via the path form: `POST /v1/api/polymarket/events-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `include_chat` | boolean |  | include_chat  |
| `include_template` | boolean |  | include_template  |

## Details

Returns one Polymarket event by its numeric `id`. The response includes the event details, its markets, the series it belongs to, and its tags. You can also set `include_chat` and `include_template` to add extra data.

### Use cases

- Load the title, dates, resolution source and status of a single Polymarket event after you found its id in a list.
- Read the markets inside an event to get each market's condition ID, CLOB token IDs and last trade price.
- Check whether an event is closed and when it closed.
- Find which series and tags an event belongs to, for grouping sports events.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/events-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 2890}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |
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
| `id / slug / ticker` | Identifiers for the event. `id` is a numeric string, and `slug` and `ticker` are text names you can use in URLs and lookups. |
| `active / closed / archived` | Status flags for the event. In this example the event is `closed` and still marked `active`. |
| `startDate / endDate / closedTime` | ISO 8601 timestamps for when the event starts, ends and was closed. |
| `description / resolutionSource` | The resolution rules in plain text and the URL of the source used to settle the event. |
| `category / seriesSlug` | The event category, such as `Sports`, and the slug of the series it belongs to. |
| `commentCount` | The number of comments on the event. |
| `markets[].id / markets[].conditionId` | The market's Polymarket id and its on-chain condition ID. |
| `markets[].clobTokenIds` | A JSON-encoded string that lists the CLOB token IDs for the market's outcomes. |
| `markets[].bestBid / markets[].bestAsk / markets[].lastTradePrice` | The best bid, best ask and last trade price of the market. |
| `series[].title / series[].recurrence` | The name of the series and how often it recurs, such as `daily`. |

### Notes

- Take the `id` from a list call such as [Polymarket List events](/apis/polymarket/events). Pass it as an integer.
- If you only know the slug, call [Polymarket Get event by slug](/apis/polymarket/events-slug) instead.
- `markets[].clobTokenIds` is a string that holds a JSON list. Parse it before you use the token IDs.
- For details on one market in the event, call [Polymarket Get market by id](/apis/polymarket/markets-by-id) with the value of `markets[].id`.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/events-by-id.json`](../../../catalog/models/polymarket/events-by-id.json) · Store page: https://www.sandbase.ai/model/polymarket/events-by-id
