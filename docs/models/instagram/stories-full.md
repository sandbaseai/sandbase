# Instagram Stories (full) API: pricing, parameters and code examples

`instagram/stories-full` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0022 per call · **Modes:** sync

Fetch a public Instagram account's currently live stories with media, type, dimensions, posting time, and 24-hour expiry by username.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0022**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/stories-full", "username": "nba"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/stories-full', {'username': 'nba'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/stories-full", {
  "username": "nba"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/stories-full", sandbase.Params{
	"username": "nba",
})
```

Same call via the path form: `POST /v1/api/instagram/stories-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username or handle without the @.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle`, and it is served only by a source that returns every…  |

## Details

Fetch a public Instagram account's currently live stories with media, type, dimensions, posting time, and 24-hour expiry by username.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/stories-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nba"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username or handle without the @. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle`, and it is served only by a source that returns every one |

### Pricing

Billed at the actual cost of each call, usually $0.0022 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/stories-full.json`](../../../catalog/models/instagram/stories-full.json) · Store page: https://www.sandbase.ai/model/instagram/stories-full
