# DataForSEO Backlinks Referring Domains API: pricing, parameters and code examples

`dataforseo/v3/backlinks/referring_domains/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02418 per call · **Modes:** sync

Returns a list of referring domains that link to a specified target domain or page. Inspect inbound domain metrics, link counts, and authority data for SEO research.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02418**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/referring_domains/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/referring_domains/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/referring_domains/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/referring_domains/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/referring_domains/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target` | string |  | Target domain or page, e.g. "nike.com".  |

## Details

Returns a list of domains that link to a target domain or page, with link counts, a spam score and a rank for each referring domain. It needs one input, `target`, such as `nike.com`.

### Use cases

- List the domains that send the most backlinks to a competitor's site.
- Spot referring domains with a high `backlinks_spam_score` before a link cleanup or disavow review.
- Find referring domains with many broken backlinks and ask them to fix the links.
- Check when each referring domain was first seen and whether it has been lost.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/referring_domains/live" \
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
        "function": "referring_domains",
        "limit": 5,
        "target": "nike.com"
      },
      "id": "11030828-2190-0273-0000-7b914a9779d5",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "backlinks": 4620412,
              "backlinks_spam_score": 18,
              "broken_backlinks": 5599,
              "broken_pages": 19,
              "domain": "syniva.es",
              "first_seen": "2024-08-04 10:12:19 +00:00",
              "lost_date": null,
              "rank": 508
            }
          ],
          "items_count": 5,
          "target": "nike.com",
          "total_count": 160401
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.9284 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.9364 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of referring domains found for the target. Use it to see how many more rows exist beyond the returned page. |
| `tasks[].result[].items_count` | Number of referring domains returned in this response. |
| `tasks[].result[].items[].domain` | The referring domain that links to the target. |
| `tasks[].result[].items[].backlinks` | Number of backlinks from this referring domain to the target. |
| `tasks[].result[].items[].rank` | Rank score of the referring domain. Higher values appear first in the sample, which suggests the list is sorted by it. |
| `tasks[].result[].items[].backlinks_spam_score` | Spam score for the backlinks from this domain. Low values such as `0` and `1` appear on the brand's own country domains. |
| `tasks[].result[].items[].broken_backlinks / tasks[].result[].items[].broken_pages` | Count of backlinks from this domain that point to broken pages, and count of broken target pages that receive them. |
| `tasks[].result[].items[].first_seen` | Date and time the referring domain was first seen linking to the target, for example `2024-08-04 10:12:19 +00:00`. |
| `tasks[].result[].items[].lost_date` | Date the link was lost. It is `null` when the domain still links to the target. |

### Notes

- Pass a domain such as `nike.com` or a page URL in `target`.
- Set `limit` to control how many rows come back, up to 100.
- Read `total_count` to see the full number of referring domains, since `items_count` only shows the rows returned.
- For the individual links behind a domain, call [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live). For overall totals for the target, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live).

### Pricing

Billed at the actual cost of each call, about $0.02418 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/referring_domains/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/referring_domains/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/referring_domains/live
