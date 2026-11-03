# Polymarket List events (keyset pagination) API: pricing, parameters and code examples

`polymarket/events-keyset` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

List events with cursor based keyset pagination. Use next_cursor as after_cursor to fetch the next page. The offset parameter is rejected.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/events-keyset"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/events-keyset', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/events-keyset", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/events-keyset", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/events-keyset` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | array |  | id  |
| `cyom` | boolean |  | cyom  |
| `live` | boolean |  | live  |
| `slug` | array |  | slug  |
| `limit` | integer |  | Maximum number of results to return (max 100) default `20`; range 1–100 |
| `order` | string |  | Comma-separated list of JSON field names to order by  |
| `closed` | boolean |  | Filter by closed state. Omitted includes open and closed events. Use true for closed events, false for open events, or any (case-insensitive) for both states. Unlike markets, any does not require an identifier filter.… one of: `any` |
| `locale` | string |  | locale  |
| `offset` | integer |  | Not allowed. Returns 422 if provided.  |
| `tag_id` | array |  | tag_id  |
| `game_id` | array |  | game_id  |
| `featured` | boolean |  | featured  |
| `tag_slug` | string |  | tag_slug  |
| `ascending` | boolean |  | Sort direction. Only used when order is set. default `true` |
| `series_id` | array |  | series_id  |
| `tag_match` | string |  | tag_match  |
| `created_by` | array |  | created_by  |
| `event_date` | string |  | event_date  |
| `event_week` | integer |  | event_week  |
| `recurrence` | string |  | recurrence  |
| `volume_max` | number |  | volume_max  |
| `volume_min` | number |  | volume_min  |
| `after_cursor` | string |  | Opaque cursor token from a previous response's next_cursor  |
| `end_date_max` | string |  | end_date_max  |
| `end_date_min` | string |  | end_date_min  |
| `include_chat` | boolean |  | When true, includes Chats and Series.Chats relations  |
| `partner_slug` | string |  | When set, external_partners are attached to matching events  |
| `related_tags` | boolean |  | related_tags  |
| `title_search` | string |  | title_search  |
| `liquidity_max` | number |  | liquidity_max  |
| `liquidity_min` | number |  | liquidity_min  |
| `exclude_tag_id` | array |  | Tag IDs to exclude. Cannot overlap with tag_id.  |
| `featured_order` | boolean |  | featured_order  |
| `start_date_max` | string |  | start_date_max  |
| `start_date_min` | string |  | start_date_min  |
| `start_time_max` | string |  | start_time_max  |
| `start_time_min` | string |  | start_time_min  |
| `parent_event_id` | integer |  | parent_event_id  |
| `include_children` | boolean |  | include_children  |
| `include_template` | boolean |  | When true, includes Templates relation  |
| `include_best_lines` | boolean |  | When true, includes BestLines relation  |

## Details

Returns a page of Polymarket events, each with its markets, series and tags. All inputs are optional filters, and you page through results with a cursor instead of an offset.

### Use cases

