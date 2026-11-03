# DataForSEO Backlinks Domain Pages Summary API: pricing, parameters and code examples

`dataforseo/v3/backlinks/domain_pages_summary/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02436 per call · **Modes:** sync

Backlink metrics for each page of a domain: backlinks, referring domains and rank per page.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02436**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/domain_pages_summary/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/domain_pages_summary/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/domain_pages_summary/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/domain_pages_summary/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/domain_pages_summary/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of pages to return.  |
| `target` | string |  | Domain or subdomain, e.g. "nike.com".  |

## Details

This API returns backlink metrics for the pages of a domain or subdomain. Each item shows the page's backlink count, referring domain count, rank and spam score. It needs a `target` domain such as `nike.com`.

### Use cases

- Find which pages on a site attract the most backlinks and referring domains.
- Check a site for pages with a high `backlinks_spam_score` that may need a link audit.
- Compare page-level rank across a domain to decide which pages to promote or update.
- Spot pages with broken backlinks that need a redirect.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/domain_pages_summary/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of pages to return. |
| `target` | string | No | Domain or subdomain, e.g. "nike.com". |

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
        "function": "domain_pages_summary",
        "limit": 10,
        "target": "nike.com"
      },
      "id": "11030828-2190-0445-0000-213f0ea7938e",
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
              "rank": 507,
              "referring_domains": 27299
            }
          ],
          "items_count": 10,
          "target": "nike.com",
          "total_count": 1659398
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "2.5869 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "2.5955 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].target` | The domain or subdomain that was analyzed. |
| `tasks[].result[].total_count` | Total number of pages found for the target. Compare it with `items_count` to see how many pages the call did not return. |
| `tasks[].result[].items_count` | Number of pages returned in this response. |
| `tasks[].result[].items[].backlinks` | Number of backlinks that point to the page. |
| `tasks[].result[].items[].referring_domains` | Number of distinct domains that link to the page. |
| `tasks[].result[].items[].rank` | Rank score for the page. Higher values appear on pages with stronger backlink profiles in this sample. |
| `tasks[].result[].items[].backlinks_spam_score` | Spam score for the page's backlinks. Higher values mean more spam-like links. |
| `tasks[].result[].items[].broken_backlinks / broken_pages` | Counts of broken backlinks and broken pages tied to the item. Both are `0` in the sample. |
| `tasks[].result[].items[].first_seen` | Date and time the page was first seen, in the format `2019-01-15 22:59:06 +00:00`. |
| `tasks[].result[].items[].lost_date` | Date the page was lost. It is `null` when the page is still live. |

### Notes

- Set `target` to a bare domain or subdomain, for example `nike.com`.
- Use `limit` to set how many pages come back. Check `total_count` to see how many pages exist for the target.
- The response lists items without a page URL field in this sample, so match items to pages with [DataForSEO Backlinks Domain Pages](/apis/dataforseo/v3/backlinks/domain_pages/live) if you need page-level detail.
- For domain-wide totals, call [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live).

### Pricing

Billed at the actual cost of each call, about $0.02436 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/domain_pages_summary/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/domain_pages_summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/domain_pages_summary/live
