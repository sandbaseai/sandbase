# Polymarket List series API: pricing, parameters and code examples

`polymarket/series` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

List series from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/series"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/series', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/series", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/series", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/series` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | array |  | slug  |
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `closed` | boolean |  | closed  |
| `offset` | integer |  | offset range 0– |
| `ascending` | boolean |  | ascending  |
| `recurrence` | string |  | recurrence  |
| `include_chat` | boolean |  | include_chat  |
| `categories_ids` | array |  | categories_ids  |
| `exclude_events` | boolean |  | exclude_events  |
| `categories_labels` | array |  | categories_labels  |

## Details

Returns a list of Polymarket series, such as the NFL, with each series' metadata, recurrence, 24-hour volume and the events that belong to it. All parameters are optional, so you can call it with no input or filter by `slug`, `closed`, `recurrence` or category.

### Use cases

- List every recurring series on Polymarket, such as daily or weekly sports series, to build a catalog.
- Pull the games inside a series with their dates, scores and tags to track results over a season.
- Rank series by `volume24hr` to see which recurring markets draw the most trading right now.
- Look up a series by `slug` to get its `id` for a follow-up call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/series" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ascending` | boolean | No | ascending |
| `categories_ids` | array | No | categories_ids |
| `categories_labels` | array | No | categories_labels |
| `closed` | boolean | No | closed |
| `exclude_events` | boolean | No | exclude_events |
| `include_chat` | boolean | No | include_chat |
| `limit` | integer | No | limit |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |
| `recurrence` | string | No | recurrence |
| `slug` | array | No | slug |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "active": true,
    "archived": false,
    "closed": false,
    "commentCount": 3097,
    "commentsEnabled": false,
    "competitive": "0",
    "createdAt": "2022-10-13T00:34:06.557Z",
    "createdBy": "15",
    "description": "NFL",
    "events": [
      {
        "active": true,
        "archived": false,
        "automaticallyActive": true,
        "automaticallyResolved": true,
        "closed": true,
        "closedTime": "2025-01-13T06:11:35Z",
        "commentCount": 3787,
        "createdAt": "2025-01-06T06:01:35.357849Z",
        "creationDate": "2025-01-13T01:00:00Z",
        "cyom": false,
        "deploying": false,
        "description": "In the upcoming NFL game, scheduled for January 12 at 8:00PM ET:\nIf the Washingt…"
      }
    ],
    "featured": false,
    "id": "1"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id / slug / ticker / title` | Identifiers and name of the series. In the example, `id` is `1`, `slug` and `ticker` are `nfl`, and `title` is `NFL`. |
| `recurrence / seriesType` | How often the series repeats (for example `daily`) and its type (for example `single`). |
| `active / closed / archived / featured` | Status flags for the series. |
| `volume24hr` | Trading volume number for the series over 24 hours, as reported by Polymarket. |
| `commentCount` | Number of comments on the series. |
| `events[].id / events[].slug / events[].seriesSlug` | Identifier and slug of each event in the series, and the slug of the series it belongs to. |
| `events[].eventDate / events[].startTime / events[].endDate` | Date of the game and the start and end timestamps of the event. |
| `events[].score / events[].period / events[].ended` | Final score as a text string such as `23-20`, the game period (for example `FT`), and whether the game has ended. |
| `events[].closed / events[].closedTime` | Whether the event's markets are closed and when they closed. |
| `events[].tags[].label / events[].tags[].slug` | Names and slugs of the tags attached to each event, such as `Sports` or `NFL (All)`. |

### Notes

- Page through results with `limit` and `offset`. Use `order` and `ascending` to control sorting.
- Set `exclude_events` to `true` to leave out the nested `events` list.
- Timestamps are ISO 8601 strings, and the IDs in the response are strings.
- To fetch one series by its ID, call [Polymarket Get series by id](/apis/polymarket/series-by-id). To list events directly, call [Polymarket List events](/apis/polymarket/events).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/series.json`](../../../catalog/models/polymarket/series.json) · Store page: https://www.sandbase.ai/model/polymarket/series
