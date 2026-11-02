# Ahrefs Ahrefs Site Metrics API: pricing, parameters and code examples

`ahrefs/metrics` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.08 per call · **Modes:** sync

Return core Site Explorer metrics for a target domain on a given date: organic and paid keyword counts, top-3 keyword count, organic traffic, and traffic value. 4xx/5xx are not charged.

## Pricing

- **$0.08 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/metrics", "date": "2026-08-01", "target": "ahrefs.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/metrics', {'date': '2026-08-01', 'target': 'ahrefs.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/metrics", {
  "date": "2026-08-01",
  "target": "ahrefs.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/metrics", sandbase.Params{
	"date": "2026-08-01",
	"target": "ahrefs.com",
})
```

Same call via the path form: `POST /v1/api/ahrefs/metrics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | Snapshot date in `YYYY-MM-DD` format.  |
| `target` | string | yes | Target domain, e.g. `ahrefs.com`.  |

## Details

Return core Site Explorer metrics for a target domain on a given date: organic and paid keyword counts, top-3 keyword count, organic traffic, and traffic value. 4xx/5xx are not charged.

The response is the official Ahrefs API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ahrefs/metrics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "ahrefs.com", "date": "2026-10-01"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | Yes | Snapshot date in `YYYY-MM-DD` format. |
| `target` | string | Yes | Target domain, e.g. `ahrefs.com`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ahrefs/metrics.json`](../../../catalog/models/ahrefs/metrics.json) · Store page: https://www.sandbase.ai/model/ahrefs/metrics
