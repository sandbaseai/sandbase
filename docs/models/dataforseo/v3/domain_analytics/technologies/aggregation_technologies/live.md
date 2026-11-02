# DataForSEO Domain Technology Aggregations API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.018 per call · **Modes:** sync

Returns aggregated domain technology data across tracked websites. Analyze the distribution and adoption trends of specific web technologies and platforms.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.018**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `technology` | string |  | Technology name, e.g. "Nginx".  |

## Details

Provides aggregated technology metrics and analytics across web domains. Useful for tracking market share and technology adoption patterns across the web.

### Use cases

- Analyze technology adoption trends across domains.
- Benchmark web framework and CMS market share.
- Evaluate competitor technology stack distribution.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"technology": "Nginx", "limit": 5}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `technology` | Technology name, e.g. "Nginx". |
| `limit` | Maximum number of results (up to 100). |

### Pricing

Billed at the actual cost of each call, about $0.018 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live
