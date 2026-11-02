# DataForSEO Backlinks List API: pricing, parameters and code examples

`dataforseo/v3/backlinks/backlinks/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02418 per call · **Modes:** sync

Returns a list of external backlinks pointing to a specified target domain or webpage. Helps SEO teams audit incoming link profiles and evaluate referring page details.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02418**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/backlinks/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/backlinks/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/backlinks/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/backlinks/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/backlinks/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target` | string |  | Target domain or page, e.g. "nike.com".  |

## Details

Returns detailed records of backlinks pointing to a specified `target`. Use this endpoint to inspect inbound links and referring domains for SEO audits.

### Use cases

- Audit incoming links to evaluate domain link equity.
- Analyze inbound anchor text and referring web pages.
- Monitor link profiles to detect new referring sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/backlinks/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 5}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `target` | Target domain or page, e.g. "nike.com". |
| `limit` | Maximum number of results (up to 100). |

### Pricing

Billed at the actual cost of each call, about $0.02418 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.
- [DataForSEO Backlinks Competitors](/model/dataforseo/v3/backlinks/competitors/live): Returns domains that compete for similar backlink profiles.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/backlinks/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/backlinks/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/backlinks/live
