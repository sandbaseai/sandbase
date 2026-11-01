# DataForSEO Backlinks Bulk Ranks

`dataforseo/v3/backlinks/bulk_ranks/live` · api · DataForSEO

Returns rank metrics for multiple domains or pages in bulk. Evaluates backlink authority and score indicators across a list of target URLs.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/bulk_ranks/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/bulk_ranks/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/bulk_ranks/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/bulk_ranks/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/bulk_ranks/live` with the body above minus `model`.

## Details

This endpoint retrieves backlink ranks and authority metrics for multiple targets in bulk. It returns evaluation data across specified domains or URLs.

### Use cases

- Evaluate rank authority for competitor domains in bulk.
- Audit backlink scores across multiple internal website pages.
- Filter prospective link-building targets based on rank metrics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/bulk_ranks/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["nike.com", "adidas.com"]}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `targets` | Target domains or pages. |

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Competitors](/model/dataforseo/v3/backlinks/competitors/live): Returns domains that compete for similar backlink profiles.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/bulk_ranks/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/bulk_ranks/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/bulk_ranks/live
