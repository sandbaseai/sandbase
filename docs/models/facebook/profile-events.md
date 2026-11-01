# Facebook Page Events

`facebook/profile-events` · api · Facebook

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

List upcoming and past events hosted by any public Facebook page by URL (name, schedule, venue, and host) as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile-events" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/brickyardoldtown"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The Facebook page link whose events to list, e.g. https://www.facebook.com/brickyardoldtown. Accepted: facebook.com/<name>, /p/<name>-<id>, /pages/<name>/<id>, /pg/<name>, /people/<name>/<id> and profile.php?id=<id>, on  |
| `cursor` | string | No | Pagination cursor from a previous response. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/profile-events.json`](../../../catalog/models/facebook/profile-events.json) · Store page: https://www.sandbase.ai/model/facebook/profile-events
