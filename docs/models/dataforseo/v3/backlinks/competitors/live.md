# DataForSEO Backlinks Competitors API: pricing, parameters and code examples

`dataforseo/v3/backlinks/competitors/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02418 per call · **Modes:** sync

Returns domains that compete for similar backlink profiles. Analyze competitor backlink sources and compare link-building overlaps across related websites.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02418**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/competitors/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/competitors/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/competitors/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/competitors/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/competitors/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target` | string |  | Target domain or page, e.g. "nike.com".  |

## Details

Returns domains that share backlink sources with a target domain or page. It needs a `target` such as `nike.com` and returns a ranked list of competing domains with the number of shared linking sources.

### Use cases

- Find the domains that compete with a brand for the same backlink sources.
- Build a list of link-building prospects from sites that link to competitors but not to you.
- Compare how much a domain's link profile overlaps with each competitor.
- Pick competitor domains to feed into a deeper backlink comparison.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/competitors/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of results (up to 100). |
| `target` | string | No | Target domain or page, e.g. "nike.com". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "backlinks",
        "function": "competitors",
        "limit": 5,
        "target": "nike.com"
      },
      "id": "11030828-2190-0461-0000-fb4014fef084",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "intersections": 1950,
              "rank": 318,
              "target": "adidas-group.com",
              "type": "backlinks_competitors"
            }
          ],
          "items_count": 5,
          "total_count": 10411
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.0989 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.1062 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].target` | Competing domain that shares backlink sources with the requested `target`. |
| `tasks[].result[].items[].intersections` | Number of intersections between the competitor and the requested `target`. A higher number means more overlap in backlink profiles. |
| `tasks[].result[].items[].rank` | Rank value for the competing domain. Higher values appear on stronger domains in this sample, such as `318` for `adidas-group.com`. |
| `tasks[].result[].items[].type` | Item type, `backlinks_competitors` for every row. |
| `tasks[].result[].items_count` | Number of competitors returned in this response. |
| `tasks[].result[].total_count` | Total number of competing domains found for the target, not only the rows returned. |
| `tasks[].data.target / tasks[].data.limit` | Echo of the `target` and `limit` values the call used. |
| `tasks[].status_code / tasks[].status_message` | Task status. `20000` with `Ok.` means the task succeeded. |

### Notes

- Set `limit` to control how many competitors come back, up to 100.
- Compare `items_count` with `total_count` to see how many more competitors exist than the response returned.
- Pass a competitor's `target` value from the results into [Domain Intersection](/apis/dataforseo/v3/backlinks/domain_intersection/live) to see the shared linking sources.
- Use [Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live) to get overall link totals for a competitor domain.

### Pricing

Billed at the actual cost of each call, about $0.02418 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/competitors/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/competitors/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/competitors/live
