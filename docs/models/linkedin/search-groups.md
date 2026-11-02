# LinkedIn Group Search API: pricing, parameters and code examples

`linkedin/search-groups` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0013 per call · **Modes:** sync

Search LinkedIn groups by keyword, 10 per page: group name, URL, member count, summary, and logo.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0013**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-groups", "query": "python"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-groups', {'query': 'python'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-groups", {
  "query": "python"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-groups", sandbase.Params{
	"query": "python",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-groups` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Which page of up to 10 groups to return, starting at 1 (1-100, default 1). Each page is billed as one request. default `1`; range 1–100 |
| `query` | string | yes | Keyword to search LinkedIn groups for (e.g. python or sales).  |

## Details

Search LinkedIn groups by keyword, 10 per page: group name, URL, member count, summary, and logo.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-groups" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "python"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search LinkedIn groups for (e.g. python or sales). |
| `page` | integer | No | Which page of up to 10 groups to return, starting at 1 (1-100, default 1). Each page is billed as one request. |

### Pricing

Billed at the actual cost of each call, usually $0.0013 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/search-groups.json`](../../../catalog/models/linkedin/search-groups.json) · Store page: https://www.sandbase.ai/model/linkedin/search-groups
