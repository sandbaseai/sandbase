# Facebook Events API: pricing, parameters and code examples

`facebook/events` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List public Facebook events for a city or place by its events-page URL (event name, date, venue, and attendance) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/events", "url": "https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/events', {'url': 'https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/events", {
  "url": "https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/events", sandbase.Params{
	"url": "https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547",
})
```

Same call via the path form: `POST /v1/api/facebook/events` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | URL of a city's or place's Facebook Events page (e.g. https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547).  |
| `time` | string |  | Timeframe filter for the returned events. Defaults to all time. one of: `today`, `this_week`, `next_week` |
| `cursor` | string |  | Pagination cursor from a previous response to fetch the next page.  |

## Details

Returns a list of public Facebook events for a city or place. It needs the URL of a Facebook Events page, such as a city's events explore page. Each event includes its name, start time, venue, and going and interested counts.

### Use cases

- Build a local "what's on" calendar for a city such as Saint Petersburg, Florida.
- Rank upcoming events by `interestedCount` and `goingCount` to find the most popular ones.
- Filter to events happening today or this week to feed a weekend guide or newsletter.
- Collect venue names and addresses to see where events are held in an area.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/events" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | URL of a city's or place's Facebook Events page (e.g. https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547). |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |
| `time` | string | No | Timeframe filter for the returned events. Defaults to all time. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "events": [
      {
        "coverImage": "https://scontent-lga3-1.xx.fbcdn.net/v/t39.30808-6/691737832_122221920272546827_…",
        "dayTimeSentence": "Sat, Nov 7 at 3:00 PM EST",
        "eventKind": "PUBLIC_TYPE",
        "goingCount": 250,
        "id": "1009766568177406",
        "interestedCount": 7400,
        "isHappeningNow": false,
        "isOnline": false,
        "isPast": false,
        "name": " 90s Day Party: St. Petersburg, FL 💿",
        "placeId": "122231702342546827",
        "placeName": "2655 6th Ave S, St Petersburg, FL 33712-1653, United States"
      }
    ],
    "nextCursor": "cur_4pRRU2-BvJCuoK3XKQ1TtA"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.events[].name` | Title of the event. |
| `data.events[].id / data.events[].url` | Event ID and the link to the event page on Facebook. |
| `data.events[].startTimestamp` | Event start time as a Unix timestamp in seconds. |
| `data.events[].dayTimeSentence` | Readable date and time text, such as `Sat, Nov 7 at 3:00 PM EST`. Multi-day events show a date range. |
| `data.events[].placeName` | Venue name or street address of the event. |
| `data.events[].placeId` | ID of the venue on Facebook. |
| `data.events[].goingCount / data.events[].interestedCount` | Number of people who marked the event as going and as interested. |
| `data.events[].isOnline / data.events[].isPast / data.events[].isHappeningNow` | Flags that show if the event is online, already over, or in progress. |
| `data.events[].coverImage` | URL of the event's cover image. |
| `data.nextCursor` | Cursor for the next page of events. |

### Notes

- Copy the `url` from the events explore page of a city or place on Facebook.
- To get the next page, send `data.nextCursor` back as `cursor` with the same `url`.
- Use `time` with `today`, `this_week`, or `next_week` to narrow the results. Without it, all upcoming events are returned.
- For full details on one event, pass its `id` to [Facebook Event Details](/apis/facebook/event-details).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/events.json`](../../../catalog/models/facebook/events.json) · Store page: https://www.sandbase.ai/model/facebook/events
