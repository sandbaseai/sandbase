# Semrush Keyword Paid Results API: pricing, parameters and code examples

`semrush/keyword-paid-results` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.04 per call · **Modes:** sync

Advertisers bidding on a keyword in Google Ads, with ad position and landing URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.04**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/keyword-paid-results", "phrase": "car insurance", "database": "us"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/keyword-paid-results', {'phrase': 'car insurance', 'database': 'us'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/keyword-paid-results", {
  "phrase": "car insurance",
  "database": "us"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/keyword-paid-results", sandbase.Params{
	"phrase": "car insurance",
	"database": "us",
})
```

Same call via the path form: `POST /v1/api/semrush/keyword-paid-results` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `phrase` | string | yes | Keyword to analyze, e.g. "running shoes".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Advertisers bidding on a keyword in Google Ads, with ad position and landing URL.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/keyword-paid-results" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"phrase": "car insurance", "database": "us"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | No | Regional Semrush database, e.g. "us", "uk", "de". |
| `phrase` | string | Yes | Keyword to analyze, e.g. "running shoes". |

### Pricing

Billed at the actual cost of each call, about $0.04 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/keyword-paid-results.json`](../../../catalog/models/semrush/keyword-paid-results.json) · Store page: https://www.sandbase.ai/model/semrush/keyword-paid-results
