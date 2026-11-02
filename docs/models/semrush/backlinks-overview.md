# Semrush Backlinks Overview API: pricing, parameters and code examples

`semrush/backlinks-overview` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.004 per call (free daily quota) · **Modes:** sync

Backlink summary for a domain or URL: Authority Score, total backlinks, referring domains, URLs and IPs.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/backlinks-overview", "target": "nike.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/backlinks-overview', {'target': 'nike.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/backlinks-overview", {
  "target": "nike.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/backlinks-overview", sandbase.Params{
	"target": "nike.com",
})
```

Same call via the path form: `POST /v1/api/semrush/backlinks-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string | yes | Domain, subdomain or URL to analyze, e.g. "nike.com".  |

## Details

Backlink summary for a domain or URL: Authority Score, total backlinks, referring domains, URLs and IPs.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/backlinks-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `target` | string | Yes | Domain, subdomain or URL to analyze, e.g. "nike.com". |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/backlinks-overview.json`](../../../catalog/models/semrush/backlinks-overview.json) · Store page: https://www.sandbase.ai/model/semrush/backlinks-overview
