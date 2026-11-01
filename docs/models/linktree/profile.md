# Linktree Profile

`linktree/profile` · api · Linktree

Get a public Linktree page by URL: title, bio, picture, contact email, linked social accounts, and every link card with its destination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linktree/profile", "url": "https://linktr.ee/mkbhd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linktree/profile', {'url': 'https://linktr.ee/mkbhd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linktree/profile", {
  "url": "https://linktr.ee/mkbhd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linktree/profile", sandbase.Params{
	"url": "https://linktr.ee/mkbhd",
})
```

Same call via the path form: `POST /v1/api/linktree/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The Linktree profile URL, e.g. https://linktr.ee/mkbhd.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `title`, and it is served only by a source that returns every one of…  |

## Details

Get a public Linktree page by URL: title, bio, picture, contact email, linked social accounts, and every link card with its destination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linktree/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://linktr.ee/mkbhd"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The Linktree profile URL, e.g. https://linktr.ee/mkbhd. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `title`, and it is served only by a source that returns every one of t |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linktree/profile.json`](../../../catalog/models/linktree/profile.json) · Store page: https://www.sandbase.ai/model/linktree/profile
