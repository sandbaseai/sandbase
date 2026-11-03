# Facebook Page Events API: pricing, parameters and code examples

`facebook/profile-events` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List upcoming and past events hosted by any public Facebook page by URL (name, schedule, venue, and host) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/profile-events", "url": "https://www.facebook.com/brickyardoldtown"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/profile-events', {'url': 'https://www.facebook.com/brickyardoldtown'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/profile-events", {
  "url": "https://www.facebook.com/brickyardoldtown"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/profile-events", sandbase.Params{
	"url": "https://www.facebook.com/brickyardoldtown",
})
```

Same call via the path form: `POST /v1/api/facebook/profile-events` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The Facebook page link whose events to list, e.g. https://www.facebook.com/brickyardoldtown. Accepted: facebook.com/<name>, /p/<name>-<id>, /pages/<name>/<id>, /pg/<name>, /people/<name>/<id> and profile.php?id=<id>,…  |
| `cursor` | string |  | Pagination cursor from a previous response.  |

## Details

This API lists the upcoming and past events hosted by a public Facebook page. It needs the page link in `url` and returns each event's name, schedule text, start time, venue name, city, and host.

### Use cases

- Build a calendar of upcoming events for a venue or promoter page.
- Track when a competitor's page schedules new events or cancels existing ones.
- Collect event links for a list of local venues, then pull full details for each event.
- Check whether a page's events are online or at a physical place.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile-events" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/brickyardoldtown"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The Facebook page link whose events to list, e.g. https://www.facebook.com/brickyardoldtown. Accepted: facebook.com/<name>, /p/<name>-<id>, /pages/<name>/<id>, /pg/<name>, /people/<name>/<id> and profile.php?id=<id>, on  |
| `cursor` | string | No | Pagination cursor from a previous response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "events": [
      {
        "city": "Wichita",
        "creatorName": "Public at the Brickyard",
        "dayTimeSentence": "Tue, Nov 17 - Nov 30",
        "id": "1324020146405525",
        "isCanceled": false,
        "isOnline": true,
        "isPast": false,
        "name": "The Jingle Returns to Public!",
        "placeName": "Public at the Brickyard",
        "startTimestamp": 1794956400,
        "url": "https://www.facebook.com/events/1324020146405525/"
      }
    ],
    "hasNextPage": false,
    "nextCursor": "cur_iay97_cKG9azuqBjh6QcbQ",
    "totalCount": 2
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
| `data.events[].dayTimeSentence` | Human-readable schedule text as shown on Facebook, such as `Sat, Dec 5 at 10:00 AM CST` or a date range. |
| `data.events[].placeName / data.events[].city` | Name of the venue and the city it is in. |
| `data.events[].creatorName` | Name of the page or account that hosts the event. |
| `data.events[].isCanceled / data.events[].isPast / data.events[].isOnline` | Flags for whether the event is canceled, already over, or held online. |
| `data.totalCount` | Number of events in this response. |
| `data.hasNextPage / data.nextCursor` | Whether more events are available, and the cursor to request them. |
| `found` | `true` when the page was found. |

### Notes

- Pass the page link in `url`. Links to a single event, group, reel, video, or search page are refused as invalid input.
- To get the next page of events, send `nextCursor` as `cursor` in a new request. Do this when `hasNextPage` is `true`.
- Use [Facebook Event Details](/apis/facebook/event-details) with an event `url` to read one event in full.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/profile-events.json`](../../../catalog/models/facebook/profile-events.json) · Store page: https://www.sandbase.ai/model/facebook/profile-events
