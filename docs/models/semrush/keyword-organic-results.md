# Semrush Keyword Organic Results API: pricing, parameters and code examples

`semrush/keyword-organic-results` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02 per call · **Modes:** sync

Domains and URLs ranking in Google organic results for a keyword, by position.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/keyword-organic-results", "phrase": "running shoes", "database": "us"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/keyword-organic-results', {'phrase': 'running shoes', 'database': 'us'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/keyword-organic-results", {
  "phrase": "running shoes",
  "database": "us"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/keyword-organic-results", sandbase.Params{
	"phrase": "running shoes",
	"database": "us",
})
```

Same call via the path form: `POST /v1/api/semrush/keyword-organic-results` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `phrase` | string | yes | Keyword to analyze, e.g. "running shoes".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Domains and URLs ranking in Google organic results for a keyword, by position.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/keyword-organic-results" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"phrase": "running shoes", "database": "us"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | No | Regional Semrush database, e.g. "us", "uk", "de". |
| `phrase` | string | Yes | Keyword to analyze, e.g. "running shoes". |

### Pricing

Billed at the actual cost of each call, about $0.02 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/keyword-organic-results.json`](../../../catalog/models/semrush/keyword-organic-results.json) · Store page: https://www.sandbase.ai/model/semrush/keyword-organic-results
