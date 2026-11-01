# Truth Social Post

`truth-social/post` · api · Truth Social

Get a single Truth Social post by its URL - text, author, engagement (likes, comments, shares), and timestamp as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "truth-social/post", "url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('truth-social/post', {'url': 'https://truthsocial.com/@realDonaldTrump/posts/116824551176646175'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("truth-social/post", {
  "url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "truth-social/post", sandbase.Params{
	"url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175",
})
```

Same call via the path form: `POST /v1/api/truth-social/post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Truth Social post URL, e.g. "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175".  |

## Details

Get a single Truth Social post by its URL - text, author, engagement (likes, comments, shares), and timestamp as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/truth-social/post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Truth Social post URL, e.g. "https://truthsocial.com/@realDonaldTrump/posts/116824551176646175". |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/truth-social/post.json`](../../../catalog/models/truth-social/post.json) · Store page: https://www.sandbase.ai/model/truth-social/post
