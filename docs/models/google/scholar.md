# Google Scholar

`google/scholar` · api · Google

Search Google Scholar for academic papers with title, authors, citation count, and PDF link.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/scholar", "query": "attention is all you need"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/scholar', {'query': 'attention is all you need'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/scholar", {
  "query": "attention is all you need"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/scholar", sandbase.Params{
	"query": "attention is all you need",
})
```

Same call via the path form: `POST /v1/api/google/scholar` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The Google Scholar search query.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `year`, and it is served only by a source that returns every one of…  |

## Details

Search Google Scholar for academic papers with title, authors, citation count, and PDF link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/scholar" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "attention is all you need"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The Google Scholar search query. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `year`, and it is served only by a source that returns every one of th |

### Pricing

Billed at the actual cost of each call, usually $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/google/scholar.json`](../../../catalog/models/google/scholar.json) · Store page: https://www.sandbase.ai/model/google/scholar
