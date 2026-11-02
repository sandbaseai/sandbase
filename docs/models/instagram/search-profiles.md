# Instagram Profile Search API: pricing, parameters and code examples

`instagram/search-profiles` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search public Instagram profiles by a bio or caption keyword.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/search-profiles", "query": "coffee roaster"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/search-profiles', {'query': 'coffee roaster'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/search-profiles", {
  "query": "coffee roaster"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/search-profiles", sandbase.Params{
	"query": "coffee roaster",
})
```

Same call via the path form: `POST /v1/api/instagram/search-profiles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Bio or caption keyword/phrase to search for.  |
| `cursor` | string |  | Pagination cursor returned by a previous response.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `private`, and it is served only by a source that returns every one…  |

## Details

Search public Instagram profiles by a bio or caption keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/search-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "coffee roaster"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Bio or caption keyword/phrase to search for. |
| `cursor` | string | No | Pagination cursor returned by a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `private`, and it is served only by a source that returns every one of |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/search-profiles.json`](../../../catalog/models/instagram/search-profiles.json) · Store page: https://www.sandbase.ai/model/instagram/search-profiles
