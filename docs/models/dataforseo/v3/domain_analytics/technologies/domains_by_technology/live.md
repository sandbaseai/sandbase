# DataForSEO Domains by Technology API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/technologies/domains_by_technology/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.018 per call · **Modes:** sync

Returns a list of websites and domains that utilize a specific technology or software stack. Useful for analyzing competitor adoption, market share, and tech stack distribution.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.018**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/technologies/domains_by_technology/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/technologies/domains_by_technology/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/technologies/domains_by_technology/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/technologies/domains_by_technology/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `technologies` | array |  | Technology names.  |

## Details

Returns a list of websites that use a given technology, such as Nginx. You send one or more technology names in `technologies` and a `limit` for the number of domains to return. The response also gives the total number of matching domains.

### Use cases

- Build a lead list of sites that run a specific web server, CMS or framework.
- Compare how many domains use one technology versus another by reading `total_count` for each.
- Find sites that use a competitor's software and read their contact emails when listed.
- Sample domains by language to see where a technology is used.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"technologies": ["Nginx"], "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of results (up to 100). |
| `technologies` | array | No | Technology names. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "domain_analytics",
        "function": "domains_by_technology",
        "limit": 5,
        "se": "technologies",
        "technologies": [
          "Nginx"
        ]
      },
      "id": "11030829-1614-0484-0000-6be563b06738",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "content_language_code": "fa",
              "country_iso_code": null,
              "description": "افزایش فروش و سهم بازار , جهت‌گیری کسب‌وکار , آماده‌سازی کارکنان , نوید ابولیان",
              "domain": "maaze.ir",
              "domain_rank": null,
              "emails": [
                "info@maaze.ir"
              ],
              "language_code": "fa",
              "last_visited": "2026-09-11 11:50:18 +00:00"
            }
          ],
          "items_count": 5,
          "offset": 0,
          "offset_token": "eyJDdXJy…",
          "total_count": 37226431
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "9.2408 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "9.2563 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of domains found for the requested technology. In the example it is 37226431 for `Nginx`. |
| `tasks[].result[].items_count` | Number of domains returned in this response. |
| `tasks[].result[].items[].domain` | Domain name of a site that uses the technology. |
| `tasks[].result[].items[].emails` | List of email addresses found for the domain. It is `null` when none were found. |
| `tasks[].result[].items[].description` | Site description text. It can be `null`. |
| `tasks[].result[].items[].language_code / content_language_code` | Language codes for the site, for example `fa` or `en`. Either can be `null`. |
| `tasks[].result[].items[].country_iso_code / domain_rank` | Country code and rank for the domain. Both were `null` in the sample, so they are not always filled. |
| `tasks[].result[].items[].last_visited` | Date and time of the last visit to the domain, as a string like `2026-10-26 04:56:41 +00:00`. |
| `tasks[].result[].offset / offset_token` | Current offset in the result list and a token for getting the next page. |

### Notes

- Pass technology names as an array in `technologies`, for example `["Nginx"]`.
- `limit` sets how many domains come back, up to 100.
- To get more domains, use `offset_token` from the response in your next request, or change `offset`.
- Check `tasks[].status_code` and `tasks_error` to confirm the task succeeded.

### Pricing

Billed at the actual cost of each call, about $0.018 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/technologies/domains_by_technology/live
