# Ahrefs Ahrefs Domain Rating

`ahrefs/domain-rating` · api · Ahrefs

Return the Ahrefs Domain Rating (0-100 authority score) and Ahrefs Rank for a target domain on a given date. 4xx/5xx are not charged.

## Pricing

- **$0.08 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/domain-rating", "date": "2026-08-01", "target": "ahrefs.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/domain-rating', {'date': '2026-08-01', 'target': 'ahrefs.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/domain-rating", {
  "date": "2026-08-01",
  "target": "ahrefs.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/domain-rating", sandbase.Params{
	"date": "2026-08-01",
	"target": "ahrefs.com",
})
```

Same call via the path form: `POST /v1/api/ahrefs/domain-rating` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | Snapshot date in `YYYY-MM-DD` format.  |
| `target` | string | yes | Target domain, e.g. `ahrefs.com`.  |

## Details

Return the Ahrefs Domain Rating (0-100 authority score) and Ahrefs Rank for a target domain on a given date. 4xx/5xx are not charged.

The response is the official Ahrefs API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ahrefs/domain-rating" \
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
Machine-readable: [`catalog/models/ahrefs/domain-rating.json`](../../../catalog/models/ahrefs/domain-rating.json) · Store page: https://www.sandbase.ai/model/ahrefs/domain-rating
