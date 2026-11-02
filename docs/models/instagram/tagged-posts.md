# Instagram Tagged Posts API: pricing, parameters and code examples

`instagram/tagged-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00188 per call · **Modes:** sync

List the posts an Instagram user is tagged in, with cursor pagination (author, caption, likes, comments).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00188**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/tagged-posts", "handle": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/tagged-posts', {'handle': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/tagged-posts", {
  "handle": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/tagged-posts", sandbase.Params{
	"handle": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/tagged-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `handle` | string | yes | Instagram username without the leading @.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `audioId`, and it is served only by a source that returns every one…  |

## Details

List the posts an Instagram user is tagged in, with cursor pagination (author, caption, likes, comments).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/tagged-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "nasa"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Instagram username without the leading @. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `audioId`, and it is served only by a source that returns every one of |

### Pricing

Billed at the actual cost of each call, usually $0.00188 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/tagged-posts.json`](../../../catalog/models/instagram/tagged-posts.json) · Store page: https://www.sandbase.ai/model/instagram/tagged-posts
