# DataForSEO Domain Analytics Technology Stats API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/technologies/technology_stats/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0672 per call · **Modes:** sync

Returns aggregated technology usage statistics across websites and web domains. Enables analysis of market adoption and trends for specific web technologies.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0672**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/technologies/technology_stats/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/technologies/technology_stats/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/technologies/technology_stats/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/technologies/technology_stats/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/technologies/technology_stats/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `technology` | string |  | Technology name, e.g. "Nginx".  |

## Details

Inspect technology adoption metrics across domains with this endpoint. It provides aggregate technology statistics for tracking domain analytics trends.

### Use cases

- Track market share and adoption trends for web technologies.
- Analyze technology stack prevalence across indexed domains.
- Benchmark technology adoption across various digital platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/technologies/technology_stats/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"technology": "Nginx"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `technology` | Technology name, e.g. "Nginx". |

### Pricing

Billed at the actual cost of each call, about $0.0672 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/technologies/technology_stats/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/technologies/technology_stats/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/technologies/technology_stats/live
