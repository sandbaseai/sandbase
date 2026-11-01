# Facebook Events

`facebook/events` · api · Facebook

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

List public Facebook events for a city or place by its events-page URL (event name, date, venue, and attendance) as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/events" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | URL of a city's or place's Facebook Events page (e.g. https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547). |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |
| `time` | string | No | Timeframe filter for the returned events. Defaults to all time. One of: `today`, `this_week`, `next_week`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/events.json`](../../../catalog/models/facebook/events.json) · Store page: https://www.sandbase.ai/model/facebook/events
