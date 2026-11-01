# Facebook Profile Reels

`facebook/profile-reels` · api · Facebook

List a Facebook page's reels by URL with cursor pagination (caption, view count, permalink, thumbnail).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/profile-reels", "url": "https://www.facebook.com/nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/profile-reels', {'url': 'https://www.facebook.com/nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/profile-reels", {
  "url": "https://www.facebook.com/nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/profile-reels", sandbase.Params{
	"url": "https://www.facebook.com/nike",
})
```

Same call via the path form: `POST /v1/api/facebook/profile-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Facebook page/profile URL.  |
| `cursor` | string |  | Pagination cursor from a previous response.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `feedbackId` or `authorVerified`, and it is served only by a source…  |

## Details

List a Facebook page's reels by URL with cursor pagination (caption, view count, permalink, thumbnail).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/nike"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Facebook page/profile URL. |
| `cursor` | string | No | Pagination cursor from a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `feedbackId` or `authorVerified`, and it is served only by a source th |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/profile-reels.json`](../../../catalog/models/facebook/profile-reels.json) · Store page: https://www.sandbase.ai/model/facebook/profile-reels
