# Semrush Keyword Difficulty API: pricing, parameters and code examples

`semrush/keyword-difficulty` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.005 per call · **Modes:** sync

Keyword difficulty score (0-100) for a phrase in a regional Semrush database.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/keyword-difficulty", "phrase": "running shoes", "database": "us"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/keyword-difficulty', {'phrase': 'running shoes', 'database': 'us'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/keyword-difficulty", {
  "phrase": "running shoes",
  "database": "us"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/keyword-difficulty", sandbase.Params{
	"phrase": "running shoes",
	"database": "us",
})
```

Same call via the path form: `POST /v1/api/semrush/keyword-difficulty` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `phrase` | string | yes | Keyword to analyze, e.g. "running shoes".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Keyword difficulty score (0-100) for a phrase in a regional Semrush database.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/keyword-difficulty" \
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

Billed at the actual cost of each call, about $0.005 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/keyword-difficulty.json`](../../../catalog/models/semrush/keyword-difficulty.json) · Store page: https://www.sandbase.ai/model/semrush/keyword-difficulty
