# Semrush Domain Paid Keywords API: pricing, parameters and code examples

`semrush/domain-paid-keywords` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.04 per call · **Modes:** sync

Keywords a domain bids on in Google Ads, with ad position, search volume, CPC and landing URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.04**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/domain-paid-keywords", "database": "us", "domain": "nike.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/domain-paid-keywords', {'database': 'us', 'domain': 'nike.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/domain-paid-keywords", {
  "database": "us",
  "domain": "nike.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/domain-paid-keywords", sandbase.Params{
	"database": "us",
	"domain": "nike.com",
})
```

Same call via the path form: `POST /v1/api/semrush/domain-paid-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | Domain to analyze, e.g. "nike.com".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Keywords a domain bids on in Google Ads, with ad position, search volume, CPC and landing URL.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/domain-paid-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"database": "us", "domain": "nike.com"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | Yes | Regional Semrush database, e.g. "us", "uk", "de". |
| `domain` | string | Yes | Domain to analyze, e.g. "nike.com". |

### Pricing

Billed at the actual cost of each call, about $0.04 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/domain-paid-keywords.json`](../../../catalog/models/semrush/domain-paid-keywords.json) · Store page: https://www.sandbase.ai/model/semrush/domain-paid-keywords
