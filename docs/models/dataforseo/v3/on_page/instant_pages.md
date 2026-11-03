# DataForSEO OnPage Instant Pages API: pricing, parameters and code examples

`dataforseo/v3/on_page/instant_pages` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00015 per call · **Modes:** sync

Returns instant page-level on-page SEO audit metrics for analyzed web pages. Inspect technical SEO elements and on-page optimization signals for audit workflows.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/on_page/instant_pages"}'
```

**Python** ([sdk/python](../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/on_page/instant_pages', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/on_page/instant_pages", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/on_page/instant_pages", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/on_page/instant_pages` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Page URL.  |

## Details

Returns instant page-level on-page SEO audit results for specific web pages. Call this endpoint to inspect technical SEO health and content optimization signals on demand.

### Use cases

- Audit single web pages instantly for technical SEO compliance.
- Analyze on-page content and structure during SEO quality checks.
- Diagnose page-level technical issues within automated SEO audit workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/on_page/instant_pages" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.python.org/"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `url` | Page URL. |

### Pricing

Billed at the actual cost of each call, about $0.00015 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/on_page/instant_pages.json`](../../../../../catalog/models/dataforseo/v3/on_page/instant_pages.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/on_page/instant_pages
