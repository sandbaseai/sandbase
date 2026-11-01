# Google Patents

`google/patents` · api · Google

Search Google Patents with title, patent number, inventor, assignee, key dates, and PDF link.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/patents", "query": "wireless charging"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/patents', {'query': 'wireless charging'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/patents", {
  "query": "wireless charging"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/patents", sandbase.Params{
	"query": "wireless charging",
})
```

Same call via the path form: `POST /v1/api/google/patents` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The Google Patents search query.  |

## Details

Search Google Patents with title, patent number, inventor, assignee, key dates, and PDF link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/patents" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "wireless charging"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The Google Patents search query. |

### Pricing

Billed at the actual cost of each call, usually $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/google/patents.json`](../../../catalog/models/google/patents.json) · Store page: https://www.sandbase.ai/model/google/patents
