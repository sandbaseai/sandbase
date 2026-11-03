# DataForSEO Backlinks Bulk Pages Summary API: pricing, parameters and code examples

`dataforseo/v3/backlinks/bulk_pages_summary/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024072 per call · **Modes:** sync

Backlink summary metrics (backlinks, referring domains, rank, spam score) for up to 1,000 pages, domains or subdomains.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024072**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/bulk_pages_summary/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/bulk_pages_summary/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/bulk_pages_summary/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/bulk_pages_summary/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/bulk_pages_summary/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Array of page URLs, domains or subdomains (up to 1,000).  |

## Details

This API returns backlink summary metrics for each page, domain or subdomain you submit. It needs a `targets` array with up to 1,000 URLs or domains.

### Use cases

- Compare the backlink profiles of competing sites in a single call.
- Screen a list of candidate link-building targets by `backlinks_spam_score` and `rank`.
- Find pages with many broken backlinks that are worth fixing or redirecting.
- Add backlink counts and rank scores to a large list of URLs in a spreadsheet or database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/bulk_pages_summary/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["https://www.nike.com/", "https://www.adidas.com/"]}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `targets` | array | No | Array of page URLs, domains or subdomains (up to 1,000). |

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
        "function": "bulk_pages_summary",
        "targets": [
          "https://www.nike.com/"
        ]
      },
      "id": "11030828-2190-0576-0000-dad739697966",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "backlinks": 1483112,
              "backlinks_spam_score": 3,
              "broken_backlinks": 0,
              "broken_pages": 0,
              "first_seen": "2019-01-15 22:59:06 +00:00",
              "lost_date": null,
              "main_domain_rank": 604,
              "rank": 507
            }
          ],
          "items_count": 2,
          "total_count": 2
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.4428 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.4506 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[]` | One summary object for each target. Items appear to follow the order of the `targets` array, though no target field is shown in the items. |
| `tasks[].result[].items[].backlinks` | Total number of backlinks found for the target. |
| `tasks[].result[].items[].backlinks_spam_score` | Spam score of the target's backlinks. A lower value means fewer spam signals. |
| `tasks[].result[].items[].broken_backlinks` | Number of backlinks that point to a broken page on the target. |
| `tasks[].result[].items[].broken_pages` | Number of broken pages on the target that still receive backlinks. |
| `tasks[].result[].items[].rank` | Rank score of the target itself. |
| `tasks[].result[].items[].main_domain_rank` | Rank score of the main domain that the target belongs to. |
| `tasks[].result[].items[].first_seen / tasks[].result[].items[].lost_date` | The date the target was first seen, and the date it was lost. `lost_date` is `null` when the target is still present. Dates use the format `2019-01-15 22:59:06 +00:00`. |
| `tasks[].result[].items_count / tasks[].result[].total_count` | Number of items returned and total number of items for the request. |

### Notes

- Pass full URLs such as `https://www.nike.com/` to get page-level metrics. The description also allows domains and subdomains.
- Each item in the sample response has no target field, so match items to your `targets` by their position in the list.
- For a deeper look at a single target, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live) or [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live).

### Pricing

Billed at the actual cost of each call, about $0.024072 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/bulk_pages_summary/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/bulk_pages_summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/bulk_pages_summary/live
