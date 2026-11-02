# Semrush Keyword Overview API: pricing, parameters and code examples

`semrush/keyword-overview` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search volume, CPC, competition and number of results for a keyword in a regional database.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/keyword-overview", "phrase": "running shoes", "database": "us"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/keyword-overview', {'phrase': 'running shoes', 'database': 'us'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/keyword-overview", {
  "phrase": "running shoes",
  "database": "us"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/keyword-overview", sandbase.Params{
	"phrase": "running shoes",
	"database": "us",
})
```

Same call via the path form: `POST /v1/api/semrush/keyword-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `phrase` | string | yes | Keyword to analyze, e.g. "running shoes".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de". default `"us"` |

## Details

Search volume, CPC, competition and number of results for a keyword in a regional database.

The result is returned in `outputs[0].data` as the official Semrush API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/keyword-overview" \
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

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/keyword-overview.json`](../../../catalog/models/semrush/keyword-overview.json) · Store page: https://www.sandbase.ai/model/semrush/keyword-overview
