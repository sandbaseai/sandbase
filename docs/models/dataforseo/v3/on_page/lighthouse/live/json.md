# DataForSEO OnPage Lighthouse Audit API: pricing, parameters and code examples

`dataforseo/v3/on_page/lighthouse/live/json` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns real-time Google Lighthouse audit data and web performance metrics for target web pages. Helps assess on-page speed, accessibility, best practices, and search optimization standards.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/on_page/lighthouse/live/json"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/on_page/lighthouse/live/json', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/on_page/lighthouse/live/json", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/on_page/lighthouse/live/json", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/on_page/lighthouse/live/json` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Page URL.  |

## Details

Runs Google Lighthouse audits on web pages and returns detailed diagnostic reports. Pass target `url` values to evaluate on-page performance, SEO, and accessibility metrics.

### Use cases

- Audit website performance and Core Web Vitals on target pages.
- Evaluate technical SEO, accessibility, and best practice compliance.
- Diagnose on-page load bottlenecks and rendering issues.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/on_page/lighthouse/live/json" \
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

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/on_page/lighthouse/live/json.json`](../../../../../../../catalog/models/dataforseo/v3/on_page/lighthouse/live/json.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/on_page/lighthouse/live/json
