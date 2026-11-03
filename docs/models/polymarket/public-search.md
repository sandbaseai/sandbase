# Polymarket Search markets, events, and profiles API: pricing, parameters and code examples

`polymarket/public-search` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Search markets, events, and profiles from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/public-search", "q": "election"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/public-search', {'q': 'election'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/public-search", {
  "q": "election"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/public-search", sandbase.Params{
	"q": "election",
})
```

Same call via the path form: `POST /v1/api/polymarket/public-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | q  |
| `page` | integer |  | page  |
| `sort` | string |  | sort  |
| `cache` | boolean |  | cache  |
| `ascending` | boolean |  | ascending  |
| `optimized` | boolean |  | optimized  |
| `events_tag` | array |  | events_tag  |
| `recurrence` | string |  | recurrence  |
| `search_tags` | boolean |  | search_tags  |
| `events_status` | string |  | events_status  |
| `exclude_tag_id` | array |  | exclude_tag_id  |
| `limit_per_type` | integer |  | limit_per_type  |
| `search_profiles` | boolean |  | search_profiles  |
| `keep_closed_markets` | integer |  | keep_closed_markets  |

## Details

Searches Polymarket for events that match a text query. Each event includes its markets, tags, and status. The only required input is `q`, a search string such as `election`.

### Use cases

- Find every Polymarket event about a topic, such as an election, to track related betting markets.
- Build a search box that lists matching events with their title, image, and slug.
- Collect the tag labels on matching events to see how Polymarket groups a topic.
- Check how many events match a keyword by reading the total result count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/public-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "election"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | q |
| `ascending` | boolean | No | ascending |
| `cache` | boolean | No | cache |
| `events_status` | string | No | events_status |
| `events_tag` | array | No | events_tag |
| `exclude_tag_id` | array | No | exclude_tag_id |
| `keep_closed_markets` | integer | No | keep_closed_markets |
| `limit_per_type` | integer | No | limit_per_type |
| `optimized` | boolean | No | optimized |
| `page` | integer | No | page |
| `recurrence` | string | No | recurrence |
| `search_profiles` | boolean | No | search_profiles |
| `search_tags` | boolean | No | search_tags |
| `sort` | string | No | sort |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "events": [
    {
      "active": true,
      "archived": false,
      "closed": true,
      "closedTime": "2023-11-08T07:31:57Z",
      "commentCount": 17,
      "commentsEnabled": false,
      "competitive": 0,
      "createdAt": "2023-11-06T15:52:14.553Z",
      "creationDate": "2023-11-06T16:29:08.874Z",
      "cyom": false,
      "deploying": false,
      "description": "This market will resolve to \"Presley\" if Brandon Presley (D) wins the 2023 Missi…"
    }
  ],
  "pagination": {
    "hasMore": true,
    "totalResults": 4713
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `events[].title` | Display name of the event, for example the election being bet on. |
| `events[].slug / events[].ticker` | Text identifier for the event. Use the slug to look up the event on its own. |
| `events[].id` | Event ID as a string. |
| `events[].active / events[].closed / events[].archived` | Status flags for the event. A closed event has ended trading, and `closedTime` shows when it closed. |
| `events[].startDate / events[].endDate` | Start and end dates of the event in ISO 8601 format. |
| `events[].description` | Resolution rules and background text for the event. Long text may be cut. |
| `events[].markets[]` | The markets inside the event. Each one has fields such as `bestBid`, `bestAsk`, `acceptingOrders`, and `clobTokenIds`. |
| `events[].markets[].bestBid / events[].markets[].bestAsk` | Best bid and best ask price for the market. |
| `events[].tags[].label / events[].tags[].slug` | Name and slug of each tag on the event, such as `Politics` or `election`. |
| `pagination.hasMore / pagination.totalResults` | `hasMore` tells you if more results exist. `totalResults` is the total number of matches. |

### Notes

- Use `page` to move through results. Check `pagination.hasMore` to see if another page exists.
- `clobTokenIds` is a JSON string that holds a list of token IDs. Parse it before use.
- Pass an event `slug` to [Polymarket Get event by slug](/apis/polymarket/events-slug) to fetch a single event.
- Pass an event `id` to [Polymarket Get event by id](/apis/polymarket/events-by-id) for the same purpose.

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/public-search.json`](../../../catalog/models/polymarket/public-search.json) · Store page: https://www.sandbase.ai/model/polymarket/public-search
