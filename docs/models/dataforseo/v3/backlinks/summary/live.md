# DataForSEO Backlinks Summary

`dataforseo/v3/backlinks/summary/live` · api · DataForSEO

Returns high-level backlink profile metrics and overview data for a target domain or URL. Helps evaluate link authority and overall link counts for SEO analysis.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/summary/live", "backlinks_status_type": "all", "internal_list_limit": 5, "target": "dataforseo.com"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/summary/live', {'backlinks_status_type': 'all', 'internal_list_limit': 5, 'target': 'dataforseo.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/summary/live", {
  "backlinks_status_type": "all",
  "internal_list_limit": 5,
  "target": "dataforseo.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/summary/live", sandbase.Params{
	"backlinks_status_type": "all",
	"internal_list_limit": 5,
	"target": "dataforseo.com",
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/summary/live` with the body above minus `model`.

## Details

Use this endpoint to retrieve summary metrics for a backlink profile. Provide target parameters to inspect overall backlink volume and referring domain totals.

### Use cases

- Assess overall backlink profile metrics for competitor research.
- Evaluate domain authority and referring domain volume.
- Monitor high-level link growth and historical SEO performance.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/summary/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `target` | Target domain or page, e.g. "nike.com". |

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/summary/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/summary/live
