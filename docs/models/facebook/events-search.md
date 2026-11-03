# Facebook Events Search API: pricing, parameters and code examples

`facebook/events-search` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search public Facebook events by keyword and get structured event records (name, schedule, venue, pricing, and attendance) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/events-search", "query": "music festival"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/events-search', {'query': 'music festival'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/events-search", {
  "query": "music festival"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/events-search", sandbase.Params{
	"query": "music festival",
})
```

Same call via the path form: `POST /v1/api/facebook/events-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The query to search events for.  |
| `cursor` | string |  | Pagination cursor from a previous response.  |

## Details

This API searches public Facebook events by keyword. It needs a `query` string and returns a list of matching events with name, date text, place, attendance counts, and a link to each event page.

### Use cases

- Find music festivals or other events that match a topic to build an event listings page.
- Compare `goingCount` and `interestedCount` across events to see which ones draw the most interest.
- Collect event venues from `placeName` and `placeId` to map where events on a topic take place.
- Pull event URLs and IDs from a search, then fetch full records for the ones you want.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/events-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "music festival"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The query to search events for. |
| `cursor` | string | No | Pagination cursor from a previous response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "events": [
      {
        "coverImage": "https://scontent-lga3-3.xx.fbcdn.net/v/t39.30808-6/699504039_1385612160276095_77…",
        "dayTimeSentence": "Saturday, August 8, 2026 at 10:00 AM – 7:00 PM PDT",
        "eventKind": "PUBLIC_TYPE",
        "goingCount": 39,
        "id": "26785548844435134",
        "interestedCount": 189,
        "isOnline": false,
        "isPast": true,
        "name": "SOULNIC Music Festival 2026",
        "placeId": "110814105639169",
        "placeName": "Grand Hope Park",
        "priceRangeText": ""
      }
    ],
    "nextCursor": "cur_ElaihBBDDUQAbGudkWvX2w"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.events[].id` | Facebook ID of the event. |
| `data.events[].name` | Title of the event. |
| `data.events[].url` | Link to the event page on Facebook. |
| `data.events[].dayTimeSentence` | Human-readable schedule text, including the time zone. Multi-day events show both start and end dates. |
| `data.events[].startTimestamp` | Event start time as a Unix timestamp in seconds. |
| `data.events[].isPast / data.events[].isOnline` | Booleans. `isPast` marks events that already happened. `isOnline` marks online events. |
| `data.events[].placeName / data.events[].placeId` | Name and Facebook ID of the venue. Both are empty strings when the event has no linked place. |
| `data.events[].goingCount / data.events[].interestedCount` | Number of people who marked themselves as going, and number who marked themselves as interested. |
| `data.events[].priceRangeText` | Price text for the event. It is an empty string when no price is listed. |
| `data.nextCursor` | Cursor to pass as `cursor` to get the next page of results. |

### Notes

- Pass `data.nextCursor` from a response as `cursor` in the next request, with the same `query`, to get more results.
- `startTimestamp` is in seconds, so multiply by 1000 for JavaScript dates.
- Results can include past events. Check `isPast` to filter them out.
- For more detail on one event, use [Facebook Event Details](/apis/facebook/event-details) with the event `id` or `url`.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/events-search.json`](../../../catalog/models/facebook/events-search.json) · Store page: https://www.sandbase.ai/model/facebook/events-search
