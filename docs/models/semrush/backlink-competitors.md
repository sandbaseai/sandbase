# Semrush Backlink Competitors API: pricing, parameters and code examples

`semrush/backlink-competitors` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.08 per call · **Modes:** sync

Domains with a backlink profile similar to the target, ranked by similarity.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.08**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/backlink-competitors", "target": "nike.com", "target_type": "root_domain"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/backlink-competitors', {'target': 'nike.com', 'target_type': 'root_domain'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/backlink-competitors", {
  "target": "nike.com",
  "target_type": "root_domain"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/backlink-competitors", sandbase.Params{
	"target": "nike.com",
	"target_type": "root_domain",
})
```

Same call via the path form: `POST /v1/api/semrush/backlink-competitors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string | yes | Domain, subdomain or URL to analyze, e.g. "nike.com".  |
| `target_type` | string | yes | Type of target: "root_domain", "domain" or "url".  |

## Details

Domains with a backlink profile similar to the target, ranked by similarity.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/backlink-competitors" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "target_type": "root_domain"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `target` | string | Yes | Domain, subdomain or URL to analyze, e.g. "nike.com". |
| `target_type` | string | Yes | Type of target: "root_domain", "domain" or "url". |

### Pricing

Billed at the actual cost of each call, about $0.08 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/backlink-competitors.json`](../../../catalog/models/semrush/backlink-competitors.json) · Store page: https://www.sandbase.ai/model/semrush/backlink-competitors
