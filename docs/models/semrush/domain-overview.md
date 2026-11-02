# Semrush Domain Overview API: pricing, parameters and code examples

`semrush/domain-overview` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Semrush rank, organic keywords, organic traffic, traffic cost and paid keywords for a domain.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/domain-overview", "domain": "nike.com", "database": "us"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/domain-overview', {'domain': 'nike.com', 'database': 'us'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/domain-overview", {
  "domain": "nike.com",
  "database": "us"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/domain-overview", sandbase.Params{
	"domain": "nike.com",
	"database": "us",
})
```

Same call via the path form: `POST /v1/api/semrush/domain-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | Domain to analyze, e.g. "nike.com".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de". default `"us"` |

## Details

Semrush rank, organic keywords, organic traffic, traffic cost and paid keywords for a domain.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/domain-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "nike.com", "database": "us"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | No | Regional Semrush database, e.g. "us", "uk", "de". |
| `domain` | string | Yes | Domain to analyze, e.g. "nike.com". |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/domain-overview.json`](../../../catalog/models/semrush/domain-overview.json) · Store page: https://www.sandbase.ai/model/semrush/domain-overview
