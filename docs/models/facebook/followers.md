# Facebook Followers

`facebook/followers` · api · Facebook

List the public followers (or accounts followed) of any Facebook page or profile URL as normalized JSON records.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.12**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/followers", "url": "https://www.facebook.com/nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/followers', {'url': 'https://www.facebook.com/nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/followers", {
  "url": "https://www.facebook.com/nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/followers", sandbase.Params{
	"url": "https://www.facebook.com/nike",
})
```

Same call via the path form: `POST /v1/api/facebook/followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Facebook page or profile URL to list follows for (e.g. https://www.facebook.com/nasa).  |
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). You are billed per result returned, so a lower limit costs less. range 1–20 |
| `followType` | string |  | Which relation to fetch: 'follower' or 'following' (e.g. follower). default `"follower"` |

## Details

List the public followers (or accounts followed) of any Facebook page or profile URL as normalized JSON records.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/nike", "limit": 3}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Facebook page or profile URL to list follows for (e.g. https://www.facebook.com/nasa). |
| `followType` | string | No | Which relation to fetch: 'follower' or 'following' (e.g. follower). Default `"follower"`. |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). You are billed per result returned, so a lower limit costs less. |

### Pricing

Billed at the actual cost of each call, usually $0.12 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/followers.json`](../../../catalog/models/facebook/followers.json) · Store page: https://www.sandbase.ai/model/facebook/followers
