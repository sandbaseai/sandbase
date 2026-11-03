# Facebook Event Details API: pricing, parameters and code examples

`facebook/event-details` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch full details for a single Facebook event by ID or URL (name, schedule, venue, hosts, and attendance) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/event-details"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/event-details', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/event-details", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/event-details", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/facebook/event-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | The event's numeric identifier.  |
| `url` | string |  | The event's Facebook URL.  |

## Details

This API returns the details of one Facebook event: its name, description, schedule, venue, hosts, and attendance counts. It needs either the event's numeric `id` or its Facebook `url`.

### Use cases

- Track how many people marked going or interested in a convention or concert.
- Pull venue name, address, and coordinates to place an event on a map.
- Check whether an event is canceled, online, or already past before listing it.
- Identify the host page of an event and link back to its Facebook profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/event-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "4045709448982422"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | The event's numeric identifier. |
| `url` | string | No | The event's Facebook URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "address": "225 W Douglas Ave, Wichita, KS 67202-3100, United States",
    "attendanceCount": 2489,
    "canViewMembers": true,
    "city": "Wichita, Kansas",
    "cityId": "105674782800210",
    "coverPhotoUrl": "https://scontent-dfw6-1.xx.fbcdn.net/v/t39.30808-6/570154625_122237652734251216_…",
    "creatorId": "61557536504734",
    "creatorName": "Kansas Comic Con",
    "dayTimeSentence": "Oct 31 at 10:00 AM – Nov 1 at 5:00 PM CST",
    "description": "Kansas Comic Con is back! Join us Saturday, October 31st and Sunday, November 1s…",
    "duration": "2 days",
    "endTime": ""
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name / data.description` | The event title and its description text. |
| `data.goingCount / data.interestedCount / data.attendanceCount` | Counts of people who responded going, people who responded interested, and the event's attendance count. |
| `data.startTimestamp` | The start of the event as a Unix timestamp in seconds. |
| `data.dayTimeSentence / data.startTimeFormatted / data.duration` | Human-readable schedule text, such as the date range with time zone and the length of the event. |
| `data.locationName / data.address / data.city` | The venue name, its street address, and the city. |
| `data.latitude / data.longitude` | Coordinates of the venue. |
| `data.hosts[].name / data.hosts[].url / data.hosts[].id` | The name, Facebook URL, and ID of each host. |
| `data.isCanceled / data.isOnline / data.isPast` | Flags that show whether the event is canceled, held online, or already over. |
| `data.privacy / data.eventKind` | The event's privacy setting and its type. |
| `found` | `true` when the event was found. |

### Notes

- Pass either `id` or `url`. The `id` is the number at the end of an event URL, such as `4045709448982422` in `https://www.facebook.com/events/4045709448982422/`.
- In the sample response, `startTime` and `endTime` are empty strings. Use `startTimestamp` for the start time.
- Use `hosts[].id` or `creatorId` to look up the host with [Facebook Profile](/apis/facebook/profile).
- To list more events from a host page, call [Facebook Page Events](/apis/facebook/profile-events).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/event-details.json`](../../../catalog/models/facebook/event-details.json) · Store page: https://www.sandbase.ai/model/facebook/event-details
