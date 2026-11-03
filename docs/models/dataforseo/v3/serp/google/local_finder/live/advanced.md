# DataForSEO Google Local Finder Advanced API: pricing, parameters and code examples

`dataforseo/v3/serp/google/local_finder/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Returns real-time Google Local Finder search engine results page data. Retrieves local business listings, map results, and advanced SERP elements based on search queries.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/local_finder/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/local_finder/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/local_finder/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/local_finder/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/local_finder/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_coordinate` | string |  | Coordinates as "latitude,longitude,zoom", e.g. "40.7128,-74.0060,14z".  |

## Details

This endpoint retrieves advanced Google Local Finder search results in real time. It returns detailed local business rankings and search engine results data.

### Use cases

- Monitor local business ranking positions across Google Local Finder results.
- Gather detailed local pack and map listing data for competitive analysis.
- Track geographic visibility and presence for local branch locations.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/local_finder/live/advanced" \
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
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/local_finder/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/local_finder/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/local_finder/live/advanced
