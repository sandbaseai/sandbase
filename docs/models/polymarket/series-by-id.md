# Polymarket Get series by id API: pricing, parameters and code examples

`polymarket/series-by-id` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get series by id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/series-by-id", "id": 1}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/series-by-id', {'id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/series-by-id", {
  "id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/series-by-id", sandbase.Params{
	"id": 1,
})
```

Same call via the path form: `POST /v1/api/polymarket/series-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `include_chat` | boolean |  | include_chat  |

## Details

Returns one Polymarket series by its numeric `id`. The response includes series details such as title, slug, recurrence and 24-hour volume, plus the events that belong to the series.

### Use cases

- Load the NFL series and list its game events with scores and dates.
- Track `volume24hr` and `commentCount` for a recurring series over time.
- Collect the event `slug` values of a series to fetch each game's markets.
- Read the tags on each event to sort series events into categories such as Sports or Games.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/series-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |
| `include_chat` | boolean | No | include_chat |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "$schema": "https://gamma-api.polymarket.com/schemas/Series.json",
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
  "featured": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title / slug / ticker` | Name and short identifiers of the series, for example `NFL` and `nfl`. |
| `recurrence / seriesType` | How often the series repeats (for example `daily`) and its type (for example `single`). |
| `volume24hr` | Trading volume figure for the series, as a number. |
| `commentCount` | Number of comments on the series. |
| `active / closed / archived` | Flags that show whether the series is live, closed or archived. |
| `events[].id / events[].slug` | Identifier and slug of each event in the series. Use them to look up the event. |
| `events[].startTime / events[].endDate / events[].closedTime` | Start time, scheduled end and actual close time of each event, as ISO 8601 timestamps. |
| `events[].score / events[].period / events[].eventWeek` | Final score, game period (for example `FT`) and week number for a sports event. |
| `events[].openInterest / events[].commentCount` | Open interest and comment count for each event. |
| `events[].tags[].label / events[].tags[].slug` | Name and slug of each tag attached to an event. |

### Notes

- `id` is required. `include_chat` is an optional boolean.
- Series and event `id` values are strings in the response, for example `"1"` and `"16407"`.
- To get full details for an event in the list, call [Polymarket Get event by slug](/apis/polymarket/events-slug) with its `slug`.
- To browse series and find ids, call [Polymarket List series](/apis/polymarket/series).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/series-by-id.json`](../../../catalog/models/polymarket/series-by-id.json) · Store page: https://www.sandbase.ai/model/polymarket/series-by-id