- Pull every closed Polymarket event in a sport or tag to build a history of past markets.
- Find open events above a volume or liquidity threshold with `volume_min` or `liquidity_min`.
- Search event titles with `title_search` to track markets on a topic.
- Walk the full event list page by page to keep a local copy in sync.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/events-keyset" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after_cursor` | string | No | Opaque cursor token from a previous response's next_cursor |
| `ascending` | boolean | No | Sort direction. Only used when order is set. |
| `closed` | boolean | No | Filter by closed state. Omitted includes open and closed events. Use true for closed events, false for open events, or any (case-insensitive) for both states. Unlike markets, any does not require an identifier filter. In |
| `created_by` | array | No | created_by |
| `cyom` | boolean | No | cyom |
| `end_date_max` | string | No | end_date_max |
| `end_date_min` | string | No | end_date_min |
| `event_date` | string | No | event_date |
| `event_week` | integer | No | event_week |
| `exclude_tag_id` | array | No | Tag IDs to exclude. Cannot overlap with tag_id. |
| `featured` | boolean | No | featured |
| `featured_order` | boolean | No | featured_order |
| `game_id` | array | No | game_id |
| `id` | array | No | id |
| `include_best_lines` | boolean | No | When true, includes BestLines relation |
| `include_chat` | boolean | No | When true, includes Chats and Series.Chats relations |
| `include_children` | boolean | No | include_children |
| `include_template` | boolean | No | When true, includes Templates relation |
| `limit` | integer | No | Maximum number of results to return (max 100) |
| `liquidity_max` | number | No | liquidity_max |
| `liquidity_min` | number | No | liquidity_min |
| `live` | boolean | No | live |
| `locale` | string | No | locale |
| `offset` | integer | No | Not allowed. Returns 422 if provided. |
| `order` | string | No | Comma-separated list of JSON field names to order by |
| `parent_event_id` | integer | No | parent_event_id |
| `partner_slug` | string | No | When set, external_partners are attached to matching events |
| `recurrence` | string | No | recurrence |
| `related_tags` | boolean | No | related_tags |
| `series_id` | array | No | series_id |
| `slug` | array | No | slug |
| `start_date_max` | string | No | start_date_max |
| `start_date_min` | string | No | start_date_min |
| `start_time_max` | string | No | start_time_max |
| `start_time_min` | string | No | start_time_min |
| `tag_id` | array | No | tag_id |
| `tag_match` | string | No | tag_match |
| `tag_slug` | string | No | tag_slug |
| `title_search` | string | No | title_search |
| `volume_max` | number | No | volume_max |
| `volume_min` | number | No | volume_min |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "$schema": "https://gamma-api.polymarket.com/schemas/EventsKeysetListResponse.json",
  "events": [
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
  ],
  "next_cursor": "baQCMe2wl4-1BqJJ87F6fVlbWuykHjYlEXNrqgeisfJ7InYiOjEsImsiOiJldmVudHMiLCJvaCI6IjRm…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `events[].id / events[].slug / events[].ticker` | Identifiers for the event. `id` is a numeric string, and `slug` and `ticker` are readable keys that match the event URL name. |
| `events[].title / events[].description` | The event question and the text that explains how its markets resolve. |
| `events[].active / events[].closed / events[].archived` | Flags for the event state. `closedTime` gives the time the event was closed. |
| `events[].startDate / events[].endDate / events[].createdAt` | ISO 8601 timestamps for when the event starts, ends and was created. |
| `events[].liquidity / events[].openInterest / events[].commentCount` | Liquidity, open interest and comment count for the event. |
| `events[].resolutionSource` | URL of the source used to settle the event. |
| `events[].markets[].bestBid / events[].markets[].bestAsk` | Best bid and best ask price for a market inside the event. |
| `events[].markets[].clobTokenIds` | Token IDs for the market outcomes, returned as a JSON-encoded string. Parse it before use. |
| `events[].tags[].id / events[].tags[].label / events[].tags[].slug` | Tags attached to the event. Use the `id` values with `tag_id` or `exclude_tag_id` to filter. |
| `events[].series[] / events[].seriesSlug` | The series the event belongs to, such as `nba` or `nfl`. |

### Notes

- Copy `next_cursor` from the response into `after_cursor` to get the next page. Do not send `offset`, which returns a 422 error.
- `limit` accepts 1 to 100 and defaults to 20.
- To fetch one event, use [Polymarket Get event by slug](/apis/polymarket/events-slug) or [Polymarket Get event by id](/apis/polymarket/events-by-id).
- For offset-style paging, use [Polymarket List events](/apis/polymarket/events).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/events-keyset.json`](../../../catalog/models/polymarket/events-keyset.json) · Store page: https://www.sandbase.ai/model/polymarket/events-keyset
