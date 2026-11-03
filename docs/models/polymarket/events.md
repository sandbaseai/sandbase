# Polymarket List events API: pricing, parameters and code examples

`polymarket/events` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

List events with offset based pagination and filter parameters.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/events"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/events', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/events", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/events", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/events` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | array |  | id  |
| `cyom` | boolean |  | cyom  |
| `slug` | array |  | slug  |
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `active` | boolean |  | active  |
| `closed` | boolean |  | Filter by closed state. Omitted includes open and closed events. Use true for closed events, false for open events, or any (case-insensitive) for both states. Unlike markets, any does not require an identifier filter.… one of: `any` |
| `offset` | integer |  | offset range 0– |
| `tag_id` | integer |  | tag_id  |
| `archived` | boolean |  | archived  |
| `featured` | boolean |  | featured  |
| `tag_slug` | string |  | tag_slug  |
| `ascending` | boolean |  | ascending  |
| `recurrence` | string |  | recurrence  |
| `volume_max` | number |  | volume_max  |
| `volume_min` | number |  | volume_min  |
| `end_date_max` | string |  | end_date_max  |
| `end_date_min` | string |  | end_date_min  |
| `include_chat` | boolean |  | include_chat  |
| `related_tags` | boolean |  | related_tags  |
| `liquidity_max` | number |  | liquidity_max  |
| `liquidity_min` | number |  | liquidity_min  |
| `exclude_tag_id` | array |  | exclude_tag_id  |
| `start_date_max` | string |  | start_date_max  |
| `start_date_min` | string |  | start_date_min  |
| `include_template` | boolean |  | include_template  |

## Details

Returns a list of Polymarket events, each with its nested markets, series and tags. All inputs are optional filters, such as `active`, `closed`, `tag_slug`, `slug`, `volume_min` and `end_date_max`, plus `limit` and `offset` for paging.

### Use cases

- Pull all open events under one tag, such as sports, and sort them by volume or liquidity.
- Find events by `slug` or `id` and read the markets inside each one.
- Track events that belong to a recurring series such as the NBA.
- Build a list of closed events in a date range for backtesting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/events" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 1, "active": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `active` | boolean | No | active |
| `archived` | boolean | No | archived |
| `ascending` | boolean | No | ascending |
| `closed` | boolean | No | Filter by closed state. Omitted includes open and closed events. Use true for closed events, false for open events, or any (case-insensitive) for both states. Unlike markets, any does not require an identifier filter. In |
| `cyom` | boolean | No | cyom |
| `end_date_max` | string | No | end_date_max |
| `end_date_min` | string | No | end_date_min |
| `exclude_tag_id` | array | No | exclude_tag_id |
| `featured` | boolean | No | featured |
| `id` | array | No | id |
| `include_chat` | boolean | No | include_chat |
| `include_template` | boolean | No | include_template |
| `limit` | integer | No | limit |
| `liquidity_max` | number | No | liquidity_max |
| `liquidity_min` | number | No | liquidity_min |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |
| `recurrence` | string | No | recurrence |
| `related_tags` | boolean | No | related_tags |
| `slug` | array | No | slug |
| `start_date_max` | string | No | start_date_max |
| `start_date_min` | string | No | start_date_min |
| `tag_id` | integer | No | tag_id |
| `tag_slug` | string | No | tag_slug |
| `volume_max` | number | No | volume_max |
| `volume_min` | number | No | volume_min |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
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
    "deploying": false,
    "description": "In the upcoming NBA game, scheduled for December 4:\n\nIf the Dallas Mavericks win…"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id / slug / ticker` | Identifiers for the event. `id` is a string, and `slug` is the text used in the event URL. |
| `title / description / category` | The event name, its resolution rules in text, and a category label such as `Sports`. |
| `active / closed / archived` | State flags for the event. In the sample, `active` and `closed` are both `true`, so do not assume `active` means open. |
| `startDate / endDate / closedTime` | Event start and end times, and the time the event closed, as ISO 8601 timestamps. |
| `commentCount` | Number of comments on the event. |
| `liquidity / openInterest` | Numeric liquidity and open interest values for the event. |
| `resolutionSource` | URL of the source named for resolving the event. |
| `markets[]` | The markets inside the event. Each one has its own `id`, `conditionId`, `endDate`, `bestBid`, `bestAsk`, `lastTradePrice` and `closed` state. |
| `markets[].clobTokenIds` | A JSON string holding the token IDs for the market outcomes. |
| `series[].slug / series[].title / series[].recurrence` | The series the event belongs to, its name, and how often it recurs, such as `daily`. |
| `tags[].id / tags[].label / tags[].slug` | Tags on the event. Use `id` with `tag_id` and `slug` with `tag_slug` to filter. |

### Notes

- Page through results with `limit` and `offset`. For cursor-based paging, use [Polymarket List events (keyset pagination)](/apis/polymarket/events-keyset).
- The response is a JSON array of events, not an object with a wrapper key.
- To fetch one event, use [Polymarket Get event by slug](/apis/polymarket/events-slug) or [Polymarket Get event by id](/apis/polymarket/events-by-id).
- Set `closed` to `any` to include both open and closed events.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/events.json`](../../../catalog/models/polymarket/events.json) · Store page: https://www.sandbase.ai/model/polymarket/events
