# DataForSEO Backlinks Summary API: pricing, parameters and code examples

`dataforseo/v3/backlinks/summary/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024036 per call · **Modes:** sync

Returns high-level backlink profile metrics and overview data for a target domain or URL. Helps evaluate link authority and overall link counts for SEO analysis.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024036**

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

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target` | string |  | Target domain or page, e.g. "nike.com".  |

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

Billed at the actual cost of each call, about $0.024036 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/summary/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/summary/live
