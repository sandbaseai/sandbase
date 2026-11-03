# DataForSEO Domains by HTML Terms API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.018 per call · **Modes:** sync

Finds domains that contain specific HTML patterns or terms. Returns matching domain profiles and technology footprints based on the analyzed web markup.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.018**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `search_terms` | array |  | HTML terms to search for.  |

## Details

Returns domains whose HTML contains the terms you search for, such as `data-reactroot`. Each item has a domain, its rank, a short site description, language and country codes, and the last visit time. The request needs a `search_terms` array and an optional `limit`.

### Use cases

- Build a list of sites that ship a specific HTML attribute or script snippet, such as `data-reactroot`.
- Sort matching sites by `domain_rank` to find the most prominent sites that use a given markup pattern.
- Collect sales leads from sites that use a given front-end framework or widget, filtered by country or language.
- Estimate how widely a markup pattern is used by reading the total match count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_terms": ["data-reactroot"], "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of results (up to 100). |
| `search_terms` | array | No | HTML terms to search for. |

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
        "function": "domains_by_html_terms",
        "limit": 5,
        "se": "technologies",
        "search_terms": [
          "data-reactroot"
        ]
      },
      "id": "11030829-1614-0511-0000-f5d65f4216b5",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "content_language_code": null,
              "country_iso_code": "WW",
              "description": "腾讯网从2003年创立至今，已经成为集新闻信息，区域垂直生活服务、社会化媒体资讯和产品为一体的互联网媒体平台。腾讯网下设新闻、科技、财经、娱乐、体育、汽车、时尚…",
              "domain": "www.qq.com",
              "domain_rank": 866,
              "emails": null,
              "language_code": "zh",
              "last_visited": "2026-04-23 20:11:13 +00:00"
            }
          ],
          "items_count": 5,
          "offset": 0,
          "offset_token": "eyJDdXJy…",
          "total_count": 330428
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "4.2292 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "4.2436 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].domain` | Domain whose HTML contains the search term. |
| `tasks[].result[].items[].domain_rank` | Rank score of the domain. Higher values appear first in the sample, so results look sorted by this field. |
| `tasks[].result[].items[].description` | Site description text, in the language of the site. |
| `tasks[].result[].items[].language_code / content_language_code` | Language codes for the domain. `content_language_code` can be `null`. |
| `tasks[].result[].items[].country_iso_code` | Country code for the domain. The sample shows `WW`, `KR` and `US`. |
| `tasks[].result[].items[].last_visited` | Date and time the domain was last visited, in the format `YYYY-MM-DD HH:MM:SS +00:00`. |
| `tasks[].result[].items[].emails` | Email addresses found for the domain. It is `null` when none are listed. |
| `tasks[].result[].total_count` | Total number of domains that match the search terms. |
| `tasks[].result[].items_count` | Number of items returned in this response. |
| `tasks[].result[].offset_token` | Token for fetching the next page of results. |

### Notes

- Set `search_terms` to a list of HTML strings. Set `limit` to cap the number of results, up to 100.
- Compare `total_count` with `items_count` to see how many matches remain beyond the current page.
- `offset_token` and `offset` are returned for paging. Pass the token back in the next request to continue.
- Each task also returns an `id`, and the response shows `status_code` `20000` when the call succeeds.

### Pricing

Billed at the actual cost of each call, about $0.018 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/technologies/domains_by_html_terms/live
