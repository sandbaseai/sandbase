# Semrush Domain vs Domain API: pricing, parameters and code examples

`semrush/domain-vs-domain` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.16 per call · **Modes:** sync

Keyword gap between domains: shared and unique keywords with each domain's ranking position.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.16**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/domain-vs-domain", "database": "us", "domains": "*|or|nike.com|*|or|adidas.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/domain-vs-domain', {'database': 'us', 'domains': '*|or|nike.com|*|or|adidas.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/domain-vs-domain", {
  "database": "us",
  "domains": "*|or|nike.com|*|or|adidas.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/domain-vs-domain", sandbase.Params{
	"database": "us",
	"domains": "*|or|nike.com|*|or|adidas.com",
})
```

Same call via the path form: `POST /v1/api/semrush/domain-vs-domain` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domains` | string | yes | Domains to compare in Semrush syntax, e.g. "*\|or\|nike.com\|*\|or\|adidas.com".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Keyword gap between domains: shared and unique keywords with each domain's ranking position.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/domain-vs-domain" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"database": "us", "domains": "*|or|nike.com|*|or|adidas.com"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | Yes | Regional Semrush database, e.g. "us", "uk", "de". |
| `domains` | string | Yes | Domains to compare in Semrush syntax, e.g. "*|or|nike.com|*|or|adidas.com". |

### Pricing

Billed at the actual cost of each call, about $0.16 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/domain-vs-domain.json`](../../../catalog/models/semrush/domain-vs-domain.json) · Store page: https://www.sandbase.ai/model/semrush/domain-vs-domain
