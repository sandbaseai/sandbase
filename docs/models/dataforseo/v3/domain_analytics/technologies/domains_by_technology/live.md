# DataForSEO Domains by Technology

`dataforseo/v3/domain_analytics/technologies/domains_by_technology/live` · api · DataForSEO

Returns a list of websites and domains that utilize a specific technology or software stack. Useful for analyzing competitor adoption, market share, and tech stack distribution.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/technologies/domains_by_technology/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/technologies/domains_by_technology/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/technologies/domains_by_technology/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/technologies/domains_by_technology/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live` with the body above minus `model`.

## Details

Query domains based on target `technology` identifiers to evaluate software adoption across the web. This endpoint returns domain analytics data for sites deploying specified tech stacks.

### Use cases

- Identify websites that run a competitor's software or plugin.
- Analyze market penetration and adoption rates for specific web technologies.
- Generate lead lists of web properties using selected frameworks or platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"technologies": ["Nginx"], "limit": 5}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `technologies` | Technology names. |
| `limit` | Maximum number of results (up to 100). |

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live
