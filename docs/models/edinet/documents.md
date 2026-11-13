# EDINET Filing List API: pricing, parameters and code examples

`edinet/documents` · data API · EDINET · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $1e-05 per call · **Modes:** sync

List the corporate disclosure documents filed with Japan's EDINET on a given date, with document ID, filer, document type, period and submission time.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$1e-05**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "edinet/documents", "date": "2026-11-10"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('edinet/documents', {'date': '2026-11-10'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("edinet/documents", {
  "date": "2026-11-10"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "edinet/documents", sandbase.Params{
	"date": "2026-11-10",
})
```

Same call via the path form: `POST /v1/api/edinet/documents` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | File date in YYYY-MM-DD format.  |
| `type` | integer |  | Response mode: 1 for metadata only, 2 for metadata plus filing list. one of: `1`, `2`; default `1` |

## Details

List the corporate disclosure documents filed with Japan's EDINET on a given date, with document ID, filer, document type, period and submission time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/edinet/documents" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date": "2026-11-10", "type": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | Yes | File date in YYYY-MM-DD format. |
| `type` | integer | No | Response mode: 1 for metadata only, 2 for metadata plus filing list. |

### Pricing

Billed at the actual upstream cost of each call (about $1e-05 for the request above). Failed calls are not charged.

---
Machine-readable: [`catalog/models/edinet/documents.json`](../../../catalog/models/edinet/documents.json) · Store page: https://www.sandbase.ai/model/edinet/documents
