# DataForSEO Google Maps Local SERP API: pricing, parameters and code examples

`dataforseo/v3/serp/google/maps/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Returns real-time Google Maps search engine results pages and local business listings. Supports local SEO monitoring and geographical business discovery directly from Google Maps.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/maps/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/maps/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/maps/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/maps/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/maps/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_coordinate` | string |  | Coordinates as "latitude,longitude,zoom", e.g. "40.7128,-74.0060,14z".  |

## Details

This endpoint delivers real-time Google Maps local business search results. It enables developers to inspect local SERP listings for regional business research and competitor tracking.

### Use cases

- Retrieve Google Maps listings for local business research.
- Analyze regional search rankings across specific geographic locations.
- Monitor local competitor visibility and presence on Google Maps.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/maps/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "coffee shop", "location_coordinate": "40.7128,-74.0060,14z", "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keyword` | Search query. |
| `location_coordinate` | Coordinates as "latitude,longitude,zoom", e.g. "40.7128,-74.0060,14z". |
| `language_code` | Language code, e.g. "en". |

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. The cost grows with the number of rows, targets or pages a call returns. `depth` sets how many result pages are fetched. Extra crawled pages, pixel rankings, async AI overview, People Also Ask clicks and search operators (site:, intitle: ...) are not supported. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/maps/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/maps/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/maps/live/advanced
